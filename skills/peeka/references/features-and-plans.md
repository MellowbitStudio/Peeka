# Features, supported formats, and plans

Documented baseline from [Peeka's public README](https://github.com/MellowbitStudio/Peeka#readme), reviewed **2026-10-04**. A later installed version or official release may differ. Format support depends on file contents, resource limits, and macOS routing to Peeka's extension.

## What Peeka does

| Capability | Behavior |
| --- | --- |
| Application packages | Show available icons, names, identifiers, versions, system requirements, and architectures for Android and Apple packages. Compatible packages with embedded icons can also receive Finder thumbnails. Metadata availability varies by package. |
| Source code | Syntax highlighting, line numbers, native text selection, and copy; source-language previews can be enabled or disabled independently in Peeka. |
| Markdown | Formatted documents with highlighted code blocks, tables, and read-only task lists. |
| Structured data | JSON, YAML, TOML, and INI offer **Source / 源码**, **Outline / 大纲**, and **Mindmap / 思维导图** views. Structures can expand or collapse; trackpads can pan and zoom mindmaps. Do not extend this three-view claim to every configuration format. |
| SQLite | Database summaries and table structure are free. Pro adds read-only record pages and BLOB prefix previews. |
| Archives | Browse supported archive listings without extracting files to disk. List and column views support folder navigation. |
| Local processing | File contents and metadata stay on the Mac for processing. No Peeka account is needed. |

## Free and Pro format matrix

The **Pro additions** column supplements the free capabilities; it does not replace them.

| Category | Free | Peeka Pro additions |
| --- | --- | --- |
| Android packages | APK | AAB, APKS, XAPK, APKM, AAR; additional permission and signing summaries where available |
| Apple packages | IPA, APP, APPEX; **outer metadata** for DMG and **flat PKG** | XCArchive, XCFramework, provisioning profiles, dylib; signing metadata where available |
| Source code | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | No additional source languages documented |
| Documents and configuration | Markdown; JSON / JSONL / NDJSON; XML; YAML; TOML; INI; properties; EditorConfig; plist; CSV / TSV; dotenv **key names only** | No additional document/configuration formats documented |
| SQLite databases | Summaries and table structure for `.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb` files containing SQLite data | Read-only record pages and BLOB prefix previews |
| Archives | ZIP; TAR; TAR.GZ / TGZ; GZ **metadata**; JAR / WAR **listings** | Supported 7z **listings** and JAR / WAR **manifest details** |

For unlisted formats or source-file suffixes, check the installed app's format list or current official documentation before claiming support. A file ending in `.db` need not be a SQLite database.

## Limits that affect answers

- **Finder routing:** TypeScript `.ts` / `.mts` and dotenv files have routing limitations. A recognized format can still be handled by macOS or another extension. Pro does not guarantee provider selection.
- **Structured data:** YAML and TOML structure views support bounded subsets of their syntax. Do not promise complete syntax coverage.
- **SQLite:** Record pages show at most **100 rows**, within a **1 MiB** display budget. BLOB previews read at most the first **4 KiB**. Peeka does not edit or maintain databases, and these previews are not a full data export.
- **Signing:** Signing metadata describes available information; it does **not verify signature validity**.
- **7z and archives:** Encrypted, solid, or unsupported 7z variants may not list. Archive listings are bounded and large archives can be incomplete. Listing support does not imply extraction or editing support.
- **Package/container scope:** DMG and flat PKG support is for outer metadata. GZ support is for metadata. Do not promise browsing or extracting their payloads.
- **Free and Pro:** Both tiers retain resource and compatibility limits. No broader numeric file-size or entry-count guarantee is documented here.

## Purchase and restore

Peeka provides free previews for common formats. **Peeka Pro** is an optional **one-time in-app purchase** with **no subscription and no per-preview charges**.

Open **Peeka → Settings → Peeka Pro / 设置 → Peeka Pro** to buy or restore. The app displays the local price supplied by **Apple StoreKit**; use that displayed price for the user's storefront instead of hard-coding a currency or amount. Let the user complete authentication and purchase confirmation. Buy Pro only when the user has authorized that purchase.

For an existing purchase, use the restore action in the same section and the Apple Account used for the purchase. Once the app reports an unlock or restore, close and reopen Finder Quick Look. A purchase message alone does not verify a particular file's preview. For a failed restore or a preview that remains locked, see [troubleshooting](troubleshooting.md).
