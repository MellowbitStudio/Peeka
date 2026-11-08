# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · 日本語 · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Peeka は、開発者向けのファイルプレビューを Finder に追加するネイティブ macOS アプリです。対応ファイルを選んで**スペースキー**を押すと、アプリパッケージ、構文強調表示されたソースコード、構造化データ、SQLite のスキーマ、アーカイブの内容一覧を確認できます。

[App Store でダウンロード](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [公式サイト](https://mellowbit.studio/peeka) · [問題を報告](https://github.com/MellowbitStudio/Peeka/issues) · [プライバシーポリシー](https://mellowbit.studio/peeka/privacy/)

**macOS 14 以降**が必要です。Mermaid の図の描画には **macOS 14.4 以降**と Pro が必要です。**英語、簡体字中国語、繁体字中国語、日本語、韓国語、ドイツ語、フランス語、スペイン語**に対応しています。

**Peeka 0.1.9 は審査を通過し、Mac App Store で公開されています。** App Store からアップデートすると、新しいプレビューを利用できます。

**TestFlight ベータ版 0.1.8 は審査を通過しました**。メンテナーが **2026-10-29** に確認しています。[TestFlight に参加](https://testflight.apple.com/join/5jM8yxDB)。

## 主な機能

以下は正式版 0.1.9 の機能です。0.1.7 からの変更は [0.1.9 の新機能](#019-の新機能)をご覧ください。

- **アプリパッケージ：** Android と Apple のパッケージ内にあるアイコン、名前、識別子、バージョン、システム要件、アーキテクチャを表示します。
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
| Android パッケージ | APK、APK と同じ形式の AAR 概要 | AAB、APKS、XAPK、APKM。取得可能な権限・署名・マニフェスト由来の要約を制限内で表示 |
| Apple パッケージ | IPA、APP、APPEX、DMG / フラット PKG のメタデータと制限内の内包アプリ情報 | XCArchive、XCFramework、Framework、dSYM、プロビジョニングプロファイル、dylib。取得可能な署名メタデータ、コンポーネント、リンク依存関係、プライバシー宣言 |
| Xcode / Swift Package | 基本概要と独立したテキストファイルの Source | 取得可能なビルド設定の宣言、依存関係の詳細、Scheme のパラメータ |
| ソースコード | 言語、テンプレート、シェーダー、ビルドスクリプト、設定を扱う 205 個のオフライン字句プロファイル；SQL、Diff / Patch、Protobuf、GraphQL | — |
| 文書と設定 | Markdown、JSON / JSONL / NDJSON、XML、YAML、TOML、INI、properties、EditorConfig、plist と関連する Apple 設定、CSV / TSV、TXT / TEXT のプレーンテキスト。dotenv はキー名のみ | — |
| Mermaid | Markdown 内の Mermaid フェンス付きソースの構文強調表示 | 単独の `.mmd` / `.mermaid` と Markdown 内の図（macOS 14.4 以降） |
| ログとレポート | `.log` / `.out` / `.trace`、`.crash`、`.ips`、認識された JSONL / NDJSON ログの構文強調表示 | 制限内の要約と構造化された詳細。Android Logcat / Android Studio のレイアウトを含む |
| データベース | SQLite の概要とテーブル構造（`.sqlite`、`.sqlite3`、`.db`、`.db3`、`.s3db`、`.sdb`） | 読み取り専用レコードページと BLOB の先頭部分 |
| アーカイブ | Apple Archive、ZIP / `.skill`、TAR、TAR.GZ / TGZ、GZ メタデータ、JAR / WAR の項目一覧 | 対応する 7z の一覧と JAR / WAR マニフェストの詳細 |

実際の表示は内容と macOS による拡張機能の選択に依存します。TypeScript の `.ts` / `.mts`、dotenv、AAR、TXT / TEXT、IPS、一部の plist / CSV にはプロバイダや振り分けの既知の制約があります。YAML と TOML の構造ビューは構文の一部に対応します。TXT / TEXT はプレーンテキストとして表示し、ログや文書の自動判別は行いません。

## 0.1.9 の新機能

- Xcode プロジェクト、Workspace、Scheme、xcconfig、Swift Package の概要を追加。基本概要と独立ファイルの Source は無料、宣言と依存関係の詳細は Pro です。
- Apple アプリのビルド情報と、Pro のコンポーネント・リンク依存関係・プライバシー宣言概要を追加。
- Apple Archive 一覧と `.skill` ZIP プレビューを追加。Android AAR は APK と共通の概要で取得可能な SDK とリソース統計を表示。
- 各言語のオフラインヘルプと無視ルール専用ハイライトを追加。
- ネイティブ表、アーカイブ詳細、ツリー展開、SQLite の選択表示、Markdown レイアウトを改善。
- オフライン Mermaid エンジンを更新し、`.mmd` の認識とズーム率表示を改善。図には Pro と macOS 14.4 以降が必要です。
- 上限付き解析、キャンセル、破損・不完全なプレビューの復旧を改善。
- Finder のファイルサムネイルは保留。クイックルックの内容とウインドウ内アイコンは引き続き利用できます。

## 使い始める

1. [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) で Peeka をダウンロードするか、[公式サイト](https://mellowbit.studio/peeka)で製品を確認します。
2. インストール後に Peeka を起動し、案内に従います。必要に応じて**システム設定**で Quick Look 拡張機能を有効にします。
3. Peeka の形式一覧で対象形式が有効か確認します。
4. **Finder** で対応ファイルを選び、**スペースキー**を押します。

スイッチの変更や Pro の解除後は Quick Look を閉じて開き直してください。メインアプリには設定案内、形式の切り替え、設定、購入機能があり、ファイルプレビューは Finder に表示されます。

形式検索と言語別のスイッチも用意されています。制約や問題は[機能リファレンス（英語）](skills/peeka/references/features-and-plans.md)と[トラブルシューティング（英語）](skills/peeka/references/troubleshooting.md)をご覧ください。

## Peeka Pro

一般的な形式は無料でプレビューできます。**Peeka Pro** は任意の**買い切りのアプリ内課金**で、**サブスクリプションやプレビューごとの料金はありません**。上表の追加形式と詳細を利用できます。

**設定 → Peeka Pro** で購入または購入の復元ができます。価格はアプリ内の Apple StoreKit が表示する現地価格をご確認ください。

一部のプレビューには制限があります。

- SQLite はページあたり最大 **100 行**、表示データは **1 MiB** まで。BLOB は先頭 **4 KiB** まで読み取ります。データベースの編集や保守は行いません。
- 署名メタデータは取得できた情報の表示であり、有効性の検証ではありません。
- ログとレポートの原文・詳細には上限があります。統計は解析されたプレビュー部分が対象です。構造化 IPS は標準クラッシュレポート（309）向けで、シンボリケーションは行いません。
- 内蔵のオフライン Pele エンジンは 20 種類の Mermaid 図に対応。未対応の構文・指令やリソース上限に達した場合は、理由と強調表示されたソースを表示します。
- Pro は対応する単一コーダーのソリッド 7z 一覧を表示できます。暗号化ヘッダー、フィルターチェーン、未対応の形式では表示できない場合があります。一覧には上限があり、大規模アーカイブは一部のみ表示される場合があります。

リソースと互換性の制約は無料版と Pro の両方に適用されます。

## AI エージェントスキル

公開 [`peeka` スキル（英語）](skills/peeka/SKILL.md)のバージョンは **0.1.9** です。Codex、Claude Code などの互換エージェントが、インストール、対応形式、無料・Pro 機能、プレビュー設定、問題解決を支援します。

リポジトリのデフォルトブランチへの公開後にインストールできます。

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

スキルには Python 3.9+ 用の [Preview Doctor](skills/peeka/references/preview-doctor.md) が付属し、ファイル形式、候補プロバイダー、時間制限付きの追跡、復元可能な拡張機能の修復に対応します。対応形式では Peeka を優先し、エージェントが該当スイッチを直接有効にします。Pro が必要な機能は購入を案内し、支払いの最終確認はユーザーが行います。未対応形式は AI が解決策を調査し、未解決の場合は個人情報を除いた GitHub 下書きを確認後に送信します。証拠がない場合、実際のプロバイダーは未確認と表示します。

このコマンドはスキルをインストールします。Peeka アプリは Mac App Store から別途ダウンロードしてください。対象エージェントの指定、グローバルインストール、ローカルテストは[スキル導入ガイド（英語）](skills/README.md)をご覧ください。デスクトップ操作にはローカルツールが必要です。Apple Account の認証と購入確認は利用者が行います。エージェントは利用者の言語で回答します。

## フィードバックとサポート

不具合や機能の要望は [Issue](https://github.com/MellowbitStudio/Peeka/issues) でお知らせください。macOS と Peeka のバージョン、ファイル形式、再現手順、期待する動作を記載してください。スクリーンショットや機密情報を含まない小さなサンプルも役立ちます。

メール：[support@mellowbit.studio](mailto:support@mellowbit.studio)。

## このリポジトリについて

[Mellowbit Studio](https://mellowbit.studio/peeka) が管理する Peeka の公開製品情報・フィードバック用リポジトリです。製品情報と公開ドキュメントを収録しています。**アプリのソースコードは含まれていません。**
