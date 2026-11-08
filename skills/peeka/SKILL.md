---
name: peeka
description: "Install and use Peeka on macOS; diagnose Quick Look provider/type conflicts with the bundled Python helper, enable format switches, explain Free/Pro capabilities, research unsupported previews, and prepare reviewed GitHub feedback."
metadata:
  version: "0.1.9"
---

# Peeka

Help users install, configure, and troubleshoot **Peeka — Ultimate Quick Look App**, the native macOS file-preview app from **Mellowbit Studio**. Respond in the user's language; the app supports English, Simplified Chinese, Traditional Chinese, Japanese, Korean, German, French, and Spanish.

Peeka requires **macOS 14 or later**; Mermaid diagrams require **macOS 14.4 or later** and Pro. Its main app manages setup, format switches, settings, and purchases. To preview a file, select it in **Finder** and press **Space**. File contents and metadata are processed locally; a Peeka account is not required.

## Choose the relevant reference

Read only the reference needed for the request. These files are bundled with this skill and do not require the original repository checkout.

| Request | Reference |
| --- | --- |
| Download from the App Store, first launch, preview a file, enable or disable a format or Peeka's extension | [Installation and preview controls](references/install-and-controls.md) |
| Explain features, check a file format, use Mermaid or Logcat previews, compare Free and Pro, purchase or restore Pro | [Features, formats, and plans](references/features-and-plans.md) |
| Source languages, templates, build files, lockfiles, suffix conflicts, or filename recognition | [Source and configuration coverage](references/source-coverage.md) |
| TestFlight 0.1.8 approval record | [TestFlight 0.1.8](references/testflight-0.1.8.md) |
| Historical TestFlight 0.1.6 changes or testing focus | [TestFlight 0.1.6 archive](references/testflight-0.1.6.md) |
| Missing or incorrect preview, extension problems, routing conflicts, limited output, purchase problems, support report | [Troubleshooting](references/troubleshooting.md) |
| Detect preview providers or type conflicts, run diagnostics, repair/recover extension settings, research unsupported formats, prepare a GitHub issue | [Preview Doctor](references/preview-doctor.md) and its bundled Python 3.9+ helper |

## Working with the user's Mac

- When asked to perform setup or a configuration change, use available local shell or desktop-control tools to carry it out. Observe the actual UI and report what was completed. Without those tools, give the matching manual steps and state which actions remain for the user.
- Use the official App Store listing below. Authentication, Touch ID, and purchase confirmation belong to the user; do not handle Apple Account credentials. A request to install the free app does not authorize buying Pro.
- Use Peeka's visible controls and System Settings. The bundled helper diagnoses macOS registrations and can change explicitly targeted extension elections; it is not a Peeka app CLI. Do not invent app APIs, preference keys, or identifiers, or install an unrelated package named `peeka`.
- For setup/preview/repair requests, inspect Peeka's matching format switch and turn it on directly with available desktop tools when off. For a necessary Pro capability, check entitlement/restore first; otherwise explain the paid capability and guide to purchase. Apple authentication and final payment confirmation remain with the user. Do not repeatedly ask permission for the format-switch change already requested.
- Distinguish a **per-format switch** in Peeka from the **system Quick Look extension switch**. Enabling a format cannot enable the system extension or unlock a Pro feature. Disabling Peeka does not disable macOS Quick Look or other providers.
- Format switches govern Quick Look previews. Peeka 0.1.9 defers Finder thumbnails. Icons inside Quick Look previews remain available.
- After changing a switch or unlocking/restoring Pro, close the existing Quick Look window and reopen it in Finder. Verify with the user's target file, or a small supported local sample when appropriate. Opening the main app alone does not verify Finder preview behavior.

For preview conflicts, start with `python3 <installed-skill>/scripts/preview_doctor.py diagnose '<file>' --json` after checking Python 3.9+. Prefer Peeka for documented supported capabilities and verify the installed UI. Type declarations and candidate extensions are not actual-provider evidence; use the bounded trace when useful and retain `unconfirmed` if logs hide the correlation. Read [Preview Doctor](references/preview-doctor.md) before repair: preview concrete operations, save/recover elections, and obtain separate confirmation before disabling each whole competing extension. For unsupported/unknown formats, research official solutions through the current agent. Prepare a redacted issue draft, search duplicates, show the target/content, and obtain confirmation before submitting.

