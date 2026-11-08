#!/usr/bin/env python3
"""Local Quick Look diagnostics. Python 3.9+, standard library only.

No subprocess uses a shell. Diagnosis never changes extension elections.
Per-format controls and purchases belong to Peeka's visible UI and the agent.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import plistlib
import re
import stat
import subprocess
import sys
import tempfile
import time
import uuid
from contextlib import contextmanager, suppress
from pathlib import Path
from xml.parsers.expat import ExpatError

ROOT = Path(__file__).resolve().parents[1]
PEEKA_BUNDLE_ID = "studio.mellowbit.peeka"
PROTOCOL = "com.apple.quicklook.preview"
SCHEMA_VERSION = 1
MAX_OUTPUT = 2 * 1024 * 1024
ELECTIONS = {"use", "ignore", "default"}
PUBLIC_UTIS = {
    "public.data", "public.text", "public.plain-text", "public.json", "public.xml",
    "public.zip-archive", "com.apple.archive", "net.daringfireball.markdown",
    "com.soulmen.ulysses3.markdown",
}
PUBLIC_PROVIDER_IDS = {
    "studio.mellowbit.peeka.quicklook", "com.ulyssesapp.mac.quicklookextension",
    "com.kingsoft.wpsoffice.mac.WPSQuickLook",
}


class DoctorError(Exception):
    pass


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def run_command(args, timeout=15):
    """Bound runtime and returned data; spool output off-memory before reading."""
    env = dict(os.environ, LC_ALL="C", LANG="C")
    try:
        with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
            process = subprocess.Popen(args, stdout=out, stderr=err, env=env)
            timed_out = False
            try:
                process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                process.kill()
                process.wait()
            out.seek(0)
            err.seek(0)
            data, errors = out.read(MAX_OUTPUT + 1), err.read(4097)
            return {
                "ok": process.returncode == 0 and not timed_out,
                "stdout": data[:MAX_OUTPUT].decode("utf-8", "replace"),
                "stderr": errors[:4096].decode("utf-8", "replace"),
                "error": "timeout" if timed_out else None,
                "truncated": len(data) > MAX_OUTPUT or len(errors) > 4096,
            }
    except OSError as exc:
        return {"ok": False, "stdout": "", "stderr": str(exc),
                "error": "unavailable", "truncated": False}


def checked_command(args, runner=run_command):
    result = runner(args)
    if not result["ok"]:
        raise DoctorError("{} failed ({}): {}".format(
            Path(args[0]).name, result.get("error") or "command error",
            result["stderr"][:300]))
    return result


def load_plist(path):
    try:
        with Path(path).open("rb") as handle:
            value = plistlib.load(handle)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError, plistlib.InvalidFileException, ExpatError):
        return {}


def strings(value):
    if isinstance(value, str):
        return [value]
    return [x for x in value if isinstance(x, str)] if isinstance(value, list) else []


def mapping(value):
    return value if isinstance(value, dict) else {}


def enclosing_app(path):
    return next((p for p in Path(path).parents if p.suffix == ".app"), None)


def parse_plugins(output):
    """Parse pluginkit -m -A -D -vv, retaining every physical instance."""
    plugins, current = [], None
    for line in output.splitlines():
        header = re.match(r"^\s*([+!\-=?]?)\s*([\w.-]+)\(([^()]*)\)\s*$", line)
        if header:
            marker, identifier, version = header.groups()
            current = {"id": identifier, "version": version, "marker": marker,
                       "election": {"+": "use", "-": "ignore", "": "default"}.get(marker, "unknown"),
                       "superseded": marker == "=", "kind": "extension"}
            plugins.append(current)
        elif current and " = " in line:
            key, value = line.strip().split(" = ", 1)
            names = {"Path": "path", "Parent Bundle": "app_path",
                     "Parent Name": "app_name", "Display Name": "display_name"}
            if key in names:
                current[names[key]] = value
    return plugins


def describe_plugin(plugin):
    info = load_plist(Path(plugin.get("path", "")) / "Contents/Info.plist")
    extension = mapping(info.get("NSExtension"))
    attributes = mapping(extension.get("NSExtensionAttributes"))
    plugin["types"] = strings(attributes.get("QLSupportedContentTypes"))
    plugin["exists"] = bool(plugin.get("path")) and Path(plugin["path"]).is_dir()
    app = Path(plugin["app_path"]) if plugin.get("app_path") else enclosing_app(plugin.get("path", ""))
    parent = load_plist(app / "Contents/Info.plist") if app else {}
    plugin["app_path"] = str(app) if app else None
    plugin["app_id"] = parent.get("CFBundleIdentifier")
    plugin["app_version"] = parent.get("CFBundleShortVersionString")
    plugin["app_name"] = parent.get("CFBundleDisplayName") or parent.get("CFBundleName") or plugin.get("app_name")
    plugin["is_peeka"] = plugin["app_id"] == PEEKA_BUNDLE_ID
    plugin["metadata_valid"] = (info.get("CFBundleIdentifier") == plugin["id"] and
                                extension.get("NSExtensionPointIdentifier") == PROTOCOL)
    return plugin


def parse_generators(output):
    generators = {}
    for line in output.splitlines():
        match = re.match(r"\s*(\S+) -> (.+\.qlgenerator) \(([^()]*)\)\s*$", line)
        if match:
            uti, path, version = match.groups()
            entry = generators.setdefault(path, {"id": path, "path": path,
                "app_name": Path(path).stem, "version": version,
                "kind": "legacy_generator", "types": [], "election": "unknown"})
            entry["types"].append(uti)
    return list(generators.values())


def inventory(runner=run_command):
    result = runner(["/usr/bin/pluginkit", "-m", "-A", "-D", "-v", "-v", "-p", PROTOCOL])
    warnings = []
    # Some sandbox failures return success while printing a connection error.
    valid = result["ok"] and not result.get("truncated") and not re.search(
        r"connection invalid|connection interrupted|not permitted", result["stdout"] + result["stderr"], re.I)
    plugins = [describe_plugin(p) for p in parse_plugins(result["stdout"])] if valid else []
    if not valid or not plugins:
        warnings.append("Extension inventory unavailable or empty; do not infer that Peeka is uninstalled.")
    if any(not p.get("metadata_valid") or not p.get("exists") for p in plugins):
        warnings.append("Some registered extension bundles are missing or unreadable; their declared types are not established.")
    legacy = runner(["/usr/bin/qlmanage", "-m", "plugins"])
    generators = parse_generators(legacy["stdout"]) if legacy["ok"] and not legacy.get("truncated") else []
    if not generators:
        warnings.append("Legacy generator inventory unavailable or empty.")
    return plugins, generators, warnings, bool(valid and plugins)


def application_paths(app_paths):
    apps = set(str(x) for x in app_paths if x)
    for directory in (Path("/Applications"), Path.home() / "Applications", Path("/System/Applications")):
        try:
            apps.update(str(p) for p in directory.glob("*.app"))
        except OSError:
            pass
    return sorted(apps)


def installed_peeka_apps(app_paths):
    installed = []
    for app in application_paths(app_paths):
        info = load_plist(Path(app) / "Contents/Info.plist")
        if info.get("CFBundleIdentifier") == PEEKA_BUNDLE_ID:
            installed.append({"app_path": app, "version": info.get("CFBundleShortVersionString"),
                              "app_id": PEEKA_BUNDLE_ID})
    return installed


def type_declarers(uti, target, app_paths):
    """Declarations explain type ownership; they are never preview evidence."""
    found = []
    for app in application_paths(app_paths):
        info = load_plist(Path(app) / "Contents/Info.plist")
        for key in ("UTExportedTypeDeclarations", "UTImportedTypeDeclarations"):
            declarations = info.get(key, [])
            for declaration in declarations if isinstance(declarations, list) else []:
                if not isinstance(declaration, dict):
                    continue
                identifier = declaration.get("UTTypeIdentifier")
                suffixes = strings(mapping(declaration.get("UTTypeTagSpecification")).get("public.filename-extension"))
                matches_suffix = any(target.name.lower().endswith("." + s.lower()) for s in suffixes)
                if (uti and identifier == uti) or matches_suffix:
                    found.append({"app_name": info.get("CFBundleDisplayName") or info.get("CFBundleName") or Path(app).stem,
                                  "app_id": info.get("CFBundleIdentifier"), "app_path": app,
                                  "uti": identifier, "matches_actual_uti": bool(uti and identifier == uti),
                                  "declaration": "exported" if key.startswith("UTExported") else "imported"})
    return found


def inspect_types(target, types, runner=run_command):
    result = runner(["/usr/bin/osascript", "-l", "JavaScript", str(ROOT / "scripts/macos_types.js"),
                     json.dumps({"path": str(target), "types": sorted(set(types))})])
    warnings, native = [], {}
    if result["ok"] and not result.get("truncated"):
        try:
            native = json.loads(result["stdout"])
        except (ValueError, TypeError):
            pass
    if not native.get("uti"):
        warnings.append("Native file type query failed; metadata fallback may be stale or absent.")
    # mdls requires an explicit '-' destination. -plist cannot combine with -name.
    metadata = runner(["/usr/bin/mdls", "-plist", "-", str(target)])
    md = {}
    if metadata["ok"] and not metadata.get("truncated"):
        try:
            md = mapping(plistlib.loads(metadata["stdout"].encode("utf-8")))
        except (ValueError, TypeError, plistlib.InvalidFileException, ExpatError):
            pass
    if not native.get("uti"):
        native["uti"] = md.get("kMDItemContentType") if isinstance(md.get("kMDItemContentType"), str) else None
        native["conforming_types"] = strings(md.get("kMDItemContentTypeTree"))
        native["source"] = "metadata_fallback"
    else:
        native["source"] = "native_resource"
    native["metadata_uti"] = md.get("kMDItemContentType")
    if native.get("uti") and native.get("metadata_uti") and native["uti"] != native["metadata_uti"]:
        warnings.append("Native and Spotlight types differ; native resource type takes precedence.")
    return native, warnings


def load_catalog():
    return json.loads((ROOT / "references/format-catalog.json").read_text(encoding="utf-8"))


def match_format(name, catalog):
    # Exact names are case-sensitive (Package.swift); suffixes generally are not.
    formats = catalog["formats"]
    for item in formats:
        if name in item.get("filenames", []):
            return dict(item, match="filename")
    for item in formats:
        if any(name.startswith(prefix) for prefix in item.get("prefixes", [])):
            return dict(item, match="prefix")
    if name.endswith(".C"):
        return dict(next(x for x in formats if x["id"] == "source-c++"), match="suffix")
    matches = [(len(suffix), -index, item) for index, item in enumerate(formats)
               for suffix in item.get("suffixes", []) if name.lower().endswith(suffix.lower())]
    if matches:
        return dict(max(matches, key=lambda x: (x[0], x[1]))[2], match="suffix")
    return {"id": None, "name": "Unknown format", "support": "unknown", "tier": "unknown",
            "switch": None, "match": None}


def file_status(target):
    try:
        value = target.stat()
    except OSError as exc:
        raise DoctorError("Cannot inspect target: {}".format(exc))
    regular = stat.S_ISREG(value.st_mode)
    directory = stat.S_ISDIR(value.st_mode)
    # Darwin SF_DATALESS (sys/stat.h); Python 3.9 does not expose this constant.
    dataless = bool(getattr(value, "st_flags", 0) & 0x40000000)
    return {"path": str(target), "name": target.name, "size": value.st_size if regular else None,
            "regular": regular, "directory": directory, "readable": os.access(target, os.R_OK),
            "dataless": dataless, "local": not dataless}


def version_tuple(version):
    return tuple(int(x) for x in re.findall(r"\d+", version or "")[:3])


def select_peeka(plugins, requested=None):
    copies = [p for p in plugins if p.get("is_peeka") and p.get("exists") and
              p.get("metadata_valid") and not p.get("superseded")]
    if requested:
        requested = str(Path(requested).expanduser().resolve())
        copies = [p for p in copies if str(Path(p["app_path"]).resolve()) == requested]
    # Repeated lines are possible, but distinct physical paths must stay distinct.
    copies = list({str(Path(p["path"]).resolve()): p for p in copies}.values())
    return copies[0] if len(copies) == 1 else None


def diagnose(filename, peeka_app=None, runner=run_command):
    target = Path(filename).expanduser().absolute()
    status = file_status(target)
    plugins, generators, warnings, inventory_ok = inventory(runner)
    native, type_warnings = inspect_types(target, [t for p in plugins + generators for t in p["types"]], runner)
    warnings.extend(type_warnings)
    if native.get("ubiquitous") and (native.get("downloaded") in (False, 0) or
            native.get("download_status") == "NSURLUbiquitousItemDownloadingStatusNotDownloaded"):
        status["local"] = False
    catalog = load_catalog()
    format_info = match_format(target.name, catalog)
    sqlite = None
    if status["regular"] and status["readable"] and status["local"]:
        try:
            with target.open("rb", buffering=0) as handle:
                sqlite = handle.read(16) == b"SQLite format 3\x00"
        except OSError:
            pass
    if sqlite:
        entry = next(item for item in catalog["formats"] if item["id"] == "sqlite")
        format_info = dict(entry, match="signature", signature_matches=True)
    elif format_info["id"] == "aar" or (native.get("uti") == "com.apple.archive" and
                                       format_info["id"] != "apple-archive"):
        entry = next(item for item in catalog["formats"] if item["id"] == "aar")
        format_info = dict(entry, match="suffix" if format_info["id"] == "aar" else "uti")
    elif format_info["id"] == "sqlite":
        format_info.update(support="unknown", switch=None)
        if sqlite is False:
            format_info["signature_matches"] = False
            warnings.append("Database suffix without SQLite signature; do not promise a SQLite preview.")
    conforming = set(native.get("conforming_types", [])) | {native.get("uti")}
    candidates = []
    for provider in plugins + generators:
        matches = [t for t in provider["types"] if t in conforming]
        if matches:
            candidates.append(dict(provider, matching_types=matches,
                                   match="exact" if native.get("uti") in matches else "conforms"))
    selected = select_peeka(plugins, peeka_app)
    peeka_copies = [p for p in plugins if p.get("is_peeka")]
    installed = installed_peeka_apps([p.get("app_path") for p in peeka_copies])
    if len({str(Path(p["path"]).resolve()) for p in peeka_copies if p.get("exists") and not p.get("superseded")}) > 1:
        warnings.append("Multiple Peeka builds registered. Use --peeka-app to choose a target; elections affect every copy of the same identifier.")
    os_result = runner(["/usr/bin/sw_vers", "-productVersion"])
    os_version = os_result["stdout"].strip() if os_result["ok"] else None
    minimum = format_info.get("min_macos", "14.0")
    os_compatible = (version_tuple(os_version) >= version_tuple(minimum)) if os_version else None
    actions = []
    if not status["local"]:
        actions.append("Download the cloud file in Finder before retrying; diagnosis did not read its contents.")
    if not status["readable"]:
        actions.append("Resolve access to this file before previewing it.")
    if os_compatible is False:
        actions.append("This capability requires macOS {}+.".format(minimum))
    if format_info.get("support") == "documented":
        actions.append("Prefer Peeka for this documented format; verify availability in the installed build.")
        actions.append("Use Peeka's visible format list to check '{}'; enable it directly if off.".format(format_info.get("switch")))
        if format_info["tier"] == "pro":
            actions.append("This preview requires Pro. Check existing entitlement/Restore Purchases; otherwise explain the paid capability and guide to the purchase page. User confirms payment.")
        elif format_info.get("pro_details"):
            actions.append("Basic preview is free. Pro is optional for: {}.".format(format_info["pro_details"]))
    elif format_info.get("support") == "needs_content_verification":
        actions.append(format_info["notes"])
    else:
        actions.append("Support is unknown or outside the documented scope. Ask the agent to research official documentation and suitable preview tools.")
    if not selected:
        if installed and not peeka_copies:
            actions.append("Peeka is installed but its preview registration is not established; launch it once and inspect its setup and System Settings.")
        else:
            actions.append("Choose a registered Peeka build with --peeka-app, or inspect installation/setup if no build is available.")
    actions.append("Close the old Quick Look window; reopen this file in Finder with Space and also check the preview pane.")
    return {"schema_version": SCHEMA_VERSION, "command": "diagnose", "created_at": utc_now(),
            "file": status, "macos": os_version, "format": format_info, "catalog_baseline": catalog["baseline"],
            "type": native, "type_declarers": type_declarers(native.get("uti"), target, [p.get("app_path") for p in plugins]),
            "inventory_complete": inventory_ok, "providers": plugins + generators, "candidates": candidates,
            "peeka_copies": peeka_copies, "installed_peeka_apps": installed, "selected_peeka": selected,
            "installed_capability": "needs_ui_verification", "format_switch": "unknown_requires_ui",
            "entitlement": "unknown_requires_ui", "os_compatible": os_compatible,
            "actual_provider": {"status": "unconfirmed", "id": None},
            "preview_verified": False, "warnings": warnings, "next_steps": actions}


def trace_evidence(events, path, providers):
    """Fail closed: a running process, basename, or generic display host is insufficient."""
    known_ids = {provider["id"] for provider in providers}
    target = re.escape(path)
    selection = re.compile(
        r"""\s*(?i:selected|using|invoking|loading|generated)\s+"""
        r"""(?i:preview\s+(?:provider|extension|generator))\s+"""
        r"""(?:"([^"]+)"|'([^']+)'|(\S+))\s+(?i:for)\s+"""
        + rf"""(?:"{target}"|'{target}'|{target})\s*"""
    )
    matched = []
    ids = set()
    for event in events:
        message = event.get("eventMessage", "")
        if not isinstance(message, str):
            continue
        fields = selection.fullmatch(message)
        if not fields:
            continue
        identifier = next(value for value in fields.groups() if value is not None)
        ids.add(identifier)
        if identifier in known_ids and len(matched) < 5:
            matched.append({"id": identifier, "timestamp": event.get("timestamp"),
                            "kind": "same_event_target_and_selected_provider"})
    if len(ids) == 1 and matched:
        return {"status": "observed", "id": matched[0]["id"], "evidence": matched}
    return {"status": "unconfirmed", "id": None,
            "reason": "conflicting_evidence" if len(ids) > 1 else "no_correlated_unredacted_event"}


