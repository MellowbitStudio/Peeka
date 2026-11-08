# TestFlight 0.1.6 (historical)

Peeka **0.1.6**, build **20261020.1**, passed TestFlight review, as confirmed by the maintainer on **2026-10-21**. The documented Mac App Store release at the time was **0.1.5**. See [Mac App Store 0.1.9](features-and-plans.md#app-store-019) for stable release guidance.

- [Official TestFlight invitation](https://testflight.apple.com/join/5jM8yxDB)
- [Beta release notes and testing focus](https://mellowbit.studio/peeka/beta-release-notes/)
- [Stable release notes](https://mellowbit.studio/peeka/release-notes/)

See the [TestFlight 0.1.8 approval record](testflight-0.1.8.md) for the later Beta.

## Changes since 0.1.5

- **Framework and dSYM (Pro):** Separate format switches, bundle identity and available Mach-O architectures, UUIDs, platforms and minimum system versions. Static ar frameworks show identity only. dSYM does not expand DWARF symbols, symbolicate reports or automatically match binaries. Neither format adds custom thumbnails. Finder may expand frameworks as directories in column view; select the bundle and press Space.
- **Archives:** Read metadata on demand for larger listings instead of retaining only the first 256 entries. Improved indexing, sorting, cancellation and preview recovery. Resource/time limits remain, and incomplete listings must be identified. This does not extract or preview contained file contents.
- **Filename encodings and 7z:** ZIP/JAR/WAR and TAR/TGZ consider common legacy encodings and preferred system languages while respecting explicit encoding declarations. Pro improves listings for supported LZMA/LZMA2 encoded headers and single-coder solid 7z layouts; unsupported layouts retain fallback.
- **Mermaid:** Bundled offline Pele 1.6.0 replaces Mermaid.js. Layout, default styling and supported syntax can differ. Pro and macOS 14.4+ remain required for diagrams; source fallback and resource limits remain. Metadata labels, localization and percentage controls are improved.

## Testing and troubleshooting

Enable the system Quick Look extension and relevant per-format switches. Check Framework Space previews and dSYM column/Space previews with Pro. Try ZIP/TAR/TGZ with more than 256 entries, nested folders, sorting and keyboard navigation; switch or close files during indexing and reopen them. Test legacy Chinese/Japanese/Korean/Western filenames, UTF-8 and ZIP Unicode Path names. Restart the app and extension after changing preferred system languages. With Pro, check supported 7z layouts and Mermaid diagrams in standalone files and Markdown, including Diagram/Source, Fit, 100%, pan/zoom and both appearances.

Recheck free Diff/Patch, APK/IPA and SQLite structure, Pro records/BLOB prefixes, purchase/restore and saved format switches. Feedback should include macOS, app version/build, file type, Pro and switch state, and reproduction steps.

These notes follow app tag **0.1.6 (`76658ef`)**. Later development-source language catalog expansions are outside this Beta baseline. Check the installed build before promising new source-language support. TestFlight approval is separate from actual Finder provider selection and minimum-system acceptance.
