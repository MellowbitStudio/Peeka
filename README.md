# Peeka

**Ultimate Quick Look App**

English · [简体中文](README.zh-CN.md)

Peeka is a native macOS app that brings developer-friendly previews to Finder. Select a supported file and press **Space** to explore application packages, read highlighted source code, browse structured data, inspect SQLite schemas, and view archive listings.

[Download on the App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Website](https://mellowbit.studio/peeka) · [Report an issue](https://github.com/MellowbitStudio/Peeka/issues) · [Privacy policy](https://mellowbit.studio/peeka/privacy/)

Requires **macOS 14 or later**. Available in **English and Simplified Chinese**.

## Features

- **Application packages:** View available icons, names, identifiers, versions, system requirements, and architectures for Android and Apple packages. Compatible packages with embedded icons can also receive Finder thumbnails.
- **Source code:** Read common development languages with syntax highlighting, line numbers, native text selection, and copy. Enable or disable previews for each source language in Peeka.
- **Markdown:** Preview formatted documents with highlighted code blocks, tables, and read-only task lists.
- **Structured data:** Switch between Source, Outline, and Mindmap views for JSON, YAML, TOML, and INI. Expand or collapse structures, and pan or zoom mindmaps with your trackpad.
- **SQLite:** View database summaries and table structure for free. Peeka Pro adds read-only record pages and BLOB prefix previews.
- **Archives:** Browse supported archive listings without extracting files to disk, with list and column views for navigating folders.
- **Local processing:** File contents and metadata are processed on your Mac. No Peeka account is required.

## Supported formats

| Category | Free previews | Peeka Pro additions |
| --- | --- | --- |
| Android packages | APK | AAB, APKS, XAPK, APKM, AAR; additional permission and signing summaries where available |
| Apple packages | IPA, APP, APPEX; outer metadata for DMG and flat PKG | XCArchive, XCFramework, provisioning profiles, dylib; signing metadata where available |
| Source code | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documents and configuration | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist, CSV / TSV; dotenv key names only | — |
| Databases | SQLite summaries and table structure (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Read-only record pages and BLOB prefix previews |
| Archives | ZIP, TAR, TAR.GZ / TGZ, GZ metadata, JAR / WAR listings | Supported 7z listings and JAR / WAR manifest details |

Preview availability depends on file contents and macOS choosing Peeka's extension. TypeScript `.ts` / `.mts` and dotenv files have Finder routing limitations. YAML and TOML structure views support bounded subsets of their syntax.

## Get started

1. Download Peeka from the [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289), or visit the [Peeka website](https://mellowbit.studio/peeka) to learn more about the app.
2. Launch Peeka after installation. Follow the setup guidance and enable its Quick Look extension in **System Settings** if needed.
3. Check that the relevant format is enabled in Peeka's format list.
4. Select a supported file in **Finder** and press **Space**.

After changing a format switch or unlocking Pro, close and reopen the Quick Look preview. The main app provides setup guidance, format controls, settings, and purchasing; file previews appear in Finder.

## Peeka Pro

Peeka includes free previews for common formats. **Peeka Pro** is an optional **one-time in-app purchase**, with **no subscription or per-preview charges**, that unlocks the additional formats and details listed above.

Purchase or restore Pro in **Settings → Peeka Pro**. The app displays the local price supplied by Apple's StoreKit.

Some previews have limits:

- SQLite record pages show up to **100 rows**, within a **1 MiB** display budget. BLOB previews read at most the first **4 KiB**. Peeka does not edit or maintain databases.
- Signing metadata describes available signing information; it does not verify signature validity.
- Encrypted, solid, or unsupported 7z variants may not list. Archive listings are bounded and may be incomplete for large archives.

Resource and compatibility limits apply to both Free and Pro previews.

## Feedback and support

For bug reports and feature requests, [open an issue](https://github.com/MellowbitStudio/Peeka/issues). Include your macOS version, Peeka version, file format, reproduction steps, and expected behavior. A screenshot or a small non-sensitive sample can help diagnose preview issues.

You can also email [support@mellowbit.studio](mailto:support@mellowbit.studio).

## About this repository

This is Peeka's public product and feedback repository, maintained by [Mellowbit Studio](https://mellowbit.studio/peeka). It contains product information and public documentation. **The app's source code is not included in this repository.**
