# Features, supported formats, and plans

Skill **0.1.5** product baseline, checked against Peeka's 0.1.5 app source and canonical format/licensing documents on **2026-10-19**, including native Diff / Patch previews and Mermaid updates. Peeka **0.1.5** has passed App Store review and is officially available, as confirmed by the maintainer on **2026-10-19**. Check the installed version, visible controls, file compatibility, and Finder provider selection when behavior differs; use [official product documentation](https://github.com/MellowbitStudio/Peeka#readme) for public updates.

## Changes after the released baseline

The following is a separate development snapshot, checked against app commit `7acb35c` on **2026-10-19**, after the `0.1.5` tag. App Store availability of these changes has not been verified. Do not assume an installed 0.1.5 build includes them.

- **Framework (Pro):** `.framework` has an independent switch. Flat and versioned bundles show identity; readable Mach-O slices add architectures, UUIDs, declared platforms, and minimum system versions. Ordinary static ar frameworks show identity only. Internal version links must remain inside the bundle.
- **dSYM (Pro):** `.dSYM` has an independent switch and shows bounded binary names and per-architecture UUIDs. It does not expand DWARF symbols, symbolicate reports, or match files automatically. UUID presence does not prove symbol completeness; absent UUIDs remain unavailable.
- **Finder behavior:** Neither format has custom thumbnails. App validation records Space previews for both and column previews for dSYM; Framework remains a directory in Finder column view. Verify the user's installed build and actual result.
- **Mermaid:** Pele 1.6.0 replaces Mermaid.js for the same 20 diagram families, targeting Mermaid 12.1.0 syntax. It uses an offline system font and Peeka light/dark themes. Layout, default styles, and supported syntax are engine-specific; old Mermaid.js styling and connector workarounds no longer describe this renderer. Diagram/source controls, Pro and macOS 14.4 requirements remain. Fit can scale below 10% for large canvases; manual zoom remains 10%–400%.

The current renderer retains the bounded offline preview model: 1 MiB input, 50,000 UTF-16 units per diagram, 500 entities/connections, 5-second rendering, 8 MiB SVG/PDF, and at most 16 Markdown diagrams. Model and canvas-size limits can also trigger source fallback. Third-party license information is available in Settings → About → Third-party Licenses.

## What Peeka does

| Capability | Behavior |
| --- | --- |
| Application packages | Show available icons, names, identifiers, versions, system requirements, and architectures for Android and Apple packages. Supported packages with readable embedded icons can receive Finder thumbnails independently of Pro and preview switches. |
| DMG / flat PKG | Show metadata and bounded embedded-app names/icons without mounting images, installing packages, executing scripts, or extracting files to disk. Partial inspection is distinct from finding no app. |
| Source code | Lightweight syntax highlighting, line numbers, native selection and copy; each source language has its own preview switch. Highlighting does not validate or execute code. |
| Markdown | Native formatted documents with highlighted code blocks, horizontally scrolling tables, read-only task lists, and permitted local images. Mermaid fences have separate source/diagram rules below. |
| Mermaid | Standalone `.mmd` / `.mermaid` and diagrams inside Markdown, with diagram/source views and vector zoom/pan. Diagram rendering requires Pro and macOS 14.4+. |
| Structured data | JSON, YAML, TOML, and INI offer Source, Outline, and Mindmap views. Structures expand/collapse; mindmaps support trackpad pan and zoom. Other configuration formats do not inherit these three views. |
| Logs and crash reports | Free highlighted source with line numbers; Pro adds bounded summaries and structured details for recognized logs, Android Logcat, `.crash`, and supported `.ips` reports. |
| SQLite | Free summaries and table structure; Pro adds read-only record pages and BLOB prefix previews. |
| Archives | Bounded list/column views with folder navigation, without extraction or previews of contained file contents. |
| Local processing | Contents and metadata are processed on the Mac. No Peeka account is required. The interface supports English, Simplified/Traditional Chinese, Japanese, Korean, German, French, and Spanish. |

## Free and Pro format matrix

The **Pro additions** column supplements free capabilities. The app requires **macOS 14+**; Mermaid diagrams additionally require **14.4+**.

