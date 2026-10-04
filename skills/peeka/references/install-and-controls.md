# Installation and preview controls

## Install from the Mac App Store

1. Confirm that the user's Mac runs **macOS 14 or later**. With local shell access, `sw_vers -productVersion` reports the macOS version. On another operating system, provide the Mac instructions; Peeka's app and Finder extension require macOS.
2. Open [Peeka's official listing](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289), App Store ID **6813012289**. Follow **Open in Mac App Store** if the page opens in a browser. Other products share the Peeka name; use this exact listing.
3. Select **Get**, **Install**, or the download icon as shown. If **Open** appears, the app is already installed. Let the user complete Apple Account authentication or Touch ID if requested.
4. Wait for installation to finish, then launch **Peeka** and follow its setup guidance. Check its Quick Look extension and the target format switch as described below.
5. Select a supported file in Finder and press **Space** to verify the preview.

When shell access is available on the user's Mac, these commands open the listing and the installed app; they do not perform the download or confirm installation:

```sh
open 'https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289'
open -a 'Peeka'
```

Run the second command after installation. App Store authentication or download problems should be resolved through the App Store rather than by downloading an unofficial binary. Use the App Store's Updates view for app updates.

## Preview a file

1. Ensure the file is available locally. If it is a cloud placeholder, download it before diagnosing a parser or extension failure.
2. Select the file in **Finder / 访达** and press **Space / 空格键**. Press Space again or close the Quick Look window to dismiss it.
3. Use the preview controls provided for that format: structured-data views, archive navigation, or database sections as applicable. See [features and plans](features-and-plans.md) for tier requirements and limits.

If local shell access is available, reveal the user's file with:

```sh
open -R '/absolute/path/to/file.json'
```

Replace the sample path with the actual path and quote it correctly. Revealing the file only selects it in Finder; press Space afterward. Opening Peeka or double-clicking the file is a different action from invoking Finder Quick Look.

## Enable or disable one format

Use this for requests such as “turn off Markdown previews” or “enable Python previews.”

1. Launch **Peeka**.
2. Find the target format or source language in the app's **format list** and set its switch to the requested state. Match the installed UI; exact labels and grouping may vary by app version or language.
3. Close any open Quick Look window and reopen the file in Finder.
4. Verify the resulting behavior. An enabled Pro format still requires Pro. An enabled format also requires the system extension to be enabled.

Source-code languages can be switched independently. For other formats, use the controls actually exposed by the installed app; do not assume a separate switch for every file extension.

Switching a format off stops Peeka's handling for that format. Finder may show a macOS preview, a preview from another extension, or a generic file display. Do not promise that Finder will show no preview at all.

## Enable or disable Peeka's Quick Look extension

Use this when setting up Peeka, or when the user asks to stop Peeka previews across formats. Keep the app installed unless removal is requested.

Start with Peeka's setup guidance. In System Settings, locate **Quick Look / 快速查看** and switch the entry or entries belonging to Peeka on or off:

| macOS UI | Typical path |
| --- | --- |
| macOS Sonoma 14 | **System Settings → Privacy & Security → Extensions → Quick Look** / **系统设置 → 隐私与安全性 → 扩展 → 快速查看** |
| Newer macOS UI | **System Settings → General → Login Items & Extensions → Quick Look** / **系统设置 → 通用 → 登录项与扩展 → 快速查看**; open the category's information button if shown |

Inspect the current UI or search System Settings for **Quick Look** or **Extensions** when the path differs. Match Peeka's visible entries rather than guessing extension names. Preview and thumbnail entries may be shown separately; change the entries that correspond to the user's request.

Close and reopen Finder Quick Look afterward. This controls Peeka's extension, while the format switches control individual supported formats. macOS Quick Look can continue using its own or other providers when Peeka is disabled.

## Verify and report

Report the app installation state, relevant format switch, relevant extension state, and observed preview result only as far as they were actually checked. If authentication or a manual UI step remains, say exactly which step the user must finish. If previewing still fails, continue with [troubleshooting](troubleshooting.md).

## Sources

Product workflow: [Peeka public documentation](https://github.com/MellowbitStudio/Peeka#readme), reviewed 2026-10-04.

System Settings paths: Apple's [Sonoma Extensions settings](https://support.apple.com/guide/mac-help/change-extensions-settings-mchl8baf92fe/14.0/mac/14.0) and [Login Items & Extensions settings](https://support.apple.com/guide/mac-help/change-login-items-extensions-settings-mtusr003/mac). Check the version selector and installed UI for version-specific labels.
