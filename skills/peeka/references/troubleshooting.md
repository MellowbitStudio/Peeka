# Troubleshooting Peeka

Use the documented product limits to separate configuration problems from unsupported files or macOS routing. Work from the observed symptom; avoid repeating checks already completed.

## Establish the symptom

Collect or inspect the relevant details:

- macOS version and Peeka version.
- File extension, actual file type, approximate size, and whether the file is available locally.
- What Finder shows after selecting the file and pressing Space: generic icon, plain text, another provider, locked feature, error, partial output, or empty preview.
- Whether Peeka's format switch and system Quick Look extension are enabled.
- Free or Pro status, and whether another small supported file previews correctly.

With local shell access, `sw_vers -productVersion` reports the macOS version. Read the Peeka version from its visible app information or installed bundle metadata; do not guess its install path or bundle identifier. Diagnose only the files relevant to the request.

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

- For **`.ts` / `.mts`** and **dotenv**, explain the documented Finder routing limitation. Do not promise that a cache reset or Pro purchase will resolve it.
- Check for another Quick Look provider if the visible preview appears to belong to another app. When testing a conflict, change one relevant provider at a time, record its prior setting, and restore settings after the comparison unless the user requested the new state.
- If Peeka was switched off, a macOS preview or another provider may still appear. Confirm that Peeka's handling is disabled rather than treating any remaining preview as a failed switch.
- Avoid renaming, overwriting, or changing file associations on the original file as a preview fix. Any experiment should use a separate non-sensitive sample.

## Only one file fails, or output is incomplete

| Symptom | What to check or explain |
| --- | --- |
| `.db` does not show database tables | The suffix is ambiguous; verify that it actually contains a SQLite database. |
| SQLite shows schema but no records | Schema is free; records and BLOB prefixes require Pro. Restore an existing purchase before suggesting a new purchase. |
| SQLite records or BLOBs are truncated | Pages have a 100-row and 1 MiB display limit; BLOBs show only the first 4 KiB. Pro retains these limits. |
| 7z listing is absent | Requires Pro and a supported variant. Encrypted, solid, or unsupported variants can still fail. |
| A large archive listing stops early | Bounded listings may be incomplete. No unlimited listing guarantee is documented. |
| YAML/TOML outline or mindmap differs from the full document | Structure views support bounded syntax subsets. Inspect the source view if available before concluding that data was lost. |
| dotenv shows keys without values | Key-name-only display is the documented behavior. Do not expose secret values in a support report. |
| DMG, flat PKG, or GZ only shows metadata | The documented scope is metadata rather than general payload browsing. |
| Signing information is absent or questioned | Metadata availability varies; Peeka is not a signature-validity verifier. |
| Finder thumbnail is missing | Thumbnail support depends on a compatible package containing an available embedded icon. Preview success alone does not guarantee a thumbnail. |

If a small supported file fails despite correct switches and tier, record its actual error and reproduction steps for support. Do not infer corruption merely from an extension failure.

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

Product behavior and limitations: [Peeka public documentation](https://github.com/MellowbitStudio/Peeka#readme), reviewed **2026-10-04**. The troubleshooting sequence is diagnostic guidance built around that baseline, not a guarantee that every issue has a local fix.
