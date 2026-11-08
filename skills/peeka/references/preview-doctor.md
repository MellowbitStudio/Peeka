# Preview Doctor

The bundled **skill 0.1.9** adds local diagnosis for macOS 14+. The helper ships with the separately installed agent skill. Use it for wrong, generic, empty, or missing Finder previews. Responses and UI guidance follow the user's language.

## Run the helper

Check `python3 --version`: Python **3.9+**, standard library only. No pip package, compiler, model API key, or background service is needed. If Python is absent or macOS prompts to install developer tools, explain the missing dependency; the helper does not install it.

Run from the installed skill directory, replacing the script path below accordingly. Sibling resources travel with the skill; the original repository checkout is not needed. These examples assume the repository root:

```sh
python3 skills/peeka/scripts/preview_doctor.py diagnose '/path/to/diagram.mmd'
python3 skills/peeka/scripts/preview_doctor.py diagnose '/path/to/diagram.mmd' --json
python3 skills/peeka/scripts/preview_doctor.py trace '/path/to/diagram.mmd' --seconds 30 --json --output '/tmp/peeka-trace.json'
python3 skills/peeka/scripts/preview_doctor.py repair '/path/to/diagram.mmd'
python3 skills/peeka/scripts/preview_doctor.py repair '/path/to/diagram.mmd' --apply
python3 skills/peeka/scripts/preview_doctor.py restore '/path/to/repair-record.json'
python3 skills/peeka/scripts/preview_doctor.py restore '/path/to/repair-record.json' --apply
python3 skills/peeka/scripts/preview_doctor.py report '/path/to/diagram.mmd' --output '/tmp/peeka-issue.md'
```

Diagnosis, tracing, reporting, and repair/restore **without `--apply`** do not change settings. `--output` creates a private file and refuses overwrite. Normal diagnosis/trace JSON includes local paths and is for local use. `report` creates a redacted Markdown draft; `report --json` wraps that Markdown without embedding the private diagnosis.

Exit 1 means invalid input, refused/failed mutation, or a command-level error. Diagnosis can exit 0 with unavailable evidence: inspect `warnings`, `inventory_complete`, and `unknown` / `unconfirmed` fields. An unavailable service or sandbox restriction does not establish that Peeka is uninstalled. Use the agent's normal permission mechanism for read-only host queries when available; otherwise report missing evidence. Do not run diagnosis with `sudo`.

## Interpret the report

- `format`: documented support, name/suffix match, tier, minimum macOS, format switch, optional Pro details. The [machine catalog](format-catalog.json) follows the 0.1.9 release. Verify the installed version and its visible controls.
- `type` / `type_declarers`: actual resource UTI, Spotlight fallback, and imported/exported app declarations. A declaration explains a suffix collision without proving preview ownership. The scan covers top-level standard application directories and parents of registered extensions, not every app on disk.
- `candidates`: modern extensions and legacy generators declaring an exact or conforming type. Eligibility is not proof of selection; inspect recorded election/superseded state.
- `peeka_copies` / `selected_peeka`: registered paths and versions. If several valid copies exist, choose the intended app with `--peeka-app '/exact/path/Peeka.app'`. Elections affect **every copy of the same identifier**, not just that path.
- `installed_peeka_apps`: apps found in the scanned locations, including installations whose preview extension is not registered. Missing registration does not mean the app is uninstalled.
- `actual_provider`: tracing requires a selection event containing the full target path and known provider identifier. A process, default opening app, basename, generic Quick Look host, or redacted log is insufficient. Missing evidence means **unconfirmed**.
- `installed_capability`, `format_switch`, `entitlement`: require visible UI verification. The helper does not read undocumented Peeka preferences or infer Pro from version numbers.

During `trace`, close the old preview and reopen the target in Finder with Space within the indicated 1–30 seconds. Avoid other previews during comparison. Log queries are bounded; raw messages are not included in results. Privacy redaction often prevents attribution. A provider invocation does not establish successful rendering. Historical trace evidence is labeled as previous evidence, not a new observation.

## Make a supported file work

