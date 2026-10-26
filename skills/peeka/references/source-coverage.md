# Source and configuration coverage — 0.1.7

Checked **2026-10-26** against app tag **0.1.7** (`a06048c`) and its canonical format documentation. **Peeka 0.1.7 is officially available on the Mac App Store**, as confirmed by the maintainer on **2026-10-26**. This reference replaces the earlier 116-profile development snapshot and describes the released baseline.

The release contains **205 free offline lexical profiles**, shared by standalone source previews and explicit Markdown fence hints. The app groups them into Source Code, Frontend & Templates, and Build Scripts; SQL, Diff / Patch, Protobuf, and GraphQL remain separate. Each language has a format switch; aliases share its switch. These are bounded, read-only previews, without code execution, full syntax validation, build inspection, or notebook-cell rendering.

## Profile catalog

The table lists recognized suffixes and filename rules. Profiles with neither a suffix nor a filename rule, such as MATLAB or Coq, are selected through content disambiguation or explicit Markdown hints. A suffix can have several language candidates; see the content-disambiguation rules below. Recognition does not establish Finder provider selection. `Dockerfile.*` is a prefix rule; other listed names are matched as basenames.

| Profile | Recognized suffixes | Filename rules |
| --- | --- | --- |
| Swift | `.swift`, `.swiftinterface` | — |
| C | `.c`, `.h` | — |
| C++ | `.cc`, `.cpp`, `.cxx`, `.hh`, `.hpp`, `.hxx`, `.cu`, `.cuh`, `.ipp`, `.tpp`, `.inl`, `.ixx`, `.cppm`, `.mpp`, `.tcc` | — |
| Objective-C | `.m`, `.mm`, `.pch` | — |
| Java | `.java`, `.jsp` | — |
| Kotlin | `.kt`, `.kts` | — |
| JavaScript | `.js`, `.mjs`, `.cjs`, `.jsx` | — |
| TypeScript | `.ts`, `.mts`, `.cts`, `.tsx` | — |
| Python | `.py`, `.pyw`, `.pyi` | `SConstruct`, `SConscript` |
| Go | `.go` | — |
| Rust | `.rs` | — |
| Shell | `.sh`, `.bash`, `.zsh`, `.ksh`, `.csh`, `.bashrc`, `.zshrc`, `.zprofile` | `.bashrc`, `.zshrc`, `.zprofile` |
| HTML | `.html`, `.htm` | — |
| CSS | `.css`, `.pcss` | — |
| C# | `.cs`, `.csx` | — |
| Ruby | `.rb`, `.rake`, `.gemspec` | `Gemfile`, `Rakefile`, `Podfile`, `Fastfile`, `Brewfile`, `Vagrantfile`, `Appfile`, `Matchfile`, `Gymfile`, `Scanfile`, `Snapfile`, `Deliverfile`, `Dangerfile`, `Guardfile`, `Capfile`, `Berksfile`, `Thorfile`, `Puppetfile`, `Steepfile` |
| PHP | `.php`, `.phtml` | — |
| Scala | `.scala`, `.sc`, `.sbt` | — |
| Groovy / Gradle | `.groovy`, `.gradle` | `Jenkinsfile` |
| Dart | `.dart` | — |
| Lua | `.lua` | — |
| Perl | `.pl`, `.pm`, `.t`, `.pod` | — |
| R | `.r` | — |
| Elixir | `.ex`, `.exs`, `.heex`, `.leex` | — |
| Erlang | `.erl`, `.hrl`, `.escript` | — |
| Haskell | `.hs`, `.lhs` | — |
| F# | `.fs`, `.fsi`, `.fsx` | — |
| OCaml | `.ml`, `.mli`, `.mll`, `.mly` | — |
| Clojure | `.clj`, `.cljs`, `.cljc`, `.edn` | — |
| Julia | `.jl` | — |
| Zig | `.zig`, `.zon` | — |
| Nim | `.nim`, `.nims` | — |
| Crystal | `.cr` | — |
| Solidity | `.sol` | — |
| PowerShell | `.ps1`, `.psm1`, `.psd1` | — |
| Windows Batch | `.bat`, `.cmd` | — |
| Visual Basic | `.vb`, `.vbs`, `.bas`, `.frm` | — |
| Assembly | `.asm`, `.s`, `.inc`, `.nasm` | — |
| Fortran | `.f`, `.for`, `.f77`, `.f90`, `.f95`, `.f03`, `.f08` | — |
| Pascal | `.pas`, `.pp`, `.dpr`, `.lpr` | — |
| SCSS | `.scss` | — |
| Sass | `.sass` | — |
| Less | `.less` | — |
| Stylus | `.styl` | — |
| Vue | `.vue` | — |
| Svelte | `.svelte` | — |
| Astro | `.astro` | — |
| EJS | `.ejs` | — |
| Handlebars | `.hbs`, `.handlebars`, `.mustache` | — |
| Pug | `.pug`, `.jade` | — |
| Liquid | `.liquid` | — |
| Twig | `.twig` | — |
| ERB | `.erb` | — |
| Makefile | `.mk`, `.makefile` | `Makefile`, `makefile`, `GNUmakefile` |
| CMake | `.cmake` | `CMakeLists.txt` |
| Dockerfile | `.dockerfile` | `Dockerfile`, `Dockerfile.*`, `Containerfile` |
| Xcode Configuration | `.xcconfig` | — |
| Clang Module Map | `.modulemap` | — |
| Metal | `.metal` | — |
| Cython | `.pyx`, `.pxd`, `.pxi` | — |
| Thrift | `.thrift` | — |
| FlatBuffers | `.fbs` | — |
| WebAssembly Text | `.wat`, `.wast` | — |
| GLSL | `.glsl`, `.vert`, `.frag`, `.geom`, `.tesc`, `.tese`, `.comp`, `.rgen`, `.rchit`, `.rahit`, `.rmiss`, `.rint`, `.rcall`, `.gsh`, `.fsh`, `.glslv`, `.glslf`, `.mesh`, `.task` | — |
| HLSL | `.hlsl`, `.hlsli`, `.cginc`, `.fx`, `.fxh` | — |
| TeX | `.tex`, `.sty`, `.cls`, `.bib`, `.ltx` | — |
| Fish | `.fish` | — |
| Lisp / Scheme / Racket / Emacs Lisp | `.lisp`, `.lsp`, `.scm`, `.rkt`, `.el` | — |
| Prolog | `.pro`, `.prolog` | — |
| Tcl | `.tcl`, `.tk`, `.xdc`, `.sdc`, `.qsf`, `.ucf` | — |
| Awk | `.awk` | — |
| Vim Script | `.vim` | — |
| AppleScript | `.applescript` | — |
| AutoHotkey | `.ahk` | — |
| GDScript | `.gd` | — |
| Ren’Py | `.rpy` | — |
| Ada | `.adb`, `.ads`, `.ada` | — |
| COBOL | `.cob`, `.cbl`, `.cpy` | — |
| D | `.d`, `.di` | — |
| Vala | `.vala`, `.vapi` | — |
| Haxe | `.hx` | — |
| Elm | `.elm` | — |
| PureScript | `.purs` | — |
| Reason | `.re`, `.rei` | — |
| ReScript | `.res`, `.resi` | — |
| Ballerina | `.bal` | — |
| V | `.vsh` | — |
| Odin | `.odin` | — |
| Wolfram Language | `.wl`, `.wls`, `.nb` | — |
| SAS | `.sas` | — |
| Stata | `.do`, `.ado` | — |
| SPSS Syntax | `.sps` | — |
| Verilog / SystemVerilog | `.v`, `.sv`, `.svh`, `.vh` | — |
| VHDL | `.vhd`, `.vhdl` | — |
| Move | `.move` | — |
| Cairo | `.cairo` | — |
| Vyper | `.vy` | — |
| Jinja / Nunjucks | `.j2`, `.jinja`, `.jinja2`, `.njk` | — |
| Haml | `.haml` | — |
| Slim | `.slim` | — |
| Razor | `.cshtml`, `.razor` | — |
| Marko | `.marko` | — |
| JSON5 / JSONC | `.json5`, `.jsonc` | — |
| Jsonnet | `.jsonnet`, `.libsonnet` | — |
| Prisma | `.prisma` | — |
| CUE | `.cue` | — |
| Rego | `.rego` | — |
| Xcode Project | `.pbxproj` | — |
| .NET Solution | `.sln` | — |
| Nix | `.nix` | — |
| Terraform / HCL | `.tf`, `.tfvars`, `.hcl` | — |
| Bazel / Starlark | `.bzl`, `.bazel` | `BUCK`, `BUILD`, `BUILD.bazel`, `WORKSPACE`, `WORKSPACE.bazel`, `MODULE.bazel` |
| Meson | — | `meson.build`, `meson_options.txt` |
| Just | `.just` | `Justfile`, `justfile`, `.justfile` |
| Ignore Rules | `.gitignore`, `.dockerignore` | `.gitignore`, `.dockerignore`, `.npmignore`, `.eslintignore`, `.prettierignore` |
| R Markdown / Quarto / Julia Markdown | `.rmd`, `.qmd`, `.jmd` | — |
| Gleam | `.gleam` | — |
| Typst | `.typ` | — |
| WGSL | `.wgsl` | — |
| QML | `.qml` | — |
| ActionScript | `.as` | — |
| CoffeeScript | `.coffee` | — |
| Standard ML | `.sml` | — |
| Raku | `.raku`, `.rakumod`, `.rakutest` | — |
| Nushell | `.nu` | — |
| Luau | `.luau` | — |
| LLVM IR | `.ll` | — |
| Yacc / Bison | `.y`, `.yacc` | — |
| Lex / Flex | `.l`, `.lex` | — |
| ANTLR | `.g4` | — |
| Forth | `.fth`, `.forth`, `.4th` | — |
| APL | `.apl` | — |
| BQN | `.bqn` | — |
| J | `.ijs` | — |
| K | `.k` | — |
| Lean | `.lean` | — |
| Agda | `.agda`, `.lagda` | — |
| Idris | `.idr`, `.lidr` | — |
| Pkl | `.pkl` | — |
| Dhall | `.dhall` | — |
| Bicep | `.bicep`, `.bicepparam` | — |
| Cap’n Proto | `.capnp` | — |
| Avro IDL | `.avdl` | — |
| Smithy | `.smithy` | — |
| Yul | `.yul` | — |
| Huff | `.huff` | — |
| Motoko | `.mo` | — |
| Tact | `.tact` | — |
| FunC | `.fc`, `.func` | — |
| Clarity | `.clar` | — |
| TEAL | `.teal` | — |
| LIGO | `.ligo`, `.mligo`, `.jsligo` | — |
| Scilla | `.scilla` | — |
| Pact | `.pact` | — |
| Sway | `.sw` | — |
| Unity ShaderLab | `.shader` | — |
| SPIR-V Assembly | `.spvasm` | — |
| Device Tree | `.dts`, `.dtsi` | — |
| Linker Script | `.ld`, `.lds` | — |
| MDX | `.mdx` | — |
| AsciiDoc | `.adoc`, `.asciidoc` | — |
| reStructuredText | `.rst` | — |
| Org | `.org` | — |
| Texinfo | `.texi`, `.texinfo` | — |
| Mako | `.mako` | — |
| EEx | `.eex` | — |
| Smarty | `.tpl` | — |
| Latte | `.latte` | — |
| Volt | `.volt` | — |
| CakePHP Template | `.ctp` | — |
| Go Template | `.gotmpl`, `.tmpl` | — |
| HJSON | `.hjson` | — |
| Configuration Source | `.conf`, `.cfg`, `.cnf`, `.config` | `.yarnrc`, `.bazelrc`, `.mailmap` |
| Windows Registry | `.reg` | — |
| QMake | `.pri` | — |
| Tool Versions | — | `.nvmrc`, `.tool-versions`, `.ruby-version`, `.node-version`, `.python-version` |
| Git Attributes | — | `.gitattributes` |
| Go Module | — | `go.mod` |
| Go Checksums | — | `go.sum` |
| Bundler Lockfile | — | `Gemfile.lock` |
| Earthfile | — | `Earthfile` |
| Tiltfile | — | `Tiltfile` |
| Snakemake | — | `Snakefile` |
| MATLAB / Octave | — | — |
| Mercury | — | — |
| Coq | — | — |
| Puppet | — | — |
| Apex | — | — |
| DTrace | — | — |
| SuperCollider | — | — |
| OpenCL C | `.cl` | — |
| Arduino | `.ino` | — |
| Processing | `.pde` | — |
| Qt Style Sheet | `.qss` | — |
| Classic ASP | `.asp` | — |
| ASP.NET | `.aspx` | — |
| ColdFusion | `.cfm`, `.cfml` | — |
| MXML | `.mxml` | — |
| Blade | `.blade.php` | — |
| Nginx | — | `nginx.conf` |
| HAProxy | — | `haproxy.cfg`, `haproxy.conf` |
| Caddyfile | — | `Caddyfile` |
| Procfile | — | `Procfile` |
| Yarn Lockfile | — | `yarn.lock`, `.yarn.lock` |
| Apache Configuration | — | `.htaccess` |