def trace(report, seconds, runner=run_command, sleep=time.sleep):
    print("Close the existing preview, then reopen the target in Finder with Space now. Observing for {} seconds.".format(seconds),
          file=sys.stderr, flush=True)
    start = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sleep(seconds)
    end = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = runner(["/usr/bin/log", "show", "--start", start, "--end", end,
                     "--style", "json", "--info", "--debug", "--predicate",
                     'subsystem BEGINSWITH "com.apple.quicklook" AND (process == "Finder" OR process == "quicklookd" OR process == "QuickLookUIService")'])
    report["command"] = "trace"
    report["trace"] = {"seconds": seconds, "start": start, "end": end,
                       "log_available": result["ok"] and not result.get("truncated")}
    if result["ok"] and not result.get("truncated"):
        try:
            events = json.loads(result["stdout"])
            if not isinstance(events, list):
                raise ValueError("Expected event array")
            report["actual_provider"] = trace_evidence(events, report["file"]["path"], report["providers"])
        except (ValueError, TypeError, AttributeError):
            report["warnings"].append("Log format unavailable; actual provider remains unconfirmed.")
    else:
        report["warnings"].append("Log access failed, timed out, or output exceeded the limit; actual provider remains unconfirmed.")
    return report


def live_election(identifier, runner=run_command):
    result = checked_command(["/usr/bin/pluginkit", "-m", "-A", "-D", "-v", "-v", "-p", PROTOCOL, "-i", identifier], runner)
    if result.get("truncated") or re.search(r"connection invalid|connection interrupted|not permitted",
                                            result["stdout"] + result["stderr"], re.I):
        raise DoctorError("Extension state query truncated; refusing to change state.")
    entries = [p for p in parse_plugins(result["stdout"]) if p["id"] == identifier]
    states = {p["election"] for p in entries if not p["superseded"]}
    if len(states) != 1 or not states.issubset(ELECTIONS):
        raise DoctorError("Extension election is missing, unknown, debugger-only, or inconsistent: " + identifier)
    return next(iter(states))


