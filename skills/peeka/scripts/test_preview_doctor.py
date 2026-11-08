"""Run: python3 -m unittest discover -s skills/peeka/scripts -p 'test_*.py' -v"""
import contextlib
import io
import json
import os
import plistlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import preview_doctor as doctor


def result(stdout="", ok=True, error=None, stderr="", truncated=False):
    return dict(stdout=stdout, ok=ok, error=error, stderr=stderr, truncated=truncated)


def plugin(identifier, app, path, election="default", types=None):
    return dict(id=identifier, app_path=str(app), path=str(path), app_name=Path(app).stem,
                app_id=doctor.PEEKA_BUNDLE_ID if "Peeka" in str(app) else "example.other",
                is_peeka="Peeka" in str(app), version="0.1.9", app_version="0.1.9", kind="extension",
                exists=True, metadata_valid=True, superseded=False, election=election,
                types=types or ["public.text"])


class Elections:
    def __init__(self, states, fail=None):
        self.states = dict(states)
        self.fail = fail
        self.mutations = []

    def __call__(self, args):
        identifier = args[args.index("-i") + 1]
        if "-m" in args:
            marker = {"use": "+", "ignore": "-", "default": "", "unknown": "?"}[self.states[identifier]]
            return result("{} {}(1.0)\n    Path = /Applications/Test.app/Contents/PlugIns/Test.appex\n".format(marker, identifier))
        election = args[args.index("-e") + 1]
        self.mutations.append((identifier, election))
        if (identifier, election) == self.fail:
            return result(ok=False, stderr="simulated failure")
        self.states[identifier] = election
        return result()


class InventoryTests(unittest.TestCase):
    def test_physical_copies_and_elections(self):
        parsed = doctor.parse_plugins("""
+ studio.mellowbit.peeka.quicklook(0.1.9)
    Path = /Applications/Peeka.app/Contents/PlugIns/PeekaQuickLook.appex
    Parent Bundle = /Applications/Peeka.app
+ studio.mellowbit.peeka.quicklook(0.1.9)
    Path = /private/tmp/Peeka.app/Contents/PlugIns/PeekaQuickLook.appex
- example.disabled(1.0)
? example.unknown(1.0)
= example.old(0.1)
  example.default(1.0)
! example.debugger(1.0)
 (7 plug-ins)
""")
        self.assertEqual(len(parsed), 7)
        self.assertNotEqual(parsed[0]["path"], parsed[1]["path"])
        self.assertEqual([x["election"] for x in parsed], ["use", "use", "ignore", "unknown", "unknown", "default", "unknown"])
        self.assertTrue(parsed[4]["superseded"])

    def test_legacy_generators_are_candidates_not_elected_extensions(self):
        entries = doctor.parse_generators("plugins:\n  public.text -> /Library/QuickLook/Text.qlgenerator (1.0)\n  public.xml -> /Library/QuickLook/Text.qlgenerator (1.0)\n")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["types"], ["public.text", "public.xml"])
        self.assertEqual(entries[0]["kind"], "legacy_generator")

    def test_sandbox_failure_is_not_absent_installation(self):
        plugins, _, warnings, complete = doctor.inventory(lambda _: result(stderr="match: Connection invalid"))
        self.assertFalse(complete)
        self.assertFalse(plugins)
        self.assertIn("do not infer", warnings[0])

    def test_metadata_identifies_peeka_without_guessing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Path(directory) / "Renamed.app"
            extension = app / "Contents/PlugIns/Preview.appex"
            (extension / "Contents").mkdir(parents=True)
            (app / "Contents/Info.plist").write_bytes(plistlib.dumps({"CFBundleIdentifier": doctor.PEEKA_BUNDLE_ID}))
            (extension / "Contents/Info.plist").write_bytes(plistlib.dumps({"CFBundleIdentifier": "actual.preview", "NSExtension": {
                "NSExtensionPointIdentifier": doctor.PROTOCOL, "NSExtensionAttributes": {"QLSupportedContentTypes": ["public.text"]}}}))
            entry = doctor.describe_plugin({"id": "actual.preview", "path": str(extension)})
            self.assertTrue(entry["is_peeka"])
            self.assertTrue(entry["metadata_valid"])
            self.assertEqual(entry["types"], ["public.text"])

    def test_native_type_wins_over_stale_metadata(self):
        def runner(args):
            if "osascript" in args[0]:
                return result(json.dumps({"uti": "com.soulmen.ulysses3.markdown", "conforming_types": ["public.text"]}))
            self.assertEqual(args[1:3], ["-plist", "-"])
            return result(plistlib.dumps({"kMDItemContentType": "public.data"}).decode())
        native, warnings = doctor.inspect_types(Path("/target.mmd"), ["public.text"], runner)
        self.assertEqual(native["uti"], "com.soulmen.ulysses3.markdown")
        self.assertEqual(native["source"], "native_resource")
        self.assertTrue(warnings)

    def test_metadata_fallback_after_timeout(self):
        def runner(args):
            if "osascript" in args[0]:
                return result(ok=False, error="timeout")
            return result(plistlib.dumps({"kMDItemContentType": "public.json", "kMDItemContentTypeTree": ["public.json", "public.text"]}).decode())
        native, warnings = doctor.inspect_types(Path("/target.json"), [], runner)
        self.assertEqual(native["uti"], "public.json")
        self.assertEqual(native["source"], "metadata_fallback")
        self.assertIn("public.text", native["conforming_types"])
        self.assertTrue(warnings)

    def test_malformed_xml_plists_are_treated_as_unavailable(self):
        malformed = '<?xml version="1.0"?><plist version="1.0"><dict>'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "Info.plist"
            path.write_text(malformed)
            self.assertEqual(doctor.load_plist(path), {})

        def runner(args):
            return result(malformed) if "mdls" in args[0] else result(ok=False)
        native, _ = doctor.inspect_types(Path("/target.md"), [], runner)
        self.assertIsNone(native["uti"])


class FormatTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = doctor.load_catalog()

    def match(self, name):
        return doctor.match_format(name, self.catalog)

    def test_exact_names_and_longest_suffix(self):
        cases = {"Package.swift": "swift-package", "Package.resolved": "swift-resolved", "Dockerfile.debug": "source-dockerfile",
                 "archive.TAR.GZ": "tgz", "archive.gz": "gzip", "file.blade.php": "source-blade",
                 "hello.C": "source-c++", "hello.c": "source-c", ".env.local": "dotenv", "go.mod": "source-go-module"}
        for name, identifier in cases.items():
            with self.subTest(name=name):
                self.assertEqual(self.match(name)["id"], identifier)
        self.assertEqual(self.match("package.swift")["id"], "source-swift")
        self.assertEqual(self.match(".env.secret")["support"], "unknown")
        self.assertEqual(self.match("file.unfamiliar")["support"], "unknown")
        self.assertEqual(self.match("binary.scpt")["support"], "outside_documented_scope")
        self.assertEqual(self.match("nginx.conf")["id"], "source-nginx")
        self.assertEqual(self.match("binary.framework")["switch"], "FRAMEWORK")

    def test_free_and_pro_are_capability_specific(self):
        self.assertEqual(self.match("test.mmd")["tier"], "pro")
        self.assertEqual(self.match("test.mmd")["min_macos"], "14.4")
        self.assertEqual(self.match("test.md")["tier"], "free")
        self.assertIn("Mermaid", self.match("test.md")["pro_details"])
        self.assertEqual(self.match("test.db")["tier"], "free")
        self.assertTrue(self.match("test.aar")["notes"])

    def test_catalog_identifiers_are_unique_across_similarly_named_languages(self):
        identifiers = [row["id"] for row in self.catalog["formats"]]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertEqual(self.match("test.cs")["id"], "source-csharp")
        self.assertEqual(self.match("test.fs")["id"], "source-fsharp")

    def test_all_documented_source_profiles_and_rules_remain_in_catalog(self):
        import re
        source = (doctor.ROOT / "references/source-coverage.md").read_text()
        table = source.split("## Profile catalog", 1)[1].split("## Shared configuration", 1)[0]
        profiles = [row for row in self.catalog["formats"] if row.get("source_profile")]
        self.assertEqual(len(profiles), 205)
        for line in table.splitlines():
            if not line.startswith("| ") or line.startswith(("| Profile", "| ---")):
                continue
            name, suffixes, filenames = [cell.strip() for cell in line.strip("|").split("|")]
            entry = next(row for row in profiles if row["name"] == name)
            self.assertEqual(set(re.findall(r"`([^`]+)`", suffixes)), set(entry["suffixes"]))
            for filename in re.findall(r"`([^`]+)`", filenames):
                if filename.endswith("*"):
                    self.assertIn(filename[:-1], entry.get("prefixes", []))
                else:
                    self.assertIn(filename, entry["filenames"])