## Shared configuration and document formats

- JSON also handles `.ipynb`, `.xctestplan`, `.storekit`, JSON-derived configuration files, and matching lockfiles such as `Package.resolved`. Notebook files show JSON source and the existing bounded structure modes, without a cell reader.
- XML handles `.storyboard`, `.xib`, `.xcscheme`, `.csproj`, `.vbproj`, `.props`, `.targets`, `.ps1xml`, and related XML-derived formats. Interface Builder files are shown as source, without instantiating views. `.svg` is XML source when Peeka is selected, rather than an image preview. `.mobileconfig` is source only, without installing profiles or validating signatures.
- Common dependency lockfiles reuse matching previews: for example `Cargo.lock` uses TOML, `composer.lock` and `flake.lock` use JSON, and `Gemfile.lock` and `yarn.lock` retain highlighted source. This is not dependency resolution or a general lockfile inspector.
- `.conf` / `.cfg` / `.cnf` / `.config` can select XML, JSON, TOML, INI, or generic configuration highlighting from bounded content. systemd `.service` / `.timer` / `.socket` / `.mount` / `.target`, `.desktop`, `.gitconfig`, and `.buckconfig` reuse INI. `.sls` / `.raml` reuse YAML. HAR / TopoJSON show JSON source, without network replay or maps.
- JSON5 / JSONC / Jsonnet / HJSON / Prisma / CUE / Rego retain source without strict JSON validation or execution. `.rmd` / `.qmd` / `.jmd`, RST, Org, and other document profiles are source highlighting rather than rendered documents. Template and embedded-language highlighting is approximate and does not compile templates or load external resources.

