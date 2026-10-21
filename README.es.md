# Peeka

**Ultimate Quick Look App**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · Español

Peeka es una app nativa de macOS que añade al Finder vistas previas pensadas para desarrolladores. Selecciona un archivo compatible y pulsa la **barra espaciadora** para explorar paquetes de aplicaciones, leer código con resaltado de sintaxis, examinar datos estructurados, consultar esquemas SQLite y ver el contenido de archivos comprimidos.

[Descargar en el App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) · [Sitio web](https://mellowbit.studio/peeka) · [Informar de un problema](https://github.com/MellowbitStudio/Peeka/issues) · [Privacidad](https://mellowbit.studio/peeka/privacy/)

Requiere **macOS 14 o posterior**; la representación gráfica de Mermaid requiere **macOS 14.4+** y Pro. Disponible en **inglés, chino simplificado y tradicional, japonés, coreano, alemán, francés y español**.

**Peeka 0.1.5 ha superado la revisión del App Store y está disponible oficialmente**, según la confirmación del **2026-10-19**. La información siguiente corresponde al producto 0.1.5 revisado ese día, con vistas previas nativas Diff / Patch y actualizaciones de Mermaid. Actualiza las instalaciones anteriores desde el App Store. La vista previa también depende de la compatibilidad del archivo y del proveedor seleccionado por el Finder.

**0.1.6 (20261020.1) · Revisión de TestFlight aprobada** · 2026-10-21 · [TestFlight](https://testflight.apple.com/join/5jM8yxDB)

## Funciones

Estas son las funciones publicadas en 0.1.5. Consulta las implementaciones posteriores en [Estado del desarrollo](#estado-del-desarrollo).

- **Paquetes de aplicaciones:** consulta los iconos, nombres, identificadores, versiones, requisitos del sistema y arquitecturas disponibles en paquetes Android y Apple. Los paquetes compatibles con iconos integrados también pueden generar miniaturas del Finder.
- **Código fuente:** resaltado de sintaxis, números de línea, selección y copia de texto nativas para lenguajes habituales. Activa o desactiva las vistas previas por lenguaje.
- **Diff / Patch:** vistas gratuitas Source, Fluid, Blocks y Unified con selección de archivos, números de línea originales y recuentos de cambios. No aplica parches ni lee los archivos mencionados.
- **Markdown:** documentos con formato, bloques de código resaltados, tablas con desplazamiento horizontal independiente, listas de tareas de solo lectura e imágenes locales con acceso autorizado.
- **Mermaid:** diagramas independientes o incluidos en Markdown, vista del código y zoom y desplazamiento vectoriales. La representación gráfica requiere Pro y macOS 14.4+; el código de los bloques Mermaid en Markdown sigue siendo gratuito.
- **Registros e informes de fallos:** lectura gratuita del texto resaltado de registros, Android Logcat e informes de fallos. Pro añade resúmenes y detalles estructurados de contenidos reconocidos dentro de límites definidos.
- **DMG y PKG planos:** consulta metadatos y nombres e iconos de apps integradas dentro de los límites de inspección, sin montar imágenes ni instalar paquetes.
- **Datos estructurados:** alterna entre Código, Esquema y Mapa mental para JSON, YAML, TOML e INI. Expande o contrae estructuras y desplaza o amplía mapas con el trackpad.
- **SQLite:** resúmenes de bases de datos y estructuras de tablas gratuitos. Pro añade páginas de registros de solo lectura y vistas previas del inicio de los BLOB.
- **Archivos comprimidos:** explora listados compatibles sin extraer archivos al disco, con vistas de lista y columnas para recorrer carpetas.
- **Procesamiento local:** el contenido y los metadatos se procesan en tu Mac. No necesitas una cuenta de Peeka.

## Formatos compatibles

| Categoría | Vistas previas gratuitas | Funciones adicionales de Peeka Pro |
| --- | --- | --- |
| Paquetes Android | APK | AAB, APKS, XAPK, APKM, AAR; resúmenes limitados de permisos, firma y manifiesto cuando estén disponibles |
| Paquetes Apple | IPA, APP, APPEX; metadatos DMG / PKG planos e información limitada de apps integradas | XCArchive, XCFramework, perfiles de aprovisionamiento, dylib; metadatos de firma disponibles |
| Código fuente | Swift, C / C++, Objective-C, Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, Shell, HTML, CSS, SQL, Diff / Patch, Protobuf, GraphQL | — |
| Documentos y configuración | Markdown, JSON / JSONL / NDJSON, XML, YAML, TOML, INI, properties, EditorConfig, plist y configuraciones Apple relacionadas, CSV / TSV, TXT / TEXT como texto sin formato; solo nombres de claves en dotenv | — |
| Mermaid | Código resaltado de bloques Mermaid en Markdown | Archivos `.mmd` / `.mermaid` independientes y diagramas Markdown (macOS 14.4+) |
| Registros e informes | Texto resaltado de `.log` / `.out` / `.trace`, `.crash`, `.ips` y registros JSONL / NDJSON reconocidos | Resúmenes limitados y detalles estructurados, con diseños Android Logcat / Android Studio |
| Bases de datos | Resúmenes SQLite y estructuras de tablas (`.sqlite`, `.sqlite3`, `.db`, `.db3`, `.s3db`, `.sdb`) | Páginas de registros de solo lectura e inicio de BLOB |
| Archivos comprimidos | ZIP, TAR, TAR.GZ / TGZ, metadatos GZ, listados JAR / WAR | Listados 7z compatibles y detalles de manifiestos JAR / WAR |

La disponibilidad depende del contenido y de que macOS elija la extensión de Peeka. TypeScript `.ts` / `.mts`, dotenv, AAR, TXT / TEXT, IPS y algunos plist / CSV tienen limitaciones conocidas de proveedor o asignación. Las vistas estructuradas YAML y TOML admiten un subconjunto limitado de su sintaxis. TXT / TEXT se mantiene como texto sin formato, sin detección automática de registros o documentos.

## Estado del desarrollo

Peeka 0.1.6 (20261020.1) ha superado la revisión de TestFlight. La Beta añade vistas Pro de Framework/dSYM y mejora las listas de archivos grandes, la codificación de nombres y los diagramas Pele sin conexión. La versión del Mac App Store sigue siendo la 0.1.5. [TestFlight](https://testflight.apple.com/join/5jM8yxDB) · [0.1.6 Beta](https://mellowbit.studio/es/peeka/beta-release-notes/)

- **Vistas previas de Framework (Pro):** identidad de `.framework` y arquitecturas Mach-O, UUID, plataformas y versiones mínimas del sistema disponibles. Admite paquetes planos y versionados de macOS; los frameworks estáticos habituales solo muestran su identidad.
- **Símbolos de depuración (Pro):** nombres de binarios y UUID por arquitectura de `.dSYM`. No expande símbolos, no simboliza informes de fallos ni relaciona automáticamente binarios con informes.
- **Motor Mermaid actualizado:** Pele 1.6.0 integrado representa 20 familias de diagramas sin conexión, con temas claro/oscuro y zoom y desplazamiento vectoriales nativos. El diseño y la compatibilidad de sintaxis pueden diferir de Mermaid.js en 0.1.5.
- **Archivos comprimidos:** metadatos bajo demanda para listas grandes, más allá de los primeros 256 elementos. Mejoras de indexación, ordenación, cancelación, recuperación y nombres con codificaciones antiguas en ZIP/JAR/WAR y TAR/TGZ. Pro mejora las cabeceras LZMA/LZMA2 y las listas solid 7z compatibles de un solo codificador. Siguen aplicándose límites de recursos y listas parciales.

Framework y dSYM tienen interruptores independientes y no generan miniaturas personalizadas. La validación local registró vistas previas con la barra espaciadora para ambos y una vista previa en columnas del Finder para dSYM. El Finder abre los frameworks como directorios en columnas.

## Primeros pasos

1. Descarga Peeka del [Mac App Store](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) o descubre la app en el [sitio web](https://mellowbit.studio/peeka).
2. Abre Peeka después de instalarlo y sigue las instrucciones. Si es necesario, activa su extensión de Vista rápida en **Ajustes del Sistema**.
3. Comprueba que el formato correspondiente esté activado en la lista de Peeka.
4. Selecciona un archivo compatible en el **Finder** y pulsa la **barra espaciadora**.

Tras cambiar un interruptor o desbloquear Pro, cierra y vuelve a abrir Vista rápida. La app principal ofrece ayuda de configuración, controles de formatos, ajustes y compras; las vistas previas aparecen en el Finder.

Los interruptores de vista previa no controlan las miniaturas de paquetes, que tampoco requieren Pro. La app incluye búsqueda de formatos e interruptores por lenguaje de código. Consulta la [referencia de funciones (inglés)](skills/peeka/references/features-and-plans.md) y la [guía de resolución de problemas (inglés)](skills/peeka/references/troubleshooting.md).

## Peeka Pro

Peeka ofrece vistas previas gratuitas para formatos habituales. **Peeka Pro** es una **compra única dentro de la app**, opcional, **sin suscripción ni cobros por vista previa**, que desbloquea los formatos y detalles adicionales de la tabla.

Compra o restaura Pro en **Ajustes → Peeka Pro**. El precio aplicable es el precio local que Apple StoreKit muestra en la app.

Algunas vistas previas tienen límites:

- SQLite muestra hasta **100 filas** por página, con un límite de visualización de **1 MiB**. Los BLOB se leen hasta los primeros **4 KiB**. Peeka no edita ni mantiene bases de datos.
- Los metadatos de firma describen la información disponible; no verifican la validez de la firma.
- El texto y los detalles de registros e informes tienen límites. Las estadísticas corresponden a la parte analizada de la vista previa. Los IPS estructurados se orientan a informes de fallos estándar (309), sin simbolización.
- La base documentada de 0.1.5 admite 20 familias de diagramas Mermaid. Si la sintaxis o las directivas no son compatibles, o se superan los recursos, se muestra el código resaltado con el motivo.
- Algunas variantes 7z cifradas, sólidas o no compatibles pueden no mostrar su listado. Las listas tienen límites y pueden quedar incompletas en archivos grandes.

Los límites de recursos y compatibilidad se aplican tanto a las vistas gratuitas como a Pro.

## Skill para agentes de IA

El [skill público `peeka` (inglés)](skills/peeka/SKILL.md), versión **0.1.5**, ayuda a Codex, Claude Code y otros agentes compatibles a instalar la app, explicar formatos y funciones gratuitas/Pro, controlar vistas previas y resolver problemas.

Cuando se publique en la rama predeterminada del repositorio, instálalo con:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

Este comando instala el skill; descarga la app Peeka por separado del Mac App Store. La [guía de instalación (inglés)](skills/README.md) explica cómo elegir agentes, instalar globalmente y probar cambios locales. Las acciones de escritorio requieren herramientas locales; tú realizas la autenticación de Apple y confirmas las compras. Los agentes responden en tu idioma.

## Comentarios y soporte

Para informar de errores o sugerir funciones, [abre una incidencia](https://github.com/MellowbitStudio/Peeka/issues). Incluye las versiones de macOS y Peeka, el formato, los pasos para reproducir el problema y el comportamiento esperado. Una captura o una muestra pequeña sin información sensible puede ayudar al diagnóstico.

Correo: [support@mellowbit.studio](mailto:support@mellowbit.studio).

## Acerca de este repositorio

Este repositorio público de producto y comentarios de Peeka está mantenido por [Mellowbit Studio](https://mellowbit.studio/peeka). Contiene información del producto y documentación pública. **No incluye el código fuente de la app.**
