# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · Deutsch · [Français](README.fr.md) · [Español](README.es.md)

Peeka ist eine native macOS-App für entwicklerfreundliche Dateivorschauen im Finder. Wähle eine unterstützte Datei und drücke die **Leertaste**, um App-Pakete, hervorgehobenen Quellcode, strukturierte Daten, SQLite-Schemata und Archivlisten anzusehen.

[Im App Store laden](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Website](https://mellowbit.studio/peeka) · [Problem melden](https://github.com/MellowbitStudio/Peeka/issues) · [Datenschutz](https://mellowbit.studio/peeka/privacy/)

Erfordert **macOS 14 oder neuer**; die Darstellung von Mermaid-Diagrammen erfordert **macOS 14.4+** und Pro. Verfügbar auf **Englisch, vereinfachtem und traditionellem Chinesisch, Japanisch, Koreanisch, Deutsch, Französisch und Spanisch**.

**Peeka 0.1.5 hat die App-Store-Prüfung bestanden und ist offiziell verfügbar**, bestätigt am **2026-10-19**. Die folgenden Angaben entsprechen dem am selben Tag geprüften Produktstand 0.1.5 einschließlich nativer Diff-/Patch-Vorschauen und Mermaid-Updates. Aktualisiere ältere Installationen über den App Store. Die Vorschau hängt auch von der Dateikompatibilität und der Auswahl des Vorschauanbieters durch den Finder ab.

**0.1.6 (20261020.1) · TestFlight-Prüfung bestanden** · 2026-10-21 · [TestFlight](https://testflight.apple.com/join/5jM8yxDB)

## Funktionen

Die folgenden Funktionen gehören zur veröffentlichten Version 0.1.5. Spätere Implementierungen stehen unter [Entwicklungsstand](#entwicklungsstand).

- **App-Pakete:** Verfügbare Symbole, Namen, Kennungen, Versionen, Systemanforderungen und Architekturen von Android- und Apple-Paketen anzeigen. Kompatible Pakete mit eingebetteten Symbolen können auch Finder-Miniaturen erhalten.
- **Quellcode:** Syntaxhervorhebung, Zeilennummern sowie native Textauswahl und Kopieren für gängige Programmiersprachen. Vorschauen lassen sich pro Sprache ein- und ausschalten.
- **Diff / Patch:** Kostenlose Ansichten Source, Fluid, Blocks und Unified mit Dateiauswahl, ursprünglichen Zeilennummern und Änderungszahlen. Patches werden weder angewendet noch werden referenzierte Dateien gelesen.
- **Markdown:** Formatierte Dokumente mit hervorgehobenen Codeblöcken, Tabellen mit unabhängigem horizontalem Bildlauf, schreibgeschützten Aufgabenlisten und freigegebenen lokalen Bildern anzeigen.
- **Mermaid:** Eigenständige Diagramme und Diagramme in Markdown mit Quellansicht sowie Vektorzoom und Schwenken anzeigen. Die grafische Darstellung erfordert Pro und macOS 14.4+; eingezäunter Mermaid-Quelltext in Markdown bleibt kostenlos.
- **Logs und Absturzberichte:** Hervorgehobener Quelltext von Logs, Android Logcat und Absturzberichten ist kostenlos. Pro ergänzt Zusammenfassungen und strukturierte Details erkannter Inhalte innerhalb festgelegter Grenzen.
- **DMG und flache PKG:** Metadaten sowie Namen und Symbole eingebetteter Apps innerhalb festgelegter Prüfgrenzen ansehen, ohne Images einzubinden oder Pakete zu installieren.
- **Strukturierte Daten:** Für JSON, YAML, TOML und INI zwischen Quelle, Gliederung und Mindmap wechseln. Strukturen auf- und zuklappen, Mindmaps per Trackpad verschieben und zoomen.
- **SQLite:** Datenbankübersichten und Tabellenstrukturen kostenlos ansehen. Pro ergänzt schreibgeschützte Datensatzseiten und Vorschauen des BLOB-Anfangs.
- **Archive:** Unterstützte Archivlisten ohne Entpacken auf die Festplatte durchsuchen; Listen- und Spaltenansicht zur Ordnernavigation.
- **Lokale Verarbeitung:** Dateiinhalte und Metadaten werden auf deinem Mac verarbeitet. Ein Peeka-Konto ist nicht erforderlich.

## Unterstützte Formate

| Kategorie | Kostenlose Vorschauen | Zusätzliche Funktionen mit Peeka Pro |
| --- | --- | --- |
| Android-Pakete | APK | AAB, APKS, XAPK, APKM, AAR; begrenzte Zusammenfassungen von Berechtigungen, Signierung und Manifestdaten, soweit verfügbar |
| Apple-Pakete | IPA, APP, APPEX; Metadaten von DMG / flachen PKG und begrenzte Informationen zu eingebetteten Apps | XCArchive, XCFramework, Bereitstellungsprofile, dylib; verfügbare Signierungsmetadaten |
| Quellcode | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, Shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| Dokumente und Konfiguration | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist und verwandte Apple-Konfigurationen, CSV / TSV, TXT / TEXT als Klartext; dotenv nur mit Schlüsselnamen | — |
| Mermaid | Hervorgehobener Mermaid-Quelltext in Markdown-Codeblöcken | Eigenständige `.mmd` / `.mermaid` und Diagramme in Markdown (macOS 14.4+) |
| Logs und Berichte | Hervorgehobener Quelltext von `.log` / `.out` / `.trace`, `.crash`, `.ips` und erkannten JSONL-/NDJSON-Logs | Begrenzte Zusammenfassungen und strukturierte Details, einschließlich Android-Logcat-/Android-Studio-Layouts |
| Datenbanken | SQLite-Übersichten und Tabellenstrukturen (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Schreibgeschützte Datensatzseiten und BLOB-Anfangsvorschauen |
| Archive | ZIP, TAR, TAR.GZ / TGZ, GZ-Metadaten, JAR-/WAR-Dateilisten | Unterstützte 7z-Listen und JAR-/WAR-Manifestdetails |

Die Verfügbarkeit hängt vom Inhalt und davon ab, ob macOS Peekas Erweiterung auswählt. Für TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS und manche plist-/CSV-Dateien gelten bekannte Einschränkungen bei Anbieterwahl oder Zuordnung. Die Strukturansichten für YAML und TOML unterstützen begrenzte Syntaxteilmengen. TXT / TEXT bleibt Klartext ohne automatische Log- oder Dokumenterkennung.

## Entwicklungsstand

Peeka 0.1.6 (20261020.1) hat die TestFlight-Prüfung bestanden. Die Beta ergänzt Pro-Vorschauen für Framework/dSYM und verbessert große Archivlisten, Dateinamencodierungen und Offline-Diagramme mit Pele. Im Mac App Store bleibt 0.1.5 aktuell. [TestFlight](https://testflight.apple.com/join/5jM8yxDB) · [0.1.6 Beta](https://mellowbit.studio/de/peeka/beta-release-notes/)

- **Framework-Vorschauen (Pro):** Identität einer `.framework` sowie verfügbare Mach-O-Architekturen, UUIDs, Plattformen und minimale Systemversionen anzeigen. Flache und versionierte macOS-Bundles werden unterstützt; gewöhnliche statische Frameworks zeigen nur die Identität.
- **Debugsymbole (Pro):** Binärdateinamen und UUIDs pro Architektur aus `.dSYM` anzeigen. Keine Symbolauflösung, Symbolikation von Absturzberichten oder automatische Zuordnung von Binärdateien zu Berichten.
- **Aktualisierter Mermaid-Renderer:** Das mitgelieferte Pele 1.6.0 rendert 20 Diagrammfamilien offline, mit hellem/dunklem Design und nativem Vektorzoom und Schwenken. Layout und Syntaxkompatibilität können vom Mermaid.js-Renderer in 0.1.5 abweichen.
- **Archive:** Metadaten großer Listen werden bei Bedarf gelesen; die feste Grenze der ersten 256 Einträge entfällt. Verbesserte Indexierung, Sortierung, Abbruch, Wiederherstellung und ältere Dateinamencodierungen in ZIP/JAR/WAR und TAR/TGZ. Pro verbessert unterstützte LZMA/LZMA2-Header und Solid-7z-Listen mit einem Coder. Ressourcenlimits und Teillisten gelten weiterhin.

Framework und dSYM haben eigene Formatschalter und keine benutzerdefinierten Miniaturen. Die lokale App-Prüfung dokumentiert funktionierende Leertasten-Vorschauen für beide sowie eine Finder-Spaltenvorschau für dSYM. Frameworks werden in der Spaltenansicht als Verzeichnisse geöffnet.

## Erste Schritte

1. Peeka aus dem [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) laden oder auf der [Website](https://mellowbit.studio/peeka) mehr erfahren.
2. Peeka nach der Installation starten und der Einrichtung folgen. Bei Bedarf die Quick-Look-Erweiterung in den **Systemeinstellungen** aktivieren.
3. Prüfen, ob das gewünschte Format in Peekas Formatliste aktiviert ist.
4. Im **Finder** eine unterstützte Datei wählen und die **Leertaste** drücken.

Nach Änderungen an Formatschaltern oder dem Freischalten von Pro die Quick-Look-Vorschau schließen und erneut öffnen. Die Haupt-App bietet Einrichtungshilfe, Formatschalter, Einstellungen und Kaufoptionen; Dateivorschauen erscheinen im Finder.

Vorschauschalter steuern keine Paketminiaturen; diese sind unabhängig von Pro. Die Haupt-App bietet Formatsuche und separate Schalter für Quellsprachen. Siehe die [Funktionsreferenz (Englisch)](skills/peeka/references/features-and-plans.md) und die [Fehlerbehebung (Englisch)](skills/peeka/references/troubleshooting.md).

## Peeka Pro

Vorschauen für gängige Formate sind kostenlos. **Peeka Pro** ist ein optionaler **einmaliger In-App-Kauf**, **ohne Abonnement oder Kosten pro Vorschau**, der die oben aufgeführten zusätzlichen Formate und Details freischaltet.

Kaufe Pro oder stelle den Kauf unter **Einstellungen → Peeka Pro** wieder her. Maßgeblich ist der lokale Preis, den Apple StoreKit in der App anzeigt.

Für einige Vorschauen gelten Grenzen:

- SQLite zeigt maximal **100 Zeilen** pro Seite bei einem Anzeigebudget von **1 MiB**. BLOB-Vorschauen lesen höchstens die ersten **4 KiB**. Peeka bearbeitet oder wartet keine Datenbanken.
- Signierungsmetadaten beschreiben verfügbare Informationen und bestätigen keine Signaturgültigkeit.
- Log- und Berichtsquellen sowie Details sind begrenzt; Statistiken beziehen sich auf den eingelesenen Vorschauabschnitt. Strukturierte IPS-Unterstützung gilt für Standard-Absturzberichte (309), ohne Symbolikation.
- Der dokumentierte Stand 0.1.5 unterstützt 20 Mermaid-Diagrammfamilien. Nicht unterstützte Syntax, Direktiven oder Ressourcenüberschreitungen führen zu hervorgehobenem Quelltext mit Begründung.
- Verschlüsselte, solide komprimierte oder nicht unterstützte 7z-Varianten lassen sich eventuell nicht auflisten. Archivlisten sind begrenzt und bei großen Archiven möglicherweise unvollständig.

Ressourcen- und Kompatibilitätsgrenzen gelten für kostenlose und Pro-Vorschauen.

## KI-Agenten-Skill

Der öffentliche [`peeka`-Skill (Englisch)](skills/peeka/SKILL.md), Version **0.1.5**, hilft Codex, Claude Code und anderen kompatiblen Agenten bei Installation, unterstützten Formaten, kostenlosen und Pro-Funktionen, Vorschauschaltern und Fehlerbehebung.

Nach der Veröffentlichung im Standardbranch dieses Repositorys installieren mit:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

Das installiert den Agenten-Skill; die App separat aus dem Mac App Store laden. Agentenauswahl, globale Installation und lokale Tests beschreibt die [Installationsanleitung (Englisch)](skills/README.md). Desktopaktionen benötigen lokale Werkzeuge; Apple-Account-Anmeldung und Kaufbestätigung übernimmst du selbst. Agenten antworten in deiner Sprache.

## Feedback und Support

Für Fehler oder Funktionswünsche ein [Issue öffnen](https://github.com/MellowbitStudio/Peeka/issues). Bitte macOS- und Peeka-Version, Dateiformat, Schritte zur Reproduktion und erwartetes Verhalten angeben. Ein Screenshot oder eine kleine Beispieldatei ohne vertrauliche Daten hilft bei der Diagnose.

E-Mail: [support@mellowbit.studio](mailto:support@mellowbit.studio).

## Über dieses Repository

Dieses öffentliche Produkt- und Feedback-Repository für Peeka wird von [Mellowbit Studio](https://mellowbit.studio/peeka) gepflegt und enthält Produktinformationen und öffentliche Dokumentation. **Der Quellcode der App ist nicht enthalten.**