## Finder routing and conflicts

Version 0.1.7 adds dotfile, extensionless build-file, and common lockfile routing. Exact `public.data` files can reach Peeka's generic fallback; recognized files use the matching format, while unrecognized generic files show basic file information. SQLite still requires its fixed magic bytes. This does not claim arbitrary unknown types or the generic text/source parent types, and a disabled matching format is not bypassed by the fallback.

Filename rules remain specific: `go.mod`, `go.sum`, `Package.resolved`, `Dockerfile.*`, `meson.build`, and `.env.local` require their documented name and matching registered type. Their suffix routes do not turn arbitrary `.mod` / `.sum` / `.resolved` / `.build` / `.local` files into the corresponding recognized format. `.env` can use the data fallback; `.env.local` has a dedicated route; other `.env.<suffix>` names still depend on that suffix's type. All recognized dotenv variants show key names only.

The release registers code-first routes for conflicting types associated with `.exs`, `.edn`, `.cue`, `.dts`, `.as`, `.mpp`, `.sdc`, `.ts`, `.mts`, `.mod`, `.rss`, and `.mobileconfig`. Real media or binary files with these types can therefore reach source previews or recoverable binary-input errors. `.svg` is explicitly handled as XML source; `.r` may carry the system Rez type and still be shown as R. Peeka does not provide video playback. macOS still chooses the actual provider; type registration alone does not prove Finder acceptance for a user's file.