| Category | Free | Peeka Pro additions |
| --- | --- | --- |
| Android packages | APK identity, icon, version, SDK, architecture, and permission count | AAB, APKS, XAPK, APKM, AAR; bounded permission/signing and manifest-derived summaries where available |
| Apple packages | IPA, APP, APPEX; DMG / flat PKG metadata and bounded embedded-app information | XCArchive, XCFramework, `.mobileprovision` / `.provisionprofile`, dylib; signing metadata where available |
| Source code | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documents and configuration | Markdown; JSON / JSONL / NDJSON; XML; YAML; TOML; INI; properties; EditorConfig; plist / entitlements / xcprivacy / strings / stringsdict; CSV / TSV; dotenv key names only; TXT / TEXT plain source | — |
| Mermaid | Highlighted `mermaid` fenced source inside Markdown | Standalone `.mmd` / `.mermaid` previews and Markdown Mermaid diagrams, on macOS 14.4+ |
| Logs and reports | Highlighted source for `.log` / `.out` / `.trace`, `.crash`, `.ips`, and recognized JSONL / NDJSON logs | Detailed summaries and structured log/crash details, including recognized Android Logcat / Android Studio layouts |
| SQLite databases | Summaries and table structure for `.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb` containing SQLite data | Read-only record pages and BLOB prefix previews |
| Archives | ZIP; TAR; TAR.GZ / TGZ; GZ metadata; JAR / WAR listings | Supported 7z listings and JAR / WAR manifest details |

For unlisted suffixes, inspect the installed format catalog or current official documentation. A `.db` suffix does not establish SQLite content. Internal content recognition does not guarantee that Finder routes an unknown or extensionless file to Peeka.

## Development source catalog (checked 2026-10-21)

The development source now has 116 free lexical profiles, including Frontend & Templates and Build Scripts, shared with Markdown fences. See the [complete source catalog and suffix/routing limits](source-coverage.md). This expansion is separate from the released 0.1.5 matrix above; App Store / TestFlight availability is unconfirmed.

## Use the preview controls

- **Source / Outline / Mindmap:** These free modes share expansion state; new files start in Source. Structure extraction needs complete bounded input, at most 1,000 nodes and 32 levels. YAML / TOML / INI are conservative projections, not complete syntax parsers; unsupported structures retain Source. Mindmap zoom is 25%–300%.
- **Diff / Patch:** Free `.diff` / `.patch` previews start in Source; switch to Fluid, Blocks, or Unified for multi-file selection, old/new paths, original file line numbers, addition/deletion counts, and no-final-newline markers. Switching modes preserves the selected file and current hunk; reopening returns to Source. Copy omits line numbers and layout padding. For selection across large-hunk text fragments, use Source.
- **Logs:** New previews start in Source. With Pro, switch to structured details for time, level, and message plus available summaries. Counts and first/last timestamps cover the parsed preview only. JSONL logs use the JSONL switch; `.log` / `.out` / `.trace` share the Logs switch. TXT / TEXT remains plain source and does not automatically detect logs, Markdown, or JSON.
- **Mermaid:** Standalone files start in Diagram; switch to read-only Source as needed. The vector canvas supports pan, pinch zoom, 10%–400% zoom, 100%, and Fit to Window. The Mermaid switch controls standalone files; the Markdown switch controls Markdown files and their fences. On macOS before 14.4, Markdown fences retain highlighted source without diagram controls, and the standalone Mermaid catalog item is hidden.
- **SQLite:** Select a table and switch between Structure and Data. Data and clickable BLOB prefixes require Pro; views and virtual/shadow tables expose structure only. Generated columns appear in schema and are omitted from record reads.
- **Archives:** Switch between List and Columns; navigate folders and sort available columns. Only retained entries are browsable. These views do not extract or open entry contents.

### Mermaid syntax and limits (released 0.1.5)

The documented 0.1.5 baseline bundles Mermaid 12.2.0 and recognizes 20 diagram families: flowchart, sequence, class, state, ER, Gantt, pie, mindmap, timeline, Git graph, journey, quadrant, requirement, Sankey, XY chart, block, packet, kanban, radar, and treemap. Common aliases include `graph`, `stateDiagram-v2`, `sankey-beta`, `xychart-beta`, `block-beta`, `packet-beta`, `radar-beta`, and `treemap-beta`.

The 0.1.5 update refines light/dark diagram styling, Timeline/state themes, Sankey labels, and Kanban colors, and fixes connector/arrow semantics and rendering cancellation. Explicit colors, line widths, and automatic layout remain respected.

Unsupported syntax, configuration directives/front matter, or resource limits produce highlighted source and a reason. Rendering is offline with bundled scripts; user HTML/scripts, external resources, navigation, and click callbacks are blocked. It is a preview, without editing or export.

Files are read up to 1 MiB; truncated source is not rendered. Each diagram is limited to 50,000 UTF-16 units, 500 entities, 500 connections, 5 seconds, and 8 MiB of generated PDF. Markdown renders at most 16 diagrams. Pro retains all budgets. New syntax and registration have local implementation/rendering evidence; actual Finder selection and minimum-system acceptance remain separate checks.

### Diff / Patch scope and limits

