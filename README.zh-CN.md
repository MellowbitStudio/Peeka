# Peeka

**Ultimate Quick Look App · 开发者文件的快速查看工具**

[English](README.md) · 简体中文

Peeka 是一款原生 macOS 应用，为「访达」带来更适合开发者的文件预览。选中受支持的文件，按下**空格键**，即可查看应用软件包信息、阅读高亮源码、浏览结构化数据、检查 SQLite 表结构和查看压缩包目录。

[在 App Store 下载](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [官网](https://mellowbit.studio/peeka) · [反馈问题](https://github.com/MellowbitStudio/Peeka/issues) · [隐私政策](https://mellowbit.studio/peeka/privacy/)

需要 **macOS 14 或更高版本**；Mermaid 图形另需 **macOS 14.4+** 和 Pro。支持**英语、简体中文、繁体中文、日语、韩语、德语、法语和西班牙语**。

**Peeka 0.1.5 已通过 App Store 审核并正式上线**，上线状态于 **2026-10-19** 确认。以下能力以 **2026-10-19** 核对的 **0.1.5 产品基线**为准，包含原生 Diff / Patch 增强预览与 Mermaid 更新。旧版用户可通过 App Store 更新；实际预览还取决于文件兼容性和访达选择的预览器。

## 主要功能

- **应用软件包：** 查看 Android 与 Apple 软件包中可用的图标、名称、标识符、版本、系统要求和架构。受支持的软件包含有可用内置图标时，还可生成访达缩略图。
- **源码：** 常见开发语言支持语法高亮、行号、原生文本选择与复制。可在 Peeka 中按语言独立开启或关闭预览。
- **Diff / Patch：** 免费提供 Source、Fluid、Blocks 和 Unified 视图，支持文件选择、原文件行号与增删统计；仅查看补丁，不应用补丁或读取所列文件。
- **Markdown：** 阅读排版后的文档，支持代码块高亮、独立横向滚动表格、只读任务列表和获准访问的本地图片。
- **Mermaid：** 预览独立图表或 Markdown 内图表，支持源码切换与矢量缩放、平移。图形渲染需 Pro 和 macOS 14.4+；Markdown 围栏源码保持免费。
- **日志与崩溃报告：** 免费阅读日志、Android Logcat 和崩溃报告的高亮原文；Pro 提供已识别内容的有界概要与结构化详情。
- **DMG 与扁平 PKG：** 无需挂载镜像或安装软件，即可读取元数据及有界探查得到的应用名称、图标。
- **结构化数据：** JSON、YAML、TOML 和 INI 提供源码、大纲与思维导图视图。支持展开或折叠结构，以及使用触控板平移和缩放思维导图。
- **SQLite：** 免费查看数据库概要与表结构。Peeka Pro 提供只读记录分页和 BLOB 前缀预览。
- **压缩包：** 无需将文件解压到磁盘即可浏览受支持的归档目录，支持列表与分栏视图。
- **本机处理：** 文件内容与元数据在 Mac 上处理，无需注册 Peeka 账号。

## 支持的格式

| 类别 | 免费预览 | Peeka Pro 扩展能力 |
| --- | --- | --- |
| Android 软件包 | APK | AAB、APKS、XAPK、APKM、AAR；适用格式的有界权限、签名和清单摘要 |
| Apple 软件包 | IPA、APP、APPEX；DMG 与扁平 PKG 的元数据及有界应用信息探查 | XCArchive、XCFramework、预置描述文件、dylib；适用格式的签名元数据 |
| 源码 | Swift、C / C++、Objective-C、Java、Kotlin、JavaScript、TypeScript、Python、Go、Rust、Shell、HTML、CSS、SQL、Diff / Patch、Protobuf、GraphQL | — |
| 文档与配置 | Markdown、JSON / JSONL / NDJSON、XML、YAML、TOML、INI、properties、EditorConfig、plist 及相关 Apple 配置、CSV / TSV、TXT / TEXT 普通原文；dotenv 仅显示键名 | — |
| Mermaid | Markdown 中 Mermaid 围栏高亮源码 | 独立 `.mmd` / `.mermaid` 与 Markdown 内图形（macOS 14.4+） |
| 日志与报告 | `.log` / `.out` / `.trace`、`.crash`、`.ips` 及已识别 JSONL / NDJSON 日志的高亮原文 | 有界概要与结构化详情，含 Android Logcat / Android Studio 版式 |
| 数据库 | SQLite 概要与表结构（`.sqlite`、`.sqlite3`、`.db`、`.db3`、`.s3db`、`.sdb`） | 只读记录分页与 BLOB 前缀预览 |
| 压缩包 | ZIP、TAR、TAR.GZ / TGZ、GZ 元数据、JAR / WAR 条目清单 | 受支持的 7z 条目清单与 JAR / WAR 清单详情 |

实际预览取决于文件内容以及 macOS 是否选择 Peeka 扩展。TypeScript 的 `.ts` / `.mts`、dotenv、AAR、TXT / TEXT、IPS 及部分 plist / CSV 存在已知预览器或分发限制。YAML 与 TOML 的结构视图支持有界语法子集。TXT / TEXT 只显示普通原文，不自动识别日志或文档类型。

## 开始使用

1. 从 [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) 下载 Peeka，也可访问 [Peeka 官网](https://mellowbit.studio/peeka)了解产品详情。
2. 安装后启动 Peeka，按引导完成设置；如有需要，在**系统设置**中启用快速查看扩展。
3. 在 Peeka 的格式列表中，确认对应格式已开启。
4. 在**访达**中选中受支持的文件，按下**空格键**。

调整格式开关或解锁 Pro 后，请关闭并重新打开快速查看窗口。主应用提供引导、格式开关、设置与购买入口，文件预览通过访达完成。

预览开关不控制软件包缩略图，缩略图也不要求 Pro。主应用日志查看器的菜单和工具栏入口已隐藏；通用 Inspector、对比与导出、Peeka 字体和视频预览尚未交付。

## Peeka Pro

Peeka 为常用格式提供免费预览。**Peeka Pro** 是可选的**一次性应用内购买**，**无订阅，也不按预览次数收费**，解锁上表中的更多格式与详情。

可在**设置 → Peeka Pro** 中购买或恢复购买。实际价格以应用内 Apple StoreKit 显示的当地价格为准。

部分预览存在以下限制：

- SQLite 每页最多 **100 行**，并受 **1 MiB** 展示预算约束；BLOB 最多预览前 **4 KiB**。Peeka 不编辑数据库或执行维护。
- 签名元数据展示可用的签名信息，不代表签名有效性验证。
- 日志与报告的原文和详情有资源上限，统计仅覆盖已解析的预览部分。IPS 结构化支持标准崩溃报告（309），不执行符号化。
- 文档所述 0.1.5 基线的 Mermaid 支持 20 类图形；不支持的语法、配置指令或超限内容会显示高亮源码与原因。
- 加密、固实或不支持的 7z 变体可能无法列出内容。归档条目数量有上限，大型压缩包可能只显示部分清单。

资源与兼容性限制同样适用于免费与 Pro 预览。

## AI Agent Skill

公开的 [`peeka` skill](skills/peeka/SKILL.md) 版本为 **0.1.5**，可供 Codex、Claude Code 等兼容的 AI Agent 使用，涵盖 App Store 下载安装、支持格式、免费与 Pro 功能、预览开关和问题排查。

Skill 发布到本仓库的默认分支后，可执行以下命令安装：

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

该命令安装的是 Agent skill；Peeka 应用需另外从 Mac App Store 下载。指定 Agent、全局安装和本地测试方式见 [skill 安装说明](skills/README.md)。执行桌面操作需要 Agent 具备本机工具，Apple 账户验证与购买确认由你完成。

## 反馈与支持

遇到问题或有功能建议，可[提交 Issue](https://github.com/MellowbitStudio/Peeka/issues)。请附上 macOS 版本、Peeka 版本、文件格式、复现步骤和预期行为。截图或不含敏感信息的小型样本有助于排查预览问题。

也可发送邮件至 [support@mellowbit.studio](mailto:support@mellowbit.studio)。

## 关于本仓库

这是由 [Mellowbit Studio](https://mellowbit.studio/peeka) 维护的 Peeka 产品介绍与反馈仓库，用于提供产品信息和公开文档。**本仓库不包含应用源码。**