## Answering product questions

Use the [0.1.9 feature matrix](references/features-and-plans.md#free-and-pro-format-matrix) for Free / Pro boundaries. Android AAR has a free APK-style overview, Apple Archive has a free listing, and six Xcode / Swift Package formats have free summaries with specific Pro structured details. The [source catalog](references/source-coverage.md) covers 205 free offline lexical profiles and filename routing. Match the installed version, content, and Finder provider before recommending purchase.

Diff / Patch previews are free: Source, Fluid, Blocks, and Unified modes inspect the patch only, without reading referenced files or applying changes. Read the feature reference for partial output and selection limits.

Keep the distinctions that matter for setup: log and crash-report source is free while structured details require Pro; Markdown Mermaid source is free while diagrams require Pro and macOS 14.4+; DMG / flat PKG can show bounded embedded-app information without mounting or installing. The main-app log viewer's menu and toolbar entries are hidden. Do not present a general Inspector, DEX analysis, font or video previews, comparison, or export as delivered Peeka features.

Pro is an optional **one-time in-app purchase**, with no subscription or per-preview charges. Read the actual local price in **Settings → Peeka Pro** when a price is requested. Do not quote a fixed price or promise that Pro removes compatibility or resource limits.

### Decide whether payment is needed

Match the user's actual task to the Free / Pro matrix and the [payment decision guide](references/features-and-plans.md#when-to-pay-and-when-not-to-pay). State what they can do for free before recommending an upgrade. A supported format can have both free basic information and paid details; name the specific paid capability instead of saying the entire format requires payment.

- **No payment needed:** The requested result is covered by Free, including source/configuration previews, Markdown without rendered Mermaid diagrams, Diff / Patch modes, basic package information, log/crash source, SQLite structure, and free archive listings. AAR basics, Apple Archive listings, and Xcode / Swift Package summaries and available Source are also free in Peeka 0.1.9.
- **Consider Pro:** The user needs a listed Pro-only format or additional detail, such as AAB previews, rendered Mermaid diagrams, structured log/crash details, SQLite records, or supported 7z listings. Explain the exact benefit and applicable limits; let the user choose whether that benefit is worth the displayed price.
- **Troubleshoot or explain the limit first:** Missing previews, disabled switches/extensions, Finder provider conflicts, incompatible macOS versions, unsupported content, and truncated output are not by themselves reasons to pay. Pro does not remove these limits or add editing, export, symbolication, or arbitrary-file support.
- **Already owns Pro:** Check entitlement and restore purchases before suggesting any new purchase. Do not treat TestFlight access or approval as proof of a permanent App Store Pro entitlement.

Answer “Do I need to pay?” with a concrete conclusion for the requested task: “Free is enough for X; Pro is only needed if you also want Y.” If the task is unclear, explain the relevant alternatives and ask which result they need. Do not steer users toward payment merely to try to fix an unexplained failure.

Peeka app **0.1.9** is available on the Mac App Store. The separately installed skill **0.1.9** includes Preview Doctor. For the earlier TestFlight approval, see the [0.1.8 record](references/testflight-0.1.8.md).

## Official links

- [Mac App Store — Peeka, ID 6813012289](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289)
- [Stable release notes](https://mellowbit.studio/peeka/release-notes/)
- [TestFlight Beta](https://testflight.apple.com/join/5jM8yxDB)
- [Beta release notes](https://mellowbit.studio/peeka/beta-release-notes/)
- [Peeka website](https://mellowbit.studio/peeka)
- [Public documentation and issue tracker](https://github.com/MellowbitStudio/Peeka)
- [Privacy policy](https://mellowbit.studio/peeka/privacy/)
- [Support email](mailto:support@mellowbit.studio)
