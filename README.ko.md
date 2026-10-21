# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · 한국어 · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Peeka는 Finder에 개발자를 위한 파일 미리보기를 더하는 네이티브 macOS 앱입니다. 지원 파일을 선택하고 **스페이스 바**를 누르면 앱 패키지, 구문 강조된 소스 코드, 구조화된 데이터, SQLite 스키마, 압축 파일 목록을 살펴볼 수 있습니다.

[App Store에서 다운로드](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [웹사이트](https://mellowbit.studio/peeka) · [문제 신고](https://github.com/MellowbitStudio/Peeka/issues) · [개인정보 처리방침](https://mellowbit.studio/peeka/privacy/)

**macOS 14 이상**이 필요합니다. Mermaid 다이어그램 렌더링에는 **macOS 14.4 이상**과 Pro가 필요합니다. **영어, 중국어 간체·번체, 일본어, 한국어, 독일어, 프랑스어, 스페인어**를 지원합니다.

**Peeka 0.1.5는 App Store 심사를 통과하여 정식 출시되었습니다**(**2026-10-19** 확인). 아래 내용은 같은 날짜에 검토한 0.1.5 제품 기준이며, 네이티브 Diff / Patch 미리보기와 Mermaid 업데이트를 포함합니다. 이전 버전은 App Store에서 업데이트하세요. 실제 미리보기는 파일 호환성과 Finder가 선택하는 제공자에 따라 달라집니다.

**0.1.6 (20261020.1) · TestFlight 심사 통과** · 2026-10-21 · [TestFlight](https://testflight.apple.com/join/5jM8yxDB)

## 주요 기능

다음은 출시된 0.1.5 기능입니다. 이후 구현된 기능은 [개발 현황](#개발-현황)을 참고하세요.

- **앱 패키지:** Android 및 Apple 패키지에 있는 아이콘, 이름, 식별자, 버전, 시스템 요구 사항, 아키텍처를 표시합니다. 호환 패키지에 내장 아이콘이 있으면 Finder 축소판도 생성할 수 있습니다.
- **소스 코드:** 일반적인 개발 언어의 구문 강조, 줄 번호, 네이티브 텍스트 선택과 복사를 지원합니다. 언어별로 미리보기를 켜거나 끌 수 있습니다.
- **Diff / Patch:** Source, Fluid, Blocks, Unified 보기를 무료로 제공합니다. 파일 선택, 원래 줄 번호, 변경 수를 표시하며 패치를 적용하거나 참조된 파일을 읽지 않습니다.
- **Markdown:** 코드 블록 구문 강조, 개별 가로 스크롤 표, 읽기 전용 작업 목록, 접근이 허용된 로컬 이미지를 포함한 문서를 표시합니다.
- **Mermaid:** 독립 파일이나 Markdown 안의 다이어그램을 미리 보고 소스 보기와 벡터 확대·축소 및 이동을 사용할 수 있습니다. 그래픽 렌더링에는 Pro와 macOS 14.4 이상이 필요하며 Markdown 코드 펜스의 소스는 무료입니다.
- **로그 및 충돌 보고서:** 로그, Android Logcat, 충돌 보고서의 구문 강조 원문은 무료입니다. Pro는 인식된 내용에 대해 정해진 범위의 요약과 구조화된 상세 정보를 제공합니다.
- **DMG 및 평면 PKG:** 이미지를 마운트하거나 패키지를 설치하지 않고 메타데이터와 제한된 탐색 범위에서 찾은 내장 앱의 이름·아이콘을 확인합니다.
- **구조화된 데이터:** JSON, YAML, TOML, INI의 소스·개요·마인드맵 보기를 전환합니다. 구조를 펼치거나 접고 트랙패드로 마인드맵을 이동하거나 확대·축소할 수 있습니다.
- **SQLite:** 데이터베이스 요약과 테이블 구조는 무료입니다. Pro는 읽기 전용 레코드 페이지와 BLOB 앞부분 미리보기를 추가합니다.
- **압축 파일:** 디스크에 압축을 풀지 않고 지원 파일의 목록을 확인하며 목록 및 열 보기로 폴더를 탐색합니다.
- **로컬 처리:** 파일 내용과 메타데이터는 Mac에서 처리합니다. Peeka 계정이 필요하지 않습니다.

## 지원 형식

| 분류 | 무료 미리보기 | Peeka Pro 추가 기능 |
| --- | --- | --- |
| Android 패키지 | APK | AAB, APKS, XAPK, APKM, AAR 및 가능한 경우 정해진 범위의 권한·서명·매니페스트 요약 |
| Apple 패키지 | IPA, APP, APPEX; DMG / 평면 PKG 메타데이터와 제한된 내장 앱 정보 | XCArchive, XCFramework, 프로비저닝 프로파일, dylib 및 사용 가능한 서명 메타데이터 |
| 소스 코드 | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, Shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| 문서 및 설정 | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist 및 관련 Apple 설정, CSV / TSV, TXT / TEXT 일반 텍스트; dotenv는 키 이름만 | — |
| Mermaid | Markdown 안 Mermaid 코드 펜스의 구문 강조 소스 | 독립 `.mmd` / `.mermaid` 및 Markdown 다이어그램(macOS 14.4 이상) |
| 로그 및 보고서 | `.log` / `.out` / `.trace`, `.crash`, `.ips`, 인식된 JSONL / NDJSON 로그의 구문 강조 원문 | 정해진 범위의 요약과 구조화된 상세 정보. Android Logcat / Android Studio 레이아웃 포함 |
| 데이터베이스 | SQLite 요약과 테이블 구조(`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | 읽기 전용 레코드 페이지와 BLOB 앞부분 미리보기 |
| 압축 파일 | ZIP, TAR, TAR.GZ / TGZ, GZ 메타데이터, JAR / WAR 항목 목록 | 지원되는 7z 목록과 JAR / WAR 매니페스트 상세 정보 |

미리보기는 내용과 macOS의 Peeka 확장 선택 여부에 따라 달라집니다. TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS 및 일부 plist / CSV에는 알려진 제공자 또는 라우팅 제약이 있습니다. YAML과 TOML 구조 보기는 문법의 일부를 지원합니다. TXT / TEXT는 일반 텍스트로 유지하며 로그나 문서 유형을 자동 감지하지 않습니다.

## 개발 현황

Peeka 0.1.6(20261020.1)이 TestFlight 심사를 통과했습니다. Beta에서 Pro Framework/dSYM 미리보기를 추가하고 대용량 아카이브 목록, 파일명 인코딩과 오프라인 Pele 다이어그램을 개선했습니다. Mac App Store 정식 버전은 0.1.5입니다. [TestFlight](https://testflight.apple.com/join/5jM8yxDB) · [0.1.6 Beta](https://mellowbit.studio/ko/peeka/beta-release-notes/)

- **Framework 미리보기(Pro):** `.framework` 식별 정보와 사용 가능한 Mach-O 아키텍처, UUID, 플랫폼, 최소 시스템 버전을 표시합니다. 평면 및 macOS 버전별 번들을 지원하며 일반적인 정적 프레임워크는 식별 정보만 표시합니다.
- **디버그 심볼 미리보기(Pro):** `.dSYM`의 바이너리 이름과 아키텍처별 UUID를 표시합니다. 심볼 확장, 충돌 보고서 심볼리케이션, 바이너리와 보고서의 자동 연결은 수행하지 않습니다.
- **Mermaid 렌더러 업데이트:** Pele 1.6.0을 포함하여 20개 다이어그램 유형을 오프라인으로 렌더링합니다. 밝은·어두운 테마와 네이티브 벡터 확대·축소 및 이동을 지원합니다. 배치와 문법 호환성은 0.1.5의 Mermaid.js와 다를 수 있습니다.
- **아카이브:** 큰 목록의 메타데이터를 필요할 때 읽으며 처음 256개 고정 제한을 없앴습니다. 인덱싱, 정렬, 취소와 복구, ZIP/JAR/WAR 및 TAR/TGZ의 레거시 파일명을 개선했습니다. Pro는 지원되는 LZMA/LZMA2 헤더 및 단일 코더 solid 7z 목록을 개선합니다. 리소스 제한과 부분 목록은 여전히 적용됩니다.

Framework와 dSYM에는 별도 형식 스위치가 있으며 사용자 지정 축소판은 없습니다. 로컬 앱 검증에서는 두 형식의 스페이스 바 미리보기와 dSYM의 Finder 열 미리보기가 작동했습니다. Framework는 열 보기에서 디렉터리로 펼쳐집니다.

## 시작하기

1. [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289)에서 Peeka를 다운로드하거나 [웹사이트](https://mellowbit.studio/peeka)에서 제품을 알아보세요.
2. 설치 후 Peeka를 실행하고 안내를 따르세요. 필요한 경우 **시스템 설정**에서 훑어보기 확장을 활성화하세요.
3. Peeka의 형식 목록에서 해당 형식이 켜져 있는지 확인하세요.
4. **Finder**에서 지원 파일을 선택하고 **스페이스 바**를 누르세요.

형식 스위치를 바꾸거나 Pro를 잠금 해제한 후에는 훑어보기를 닫았다가 다시 여세요. 기본 앱은 설정 안내, 형식 제어, 설정 및 구매 기능을 제공하며 파일 미리보기는 Finder에 표시됩니다.

미리보기 스위치는 패키지 축소판을 제어하지 않으며 축소판에는 Pro가 필요하지 않습니다. 기본 앱은 형식 검색과 소스 언어별 스위치를 제공합니다. 자세한 제약은 [기능 참고 문서(영어)](skills/peeka/references/features-and-plans.md)와 [문제 해결(영어)](skills/peeka/references/troubleshooting.md)을 참고하세요.

## Peeka Pro

일반 형식은 무료로 미리 볼 수 있습니다. **Peeka Pro**는 선택 사항인 **일회성 앱 내 구입**으로, **구독이나 미리보기당 요금 없이** 위 표의 추가 형식과 상세 정보를 제공합니다.

**설정 → Peeka Pro**에서 구입하거나 구입 항목을 복원하세요. 가격은 앱의 Apple StoreKit에 표시되는 현지 가격을 따릅니다.

일부 미리보기에는 다음 제한이 있습니다.

- SQLite는 페이지당 최대 **100행**, 표시 데이터는 **1 MiB**까지입니다. BLOB는 앞 **4 KiB**만 읽습니다. 데이터베이스를 편집하거나 유지 관리하지 않습니다.
- 서명 메타데이터는 사용 가능한 정보를 설명하며 서명의 유효성을 검증하지 않습니다.
- 로그와 보고서의 원문·상세 정보에는 상한이 있습니다. 통계는 파싱된 미리보기 부분을 대상으로 합니다. 구조화된 IPS는 표준 충돌 보고서(309)를 지원하며 심볼리케이션은 수행하지 않습니다.
- 0.1.5 문서 기준으로 Mermaid는 20개 유형을 지원합니다. 지원하지 않는 문법·지시문 또는 리소스 한도 초과 시 이유와 함께 구문 강조 소스를 표시합니다.
- 암호화, 솔리드 압축 또는 지원하지 않는 7z 변형은 목록이 표시되지 않을 수 있습니다. 목록에는 상한이 있으므로 큰 압축 파일은 일부만 표시될 수 있습니다.

리소스와 호환성 제한은 무료 및 Pro 미리보기에 모두 적용됩니다.

## AI 에이전트 스킬

공개 [`peeka` 스킬(영어)](skills/peeka/SKILL.md)의 버전은 **0.1.5**입니다. Codex, Claude Code 등 호환 에이전트의 App Store 설치, 지원 형식 및 무료·Pro 기능 설명, 미리보기 제어, 문제 해결을 돕습니다.

파일이 저장소 기본 브랜치에 게시된 후 다음 명령으로 설치하세요.

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

이 명령은 에이전트 스킬을 설치합니다. Peeka 앱은 Mac App Store에서 별도로 다운로드하세요. 에이전트 지정, 전역 설치, 로컬 테스트는 [스킬 설치 안내(영어)](skills/README.md)를 참고하세요. 데스크톱 작업에는 로컬 도구가 필요하며 Apple 계정 인증과 구매 확인은 사용자가 수행합니다. 에이전트는 사용자의 언어로 응답합니다.

## 의견 및 지원

버그나 기능 제안은 [Issue](https://github.com/MellowbitStudio/Peeka/issues)로 알려주세요. macOS 및 Peeka 버전, 파일 형식, 재현 단계, 예상 동작을 포함하세요. 스크린샷이나 민감한 정보가 없는 작은 샘플도 도움이 됩니다.

이메일: [support@mellowbit.studio](mailto:support@mellowbit.studio).

## 저장소 소개

[Mellowbit Studio](https://mellowbit.studio/peeka)가 관리하는 Peeka의 공개 제품 및 피드백 저장소입니다. 제품 정보와 공개 문서를 제공합니다. **앱 소스 코드는 포함하지 않습니다.**