## Content disambiguation and non-text limits

Bounded content checks can select another supported language for these overlapping suffixes. Without clear evidence, the default remains; conflicting evidence also keeps the default.

| Suffix | Default | Other recognized candidates |
| --- | --- | --- |
| `.m` | Objective-C | MATLAB / Octave, Mercury |
| `.v` | Verilog | Coq, V |
| `.pp` | Pascal | Puppet |
| `.pro` | Prolog | QMake |
| `.inc` | Assembly | PHP, Pascal |
| `.cls` | TeX | Visual Basic / VBA, Apex |
| `.d` | D | DTrace |
| `.fs` | F# | GLSL; `.fsi` stays F# |
| `.sc` | Scala | SuperCollider |
| `.vsh` | V | GLSL |
| `.do` | Stata | ModelSim Tcl |
| `.h` | C | C++, Objective-C |
| `.tpl` / `.tmpl` | Smarty / Go Template | Other supported template profiles with explicit features |

Probes inspect at most 64 KiB and are not complete parsers. `.pl` stays Perl. Uppercase `.C` selects C++, while lowercase `.c` and Markdown hint `C` select C; other suffix matching is case-insensitive. Markdown language hints can explicitly choose a profile, including `v` for V and `verilog` for Verilog.

Text previews remain local and bounded to **1 MiB**, with truncation and invalid/binary-input rejection. Wolfram `.nb` means readable source, not a binary notebook. AppleScript supports `.applescript`, not compiled `.scpt` / `.scptd`; SPSS supports `.sps`, not binary datasets. `.docc` directory previews and MATLAB `.mlx` are outside this text baseline. Pro does not remove these budgets or routing limits.
