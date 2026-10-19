---
name: peeka
description: "Install and use Mellowbit Studio's Peeka Quick Look app on macOS. Use for App Store setup; package, source, Markdown, Mermaid, Diff / Patch, Logcat, crash-report, SQLite, and archive previews; Free versus Pro features; format and extension switches; and troubleshooting Finder previews."
metadata:
  version: "0.1.5"
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
| Missing or incorrect preview, extension problems, routing conflicts, limited output, purchase problems, support report | [Troubleshooting](references/troubleshooting.md) |

## Working with the user's Mac

- When asked to perform setup or a configuration change, use available local shell or desktop-control tools to carry it out. Observe the actual UI and report what was completed. Without those tools, give the matching manual steps and state which actions remain for the user.
- Use the official App Store listing below. Authentication, Touch ID, and purchase confirmation belong to the user; do not handle Apple Account credentials. A request to install the free app does not authorize buying Pro.
- Use Peeka's visible controls and System Settings. No public Peeka CLI, HTTP API, preference keys, or bundle identifiers are documented by this skill; do not invent them or install an unrelated package named `peeka`.
- Distinguish a **per-format switch** in Peeka from the **system Quick Look extension switch**. Enabling a format cannot enable the system extension or unlock a Pro feature. Disabling Peeka does not disable macOS Quick Look or other providers.
- Format switches govern Quick Look previews. Finder package thumbnails have separate extension and icon requirements; they do not require Pro and do not follow preview format switches.
- After changing a switch or unlocking/restoring Pro, close the existing Quick Look window and reopen it in Finder. Verify with the user's target file, or a small supported local sample when appropriate. Opening the main app alone does not verify Finder preview behavior.

## Answering product questions

Use the bundled feature matrix for the released baseline. The feature reference separately records development changes after the 0.1.5 tag (Framework, dSYM, and Pele); check the installed build before promising those capabilities. For a particular file, explain the supported category, the required tier, and any relevant content or routing limitation. Extension names alone do not guarantee compatibility; macOS chooses the preview provider.

Diff / Patch previews are free: Source, Fluid, Blocks, and Unified modes inspect the patch only, without reading referenced files or applying changes. Read the feature reference for partial output and selection limits.

Keep the distinctions that matter for setup: log and crash-report source is free while structured details require Pro; Markdown Mermaid source is free while diagrams require Pro and macOS 14.4+; DMG / flat PKG can show bounded embedded-app information without mounting or installing. The main-app log viewer's menu and toolbar entries are hidden. Do not present a general Inspector, DEX analysis, font or video previews, comparison, or export as delivered Peeka features.

Pro is an optional **one-time in-app purchase**, with no subscription or per-preview charges. Read the actual local price in **Settings → Peeka Pro** when a price is requested. Do not quote a fixed price or promise that Pro removes compatibility or resource limits.

Skill version **0.1.5** describes Peeka's **0.1.5 product baseline**, checked against the app's canonical format documentation and implementation on **2026-10-19**, including native Diff / Patch previews and Mermaid updates. **Peeka 0.1.5 has passed App Store review and is officially available**, as confirmed by the maintainer on **2026-10-19**. Users on older builds can update through the App Store. For changed behavior, check the installed app and current official sources when accessible; otherwise identify the answer as the bundled 0.1.5 baseline. Finder provider selection and file compatibility still determine actual preview behavior. This public repository contains product information and feedback, without app source code.

## Official links

- [Mac App Store — Peeka, ID 6813012289](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289)
- [Peeka website](https://mellowbit.studio/peeka)
- [Public documentation and issue tracker](https://github.com/MellowbitStudio/Peeka)
- [Privacy policy](https://mellowbit.studio/peeka/privacy/)
- [Support email](mailto:support@mellowbit.studio)