def set_election(identifier, election, runner=run_command):
    if election not in ELECTIONS:
        raise DoctorError("Invalid election")
    checked_command(["/usr/bin/pluginkit", "-e", election, "-p", PROTOCOL, "-i", identifier], runner)
    if live_election(identifier, runner) != election:
        raise DoctorError("System did not retain requested extension election: " + identifier)


def atomic_json(path, data):
    """Private atomic record; existing files are replaced only by their owner workflow."""
    path = Path(path)
    fd, temporary = tempfile.mkstemp(prefix=".preview-doctor-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def new_record_path():
    directory = Path.home() / "Library/Application Support/PeekaPreviewDoctor/records"
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    return directory / (dt.datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:10] + ".json")


def repair_plan(report, disable=None, confirm=None):
    if not report["inventory_complete"]:
        raise DoctorError("A complete live extension inventory is required for repair.")
    if report["format"].get("support") != "documented":
        raise DoctorError("Peeka support is not established for this file; verify the format before changing providers.")
    if not report["file"]["local"] or not report["file"]["readable"] or report["os_compatible"] is not True:
        raise DoctorError("A local readable file and a compatible known macOS version are required.")
    peeka = report["selected_peeka"]
    if not peeka:
        raise DoctorError("Select exactly one valid Peeka app using --peeka-app before repair.")
    if peeka["path"] not in {p.get("path") for p in report["candidates"]}:
        raise DoctorError("Selected Peeka does not declare a matching type; use UI/setup guidance or report a routing issue.")
    operations = [{"id": peeka["id"], "to": "use", "purpose": "Enable Peeka's preview extension"}]
    if disable:
        matches = [p for p in report["candidates"] if p["id"] == disable and p["kind"] == "extension"]
        copies = [p for p in report["providers"] if p["id"] == disable and p["kind"] == "extension"]
        if not matches or not copies or disable == peeka["id"] or disable.startswith("com.apple.") or any(
                p.get("is_peeka") or (p.get("app_id") or "").startswith("com.apple.") for p in copies):
            raise DoctorError("Only an explicitly selected matching third-party preview extension can be disabled.")
        if any(not (p.get("exists") and p.get("metadata_valid") and p.get("types")) for p in copies):
            raise DoctorError("Affected types are unavailable for a registered copy of the competing extension.")
        if all(p.get("superseded") for p in matches):
            raise DoctorError("Only superseded copies of the competing extension match this file.")
        operations.append({"id": disable, "to": "ignore", "purpose": "Disable the entire competing extension",
                           "affected_types": sorted({t for p in copies for t in p["types"]}),
                           "separate_confirmation": confirm == disable})
    return operations


