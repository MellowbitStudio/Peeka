# Development source coverage

Checked **2026-10-21** against the current development source, including uncommitted changes. This is **not the released 0.1.5 baseline**. App Store / TestFlight availability for this expansion is unconfirmed; check the installed build before promising support. No Skill or app release version is advanced by this reference.

The current source contains **116 free lexical profiles** shared by standalone source previews and explicit Markdown fence hints. These provide bounded, read-only highlighting, not syntax validation, code execution, a notebook reader, or build inspection. The app groups them into Source Code, Frontend & Templates, and Build Scripts; SQL, Diff / Patch, Protobuf and GraphQL remain separate. Aliases share the corresponding language switch.

| Profile | Standalone suffixes |
| --- | --- |
| Swift | `.swift`, `.swiftinterface` |
| C | `.c`, `.h` |
| C++ | `.cc`, `.cpp`, `.cxx`, `.hh`, `.hpp`, `.hxx`, `.cu`, `.cuh`, `.ipp`, `.tpp`, `.inl` |
| Objective-C | `.m`, `.mm`, `.pch` |
| Java | `.java`, `.jsp` |
| Kotlin | `.kt`, `.kts` |
| JavaScript | `.js`, `.mjs`, `.cjs`, `.jsx` |
| TypeScript | `.ts`, `.mts`, `.cts`, `.tsx` |
| Python | `.py`, `.pyw`, `.pyi` |
| Go | `.go` |
| Rust | `.rs` |
| Shell | `.sh`, `.bash`, `.zsh`, `.ksh`, `.csh`, `.bashrc`, `.zshrc`, `.zprofile` |
| HTML | `.html`, `.htm` |
| CSS | `.css`, `.pcss` |
| C# | `.cs`, `.csx` |
| Ruby | `.rb`, `.rake`, `.gemspec` |
| PHP | `.php`, `.phtml` |
| Scala | `.scala`, `.sc`, `.sbt` |
| Groovy / Gradle | `.groovy`, `.gradle` |
| Dart | `.dart` |
| Lua | `.lua` |
| Perl | `.pl`, `.pm`, `.t`, `.pod` |
| R | `.r` |
| Elixir | `.ex`, `.exs`, `.heex`, `.leex` |
| Erlang | `.erl`, `.hrl`, `.escript` |
| Haskell | `.hs`, `.lhs` |
| F# | `.fs`, `.fsi`, `.fsx` |
| OCaml | `.ml`, `.mli`, `.mll`, `.mly` |
| Clojure | `.clj`, `.cljs`, `.cljc`, `.edn` |
| Julia | `.jl` |
| Zig | `.zig`, `.zon` |
| Nim | `.nim`, `.nims` |
| Crystal | `.cr` |
| Solidity | `.sol` |
| PowerShell | `.ps1`, `.psm1`, `.psd1` |
| Windows Batch | `.bat`, `.cmd` |
| Visual Basic | `.vb`, `.vbs`, `.bas` |
| Assembly | `.asm`, `.s`, `.inc`, `.nasm` |
| Fortran | `.f`, `.for`, `.f77`, `.f90`, `.f95`, `.f03`, `.f08` |
| Pascal | `.pas`, `.pp`, `.dpr`, `.lpr` |
| SCSS | `.scss` |
| Sass | `.sass` |
| Less | `.less` |
| Stylus | `.styl` |
| Vue | `.vue` |
| Svelte | `.svelte` |
| Astro | `.astro` |
| EJS | `.ejs` |
| Handlebars | `.hbs`, `.handlebars`, `.mustache` |
| Pug | `.pug` |
| Liquid | `.liquid` |
| Twig | `.twig` |
| ERB | `.erb` |
| Makefile | `.mk`, `.makefile` |
| CMake | `.cmake` |
| Dockerfile | `.dockerfile` |
| Xcode Configuration | `.xcconfig` |
| Clang Module Map | `.modulemap` |
| Metal | `.metal` |
| Cython | `.pyx`, `.pxd`, `.pxi` |
| Thrift | `.thrift` |
| FlatBuffers | `.fbs` |
| WebAssembly Text | `.wat`, `.wast` |
| GLSL | `.glsl`, `.vert`, `.frag`, `.geom`, `.tesc`, `.tese`, `.comp` |
| HLSL | `.hlsl`, `.hlsli` |
| TeX | `.tex`, `.sty`, `.cls`, `.bib` |
| Fish | `.fish` |
| Lisp / Scheme / Racket / Emacs Lisp | `.lisp`, `.lsp`, `.scm`, `.rkt`, `.el` |
| Prolog | `.pro`, `.prolog` |
| Tcl | `.tcl`, `.tk` |
| Awk | `.awk` |
| Vim Script | `.vim` |
| AppleScript | `.applescript` |
| AutoHotkey | `.ahk` |
| GDScript | `.gd` |
| Ren’Py | `.rpy` |
| Ada | `.adb`, `.ads`, `.ada` |
| COBOL | `.cob`, `.cbl`, `.cpy` |
| D | `.d`, `.di` |
| Vala | `.vala`, `.vapi` |
| Haxe | `.hx` |
| Elm | `.elm` |
| PureScript | `.purs` |
| Reason | `.re`, `.rei` |
| ReScript | `.res`, `.resi` |
| Ballerina | `.bal` |
| V | `.vsh` |
| Odin | `.odin` |
| Wolfram Language | `.wl`, `.wls`, `.nb` |
| SAS | `.sas` |
| Stata | `.do`, `.ado` |
| SPSS Syntax | `.sps` |
| Verilog / SystemVerilog | `.v`, `.sv`, `.svh`, `.vh` |
| VHDL | `.vhd`, `.vhdl` |
| Move | `.move` |
| Cairo | `.cairo` |
| Vyper | `.vy` |
| Jinja / Nunjucks | `.j2`, `.jinja`, `.jinja2`, `.njk` |
| Haml | `.haml` |
| Slim | `.slim` |
| Razor | `.cshtml`, `.razor` |
| Marko | `.marko` |
| JSON5 / JSONC | `.json5`, `.jsonc` |
| Jsonnet | `.jsonnet`, `.libsonnet` |
| Prisma | `.prisma` |
| CUE | `.cue` |
| Rego | `.rego` |
| Xcode Project | `.pbxproj` |
| .NET Solution | `.sln` |
| Nix | `.nix` |
| Terraform / HCL | `.tf`, `.tfvars`, `.hcl` |
| Bazel / Starlark | `.bzl`, `.bazel` |
| Meson | Exact filenames `meson.build`, `meson_options.txt` |
| Just | `.just` |
| Ignore Rules | `.gitignore`, `.dockerignore` |
| R Markdown / Quarto / Julia Markdown | `.rmd`, `.qmd`, `.jmd` |

