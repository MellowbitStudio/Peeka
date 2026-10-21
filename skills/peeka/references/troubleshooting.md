# Troubleshooting Peeka

Skill **0.1.6**, product baseline reviewed **2026-10-19**. Peeka **0.1.5** has passed App Store review and is officially available, as confirmed by the maintainer on **2026-10-19**. Check for an App Store update on older builds, and match troubleshooting to the installed version and UI.

Peeka **0.1.6 (20261020.1)** has passed TestFlight review, confirmed by the maintainer on **2026-10-21**. The Mac App Store release remains **0.1.5**. Match guidance to the installed channel and build; see [TestFlight 0.1.6](testflight-0.1.6.md).

Use the documented product limits to separate configuration problems from unsupported files or macOS routing. Work from the observed symptom; avoid repeating checks already completed.

## Establish the symptom

Collect or inspect the relevant details:

- macOS version and Peeka version.
- File extension, actual file type, approximate size, and whether the file is available locally.
- What Finder shows after selecting the file and pressing Space: generic icon, plain text, another provider, locked feature, error, partial output, or empty preview.
- Whether Peeka's format switch and system Quick Look extension are enabled.
- Free or Pro status, and whether another small supported file previews correctly.

With local shell access, `sw_vers -productVersion` reports the macOS version. Read the Peeka version from its visible app information or installed bundle metadata; do not guess its install path or bundle identifier. Diagnose only the files relevant to the request.

## Diff / Patch shows Source or partial output