1. Diagnose the target. Resolve cloud download/access first. Prefer **Peeka** for documented supported capabilities, checking the installed build and actual content, especially `.db`, `.aar`, `.ts`, and `.mmd`. Generic `public.data` information is not specialized support.
2. **Operate Peeka directly for setup, preview, or repair requests.** With available desktop tools, open the selected app, search the format list, inspect the matching switch, and turn it on if off. Do not merely give manual steps when you can operate the UI. For an ambiguous `.aar`, identify the content before choosing the Android AAR, Apple Archive, or ZIP switch. Use shared alias switches. Standalone `.mmd` / `.mermaid` uses Mermaid, fenced diagrams use Markdown. A diagnosis-only request does not request settings changes.
3. For a necessary **Pro** capability, inspect entitlement first. If already owned, use Restore Purchases before suggesting payment. Otherwise explain the specific paid benefit and guide to **Settings → Peeka Pro**, or the purchase page opened by the switch. The user completes sign-in, Touch ID, and final purchase confirmation. Do not click the final payment confirmation or handle credentials. Free basics are sufficient when they meet the task; payment does not repair routing or content limits.
4. For the system extension, inspect `repair FILE` before `repair FILE --apply`, or operate the matching System Settings control. Script repair requires a complete inventory, one valid selected Peeka build, matching type, local readable target, and compatible known macOS. Enabling an extension cannot force Finder provider selection.
5. For a confirmed competitor or an explicitly explained comparison, show a concrete plan:

   ```sh
   python3 skills/peeka/scripts/preview_doctor.py repair '/path/to/diagram.mmd' --disable-extension 'observed.competitor.identifier'
   ```

   Explain all declared affected types and all copies of the identifier. **Obtain separate confirmation for this whole extension**, even after a general repair request. Then repeat with `--apply --confirm-disable 'observed.competitor.identifier'`. The CLI accepts one competitor per invocation; do not loop over competitors or infer consent for others. System extensions, legacy generators, and unidentified extensions are ineligible. Give manual steps for legacy conflicts; do not delete/move generators.
6. Close and reopen the file in Finder; verify Space and the preview pane. Report configuration success, observed provider, and successful rendering separately. Never mark previews verified from command success alone. Restore temporary comparisons, or unsuccessful changes when they should not remain.

### Recovery

Before any election change, original `use` / `ignore` / `default` states are saved in a private JSON journal under `~/Library/Application Support/PeekaPreviewDoctor/records/`. Results give its exact path. Unknown/debugger-only/inconsistent states stop repair. The helper does not modify original files, opening associations, app bundles, format preferences, global caches, or the Launch Services database.

Partial failures trigger compare-and-restore rollback. For incomplete rollback, preserve the record and inspect live state; do not report success. `restore RECORD` previews recovery; `restore RECORD --apply` performs it. Recovery refuses a later **different** election, and restores `default` as default. An external change away and back to the same value cannot be detected. UI format-switch changes are outside this journal: record their prior state in the chat. Restore only tool-generated records for the intended operation.

## Unsupported formats and GitHub

For `unknown` or `outside_documented_scope`, establish the actual format and intended result. Use the current AI agent's web tools to research official documentation and trustworthy projects, preferring existing macOS capabilities where suitable. Distinguish Finder Quick Look from opening an editor or converting a separate copy. Explain whether the option supplies a preview, source view, or another result. Research does not authorize software installation, uploads, file execution, or purchases.

For unresolved Peeka issues, generate `report FILE`; optionally add `--trace-record '/path/to/trace.json'` and `--repair-record '/path/to/repair-record.json'` from the same target. The allowlisted draft omits raw logs, filenames, private paths, contents, and unknown third-party identifiers. Review it and fill the expected/actual behavior, sanitized exact error, observed UI switch/entitlement, reproduction, and relevant public competitor name. Review additions and any separate minimal sample for private information.

Use [MellowbitStudio/Peeka](https://github.com/MellowbitStudio/Peeka/issues) for Peeka bugs/features. Establish the official repository before reporting another tool. Search duplicates and recommend a suitable existing report when available. Show the complete draft and target repository, **obtain submission confirmation**, then submit using an available GitHub connector or authenticated CLI and return the link. If unavailable, leave the concrete draft. The helper never submits issues automatically.

## Maintenance and validation

Maintain `format-catalog.json` with the feature/source references, distinguishing released support from dated source capabilities. Runtime uses JSON rather than parsing Markdown. Tests check all 205 source profiles and their documented suffix/name rules; add behavioral cases for changed capabilities.

```sh
python3 -m unittest discover -s skills/peeka/scripts -p 'test_*.py' -v
```

Interfaces: [Quick Look supported types](https://developer.apple.com/documentation/quicklook), `man pluginkit`, `qlmanage -h`, and [Login Items & Extensions](https://support.apple.com/guide/mac-help/change-login-items-extensions-settings-mtusr003/mac). PlugInKit interventions are limited maintenance operations, not a permanent global priority API.