Exact basenames: `Makefile`, `makefile`, `GNUmakefile`, `CMakeLists.txt`, `Dockerfile`, `Dockerfile.*`, `BUILD`, `BUILD.bazel`, `WORKSPACE`, `WORKSPACE.bazel`, `MODULE.bazel`, `meson.build`, `meson_options.txt`, `Justfile`, `justfile`, `.justfile`, `.gitignore`, `.dockerignore`, `.bashrc`, `.zshrc`, `.zprofile`. Recognition does not guarantee Finder selection; generic text/data/source UTIs are not claimed to force routing.

Engineering metadata reuses existing format switches: `.xctestplan` / `.storekit` use JSON; `.xcscheme`, `.csproj`, `.vbproj`, `.props`, `.targets` and `.ps1xml` use XML. JSON5 / JSONC retain source without strict JSON validation. `.rmd` / `.qmd` / `.jmd` retain source; embedded and literate syntax highlighting is approximate. Jinja / Nunjucks share a profile; Mustache shares Handlebars.

`.pbxproj` also declares the specific system type `com.apple.xcode.projectdata`. CUE `.cue` can instead resolve to IINA’s `io.iina.cue` audio cue-sheet type; Peeka does not claim that unrelated type, so Finder routing remains limited.

Extension conflicts remain explicit: `.m` uses Objective-C, `.pl` Perl, `.v` Verilog / SystemVerilog, `.vsh` V, and `.R` / `.r` R. Markdown hint `v` selects V; use `verilog` for Verilog. MATLAB / Octave `.m`, Prolog `.pl` and V `.v` have no automatic content disambiguation. `.ts` / `.mts` can still route to system video; Peeka does not claim movie types. `.wl` / `.wls` and text `.nb` show Wolfram source only. AppleScript supports text `.applescript`, not compiled `.scpt` / `.scptd`; SPSS supports `.sps`, not binary datasets. `.docc` is a directory and `.mlx` is not plain text; neither is added.

Text remains local and bounded to 1 MiB, with truncation and invalid/binary-input rejection. Pro does not remove these budgets or routing limits. Build, production rendering, registration and Finder activation are separate evidence; consult the installed build and current published notes.
