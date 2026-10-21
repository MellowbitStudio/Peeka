# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · 日本語 · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Peeka は、開発者向けのファイルプレビューを Finder に追加するネイティブ macOS アプリです。対応ファイルを選んで**スペースキー**を押すと、アプリパッケージ、構文強調表示されたソースコード、構造化データ、SQLite のスキーマ、アーカイブの内容一覧を確認できます。

[App Store でダウンロード](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [公式サイト](https://mellowbit.studio/peeka) · [問題を報告](https://github.com/MellowbitStudio/Peeka/issues) · [プライバシーポリシー](https://mellowbit.studio/peeka/privacy/)

**macOS 14 以降**が必要です。Mermaid の図の描画には **macOS 14.4 以降**と Pro が必要です。**英語、簡体字中国語、繁体字中国語、日本語、韓国語、ドイツ語、フランス語、スペイン語**に対応しています。

**Peeka 0.1.5 は App Store の審査に合格し、正式公開されています**（**2026-10-19** 確認）。以下は同日に確認した 0.1.5 の製品仕様で、ネイティブの Diff / Patch プレビューと Mermaid の更新を含みます。旧バージョンは App Store で更新してください。利用できるプレビューはファイルの互換性と Finder が選択するプロバイダにも依存します。

**0.1.6 (20261020.1) · TestFlight 審査通過** · 2026-10-21 · [TestFlight](https://testflight.apple.com/join/5jM8yxDB)

## 主な機能

以下は公開済みの 0.1.5 の機能です。それ以降の実装は[開発状況](#開発状況)をご覧ください。

- **アプリパッケージ：** Android と Apple のパッケージ内にあるアイコン、名前、識別子、バージョン、システム要件、アーキテクチャを表示します。互換性のあるパッケージにアイコンが含まれる場合、Finder のサムネイルも生成できます。
- **ソースコード：** 一般的な開発言語の構文強調表示、行番号、ネイティブのテキスト選択とコピーに対応。言語ごとにプレビューを切り替えられます。
- **Diff / Patch：** Source、Fluid、Blocks、Unified ビューを無料で利用できます。ファイル選択、元の行番号、変更数を表示し、パッチの適用や参照先ファイルの読み取りは行いません。
- **Markdown：** コードブロックの構文強調表示、個別に横スクロールできる表、読み取り専用のタスクリスト、アクセスが許可されたローカル画像を含む文書を表示します。
- **Mermaid：** 単独ファイルと Markdown 内の図を表示。ソース表示とベクターのズーム・パンに対応します。図の描画には Pro と macOS 14.4 以降が必要で、Markdown 内のフェンス付きソースは無料です。
- **ログとクラッシュレポート：** ログ、Android Logcat、クラッシュレポートの構文強調表示は無料。Pro では認識した内容の範囲を制限した要約と構造化された詳細を表示します。
- **DMG とフラット PKG：** マウントやインストールをせずに、メタデータと、制限内で調べた内包アプリの名前・アイコンを表示します。
- **構造化データ：** JSON、YAML、TOML、INI のソース、アウトライン、マインドマップを切り替えられます。展開・折りたたみやトラックパッドでのパン・ズームに対応します。
- **SQLite：** データベースの概要とテーブル構造は無料。Pro で読み取り専用のレコードページと BLOB の先頭部分を表示できます。
- **アーカイブ：** ディスクに展開せずに対応アーカイブの一覧を表示し、リスト・カラム表示でフォルダを移動できます。
- **ローカル処理：** ファイルの内容とメタデータは Mac 上で処理します。Peeka アカウントは不要です。

## 対応形式

| 分類 | 無料プレビュー | Peeka Pro の追加機能 |
| --- | --- | --- |
| Android パッケージ | APK | AAB、APKS、XAPK、APKM、AAR。取得可能な権限・署名・マニフェスト由来の要約を制限内で表示 |
| Apple パッケージ | IPA、APP、APPEX、DMG / フラット PKG のメタデータと制限内の内包アプリ情報 | XCArchive、XCFramework、プロビジョニングプロファイル、dylib、取得可能な署名メタデータ |
| ソースコード | Swift、C / C++、Objective-C、Java、Kotlin、JavaScript、TypeScript、Python、Go、Rust、Shell、HTML、CSS、SQL、Diff / Patch、Protobuf、GraphQL | — |
| 文書と設定 | Markdown、JSON / JSONL / NDJSON、XML、YAML、TOML、INI、properties、EditorConfig、plist と関連する Apple 設定、CSV / TSV、TXT / TEXT のプレーンテキスト。dotenv はキー名のみ | — |
| Mermaid | Markdown 内の Mermaid フェンス付きソースの構文強調表示 | 単独の `.mmd` / `.mermaid` と Markdown 内の図（macOS 14.4 以降） |
| ログとレポート | `.log` / `.out` / `.trace`、`.crash`、`.ips`、認識された JSONL / NDJSON ログの構文強調表示 | 制限内の要約と構造化された詳細。Android Logcat / Android Studio のレイアウトを含む |
| データベース | SQLite の概要とテーブル構造（`.sqlite`、`.sqlite3`、`.db`、`.db3`、`.s3db`、`.sdb`） | 読み取り専用レコードページと BLOB の先頭部分 |
| アーカイブ | ZIP、TAR、TAR.GZ / TGZ、GZ メタデータ、JAR / WAR の項目一覧 | 対応する 7z の一覧と JAR / WAR マニフェストの詳細 |

実際の表示は内容と macOS による拡張機能の選択に依存します。TypeScript の `.ts` / `.mts`、dotenv、AAR、TXT / TEXT、IPS、一部の plist / CSV にはプロバイダや振り分けの既知の制約があります。YAML と TOML の構造ビューは構文の一部に対応します。TXT / TEXT はプレーンテキストとして表示し、ログや文書の自動判別は行いません。

## 開発状況

Peeka 0.1.6（20261020.1）が TestFlight 審査を通過しました。Beta では Pro の Framework/dSYM プレビュー、大規模アーカイブ一覧、ファイル名の文字コード、オフライン Pele 図を追加・改善。Mac App Store の正式版は引き続き 0.1.5 です。 [TestFlight](https://testflight.apple.com/join/5jM8yxDB) · [0.1.6 Beta](https://mellowbit.studio/ja/peeka/beta-release-notes/)

- **Framework プレビュー（Pro）：** `.framework` の識別情報と、取得可能な Mach-O アーキテクチャ、UUID、プラットフォーム、最低 OS バージョンを表示。フラット形式と macOS のバージョン付きバンドルに対応し、一般的な静的フレームワークは識別情報のみ表示します。
- **デバッグシンボル（Pro）：** `.dSYM` のバイナリ名とアーキテクチャ別 UUID を表示。シンボル展開、クラッシュのシンボリケーション、バイナリとレポートの自動照合は行いません。
- **Mermaid エンジン更新：** Pele 1.6.0 を同梱し、20 種類の図をオフライン描画。ライト・ダークテーマとネイティブのベクターズーム・パンに対応します。配置と構文互換性は 0.1.5 の Mermaid.js と異なる場合があります。
- **アーカイブ：** 大規模な一覧のメタデータを必要時に読み取り、先頭 256 件の固定制限を廃止。索引、並べ替え、キャンセル、復旧、ZIP/JAR/WAR・TAR/TGZ の旧文字コードのファイル名を改善。Pro では対応する LZMA/LZMA2 ヘッダーと単一コーダーの solid 7z 一覧を改善。リソース制限や部分的な一覧は引き続き適用されます。

Framework と dSYM はそれぞれ独立した形式スイッチがあり、カスタムサムネイルはありません。ローカル検証では両方のスペースキープレビューと dSYM の Finder カラムプレビューが動作しました。Framework はカラム表示でフォルダとして展開されます。

## 使い始める

1. [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) で Peeka をダウンロードするか、[公式サイト](https://mellowbit.studio/peeka)で製品を確認します。
2. インストール後に Peeka を起動し、案内に従います。必要に応じて**システム設定**で Quick Look 拡張機能を有効にします。
3. Peeka の形式一覧で対象形式が有効か確認します。
4. **Finder** で対応ファイルを選び、**スペースキー**を押します。

スイッチの変更や Pro の解除後は Quick Look を閉じて開き直してください。メインアプリには設定案内、形式の切り替え、設定、購入機能があり、ファイルプレビューは Finder に表示されます。

プレビュースイッチはパッケージのサムネイルを制御せず、サムネイルに Pro は不要です。形式検索と言語別のスイッチも用意されています。制約や問題は[機能リファレンス（英語）](skills/peeka/references/features-and-plans.md)と[トラブルシューティング（英語）](skills/peeka/references/troubleshooting.md)をご覧ください。

## Peeka Pro

一般的な形式は無料でプレビューできます。**Peeka Pro** は任意の**買い切りのアプリ内課金**で、**サブスクリプションやプレビューごとの料金はありません**。上表の追加形式と詳細を利用できます。

**設定 → Peeka Pro** で購入または購入の復元ができます。価格はアプリ内の Apple StoreKit が表示する現地価格をご確認ください。

一部のプレビューには制限があります。

- SQLite はページあたり最大 **100 行**、表示データは **1 MiB** まで。BLOB は先頭 **4 KiB** まで読み取ります。データベースの編集や保守は行いません。
- 署名メタデータは取得できた情報の表示であり、有効性の検証ではありません。
- ログとレポートの原文・詳細には上限があります。統計は解析されたプレビュー部分が対象です。構造化 IPS は標準クラッシュレポート（309）向けで、シンボリケーションは行いません。
- 0.1.5 の文書基準では Mermaid の 20 種類の図に対応。未対応の構文・指令やリソース上限に達した場合は、理由と構文強調表示されたソースを表示します。
- 暗号化・ソリッド圧縮・未対応方式の 7z は一覧を表示できない場合があります。一覧には上限があり、大きなアーカイブでは一部のみ表示されます。

リソースと互換性の制約は無料版と Pro の両方に適用されます。

## AI エージェントスキル

公開 [`peeka` スキル（英語）](skills/peeka/SKILL.md)のバージョンは **0.1.5** です。Codex、Claude Code などの互換エージェントが、インストール、対応形式、無料・Pro 機能、プレビュー設定、問題解決を支援します。

リポジトリのデフォルトブランチへの公開後にインストールできます。

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

このコマンドはスキルをインストールします。Peeka アプリは Mac App Store から別途ダウンロードしてください。対象エージェントの指定、グローバルインストール、ローカルテストは[スキル導入ガイド（英語）](skills/README.md)をご覧ください。デスクトップ操作にはローカルツールが必要です。Apple Account の認証と購入確認は利用者が行います。エージェントは利用者の言語で回答します。

## フィードバックとサポート

不具合や機能の要望は [Issue](https://github.com/MellowbitStudio/Peeka/issues) でお知らせください。macOS と Peeka のバージョン、ファイル形式、再現手順、期待する動作を記載してください。スクリーンショットや機密情報を含まない小さなサンプルも役立ちます。

メール：[support@mellowbit.studio](mailto:support@mellowbit.studio)。

## このリポジトリについて

[Mellowbit Studio](https://mellowbit.studio/peeka) が管理する Peeka の公開製品情報・フィードバック用リポジトリです。製品情報と公開ドキュメントを収録しています。**アプリのソースコードは含まれていません。**
