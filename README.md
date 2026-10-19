# Peeka

**Ultimate Quick Look App**

English · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Peeka is a native macOS app that brings developer-friendly previews to Finder. Select a supported file and press **Space** to explore application packages, read highlighted source code, browse structured data, inspect SQLite schemas, and view archive listings.

[Download on the App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Website](https://mellowbit.studio/peeka) · [Report an issue](https://github.com/MellowbitStudio/Peeka/issues) · [Privacy policy](https://mellowbit.studio/peeka/privacy/)

Requires **macOS 14 or later**; Mermaid diagrams require **macOS 14.4+** and Pro. Available in **English, Simplified Chinese, Traditional Chinese, Japanese, Korean, German, French, and Spanish**.

**Peeka 0.1.5 has passed App Store review and is officially available**, as confirmed on **2026-10-19**. The capabilities below follow the 0.1.5 product baseline reviewed **2026-10-19**, including native Diff / Patch previews and Mermaid updates. Update older installations through the App Store; preview availability also depends on file compatibility and Finder provider selection.

## Features

- **Application packages:** View available icons, names, identifiers, versions, system requirements, and architectures for Android and Apple packages. Compatible packages with embedded icons can also receive Finder thumbnails.
- **Source code:** Read common development languages with syntax highlighting, line numbers, native text selection, and copy. Enable or disable previews for each source language in Peeka.
- **Diff / Patch:** Free Source, Fluid, Blocks, and Unified views with file selection, original line numbers, and change counts. Inspect patches without applying them or reading referenced files.
- **Markdown:** Preview formatted documents with highlighted code blocks, horizontally scrolling tables, read-only task lists, and permitted local images.
- **Mermaid:** Preview standalone diagrams or diagrams inside Markdown, with source views and vector zoom/pan. Graphical rendering requires Pro and macOS 14.4+; Markdown fenced source remains free.
- **Logs and crash reports:** Read highlighted log, Android Logcat, and crash-report source for free. Pro adds bounded summaries and structured details for recognized content.
- **DMG and flat PKG:** Inspect metadata and bounded embedded-app names/icons without mounting images or installing packages.
- **Structured data:** Switch between Source, Outline, and Mindmap views for JSON, YAML, TOML, and INI. Expand or collapse structures, and pan or zoom mindmaps with your trackpad.
- **SQLite:** View database summaries and table structure for free. Peeka Pro adds read-only record pages and BLOB prefix previews.
- **Archives:** Browse supported archive listings without extracting files to disk, with list and column views for navigating folders.
- **Local processing:** File contents and metadata are processed on your Mac. No Peeka account is required.

## Supported formats

| Category | Free previews | Peeka Pro additions |
| --- | --- | --- |
| Android packages | APK | AAB, APKS, XAPK, APKM, AAR; bounded permissions, signing, and manifest-derived summaries where available |
| Apple packages | IPA, APP, APPEX; DMG / flat PKG metadata and bounded embedded-app information | XCArchive, XCFramework, provisioning profiles, dylib; signing metadata where available |
| Source code | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documents and configuration | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist and related Apple configuration files, CSV / TSV, TXT / TEXT plain source; dotenv key names only | — |
| Mermaid | Highlighted Mermaid fenced source in Markdown | Standalone `.mmd` / `.mermaid` and Markdown diagrams (macOS 14.4+) |
| Logs and reports | Highlighted `.log` / `.out` / `.trace`, `.crash`, `.ips`, and recognized JSONL / NDJSON logs | Bounded summaries and structured details, including Android Logcat / Android Studio layouts |
| Databases | SQLite summaries and table structure (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Read-only record pages and BLOB prefix previews |
| Archives | ZIP, TAR, TAR.GZ / TGZ, GZ metadata, JAR / WAR listings | Supported 7z listings and JAR / WAR manifest details |

Preview availability depends on file contents and macOS choosing Peeka's extension. TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS, and some plist / CSV files have known provider or routing limitations. YAML and TOML structure views support bounded subsets of their syntax. TXT / TEXT stays plain source without automatic log or document detection.

## Get started

1. Download Peeka from the [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289), or visit the [Peeka website](https://mellowbit.studio/peeka) to learn more about the app.
2. Launch Peeka after installation. Follow the setup guidance and enable its Quick Look extension in **System Settings** if needed.
3. Check that the relevant format is enabled in Peeka's format list.
4. Select a supported file in **Finder** and press **Space**.

After changing a format switch or unlocking Pro, close and reopen the Quick Look preview. The main app provides setup guidance, format controls, settings, and purchasing; file previews appear in Finder.

Preview switches do not control package thumbnails, which are independent of Pro. The main-app log viewer's menu/toolbar entries are hidden; a general Inspector, comparison/export, and Peeka font/video previews are not delivered.

## Peeka Pro

Peeka includes free previews for common formats. **Peeka Pro** is an optional **one-time in-app purchase**, with **no subscription or per-preview charges**, that unlocks the additional formats and details listed above.

Purchase or restore Pro in **Settings → Peeka Pro**. The app displays the local price supplied by Apple's StoreKit.

Some previews have limits:

- SQLite record pages show up to **100 rows**, within a **1 MiB** display budget. BLOB previews read at most the first **4 KiB**. Peeka does not edit or maintain databases.
- Signing metadata describes available signing information; it does not verify signature validity.
- Logs and reports show only bounded source/details; statistics describe the parsed preview, not the whole file. Structured IPS support targets standard crash reports (309), without symbolication.
- Mermaid supports 20 diagram families in the documented 0.1.5 baseline. Unsupported syntax, directives, or resource limits fall back to highlighted source with a reason.
- Encrypted, solid, or unsupported 7z variants may not list. Archive listings are bounded and may be incomplete for large archives.

Resource and compatibility limits apply to both Free and Pro previews.

## AI agent skill

The public [`peeka` skill](skills/peeka/SKILL.md), version **0.1.5**, helps Codex, Claude Code, and other compatible agents install Peeka from the App Store, explain supported formats and Free / Pro features, enable or disable previews, and troubleshoot issues.

After the skill is published to this repository's default branch, install it with:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

This installs the agent skill; download the Peeka app separately from the Mac App Store. See the [skill installation guide](skills/README.md) for targeting agents, global installation, and local testing. Desktop actions require local tools; Apple Account authentication and purchase confirmation remain with you.

## Feedback and support

For bug reports and feature requests, [open an issue](https://github.com/MellowbitStudio/Peeka/issues). Include your macOS version, Peeka version, file format, reproduction steps, and expected behavior. A screenshot or a small non-sensitive sample can help diagnose preview issues.

You can also email [support@mellowbit.studio](mailto:support@mellowbit.studio).

## About this repository

This is Peeka's public product and feedback repository, maintained by [Mellowbit Studio](https://mellowbit.studio/peeka). It contains product information and public documentation. **The app's source code is not included in this repository.**
