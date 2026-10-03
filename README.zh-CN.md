# Peeka

**Ultimate Quick Look App · 开发者文件的快速查看工具**

[English](README.md) · 简体中文

Peeka 是一款原生 macOS 应用，为「访达」带来更适合开发者的文件预览。选中受支持的文件，按下**空格键**，即可查看应用软件包信息、阅读高亮源码、浏览结构化数据、检查 SQLite 表结构和查看压缩包目录。

[官网](https://mellowbit.studio/peeka) · [反馈问题](https://github.com/MellowbitStudio/Peeka/issues) · [隐私政策](https://mellowbit.studio/peeka/privacy/)

需要 **macOS 14 或更高版本**。支持**英语和简体中文**。

## 主要功能

- **应用软件包：** 查看 Android 与 Apple 软件包中可用的图标、名称、标识符、版本、系统要求和架构。受支持的软件包含有可用内置图标时，还可生成访达缩略图。
- **源码：** 常见开发语言支持语法高亮、行号、原生文本选择与复制。可在 Peeka 中按语言独立开启或关闭预览。
- **Markdown：** 阅读排版后的文档，支持代码块高亮、表格和只读任务列表。
- **结构化数据：** JSON、YAML、TOML 和 INI 提供源码、大纲与思维导图视图。支持展开或折叠结构，以及使用触控板平移和缩放思维导图。
- **SQLite：** 免费查看数据库概要与表结构。Peeka Pro 提供只读记录分页和 BLOB 前缀预览。
- **压缩包：** 无需将文件解压到磁盘即可浏览受支持的归档目录，支持列表与分栏视图。
- **本机处理：** 文件内容与元数据在 Mac 上处理，无需注册 Peeka 账号。

## 支持的格式

| 类别 | 免费预览 | Peeka Pro 扩展能力 |
| --- | --- | --- |
| Android 软件包 | APK | AAB、APKS、XAPK、APKM、AAR；适用格式的更多权限与签名摘要 |
| Apple 软件包 | IPA、APP、APPEX；DMG 与扁平 PKG 的外层元数据 | XCArchive、XCFramework、预置描述文件、dylib；适用格式的签名元数据 |
| 源码 | Swift、C / C++、Objective-C、Java、Kotlin、JavaScript、TypeScript、Python、Go、Rust、Shell、HTML、CSS、SQL、Diff / Patch、Protobuf、GraphQL | — |
| 文档与配置 | Markdown、JSON / JSONL / NDJSON、XML、YAML、TOML、INI、properties、EditorConfig、plist、CSV / TSV；dotenv 仅显示键名 | — |
| 数据库 | SQLite 概要与表结构（`.sqlite`、`.sqlite3`、`.db`、`.db3`、`.s3db`、`.sdb`） | 只读记录分页与 BLOB 前缀预览 |
| 压缩包 | ZIP、TAR、TAR.GZ / TGZ、GZ 元数据、JAR / WAR 条目清单 | 受支持的 7z 条目清单与 JAR / WAR 清单详情 |

实际预览取决于文件内容以及 macOS 是否选择 Peeka 扩展。TypeScript 的 `.ts` / `.mts` 和 dotenv 文件存在访达分发限制。YAML 与 TOML 的结构视图支持有界语法子集。

## 开始使用

1. 访问 [Peeka 官网](https://mellowbit.studio/peeka)，了解应用与获取渠道。
2. 安装后启动 Peeka，按引导完成设置；如有需要，在**系统设置**中启用快速查看扩展。
3. 在 Peeka 的格式列表中，确认对应格式已开启。
4. 在**访达**中选中受支持的文件，按下**空格键**。

调整格式开关或解锁 Pro 后，请关闭并重新打开快速查看窗口。主应用提供引导、格式开关、设置与购买入口，文件预览通过访达完成。

## Peeka Pro

Peeka 为常用格式提供免费预览。**Peeka Pro** 是可选的**一次性应用内购买**，**无订阅，也不按预览次数收费**，解锁上表中的更多格式与详情。

可在**设置 → Peeka Pro** 中购买或恢复购买。实际价格以应用内 Apple StoreKit 显示的当地价格为准。

部分预览存在以下限制：

- SQLite 每页最多 **100 行**，并受 **1 MiB** 展示预算约束；BLOB 最多预览前 **4 KiB**。Peeka 不编辑数据库或执行维护。
- 签名元数据展示可用的签名信息，不代表签名有效性验证。
- 加密、固实或不支持的 7z 变体可能无法列出内容。归档条目数量有上限，大型压缩包可能只显示部分清单。

资源与兼容性限制同样适用于免费与 Pro 预览。

## 反馈与支持

遇到问题或有功能建议，可[提交 Issue](https://github.com/MellowbitStudio/Peeka/issues)。请附上 macOS 版本、Peeka 版本、文件格式、复现步骤和预期行为。截图或不含敏感信息的小型样本有助于排查预览问题。

也可发送邮件至 [support@mellowbit.studio](mailto:support@mellowbit.studio)。

## 关于本仓库

这是由 [Mellowbit Studio](https://mellowbit.studio/peeka) 维护的 Peeka 产品介绍与反馈仓库，用于提供产品信息和公开文档。**本仓库不包含应用源码。**
