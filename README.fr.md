# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · Français · [Español](README.es.md)

Peeka est une app macOS native qui ajoute au Finder des aperçus adaptés aux développeurs. Sélectionnez un fichier pris en charge et appuyez sur **Espace** pour explorer des paquets d’applications, lire du code avec coloration syntaxique, parcourir des données structurées, consulter des schémas SQLite et afficher le contenu d’archives.

[Télécharger sur l’App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Site web](https://mellowbit.studio/peeka) · [Signaler un problème](https://github.com/MellowbitStudio/Peeka/issues) · [Confidentialité](https://mellowbit.studio/peeka/privacy/)

Nécessite **macOS 14 ou ultérieur** ; le rendu des diagrammes Mermaid nécessite **macOS 14.4+** et Pro. Disponible en **anglais, chinois simplifié et traditionnel, japonais, coréen, allemand, français et espagnol**.

**Peeka 0.1.9 a été approuvé et est disponible sur le Mac App Store.** Mettez l’app à jour depuis l’App Store pour accéder aux nouveaux aperçus.

**La bêta TestFlight 0.1.8 a été approuvée**, comme confirmé par le responsable le **2026-10-29**. [Rejoindre TestFlight](https://testflight.apple.com/join/5jM8yxDB).

## Fonctionnalités

Ces fonctionnalités sont disponibles dans la version 0.1.9. Consultez les [nouveautés](#nouveautés-de-la-version-019) depuis la version 0.1.7.

- **Paquets d’applications :** consultez les icônes, noms, identifiants, versions, exigences système et architectures disponibles dans les paquets Android et Apple.
- **Code source :** coloration syntaxique, numéros de ligne, sélection et copie natives pour les langages courants. Activez ou désactivez les aperçus par langage.
- **Diff / Patch :** vues gratuites Source, Fluid, Blocks et Unified, avec sélection de fichiers, numéros de ligne d’origine et décompte des modifications. Les correctifs ne sont ni appliqués ni utilisés pour lire les fichiers référencés.
- **Markdown :** documents mis en forme avec blocs de code colorés, tableaux à défilement horizontal indépendant, listes de tâches en lecture seule et images locales dont l’accès est autorisé.
- **Mermaid :** diagrammes autonomes ou intégrés à Markdown, vue source, zoom et déplacement vectoriels. Le rendu graphique nécessite Pro et macOS 14.4+ ; le code des blocs Mermaid dans Markdown reste gratuit.
- **Journaux et rapports de plantage :** lecture gratuite du texte coloré des journaux, d’Android Logcat et des rapports de plantage. Pro ajoute des résumés et détails structurés dans des limites définies pour les contenus reconnus.
- **DMG et PKG plats :** consultez les métadonnées ainsi que les noms et icônes d’apps intégrées détectés dans les limites d’analyse, sans monter d’image ni installer de paquet.
- **Données structurées :** vues Source, Plan et Carte mentale pour JSON, YAML, TOML et INI. Développez ou repliez les structures, déplacez et zoomez les cartes au trackpad.
- **SQLite :** résumés des bases et structures des tables gratuits. Pro ajoute des pages d’enregistrements en lecture seule et l’aperçu du début des BLOB.
- **Archives :** parcourez les listes prises en charge sans extraire de fichiers sur le disque, avec vues en liste et en colonnes pour naviguer dans les dossiers.
- **Traitement local :** le contenu et les métadonnées des fichiers sont traités sur votre Mac. Aucun compte Peeka n’est requis.

## Formats pris en charge

| Catégorie | Aperçus gratuits | Ajouts de Peeka Pro |
| --- | --- | --- |
| Paquets Android | APK et résumé AAR de type APK | AAB, APKS, XAPK, APKM ; résumés limités des autorisations, de la signature et du manifeste, selon disponibilité |
| Paquets Apple | IPA, APP, APPEX ; métadonnées DMG / PKG plats et informations limitées sur les apps intégrées | XCArchive, XCFramework, Framework, dSYM, profils de provisionnement, dylib, métadonnées de signature, composants, dépendances liées et déclarations de confidentialité, selon disponibilité |
| Xcode / Swift Package | Résumés de base et Source pour les fichiers texte autonomes | Paramètres de compilation déclarés, détails des dépendances et paramètres de Scheme, selon disponibilité |
| Code source | 205 profils lexicaux hors ligne pour langages, modèles, shaders, scripts de compilation et configurations ; SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documents et configuration | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist et configurations Apple associées, CSV / TSV, TXT / TEXT en texte brut ; noms de clés uniquement pour dotenv | — |
| Mermaid | Code coloré des blocs Mermaid dans Markdown | Fichiers `.mmd` / `.mermaid` autonomes et diagrammes Markdown (macOS 14.4+) |
| Journaux et rapports | Texte coloré des `.log` / `.out` / `.trace`, `.crash`, `.ips` et journaux JSONL / NDJSON reconnus | Résumés limités et détails structurés, avec présentations Android Logcat / Android Studio |
| Bases de données | Résumés SQLite et structures des tables (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Pages d’enregistrements en lecture seule et début des BLOB |
| Archives | Apple Archive, ZIP / `.skill`, TAR, TAR.GZ / TGZ, métadonnées GZ, listes JAR / WAR | Listes 7z prises en charge et détails des manifestes JAR / WAR |

L’aperçu dépend du contenu et du choix de l’extension Peeka par macOS. TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS et certains fichiers plist / CSV ont des limites connues de fournisseur ou d’acheminement. Les vues structurées YAML et TOML prennent en charge un sous-ensemble limité de leur syntaxe. TXT / TEXT reste du texte brut, sans détection automatique de journal ou de document.

## Nouveautés de la version 0.1.9

- Ajout de résumés Xcode, Workspace, Scheme, xcconfig et Swift Package. Résumés de base et Source des fichiers autonomes gratuits. Pro donne accès aux déclarations et aux détails des dépendances.
- Ajout d’informations de compilation Apple et de résumés Pro des composants, dépendances liées et déclarations de confidentialité.
- Ajout de listes Apple Archive et d’aperçus ZIP `.skill`. Android AAR reprend le résumé APK avec les SDK et statistiques de ressources disponibles.
- Ajout d’une aide hors ligne localisée et d’une coloration dédiée aux règles d’exclusion.
- Amélioration des tableaux natifs, détails d’archives, transitions d’arborescence, sélection SQLite et présentation Markdown.
- Mise à jour du moteur Mermaid hors ligne. La reconnaissance des fichiers `.mmd` et l’affichage du niveau de zoom ont été améliorés. Les diagrammes nécessitent Pro et macOS 14.4+.
- Amélioration de l’analyse bornée, de l’annulation et de la reprise des aperçus incomplets ou endommagés.
- Vignettes de fichiers Finder différées dans cette version. Les aperçus Coup d’œil et leurs icônes restent disponibles.

## Premiers pas

1. Téléchargez Peeka sur le [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289), ou découvrez l’app sur le [site web](https://mellowbit.studio/peeka).
2. Lancez Peeka après l’installation et suivez les instructions. Si nécessaire, activez son extension Coup d’œil dans les **Réglages Système**.
3. Vérifiez que le format concerné est activé dans la liste de Peeka.
4. Sélectionnez un fichier pris en charge dans le **Finder** et appuyez sur **Espace**.

Après un changement de format ou le déverrouillage de Pro, fermez puis rouvrez Coup d’œil. L’app principale fournit l’aide à la configuration, les contrôles des formats, les réglages et les achats ; les aperçus apparaissent dans le Finder.

L’app propose une recherche de formats et des interrupteurs par langage source. Consultez la [référence des fonctions (anglais)](skills/peeka/references/features-and-plans.md) et le [dépannage (anglais)](skills/peeka/references/troubleshooting.md).

## Peeka Pro

Les formats courants bénéficient d’aperçus gratuits. **Peeka Pro** est un **achat intégré unique** facultatif, **sans abonnement ni facturation par aperçu**, qui débloque les formats et détails supplémentaires du tableau.

Achetez ou restaurez Pro dans **Réglages → Peeka Pro**. Le prix applicable est le prix local affiché dans l’app par Apple StoreKit.

Certains aperçus sont limités :

- SQLite affiche au plus **100 lignes** par page, dans une limite d’affichage de **1 MiB**. Les aperçus BLOB lisent les **4 KiB** initiaux au maximum. Peeka ne modifie pas les bases et n’en assure pas la maintenance.
- Les métadonnées de signature décrivent les informations disponibles, sans vérifier la validité de la signature.
- Le texte et les détails des journaux et rapports sont limités ; les statistiques concernent la partie analysée de l’aperçu. Les IPS structurés visent les rapports de plantage standard (309), sans symbolication.
- Le moteur Pele intégré prend en charge 20 familles de diagrammes Mermaid hors ligne. Une syntaxe ou des directives non prises en charge, ou le dépassement des ressources, entraînent l’affichage du code coloré avec une explication.
- Pro peut afficher les listes 7z solides compatibles à un seul codeur. Les en-têtes chiffrés, chaînes de filtres ou variantes non prises en charge peuvent empêcher l’affichage. Les listes sont limitées et peuvent être incomplètes pour les grandes archives.

Les limites de ressources et de compatibilité s’appliquent aux aperçus gratuits comme à Pro.

## Skill pour agents IA

Le [skill public `peeka` (anglais)](skills/peeka/SKILL.md), version **0.1.9**, aide Codex, Claude Code et d’autres agents compatibles à installer l’app, expliquer les formats et fonctions gratuites/Pro, gérer les aperçus et résoudre les problèmes.

Après publication dans la branche par défaut du dépôt, installez-le avec :

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

Le skill inclut [Preview Doctor](skills/peeka/references/preview-doctor.md) pour Python 3.9+ : diagnostic des types et fournisseurs possibles, observation limitée dans le temps et modification réversible des extensions. Pour les formats pris en charge, l’agent privilégie Peeka et active directement le bon interrupteur. Il explique les fonctions nécessitant Pro et vous guide vers l’achat, dont vous confirmez le paiement. Pour les autres formats, l’IA recherche une solution. Les problèmes non résolus donnent lieu à un brouillon GitHub expurgé, soumis après votre accord. Sans preuve suffisante, le fournisseur réel reste non confirmé.

Cette commande installe le skill ; téléchargez l’app séparément sur le Mac App Store. Le [guide d’installation (anglais)](skills/README.md) décrit le choix des agents, l’installation globale et les essais locaux. Les actions sur le bureau nécessitent des outils locaux ; vous effectuez l’authentification Apple et confirmez les achats. Les agents répondent dans votre langue.

## Retours et assistance

Pour un bug ou une suggestion, [ouvrez une issue](https://github.com/MellowbitStudio/Peeka/issues) avec les versions de macOS et Peeka, le format, les étapes de reproduction et le résultat attendu. Une capture ou un petit exemple sans données sensibles facilite le diagnostic.

Contact : [support@mellowbit.studio](mailto:support@mellowbit.studio).

## À propos de ce dépôt

Ce dépôt public de présentation et de retours sur Peeka est maintenu par [Mellowbit Studio](https://mellowbit.studio/peeka). Il contient des informations produit et de la documentation publique. **Le code source de l’app n’est pas inclus.**