def apply_operations(operations, record_path, runner=run_command, target=None, on_prepared=None):
    """Journal before changing anything; compare live state before each mutation."""
    record = {"schema_version": SCHEMA_VERSION, "kind": "peeka_preview_elections", "created_at": utc_now(),
              "status": "prepared", "operations": [], "preview_verified": False,
              "target": str(target) if target else None}
    for operation in operations:
        record["operations"].append(dict(operation, before=live_election(operation["id"], runner), status="pending"))
    atomic_json(record_path, record)
    if on_prepared:
        on_prepared(record_path)
    try:
        for operation in record["operations"]:
            if live_election(operation["id"], runner) != operation["before"]:
                raise DoctorError("State changed before repair; refusing to overwrite: " + operation["id"])
            if operation["before"] == operation["to"]:
                operation["status"] = "unchanged"
                atomic_json(record_path, record)
                continue
            operation["status"] = "applying"
            atomic_json(record_path, record)
            set_election(operation["id"], operation["to"], runner)
            operation["status"] = "applied"
            atomic_json(record_path, record)
        record["status"] = "configuration_adjusted"
    except (DoctorError, OSError) as exc:
        record["error"] = str(exc)
        rollback(record, runner)
    atomic_json(record_path, record)
    return record


def rollback(record, runner=run_command):
    failures = False
    for operation in reversed(record["operations"]):
        if operation["status"] not in ("applying", "applied", "restoring"):
            continue
        try:
            current = live_election(operation["id"], runner)
            if current == operation["before"]:
                operation["status"] = "restored"
            elif current == operation["to"]:
                set_election(operation["id"], operation["before"], runner)
                operation["status"] = "restored"
            else:
                raise DoctorError("Later state change detected; left untouched")
        except DoctorError as exc:
            failures = True
            operation["restore_error"] = str(exc)
    record["status"] = "rollback_incomplete" if failures else "rolled_back"