class DiagnosisTests(unittest.TestCase):
    def diagnose(self, path, providers, native=None):
        native = native or {"uti": "com.soulmen.ulysses3.markdown", "conforming_types": ["public.text"], "source": "native_resource"}
        with patch.object(doctor, "inventory", return_value=(providers, [], [], True)), \
                patch.object(doctor, "inspect_types", return_value=(native, [])), \
                patch.object(doctor, "installed_peeka_apps", return_value=[]), \
                patch.object(doctor, "type_declarers", return_value=[{"app_name": "Ulysses", "uti": "com.soulmen.ulysses3.markdown", "declaration": "exported"}]):
            return doctor.diagnose(path, runner=lambda _: result("14.4\n"))

    def test_mmd_declaration_is_not_preview_ownership(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "test.mmd"
            target.write_text("flowchart LR\nA-->B\n")
            providers = [plugin("peeka.preview", "/Applications/Peeka.app", "/peeka"),
                         plugin("ulysses.preview", "/Applications/Ulysses.app", "/ulysses", types=["com.soulmen.ulysses3.sheet"])]
            report = self.diagnose(target, providers)
            self.assertEqual([p["id"] for p in report["candidates"]], ["peeka.preview"])
            self.assertEqual(report["actual_provider"]["status"], "unconfirmed")
            self.assertEqual(report["installed_capability"], "needs_ui_verification")
            self.assertFalse(report["preview_verified"])

    def test_database_suffix_does_not_establish_sqlite_content(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "not-sqlite.db"
            target.write_text("not a database")
            self.assertEqual(self.diagnose(target, [])["format"]["support"], "unknown")
            target.write_bytes(b"SQLite format 3\x00")
            self.assertEqual(self.diagnose(target, [])["format"]["support"], "documented")

    def test_sqlite_signature_precedes_missing_or_misleading_suffix(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ("database", "database.md", "database.aar"):
                with self.subTest(name=name):
                    target = Path(directory) / name
                    target.write_bytes(b"SQLite format 3\x00")
                    report = self.diagnose(target, [], {"uti": "public.data"})
                    self.assertEqual(report["format"]["id"], "sqlite")
                    self.assertEqual(report["format"]["match"], "signature")

    def test_ambiguous_archive_does_not_select_a_switch_or_allow_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            for name, uti in (("sample.aar", "public.zip-archive"), ("sample", "com.apple.archive")):
                with self.subTest(name=name):
                    target = Path(directory) / name
                    target.write_bytes(b"PK\x03\x04")
                    report = self.diagnose(target, [], {"uti": uti})
                    self.assertEqual(report["format"]["support"], "needs_content_verification")
                    self.assertIsNone(report["format"]["switch"])
                    self.assertFalse(any("enable it directly" in step for step in report["next_steps"]))
                    with self.assertRaisesRegex(doctor.DoctorError, "verify the format"):
                        doctor.repair_plan(report)

    def test_cloud_placeholder_is_not_read(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "cloud.db"
            target.write_text("not a database")
            native = {"uti": "public.data", "downloaded": False, "ubiquitous": True}
            catalog = doctor.load_catalog()
            with patch.object(Path, "open", side_effect=AssertionError("must not read file contents")):
                with patch.object(doctor, "load_catalog", return_value=catalog):
                    report = self.diagnose(target, [], native)
            self.assertFalse(report["file"]["local"])
            self.assertNotIn("signature_matches", report["format"])

    def test_multiple_copies_need_explicit_target(self):
        first = plugin("peeka.preview", "/Applications/Peeka.app", "/first")
        second = plugin("peeka.preview", "/tmp/Peeka.app", "/second")
        self.assertIsNone(doctor.select_peeka([first, second]))
        self.assertEqual(doctor.select_peeka([first, second], "/tmp/Peeka.app")["path"], "/second")

    def test_installed_app_without_registration_is_identifiable(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Path(directory) / "Renamed.app"
            (app / "Contents").mkdir(parents=True)
            (app / "Contents/Info.plist").write_bytes(plistlib.dumps({"CFBundleIdentifier": doctor.PEEKA_BUNDLE_ID,
                                                                    "CFBundleShortVersionString": "0.1.7"}))
            with patch.object(doctor, "application_paths", return_value=[str(app)]):
                found = doctor.installed_peeka_apps([])
            self.assertEqual(found[0]["app_path"], str(app))
            self.assertEqual(found[0]["version"], "0.1.7")


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.path = "/Users/person/private/sample.mmd"
        self.providers = [{"id": "example.preview"}]

    def evidence(self, messages):
        return doctor.trace_evidence([{"eventMessage": message} for message in messages], self.path, self.providers)

    def test_only_correlated_selected_provider_counts(self):
        evidence = self.evidence(['Selected preview provider example.preview for "' + self.path + '"'])
        self.assertEqual(evidence["status"], "observed")
        self.assertEqual(evidence["id"], "example.preview")
        self.assertNotIn(self.path, json.dumps(evidence))

    def test_private_paths_candidates_and_running_process_are_insufficient(self):
        for message in ["Selected preview provider example.preview for <private>",
                        "Selected preview provider example.preview for sample.mmd",
                        "Running example.preview " + self.path,
                        "Candidate preview provider example.preview " + self.path,
                        "Not selected preview provider example.preview " + self.path,
                        "Loading preview extension example.preview failed " + self.path,
                        "Selected preview provider example.preview " + self.path + ".other",
                        "Selected preview provider example.preview.evil " + self.path]:
            with self.subTest(message=message):
                self.assertEqual(self.evidence([message])["status"], "unconfirmed")

    def test_provider_is_extracted_from_the_event_and_never_from_target_path(self):
        self.path = "/tmp/example.preview/sample.mmd"
        unknown_selection = 'Selected preview provider unlisted.preview for "' + self.path + '"'
        self.assertEqual(self.evidence([unknown_selection])["status"], "unconfirmed")
        known_selection = 'Selected preview provider "example.preview" for "' + self.path + '"'
        self.assertEqual(self.evidence([known_selection])["id"], "example.preview")
        self.assertEqual(self.evidence([known_selection, unknown_selection])["reason"], "conflicting_evidence")

    def test_permission_failure_and_capture_bound(self):
        report = {"file": {"path": self.path}, "providers": self.providers, "warnings": [],
                  "actual_provider": {"status": "unconfirmed", "id": None}}
        sleeps = []
        with contextlib.redirect_stderr(io.StringIO()):
            traced = doctor.trace(report, 30, runner=lambda _: result(ok=False, stderr="Operation not permitted"), sleep=sleeps.append)
        self.assertEqual(sleeps, [30])
        self.assertEqual(traced["actual_provider"]["status"], "unconfirmed")
        self.assertFalse(traced["trace"]["log_available"])


class RepairTests(unittest.TestCase):
    def test_journal_precedes_mutation_and_failure_rolls_back(self):
        states = Elections({"peeka.preview": "default", "other.preview": "use"}, fail=("other.preview", "ignore"))
        with tempfile.TemporaryDirectory() as directory:
            record_path = Path(directory) / "record.json"
            def runner(args):
                if "-e" in args:
                    self.assertTrue(record_path.exists())
                    self.assertIn("before", json.loads(record_path.read_text())["operations"][0])
                return states(args)
            record = doctor.apply_operations([{"id": "peeka.preview", "to": "use"}, {"id": "other.preview", "to": "ignore"}], record_path, runner)
            self.assertEqual(record["status"], "rolled_back")
            self.assertEqual(states.states, {"peeka.preview": "default", "other.preview": "use"})
            self.assertEqual(record_path.stat().st_mode & 0o777, 0o600)

    def test_restore_preserves_default_and_does_not_touch_unchanged_settings(self):
        states = Elections({"peeka.preview": "default", "other.preview": "ignore"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            record = doctor.apply_operations([{"id": "peeka.preview", "to": "use"}, {"id": "other.preview", "to": "ignore"}], path, states)
            self.assertEqual(record["status"], "configuration_adjusted")
            self.assertFalse(record["preview_verified"])
            plan = doctor.restore_record(path, runner=states)
            self.assertEqual(plan["status"], "restore_plan")
            self.assertEqual(states.states["peeka.preview"], "use")
            restored = doctor.restore_record(path, apply=True, runner=states)
            self.assertEqual(restored["status"], "restored")
            self.assertEqual(states.states, {"peeka.preview": "default", "other.preview": "ignore"})
            self.assertEqual(states.mutations, [("peeka.preview", "use"), ("peeka.preview", "default")])

    def test_later_state_changes_are_not_overwritten(self):
        states = Elections({"peeka.preview": "default"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            doctor.apply_operations([{"id": "peeka.preview", "to": "use"}], path, states)
            states.states["peeka.preview"] = "ignore"
            with self.assertRaisesRegex(doctor.DoctorError, "changed after"):
                doctor.restore_record(path, apply=True, runner=states)
            self.assertEqual(states.states["peeka.preview"], "ignore")

    def test_unknown_election_stops_before_any_mutation(self):
        states = Elections({"peeka.preview": "unknown"})
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(doctor.DoctorError):
                doctor.apply_operations([{"id": "peeka.preview", "to": "use"}], Path(directory) / "record.json", states)
        self.assertEqual(states.mutations, [])

    def test_failed_rollback_preserves_record_and_can_be_retried(self):
        states = Elections({"peeka.preview": "default", "other.preview": "use"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            def runner(args):
                if "-e" in args and (args[args.index("-i") + 1], args[args.index("-e") + 1]) in {
                        ("other.preview", "ignore"), ("peeka.preview", "default")}:
                    return result(ok=False, stderr="simulated mutation failure")
                return states(args)
            record = doctor.apply_operations([{"id": "peeka.preview", "to": "use"}, {"id": "other.preview", "to": "ignore"}], path, runner)
            self.assertEqual(record["status"], "rollback_incomplete")
            self.assertTrue(record["operations"][0]["restore_error"])
            restored = doctor.restore_record(path, apply=True, runner=states)
            self.assertEqual(restored["status"], "restored")
            self.assertEqual(states.states, {"peeka.preview": "default", "other.preview": "use"})

    def test_restore_refuses_a_race_after_preflight(self):
        states = Elections({"peeka.preview": "default"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            doctor.apply_operations([{"id": "peeka.preview", "to": "use"}], path, states)
            reads = []
            def runner(args):
                if "-m" in args:
                    reads.append(True)
                    if len(reads) > 1:
                        states.states["peeka.preview"] = "ignore"
                return states(args)
            with self.assertRaisesRegex(doctor.DoctorError, "changed during"):
                doctor.restore_record(path, apply=True, runner=runner)
            self.assertEqual(states.states["peeka.preview"], "ignore")

    def test_apply_requires_separate_confirmation_for_competitor(self):
        peeka = plugin("peeka.preview", "/Applications/Peeka.app", "/peeka")
        other = plugin("other.preview", "/Applications/Other.app", "/other")
        report = {"inventory_complete": True, "format": {"support": "documented"},
                  "file": {"local": True, "readable": True}, "os_compatible": True,
                  "selected_peeka": peeka, "candidates": [peeka, other], "providers": [peeka, other]}
        with patch.object(doctor, "diagnose", return_value=report), \
                patch.object(doctor, "apply_operations") as apply, \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = doctor.main(["repair", "/sample.mmd", "--apply", "--disable-extension", "other.preview"])
        self.assertEqual(code, 1)
        apply.assert_not_called()

    def test_selected_build_must_itself_match_target_type(self):
        selected = plugin("peeka.preview", "/Applications/Peeka.app", "/selected")
        other_copy = plugin("peeka.preview", "/tmp/Peeka.app", "/other")
        report = {"inventory_complete": True, "format": {"support": "documented"},
                  "file": {"local": True, "readable": True}, "os_compatible": True,
                  "selected_peeka": selected, "candidates": [other_copy]}
        with self.assertRaisesRegex(doctor.DoctorError, "does not declare"):
            doctor.repair_plan(report)

    def test_competitor_has_separate_confirmation_and_affected_types(self):
        peeka = plugin("peeka.preview", "/Applications/Peeka.app", "/peeka")
        other = plugin("other.preview", "/Applications/Other.app", "/other", types=["public.text", "public.xml"])
        older = plugin("other.preview", "/tmp/Other.app", "/older", types=["public.image"])
        older["superseded"] = True
        report = {"inventory_complete": True, "format": {"support": "documented"},
                  "file": {"local": True, "readable": True}, "os_compatible": True,
                  "selected_peeka": peeka, "candidates": [peeka, other], "providers": [peeka, other, older]}
        operation = doctor.repair_plan(report, "other.preview")[-1]
        self.assertFalse(operation["separate_confirmation"])
        self.assertEqual(operation["affected_types"], ["public.image", "public.text", "public.xml"])
        self.assertTrue(doctor.repair_plan(report, "other.preview", "other.preview")[-1]["separate_confirmation"])
        older["metadata_valid"] = False
        with self.assertRaisesRegex(doctor.DoctorError, "Affected types are unavailable"):
            doctor.repair_plan(report, "other.preview", "other.preview")
        older.update(metadata_valid=True, app_id="com.apple.system")
        with self.assertRaises(doctor.DoctorError):
            doctor.repair_plan(report, "other.preview", "other.preview")


class ReportAndCLITests(unittest.TestCase):
    def test_invalid_output_prevents_repair_and_restore(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "missing" / "output.json"
            with patch.object(doctor.platform, "system", return_value="Darwin"), \
                    patch.object(doctor, "diagnose", return_value={}), \
                    patch.object(doctor, "repair_plan", return_value=[]), \
                    patch.object(doctor, "apply_operations") as apply, \
                    patch.object(doctor, "restore_record") as restore, \
                    contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                for command in ("repair", "restore"):
                    self.assertEqual(doctor.main([command, "target", "--apply", "--output", str(output)]), 1)
            apply.assert_not_called()
            restore.assert_not_called()

    def test_repair_prints_durable_recovery_path_even_if_rediagnosis_fails(self):
        states = Elections({"peeka.preview": "default"})
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            output = Path(directory) / "output.json"
            stderr = io.StringIO()
            def runner(args):
                if "-e" in args:
                    self.assertTrue(output.exists())
                    self.assertEqual(doctor.read_record(journal)["status"], "prepared")
                    self.assertIn("Recovery record: " + str(journal), stderr.getvalue())
                return states(args)
            apply_operations = doctor.apply_operations
            with patch.object(doctor.platform, "system", return_value="Darwin"), \
                    patch.object(doctor, "diagnose", side_effect=[
                        {"file": {"path": "/sample.mmd"}}, doctor.DoctorError("target disappeared")]), \
                    patch.object(doctor, "repair_plan", return_value=[{"id": "peeka.preview", "to": "use"}]), \
                    patch.object(doctor, "new_record_path", return_value=journal), \
                    patch.object(doctor, "apply_operations", side_effect=lambda *a, **kw: apply_operations(*a, runner=runner, **kw)), \
                    contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = doctor.main(["repair", "/sample.mmd", "--apply", "--json", "--output", str(output)])
            self.assertEqual(code, 1)
            self.assertFalse(output.exists())
            self.assertEqual(states.mutations, [("peeka.preview", "use")])
            self.assertEqual(doctor.read_record(journal)["status"], "configuration_adjusted")

    def test_issue_report_does_not_leak_filename_path_contents_or_logs(self):
        report = {"file": {"path": "/Users/alice/secret/project-secret.mmd", "name": "project-secret.mmd", "size": 1024},
                  "macos": "14.4", "format": doctor.match_format("project-secret.mmd", doctor.load_catalog()),
                  "type": {"uti": "com.private.customer.data"},
                  "peeka_copies": [], "actual_provider": {"status": "unconfirmed", "id": None},
                  "candidates": [{"kind": "extension", "id": "private.secret.bundle", "match": "conforms", "election": "use"}],
                  "warnings": ["secret log with /Users/alice"], "raw_logs": "SECRET CONTENT"}
        draft = doctor.issue_draft(report)
        for secret in ["alice", "project-secret", "/Users", "SECRET CONTENT", "private.secret.bundle", "com.private.customer"]:
            self.assertNotIn(secret, draft)
        self.assertIn(".mmd", draft)
        report["previous_trace"] = {"created_at": "2026-11-06T08:00:00+00:00", "actual_provider": {
            "status": "observed", "id": "studio.mellowbit.peeka.quicklook"}}
        historical = doctor.issue_draft(report)
        self.assertIn("(historical)", historical)
        self.assertIn("2026-11-06T08:00:00+00:00", historical)
        self.assertIn("studio.mellowbit.peeka.quicklook", historical)
        report["file"]["name"] = "project.ACME-MERGER-Q4"
        report["type"]["uti"] = "public.ACME-MERGER-Q4"
        report["candidates"][0]["id"] = "com.apple.ACME-MERGER-Q4"
        self.assertNotIn("ACME-MERGER-Q4", doctor.issue_draft(report))

    def test_cli_help_and_trace_limit(self):
        args = doctor.parser().parse_args(["diagnose", "a file;$(touch nope).mmd", "--json"])
        self.assertEqual(args.target, "a file;$(touch nope).mmd")
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            doctor.parser().parse_args(["trace", "target.mmd", "--seconds", "31"])

    def test_run_command_timeout_and_missing_binary(self):
        timed = doctor.run_command([sys.executable, "-c", "import time; time.sleep(2)"], timeout=0.05)
        self.assertFalse(timed["ok"])
        self.assertEqual(timed["error"], "timeout")
        self.assertFalse(doctor.run_command(["/nonexistent/peeka-doctor-test"])["ok"])


if __name__ == "__main__":
    unittest.main()
