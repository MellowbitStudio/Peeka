---
name: peeka
description: "Install and use Mellowbit Studio's Peeka Quick Look app on macOS. Use for App Store setup, supported file previews, Free versus Pro features, enabling or disabling formats and extensions, and troubleshooting Finder previews."
---

# Peeka

Help users install, configure, and troubleshoot **Peeka — Ultimate Quick Look App**, the native macOS file-preview app from **Mellowbit Studio**. Respond in the user's language; the app supports English and Simplified Chinese.

Peeka requires **macOS 14 or later**. Its main app manages setup, format switches, settings, and purchases. To preview a file, select it in **Finder** and press **Space**. File contents and metadata are processed locally; a Peeka account is not required.

## Choose the relevant reference

Read only the reference needed for the request. These files are bundled with this skill and do not require the original repository checkout.

| Request | Reference |
| --- | --- |
| Download from the App Store, first launch, preview a file, enable or disable a format or Peeka's extension | [Installation and preview controls](references/install-and-controls.md) |
| Explain features, check a file format, compare Free and Pro, purchase or restore Pro | [Features, formats, and plans](references/features-and-plans.md) |
| Missing or incorrect preview, extension problems, routing conflicts, limited output, purchase problems, support report | [Troubleshooting](references/troubleshooting.md) |

## Working with the user's Mac

- When asked to perform setup or a configuration change, use available local shell or desktop-control tools to carry it out. Observe the actual UI and report what was completed. Without those tools, give the matching manual steps and state which actions remain for the user.
- Use the official App Store listing below. Authentication, Touch ID, and purchase confirmation belong to the user; do not handle Apple Account credentials. A request to install the free app does not authorize buying Pro.
- Use Peeka's visible controls and System Settings. No public Peeka CLI, HTTP API, preference keys, or bundle identifiers are documented by this skill; do not invent them or install an unrelated package named `peeka`.
- Distinguish a **per-format switch** in Peeka from the **system Quick Look extension switch**. Enabling a format cannot enable the system extension or unlock a Pro feature. Disabling Peeka does not disable macOS Quick Look or other providers.
- After changing a switch or unlocking/restoring Pro, close the existing Quick Look window and reopen it in Finder. Verify with the user's target file, or a small supported local sample when appropriate. Opening the main app alone does not verify Finder preview behavior.

## Answering product questions

Use the bundled feature matrix for the documented baseline. For a particular file, explain the supported category, the required tier, and any relevant content or routing limitation. Extension names alone do not guarantee compatibility; macOS chooses the preview provider.

Pro is an optional **one-time in-app purchase**, with no subscription or per-preview charges. Read the actual local price in **Settings → Peeka Pro** when a price is requested. Do not quote a fixed price or promise that Pro removes compatibility or resource limits.

The product facts bundled here come from Peeka's public repository documentation, reviewed on **2026-10-04**. For a request about a newer release, current availability, or changed behavior, check the installed app and current official sources when accessible. If they are unavailable, identify the answer as the documented baseline rather than a live verification. This public repository contains product information and feedback, without app source code.

## Official links

- [Mac App Store — Peeka, ID 6813012289](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289)
- [Peeka website](https://mellowbit.studio/peeka)
- [Public documentation and issue tracker](https://github.com/MellowbitStudio/Peeka)
- [Privacy policy](https://mellowbit.studio/peeka/privacy/)
- [Support email](mailto:support@mellowbit.studio)