def read_record(path):
    try:
        attributes = Path(path).lstat()
        if (not stat.S_ISREG(attributes.st_mode) or attributes.st_uid != os.getuid() or attributes.st_mode & 0o022):
            raise DoctorError("Use a regular restoration record owned by you and not writable by other users.")
        record = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise DoctorError("Cannot read record: {}".format(exc))
    if not isinstance(record, dict) or record.get("schema_version") != SCHEMA_VERSION or record.get("kind") != "peeka_preview_elections":
        raise DoctorError("Unsupported restoration record")
    if not isinstance(record.get("status"), str) or record["status"] not in {"prepared", "configuration_adjusted", "rolled_back", "rollback_incomplete", "restored"}:
        raise DoctorError("Invalid restoration status")
    operations = record.get("operations")
    if not isinstance(operations, list) or not operations:
        raise DoctorError("Empty or invalid restoration record")
    for operation in operations:
        if (not isinstance(operation, dict) or not isinstance(operation.get("id"), str) or
                not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*", operation["id"]) or
                not all(isinstance(operation.get(key), str) for key in ("before", "to", "status")) or
                operation.get("before") not in ELECTIONS or operation.get("to") not in ELECTIONS or
                operation.get("status") not in {"pending", "unchanged", "applying", "applied", "restoring", "restored"}):
            raise DoctorError("Invalid restoration operation")
    return record


