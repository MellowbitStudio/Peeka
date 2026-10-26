# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · 繁體中文 · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Peeka 是原生 macOS App，為 Finder 帶來適合開發者的檔案預覽。選取支援的檔案並按下**空白鍵**，即可查看應用程式套件、閱讀高亮原始碼、瀏覽結構化資料、檢查 SQLite 結構與封存檔目錄。

[從 App Store 下載](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [官網](https://mellowbit.studio/peeka) · [回報問題](https://github.com/MellowbitStudio/Peeka/issues) · [隱私權政策](https://mellowbit.studio/peeka/privacy/)

需要 **macOS 14 或以上版本**；Mermaid 圖表另需 **macOS 14.4+** 與 Pro。支援**英文、簡體中文、繁體中文、日文、韓文、德文、法文與西班牙文**。

**Peeka 0.1.7 已通過 App Store 審查並正式上架**，由維護者於 **2026-10-26** 確認。透過 App Store 更新，即可使用擴充的原始碼高亮、Pro Framework/dSYM 預覽、封存檔改進與離線 Pele 圖表。實際預覽仍取決於檔案相容性與 Finder 選用的預覽器。

## 主要功能

以下介紹已發布的 0.1.7 功能；相較於 0.1.5 的變更請見 [0.1.7 更新內容](#017-更新內容)。

- **應用程式套件：** 查看 Android 與 Apple 套件中可用的圖示、名稱、識別碼、版本、系統需求與架構。相容套件若內含可用圖示，也可產生 Finder 縮圖。
- **原始碼：** 常見開發語言支援語法高亮、行號、原生文字選取與複製，可依語言開啟或關閉預覽。
- **Diff / Patch：** 免費提供 Source、Fluid、Blocks 與 Unified 檢視，包含檔案選取、原始行號與增刪統計。只檢視修補檔，不套用修補或讀取列出的檔案。
- **Markdown：** 預覽排版文件，支援程式碼區塊高亮、可獨立水平捲動的表格、唯讀工作清單與獲准存取的本機圖片。
- **Mermaid：** 預覽獨立圖表或 Markdown 內圖表，支援原始碼檢視與向量縮放、平移。圖形需 Pro 與 macOS 14.4+；Markdown 圍欄原始碼維持免費。
- **日誌與當機報告：** 免費閱讀日誌、Android Logcat 與當機報告的高亮原文。Pro 提供已識別內容的有限範圍摘要與結構化詳細資訊。
- **DMG 與平面 PKG：** 不掛載映像檔或安裝套件，即可讀取中繼資料及在資源限制內取得的內嵌 App 名稱與圖示。
- **結構化資料：** JSON、YAML、TOML 與 INI 提供原始碼、大綱與心智圖檢視，可展開或收合結構，並用觸控式軌跡板平移、縮放心智圖。
- **SQLite：** 免費查看資料庫摘要與資料表結構。Pro 加入唯讀資料分頁與 BLOB 前綴預覽。
- **封存檔：** 不解壓縮至磁碟即可瀏覽支援的目錄，並以列表或分欄檢視導覽資料夾。
- **本機處理：** 檔案內容與中繼資料在 Mac 上處理，不需要 Peeka 帳號。

## 支援格式

| 類別 | 免費預覽 | Peeka Pro 擴充功能 |
| --- | --- | --- |
| Android 套件 | APK | AAB、APKS、XAPK、APKM、AAR；適用時提供有限範圍的權限、簽署與資訊清單摘要 |
| Apple 套件 | IPA、APP、APPEX；DMG / 平面 PKG 中繼資料與有限範圍的內嵌 App 資訊 | XCArchive、XCFramework、Framework、dSYM、佈建描述檔、dylib；可用的簽署中繼資料 |
| 原始碼 | 205 個離線詞法設定，涵蓋程式語言、範本、著色器、建置腳本與設定；SQL、Diff / Patch、Protobuf、GraphQL | — |
| 文件與設定 | Markdown、JSON / JSONL / NDJSON、XML、YAML、TOML、INI、properties、EditorConfig、plist 與相關 Apple 設定、CSV / TSV、TXT / TEXT 純文字；dotenv 僅顯示鍵名 | — |
| Mermaid | Markdown 中 Mermaid 圍欄的高亮原始碼 | 獨立 `.mmd` / `.mermaid` 與 Markdown 圖表（macOS 14.4+） |
| 日誌與報告 | `.log` / `.out` / `.trace`、`.crash`、`.ips` 與已識別 JSONL / NDJSON 日誌的高亮原文 | 有限範圍的摘要與結構化詳細資訊，含 Android Logcat / Android Studio 版面 |
| 資料庫 | SQLite 摘要與資料表結構（`.sqlite`、`.sqlite3`、`.db`、`.db3`、`.s3db`、`.sdb`） | 唯讀資料分頁與 BLOB 前綴預覽 |
| 封存檔 | ZIP、TAR、TAR.GZ / TGZ、GZ 中繼資料、JAR / WAR 項目清單 | 支援的 7z 清單與 JAR / WAR 資訊清單詳細內容 |

預覽取決於內容與 macOS 是否選用 Peeka 擴充功能。TypeScript `.ts` / `.mts`、dotenv、AAR、TXT / TEXT、IPS 與部分 plist / CSV 有已知預覽器或路由限制。YAML 與 TOML 結構檢視支援有限的語法子集。TXT / TEXT 保持純文字，不自動識別為日誌或文件。

## 0.1.7 更新內容

0.1.7 將以下更新帶入 Mac App Store 正式版，包含先前在 0.1.6 Beta 推出的改進。[版本說明](https://mellowbit.studio/zh-tw/peeka/release-notes/)

- **原始碼高亮擴充（免費）：** 205 個離線詞法設定涵蓋程式語言、範本、著色器、建置腳本與設定檔，提供各語言獨立開關，並與 Markdown 程式碼區塊共用高亮。不執行程式碼，也不代表完整語法驗證。
- **檔案辨識：** 改進點檔案、無副檔名建置檔案和常見鎖定檔的辨識與 Finder 分發。未辨識的通用檔案顯示基本資訊；`.ipynb` 顯示 JSON 原始碼。實際預覽仍取決於 macOS 的預覽器選擇。
- **Framework 預覽（Pro）：** 查看 `.framework` 身分與可用的 Mach-O 架構、UUID、平台及最低系統版本。支援平面與 macOS 版本化套件；一般靜態框架只顯示身分資訊。
- **偵錯符號預覽（Pro）：** 查看 `.dSYM` 的二進位檔名稱與各架構 UUID；不展開符號、不符號化當機報告，也不自動配對二進位檔與報告。
- **Mermaid 引擎更新：** 內建 Pele 1.6.0，離線繪製 20 類圖表，支援淺色／深色主題與原生向量縮放、平移。版面與語法相容性可能不同於 0.1.5 的 Mermaid.js 引擎。
- **封存檔：** 大型列表按需讀取中繼資料，不再固定為前 256 項；改進索引、排序、取消與恢復，以及 ZIP/JAR/WAR、TAR/TGZ 舊編碼檔名識別；Pro 改進支援的 LZMA/LZMA2 編碼標頭與單編碼器 solid 7z 列表。仍受資源限制，可能顯示不完整列表。

Framework 與 dSYM 各有獨立開關，均無自訂縮圖。本機 App 驗收記錄顯示兩者的空白鍵預覽與 dSYM 的 Finder 分欄預覽可用；Framework 在分欄中仍作為目錄展開。

## 開始使用

1. 從 [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) 下載 Peeka，或到 [Peeka 官網](https://mellowbit.studio/peeka)了解產品。
2. 安裝後啟動 Peeka，依引導設定；必要時在**系統設定**啟用快速查看擴充功能。
3. 確認 Peeka 格式列表已開啟對應格式。
4. 在 **Finder** 選取支援的檔案並按下**空白鍵**。

變更格式開關或解鎖 Pro 後，請關閉並重新開啟快速查看。主 App 提供設定引導、格式控制、設定與購買入口；檔案預覽顯示於 Finder。

預覽開關不控制套件縮圖；縮圖也不需要 Pro。主 App 支援格式搜尋與各原始碼語言的獨立開關。限制與常見問題請見[功能參考（英文）](skills/peeka/references/features-and-plans.md)與[疑難排解（英文）](skills/peeka/references/troubleshooting.md)。

## Peeka Pro

常見格式可免費預覽。**Peeka Pro** 是選購的**一次性 App 內購買**，**無訂閱，也不按預覽次數收費**，可解鎖上表所列的額外格式與詳細資訊。

請在**設定 → Peeka Pro** 購買或回復購買項目。價格以 App 內 Apple StoreKit 顯示的當地價格為準。

部分預覽有限制：

- SQLite 每頁最多 **100 列**，展示資料上限為 **1 MiB**；BLOB 最多讀取前 **4 KiB**。Peeka 不編輯或維護資料庫。
- 簽署中繼資料只描述可用資訊，不驗證簽章有效性。
- 日誌與報告的原文與詳細資訊有資源上限；統計只涵蓋已解析的預覽部分。結構化 IPS 支援標準當機報告（309），不執行符號化。
- 內建離線 Pele 引擎支援 20 類 Mermaid 圖表。不支援的語法、指令或超出資源限制的內容會退回高亮原始碼並說明原因。
- Pro 可列出支援的單一編碼器固實 7z 目錄；加密標頭、篩選鏈或不支援的變體可能無法列出。封存檔列表受資源限制，大型檔案可能只顯示部分清單。

免費與 Pro 預覽均受資源與相容性限制。

## AI Agent Skill

公開的 [`peeka` skill（英文）](skills/peeka/SKILL.md) 版本為 **0.1.7**，協助 Codex、Claude Code 等相容 Agent 安裝 Peeka、了解格式與免費／Pro 功能、控制預覽與排解問題。

Skill 發布至本儲存庫預設分支後，可使用：

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

這會安裝 Agent skill；Peeka App 需另從 Mac App Store 下載。指定 Agent、全域安裝與本機測試請見 [skill 安裝說明（英文）](skills/README.md)。桌面操作需要本機工具；Apple 帳號驗證與購買確認由你完成。Agent 依使用者語言回覆。

## 意見與支援

問題與功能建議請[提交 Issue](https://github.com/MellowbitStudio/Peeka/issues)，附上 macOS 與 Peeka 版本、檔案格式、重現步驟及預期行為。螢幕截圖或不含敏感資訊的小型範例有助於診斷。

也可聯絡 [support@mellowbit.studio](mailto:support@mellowbit.studio)。

## 關於本儲存庫

這是 [Mellowbit Studio](https://mellowbit.studio/peeka) 維護的 Peeka 公開產品與意見回饋儲存庫，提供產品資訊與公開文件。**本儲存庫不包含 App 原始碼。**
