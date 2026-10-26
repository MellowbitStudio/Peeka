# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · Français · [Español](README.es.md)

Peeka est une app macOS native qui ajoute au Finder des aperçus adaptés aux développeurs. Sélectionnez un fichier pris en charge et appuyez sur **Espace** pour explorer des paquets d’applications, lire du code avec coloration syntaxique, parcourir des données structurées, consulter des schémas SQLite et afficher le contenu d’archives.

[Télécharger sur l’App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Site web](https://mellowbit.studio/peeka) · [Signaler un problème](https://github.com/MellowbitStudio/Peeka/issues) · [Confidentialité](https://mellowbit.studio/peeka/privacy/)

Nécessite **macOS 14 ou ultérieur** ; le rendu des diagrammes Mermaid nécessite **macOS 14.4+** et Pro. Disponible en **anglais, chinois simplifié et traditionnel, japonais, coréen, allemand, français et espagnol**.

**Peeka 0.1.7 a été approuvé par l’App Store et est officiellement disponible**, état confirmé par le mainteneur le **2026-10-26**. Mettez l’app à jour via l’App Store pour la coloration du code étendue, les aperçus Pro Framework/dSYM, les améliorations d’archives et les diagrammes Pele hors ligne. Les aperçus dépendent de la compatibilité des fichiers et du fournisseur choisi par le Finder.

## Fonctionnalités

Voici les fonctions publiées dans la version 0.1.7. Consultez les changements depuis 0.1.5 dans les [nouveautés](#nouveautés-de-la-version-017).

- **Paquets d’applications :** consultez les icônes, noms, identifiants, versions, exigences système et architectures disponibles dans les paquets Android et Apple. Les paquets compatibles contenant une icône peuvent aussi recevoir une vignette dans le Finder.
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
| Paquets Android | APK | AAB, APKS, XAPK, APKM, AAR ; résumés limités des autorisations, de la signature et du manifeste, selon disponibilité |
| Paquets Apple | IPA, APP, APPEX ; métadonnées DMG / PKG plats et informations limitées sur les apps intégrées | XCArchive, XCFramework, Framework, dSYM, profils de provisionnement, dylib ; métadonnées de signature disponibles |
| Code source | 205 profils lexicaux hors ligne pour langages, modèles, shaders, scripts de compilation et configurations ; SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documents et configuration | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist et configurations Apple associées, CSV / TSV, TXT / TEXT en texte brut ; noms de clés uniquement pour dotenv | — |
| Mermaid | Code coloré des blocs Mermaid dans Markdown | Fichiers `.mmd` / `.mermaid` autonomes et diagrammes Markdown (macOS 14.4+) |
| Journaux et rapports | Texte coloré des `.log` / `.out` / `.trace`, `.crash`, `.ips` et journaux JSONL / NDJSON reconnus | Résumés limités et détails structurés, avec présentations Android Logcat / Android Studio |
| Bases de données | Résumés SQLite et structures des tables (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Pages d’enregistrements en lecture seule et début des BLOB |
| Archives | ZIP, TAR, TAR.GZ / TGZ, métadonnées GZ, listes JAR / WAR | Listes 7z prises en charge et détails des manifestes JAR / WAR |

L’aperçu dépend du contenu et du choix de l’extension Peeka par macOS. TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS et certains fichiers plist / CSV ont des limites connues de fournisseur ou d’acheminement. Les vues structurées YAML et TOML prennent en charge un sous-ensemble limité de leur syntaxe. TXT / TEXT reste du texte brut, sans détection automatique de journal ou de document.

## Nouveautés de la version 0.1.7

La version 0.1.7 apporte les mises à jour suivantes au Mac App Store, y compris les améliorations de la Beta 0.1.6. [Notes de version](https://mellowbit.studio/fr/peeka/release-notes/)

- **Coloration du code étendue (gratuite) :** 205 profils lexicaux hors ligne couvrent langages, modèles, shaders, scripts de compilation et configurations, avec des interrupteurs par langage et une coloration partagée avec les blocs Markdown. Sans exécution du code ni validation syntaxique complète.
- **Reconnaissance des fichiers :** Reconnaissance et routage Finder améliorés pour les fichiers cachés, les fichiers de compilation sans extension et les fichiers de verrouillage courants. Les fichiers génériques non reconnus affichent les informations de base ; `.ipynb` affiche le code JSON. macOS choisit toujours le fournisseur d’aperçu.
- **Aperçus Framework (Pro) :** identité des `.framework` et architectures Mach-O, UUID, plateformes et versions système minimales disponibles. Les paquets plats et versionnés macOS sont pris en charge ; les frameworks statiques ordinaires affichent uniquement leur identité.
- **Symboles de débogage (Pro) :** noms des binaires et UUID par architecture dans les `.dSYM`. Pas de développement des symboles, de symbolication des rapports ni d’association automatique entre binaires et rapports.
- **Moteur Mermaid mis à jour :** Pele 1.6.0 est intégré pour afficher hors ligne 20 familles de diagrammes, avec thèmes clair/sombre, zoom et déplacement vectoriels natifs. La mise en page et la compatibilité syntaxique peuvent différer du moteur Mermaid.js de 0.1.5.
- **Archives :** lecture des métadonnées à la demande pour les grandes listes, au-delà des 256 premiers éléments. Amélioration de l’indexation, du tri, de l’annulation, de la reprise et des anciens encodages de noms ZIP/JAR/WAR et TAR/TGZ. Pro améliore les en-têtes LZMA/LZMA2 et les listes solid 7z pris en charge à un seul coder. Les limites de ressources et les listes partielles restent possibles.

Framework et dSYM ont des interrupteurs indépendants et aucune vignette personnalisée. La validation locale de l’app a constaté le fonctionnement des aperçus avec Espace pour les deux formats et de l’aperçu en colonnes du Finder pour dSYM. Les frameworks s’ouvrent comme des dossiers en colonnes.

## Premiers pas

1. Téléchargez Peeka sur le [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289), ou découvrez l’app sur le [site web](https://mellowbit.studio/peeka).
2. Lancez Peeka après l’installation et suivez les instructions. Si nécessaire, activez son extension Coup d’œil dans les **Réglages Système**.
3. Vérifiez que le format concerné est activé dans la liste de Peeka.
4. Sélectionnez un fichier pris en charge dans le **Finder** et appuyez sur **Espace**.

Après un changement de format ou le déverrouillage de Pro, fermez puis rouvrez Coup d’œil. L’app principale fournit l’aide à la configuration, les contrôles des formats, les réglages et les achats ; les aperçus apparaissent dans le Finder.

Les interrupteurs d’aperçu ne contrôlent pas les vignettes de paquets, qui ne nécessitent pas Pro. L’app propose une recherche de formats et des interrupteurs par langage source. Consultez la [référence des fonctions (anglais)](skills/peeka/references/features-and-plans.md) et le [dépannage (anglais)](skills/peeka/references/troubleshooting.md).

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

Le [skill public `peeka` (anglais)](skills/peeka/SKILL.md), version **0.1.7**, aide Codex, Claude Code et d’autres agents compatibles à installer l’app, expliquer les formats et fonctions gratuites/Pro, gérer les aperçus et résoudre les problèmes.

Après publication dans la branche par défaut du dépôt, installez-le avec :

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

Cette commande installe le skill ; téléchargez l’app séparément sur le Mac App Store. Le [guide d’installation (anglais)](skills/README.md) décrit le choix des agents, l’installation globale et les essais locaux. Les actions sur le bureau nécessitent des outils locaux ; vous effectuez l’authentification Apple et confirmez les achats. Les agents répondent dans votre langue.

## Retours et assistance

Pour un bug ou une suggestion, [ouvrez une issue](https://github.com/MellowbitStudio/Peeka/issues) avec les versions de macOS et Peeka, le format, les étapes de reproduction et le résultat attendu. Une capture ou un petit exemple sans données sensibles facilite le diagnostic.

Contact : [support@mellowbit.studio](mailto:support@mellowbit.studio).

## À propos de ce dépôt

Ce dépôt public de présentation et de retours sur Peeka est maintenu par [Mellowbit Studio](https://mellowbit.studio/peeka). Il contient des informations produit et de la documentation publique. **Le code source de l’app n’est pas inclus.**