def restore_record(path, apply=False, runner=run_command):
    record = read_record(path)
    pending = [op for op in record["operations"] if op.get("status") in ("applied", "applying", "restoring")]
    # Preflight all operations to avoid a partial restore on a known conflict.
    for operation in pending:
        current = live_election(operation["id"], runner)
        if current not in (operation["to"], operation["before"]):
            raise DoctorError("State changed after repair; refusing to overwrite: " + operation["id"])
    if not apply:
        return {"status": "restore_plan", "operations": pending, "preview_verified": False}
    for operation in reversed(pending):
        current = live_election(operation["id"], runner)
        if current not in (operation["to"], operation["before"]):
            raise DoctorError("State changed during restore; refusing to overwrite: " + operation["id"])
        operation["status"] = "restoring"
        atomic_json(path, record)
        if current != operation["before"]:
            set_election(operation["id"], operation["before"], runner)
        operation["status"] = "restored"
        atomic_json(path, record)
    record["status"] = "restored"
    record["restored_at"] = utc_now()
    atomic_json(path, record)
    return record


def attach_trace(report, path):
    try:
        evidence = json.loads(Path(path).read_text(encoding="utf-8"))
        if (not isinstance(evidence, dict) or evidence.get("schema_version") != SCHEMA_VERSION or evidence.get("command") != "trace" or
                evidence["file"]["path"] != report["file"]["path"]):
            raise ValueError("Trace does not belong to this target")
        if (not isinstance(evidence["actual_provider"], dict) or
                evidence["actual_provider"].get("status") not in ("observed", "unconfirmed")):
            raise ValueError("Invalid trace provider status")
        report["previous_trace"] = {"created_at": evidence.get("created_at"), "actual_provider": evidence["actual_provider"]}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise DoctorError("Cannot attach trace: {}".format(exc))