Enhanced Diff modes are free. A new preview always starts in Source; select Fluid, Blocks, or Unified when complete hunks are available. Binary or metadata-only patches do not contain text changes to display. Unsupported syntax, malformed counts, and truncated input can leave only Source or prior complete hunks with an explanation. Consecutive mail patches are supported, including unsigned output. For continuous selection across large-hunk fragments, switch to Source. Do not apply the patch or open its referenced files as a preview repair. See [Diff limits](features-and-plans.md#diff--patch-scope-and-limits).

## No Peeka preview, or only a generic icon

1. Confirm macOS 14 or later and launch the installed Peeka app once to follow setup guidance.
2. Check the target format's tier and limits in [features and plans](features-and-plans.md).
3. Check both the app's format switch and its system Quick Look extension using [installation and controls](install-and-controls.md).
4. Close the Quick Look window, select the locally available file in Finder, and press Space again.
5. Compare with a small known supported file, such as a simple `.json` or `.md` file. A comparison that works points toward file contents, format limits, or type routing; it does not prove every other format is configured correctly.
6. If the extension entry is missing or the problem affects multiple supported samples, check for an App Store update and relaunch Peeka. A normal Mac restart can be a later recovery step if registration still appears stale; let the user save work first.

App Store download failures occur before Peeka's preview extension is available. Inspect the Store's reported error, network availability, account state, and compatibility; do not treat purchasing Pro as a fix for installation.

## Finder uses another provider, or previews ignore a switch

macOS decides which Quick Look extension handles a file. Closing and reopening the preview is necessary after switch changes, but an enabled switch cannot force macOS to choose Peeka.

- For **`.ts` / `.mts`**, **dotenv**, **AAR**, **TXT / TEXT**, **IPS**, and some plist / CSV files, account for documented system-provider/type conflicts. Android AAR may be identified as Apple Archive; Peeka does not claim that broad type. Do not promise that a cache reset or Pro purchase resolves routing.
- A `.mmd` file may be assigned another app's Markdown type (including Ulysses). Current source declares a relevant candidate, but registration/type matching alone does not establish that Finder selected Peeka. Compare the observed preview and the installed build before calling it fixed.
- Check for another Quick Look provider if the visible preview appears to belong to another app. When testing a conflict, change one relevant provider at a time, record its prior setting, and restore settings after the comparison unless the user requested the new state.
- If Peeka was switched off, a macOS preview or another provider may still appear. Confirm that Peeka's handling is disabled rather than treating any remaining preview as a failed switch.
- Avoid renaming, overwriting, or changing file associations on the original file as a preview fix. Any experiment should use a separate non-sensitive sample.

## Only one file fails, or output is incomplete

| Symptom | What to check or explain |
| --- | --- |
| `.db` does not show database tables | The suffix is ambiguous; verify that it actually contains a SQLite database. |
| An extensionless database or unknown suffix gets a generic preview | Internal SQLite/content recognition does not guarantee Finder routing. Do not change the original filename or claim arbitrary-file support. |
| SQLite shows schema but no records | Schema is free; records and BLOB prefixes require Pro. Restore an existing purchase before suggesting a new purchase. |
| SQLite records or BLOBs are truncated | Pages have a 100-row and 1 MiB display limit; BLOBs show only the first 4 KiB. Pro retains these limits. |
| 7z listing is absent | Requires Pro and a supported variant. Encrypted, solid, or unsupported variants can still fail. |
| A large archive listing stops early | Bounded listings may be incomplete. No unlimited listing guarantee is documented. |
| YAML/TOML outline or mindmap differs from the full document | Structure views support bounded syntax subsets. Inspect the source view if available before concluding that data was lost. |
| dotenv shows keys without values | Key-name-only display is the documented behavior. Do not expose secret values in a support report. |
| DMG / flat PKG shows only metadata or a partial app list | Current source can inspect supported containers for app names/icons, within budgets. Unsupported/encrypted variants or limits may yield partial results; only complete inspection can establish that no app was found. Do not mount/install as a preview repair. |
| GZ only shows metadata | Standalone gzip does not browse payloads or verify total uncompressed size; TAR.GZ / TGZ has a separate listing path and switch. |
| A log has no structured mode or summary | Highlighted source is free; structured details require Pro and recognized content. TXT / TEXT does not detect logs; binary traces and `.logarchive` are outside support. |
| Logcat stays plain source or omits statistics | Check the actual layout. `raw` is plain text; `long` needs properly framed multiple records. Statistics cover parsed preview records, not the whole file; budget-truncated final lines do not supply guessed tags or severity. |
| An IPS report lacks structured crash details | Structured support targets standard crash reports (309). Other report types, damage, or truncation retain source; Peeka does not symbolicate or infer a crash cause. |
| Binary / OpenStep plist shows only keys | A key-name projection is intentional, not a full source dump; corrupt binary input does not fall back to unreadable text. |
| A Markdown image is missing | It must be an authorized regular local file inside the document directory and within image budgets. Remote/data URLs, traversal, and symlinks are blocked; adjacent-file sandbox access may be unavailable. |
| Signing information is absent or questioned | Metadata availability varies; Peeka is not a signature-validity verifier. |
| Finder thumbnail is missing | Only supported Android/Apple packages with readable embedded icons get Peeka thumbnails. Check the separate thumbnail extension and Finder icon-preview setting; Pro and preview switches do not gate thumbnails. DMG / PKG, text, diagrams, databases, and generic archives retain system icons. |

If a small supported file fails despite correct switches and tier, record its actual error and reproduction steps for support. Do not infer corruption merely from an extension failure.

## Framework or dSYM preview is missing

These Pro formats are included in the approved TestFlight 0.1.6 Beta; first check the installed version and channel, then check Pro and the individual Framework/dSYM switch. Frameworks may expand as directories in Finder column view; select the bundle and press Space. Neither format provides custom thumbnails. Static framework identity-only output and missing dSYM UUIDs are not evidence of a routing failure. See the [TestFlight 0.1.6 details](features-and-plans.md#testflight-016-beta).

## Mermaid shows source, no diagram, or no format switch

1. Check **macOS 14.4+** and an installed build containing Mermaid support. Earlier systems hide the standalone row and keep Markdown fences as highlighted source, without diagram controls.
2. Check Pro and the correct switch: standalone `.mmd` / `.mermaid` uses Mermaid; a Markdown fence uses Markdown. Enabling Mermaid cannot override a disabled Markdown switch.
3. Inspect the displayed fallback reason. Unsupported syntax, directives/front matter, truncated input, or graph/render budgets retain source. Compare with a small supported diagram, such as `flowchart LR` followed by `A --> B`, in a separate sample.
4. If a small graph also fails, preserve the exact rendering error and installed version. A rendering failure inside Peeka differs from Finder choosing another provider; purchasing again does not repair either.

## A main-app file-opening command is missing

The main app provides setup, the searchable format catalog, settings, and purchasing. Its retained log viewer's toolbar/menu and Open Log File / Command-O entries are hidden. Use Finder Space for previews; do not guide users to a delivered general Inspector, Mermaid editor/export, or log-opening menu. The main window is single-instance; Command-N does not create another window.

## Pro is still locked or restore fails

1. Open **Settings → Peeka Pro** and inspect the displayed entitlement or error.
2. Use the restore action with the Apple Account used for the purchase. Let the user handle sign-in or authentication. A Peeka account is not required.
3. Verify network access if StoreKit reports a connectivity problem; check for an App Store update if appropriate.
4. Once the app reports Pro as unlocked, close and reopen Quick Look and test the requested feature.
5. If entitlement remains missing or restore fails, preserve the displayed error and prepare a support report. Do not recommend buying again as the default remedy.

## Escalate with useful evidence

Prepare a report for [GitHub Issues](https://github.com/MellowbitStudio/Peeka/issues) or [support@mellowbit.studio](mailto:support@mellowbit.studio). Include:

```text
Title: [format] Brief description of the preview problem
macOS version:
Peeka version:
File format and approximate size:
Free / Pro status:
Relevant format switch and Quick Look extension state:
Steps to reproduce:
Expected behavior:
Actual behavior / exact error:
Checks already performed and their results:
Optional redacted screenshot or small non-sensitive sample:
```

Prepare the report in the chat or a local file. Send an email or submit an issue only when the user asks to do so. Omit credentials, dotenv values, private database records, signing keys, and other sensitive material from attached evidence; a minimal sanitized sample is preferable.

No Peeka-specific terminal repair commands are documented in this public skill. Use supported UI controls and observed evidence rather than guessed `defaults` keys, extension identifiers, preference deletion, or global Quick Look resets.

## Source

Product behavior and limitations: Peeka's 0.1.5 app source and canonical format/licensing documents, reviewed **2026-10-19**, summarized in [features and plans](features-and-plans.md). App Store approval and official availability of 0.1.5 were confirmed by the maintainer on **2026-10-19**. Public updates: [Peeka documentation](https://github.com/MellowbitStudio/Peeka#readme). The sequence is diagnostic guidance; some issues depend on file compatibility or macOS provider selection and may not have a local fix.