Parses unified diff and Git text patches, including consecutive `git format-patch --stdout` mail patches with or without signatures, quoted/space/Unicode paths, renames, copies, and mode metadata. Reads only the bounded patch, without opening referenced paths or repositories, applying patches, staging, or merging. It cannot compare arbitrary files or expand missing context.

Input is limited to 1 MiB; enhanced views retain at most 256 files, 4,096 hunks, and 100,000 body lines across the input. Truncation or malformed counts retain prior complete hunks with a partial/damaged explanation. Unsupported constructs such as combined diff fall back to Source; binary and metadata-only changes show available metadata. No inline character differences are provided.

### Logcat and crash-report scope

Recognized Logcat layouts include `brief`, `process`, `tag`, `thread`, `time`, `threadtime`, and `long`, with supported epoch/monotonic timestamps, UID and ANSI-color modifiers, plus Android Studio layouts with or without package columns. Recognition depends on content. `raw` lacks distinguishable metadata and stays plain source; `long` requires at least two properly framed record blocks. Stack/continuation lines remain separate details. PID/TID/UID and Studio package columns remain in source rather than separate structured columns.

`.out` / `.trace` support readable UTF-8 logs, not binary trace formats. Log source is bounded to 1 MiB; structured details to 2,000 entries, each up to 16 Ki characters. Incomplete budget-truncated final lines retain source without guessed severity/tag statistics. `.crash` shows available report fields; structured `.ips` supports standard crash reports (309), without symbolication or root-cause analysis. Unsupported or damaged reports retain source with an explanation.

## Other limits that affect answers

- **Finder routing:** `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS, and some plist / CSV files may use system or other providers. Pro does not force provider selection. No blanket claim to arbitrary files or extensionless SQLite is provided.
- **Markdown and text:** Most source previews read at most 1 MiB of UTF-8. Markdown images require authorized regular local files inside the document directory; remote/data URLs, path traversal, and symlinks are rejected. Missing or inaccessible images show alternate text/reasons. Raw HTML is displayed safely, without execution. CSV / TSV shows source and summaries, not a spreadsheet editor.
- **Plist and dotenv:** Binary/OpenStep plist can show key-name summaries instead of full source; invalid binary plist does not fall back to garbled text. dotenv intentionally exposes keys only, including names such as `.env.local` and `.env.txt`; no Outline/Mindmap or secret-value display.
- **Android:** Pro permission lists are capped at 12; available manifest summaries include application flags, component counts, declared deep-link rules, technologies, resources, and contents. Missing flags are not inferred as false; links are not domain-verified. Split containers summarize base-APK details, not an exhaustive aggregation of every split. AAR is an Android library, not an APK-set container.
- **Signing:** Available identities, schemes, and certificate summaries do not verify signature validity or installer trust. Provisioning profiles show bounded capabilities and certificate counts, not full certificate dumps.
- **SQLite:** Record pages contain at most 100 rows within 1 MiB; text cells are limited to 512 Unicode scalars. BLOB previews show at most 4 KiB; large WITHOUT ROWID BLOBs may remain size-only. No editing, repair, total row counting, record search/filter/sort, or export. A readonly recovery/locking error is not a request to modify the database.
- **Archives:** Listings retain at most 256 entries. Encrypted, solid, or unsupported 7z variants may yield only type, size, and an unable-to-list state. GZ shows header metadata rather than payload browsing or a verified total uncompressed size.
- **DMG / PKG:** Supported variants permit bounded app/icon discovery, not general payload browsing. Encrypted or unsupported variants and resource limits can leave partial results. Old directory-style PKG is unsupported. Finder thumbnails remain system icons.
- **Product scope:** No delivered general Inspector, DEX analysis, comparison/export, Peeka font/video previews, or `.logarchive` support. The retained main-app log viewer has hidden menu/toolbar entries; use Finder Quick Look as the normal workflow.

## Purchase and restore

Peeka Pro is an optional **one-time in-app purchase**, with **no subscription or per-preview charges**. Open **Peeka → Settings → Peeka Pro** for purchase/restore; use the local price displayed by Apple StoreKit. The user completes authentication and purchase confirmation. An installation request alone does not authorize buying Pro.

Enabling a locked Pro format opens a purchase page in the main app; do not promise a locked page inside Finder, because Quick Look rejects unentitled Pro-format requests before parsing. Free-format basic information remains available with deep fields omitted.

When purchase/restore newly grants Pro, Pro-format preview switches are enabled automatically; previously disabled free formats stay disabled. Refreshing an existing entitlement or restoring an already-unlocked purchase preserves later switch choices. Mermaid still requires macOS 14.4+. Close and reopen Quick Look and verify the requested feature; purchase success alone is not preview evidence. See [troubleshooting](troubleshooting.md) when restore fails.