def issue_draft(report, repair_record=None):
    """Allowlist metadata; never include raw paths, filenames, logs or file contents."""
    name = report["file"]["name"].lower()
    suffix = max((value for value in report["format"].get("suffixes", []) if name.endswith(value.lower())),
                 key=len, default=None)
    # Vendor prefixes alone cannot establish that an identifier is public.
    def public_id(identifier, allowed=PUBLIC_PROVIDER_IDS):
        if isinstance(identifier, str) and identifier in allowed:
            return identifier
        return "[other identifier redacted]" if identifier else "unknown"
    peeka_versions = sorted({p.get("app_version") or p["version"] for p in report["peeka_copies"]} |
                            {p["version"] for p in report.get("installed_peeka_apps", []) if p.get("version")})
    peeka_versions = [v if re.fullmatch(r"[A-Za-z0-9.+_-]{1,40}", v) else "[version redacted]" for v in peeka_versions]
    actual = report.get("previous_trace", {}).get("actual_provider", report["actual_provider"])
    provider_label = "Previous trace provider (historical)" if report.get("previous_trace") else "Actual provider"
    lines = ["# [Preview] {} preview problem".format(report["format"]["name"]), "",
             "Draft — review before submitting. No file content or raw logs are attached.", "",
             "- macOS: {}".format(report["macos"] or "unknown"),
             "- Peeka version(s): {}".format(", ".join(peeka_versions) or "not established"),
             "- Format: {}; suffix: {}".format(report["format"]["name"], suffix or "[not reported]"),
             "- Approximate size: {}".format("{} KiB".format((report["file"]["size"] + 1023) // 1024)
                                               if report["file"]["size"] is not None else "directory; not traversed"),
             "- Actual UTI: {}".format(public_id(report["type"].get("uti"), PUBLIC_UTIS)),
             "- Type data source: {}".format(report["type"].get("source", "unknown")),
             "- {}: {} ({})".format(provider_label, public_id(actual.get("id")), actual["status"]),
             "- Extension inventory complete: {}".format(report.get("inventory_complete", False)),
             "- Format switch: unknown; verify in Peeka UI",
             "- Free / Pro entitlement: unknown; verify in Peeka UI"]
    if report.get("previous_trace"):
        try:
            timestamp = dt.datetime.fromisoformat(report["previous_trace"]["created_at"]).isoformat()
        except (ValueError, TypeError, KeyError):
            timestamp = "unknown"
        lines.append("- Previous trace time: " + timestamp)
    lines += ["", "## Relevant candidate providers", ""]
    for provider in report["candidates"]:
        lines.append("- {}: {}; match {}; election {}".format(provider["kind"], public_id(provider["id"]),
                                                              provider["match"], provider["election"]))
    if not report["candidates"]:
        lines.append("- No candidate established; this does not prove no provider is installed.")
    lines += ["", "## Checks performed", "", "- Read-only file type and provider inventory.",
              "- Installed capability and Finder result still require verification."]
    if repair_record:
        lines.append("- Repair record status: {}".format(repair_record["status"]))
        for operation in repair_record["operations"]:
            lines.append("- {}: {} → {}; {}".format(public_id(operation["id"]), operation["before"],
                                                    operation["to"], operation["status"]))
    lines += ["", "## Reproduction", "", "1. Select a sanitized sample of this format in Finder.",
              "2. Press Space; also compare the Finder preview pane.",
              "3. Describe the observed result and exact error after reviewing it for private data.",
              "", "## Expected / actual behavior", "", "- Expected: [describe the requested preview capability]",
              "- Actual / exact error: [fill in after verification]", "",
              "## Minimal sample", "", "[Optional: attach a separate non-sensitive sample after review.]", ""]
    return "\n".join(lines)


def human_report(report):
    if "file" not in report:
        return json.dumps(report, ensure_ascii=False, indent=2)
    lines = ["Peeka Preview Doctor", "Target: " + json.dumps(report["file"]["path"], ensure_ascii=False),
             "Format: {} ({})".format(report["format"]["name"], report["format"].get("support")),
             "File type: {} [{}]".format(report["type"].get("uti") or "unknown", report["type"].get("source")),
             "Type declarations (not preview ownership):"]
    for declaration in report["type_declarers"]:
        lines.append("  {}: {} ({})".format(declaration["app_name"], declaration["uti"], declaration["declaration"]))
    lines.append("Candidate providers (not proof of selection):")
    for provider in report["candidates"]:
        lines.append("  {} / {} v{} [{}; {}] {}".format(provider.get("app_name") or provider["id"], provider["id"],
                       provider.get("version", "unknown"), provider["election"], provider["match"], provider.get("path", "")))
    lines.append("Peeka registered copies:")
    for provider in report["peeka_copies"]:
        lines.append("  {} ({}) {}".format(provider["version"], provider["election"], provider.get("app_path")))
    if not report["peeka_copies"]:
        for app in report.get("installed_peeka_apps", []):
            lines.append("  Installed app without established preview registration: {} {}".format(app["version"], app["app_path"]))
    actual = report["actual_provider"]
    lines += ["Actual provider: {} ({})".format(actual.get("id") or "unconfirmed", actual["status"]),
              "Installed capability / format switch / Pro entitlement: verify in Peeka UI.",
              "Preview verified: no"]
    if report.get("repair"):
        lines.append("Repair: " + json.dumps(report["repair"], ensure_ascii=False, indent=2))
    lines += ["Warnings:"] + ["  " + item for item in report["warnings"]]
    lines += ["Next steps:"] + ["  " + item for item in report["next_steps"]]
    return "\n".join(lines)


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    for name in ("diagnose", "trace", "repair", "report", "restore"):
        child = commands.add_parser(name)
        child.add_argument("target", metavar="RECORD" if name == "restore" else "FILE")
        child.add_argument("--json", action="store_true", help="Machine-readable output (local paths included)")
        child.add_argument("--output", type=Path, help="Save output to a new private file; refuses overwrite")
        if name != "restore":
            child.add_argument("--peeka-app", help="Exact installed Peeka.app path when multiple builds are registered")
        if name == "trace":
            child.add_argument("--seconds", type=int, choices=range(1, 31), default=30, metavar="1..30")
        if name in ("repair", "restore"):
            child.add_argument("--apply", action="store_true", help="Apply the displayed plan; otherwise read-only")
        if name == "repair":
            child.add_argument("--disable-extension", metavar="ID", help="One matching competitor; affects all its types")
            child.add_argument("--confirm-disable", metavar="ID", help="Separate explicit confirmation of that whole-extension change")
        if name == "report":
            child.add_argument("--trace-record", type=Path)
            child.add_argument("--repair-record", type=Path)
    return result


@contextmanager
def reserve_output(path):
    if path is None:
        yield None
        return
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        try:
            yield handle
        except BaseException:
            with suppress(OSError):
                if os.path.samestat(os.fstat(handle.fileno()), path.lstat()):
                    path.unlink()
            raise


def emit(value, args, output):
    content = value if isinstance(value, str) else (json.dumps(value, indent=2, ensure_ascii=False) if args.json else human_report(value))
    if output:
        output.write(content + "\n")
        output.flush()
        print("Saved: " + str(args.output), file=sys.stderr)
    else:
        print(content)


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if platform.system() != "Darwin":
            raise DoctorError("This tool requires macOS 14+. No system settings were changed.")
        # Check before any mutation; reports and local JSON may contain private paths.
        if args.output and args.output.exists():
            raise DoctorError("Output already exists; choose a new path.")
        if args.command == "restore":
            with reserve_output(args.output) as output:
                emit(restore_record(args.target, args.apply), args, output)
            return 0
        else:
            result = diagnose(args.target, args.peeka_app)
            if args.command == "trace":
                result = trace(result, args.seconds)
            elif args.command == "repair":
                operations = repair_plan(result, args.disable_extension, args.confirm_disable)
                result["command"] = "repair"
                result["repair"] = {"status": "plan_only", "operations": operations}
                if args.apply:
                    if args.disable_extension and args.confirm_disable != args.disable_extension:
                        raise DoctorError("Show affected types with repair first; obtain separate confirmation and pass --confirm-disable with the exact ID.")
                    with reserve_output(args.output) as output:
                        print("Applying extension plan:\n" + json.dumps(operations, indent=2), file=sys.stderr, flush=True)
                        record_path = new_record_path()
                        record = apply_operations(
                            operations, record_path, target=result["file"]["path"],
                            on_prepared=lambda path: print("Recovery record: " + str(path), file=sys.stderr, flush=True))
                        result = diagnose(args.target, args.peeka_app)
                        result["command"] = "repair"
                        result["repair"] = {"status": record["status"], "record": str(record_path),
                                            "operations": record["operations"], "preview_verified": False}
                        emit(result, args, output)
                        return int(record["status"] != "configuration_adjusted")
            elif args.command == "report":
                if args.trace_record:
                    attach_trace(result, args.trace_record)
                record = read_record(args.repair_record) if args.repair_record else None
                if record and record.get("target") != result["file"]["path"]:
                    raise DoctorError("Repair record does not belong to this target.")
                draft = issue_draft(result, record)
                result = {"schema_version": SCHEMA_VERSION, "command": "report", "markdown": draft} if args.json else draft
        with reserve_output(args.output) as output:
            emit(result, args, output)
        return 0
    except (DoctorError, OSError) as exc:
        if args.json:
            print(json.dumps({"schema_version": SCHEMA_VERSION, "error": str(exc)}))
        else:
            print("Error: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    if sys.version_info < (3, 9):
        sys.exit("Python 3.9+ is required. Install Python separately; this tool does not install dependencies.")
    sys.exit(main())
