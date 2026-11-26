# webpack (npm): changes after 2025-06-01

- Latest stable on the registry: **5.113.0** (2026-11-19). Built 2026-11-25.
- 41 stable releases after the cut-off: 5.100.0 (2025-07-09) to 5.113.0 (2026-11-19).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 5.113.0 (2026-11-19) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51130)
- Drop unread call arguments and fold `Object.keys` and `.length` when minifying. (by @alexander-akait in
### 5.111.0 (2026-09-14) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51110)
- Remove `experiments.outputModule`, set `output.module` to emit ESM instead. (by @alexander-akait in
- Drop an implied shorthand slot, fold a math function, tighten color conversion. (by @alexander-akait in
- Drop what is already said or only a gone engine reads, add `lowerUnsupported`. (by @alexander-akait in
### 5.110.0 (2026-08-27) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51100)
- Patch the HTML `<head>` in place on hot update instead of forcing a full reload, including when a `<script>` that never executed is removed. (by @alexander-akait in

## Deprecated
### 5.113.0 (2026-11-19) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51130)
- Make the `MultiCompiler` `done` hook async; its sync `call` is deprecated. (by @alexander-akait in
### 5.112.0 (2026-10-15) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51120)
- Export more plugins under their scope, move eleven loose exports under theirs, deprecate the old, and expose `template.DependencyTemplate`, `module.NullFactory` and `util.makeSerializable`. (by @alexander-akait in
- Rename the `Harmony*` names to `ESM*` and deprecate the old spellings. (by @hai-x in
### 5.109.0 (2026-07-23) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51090)
- Deprecate the `importMetaContext` parser option in favor of `importMeta.webpackContext`. (by @alexander-akait in

## New APIs and features
### 5.113.0 (2026-11-19) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51130)
- Treat pure CommonJS exports and `require()` of pure modules as side-effect free. (by @hai-x in
- Add `compilation.hooks.chunkHashDependencies` for chunks naming other chunks. (by @alexander-akait in
- Add a `sourceTest` condition to `use` items; match `/g` regexps reliably. (by @xiaoxiaojx in
- Add optional SVG minification and preserve XML values and HTML style boundaries. (by @alexander-akait in
- Allow `usedExports` and `mangleExports` with `cacheUnaffected`. (by @alexander-akait in
- Add an `updateManifest` HMR hook so plugins add their own hot update data. (by @alexander-akait in
- Add a `transport` hook to `webpack.hmr.LazyCompilationPlugin`, so a development server can serve the lazy compilation backend from its own server, and pass the options it settles on to a custom backend, which can bring its own […]
- Restore deep import paths Module Federation loads and expose its helpers. (by @alexander-akait in
### 5.112.0 (2026-10-15) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51120)
- Apply `plugins` set on a multi-configuration array to the `MultiCompiler`. (by @alexander-akait in
- Add `optimization.minimize.css.dropOverriddenDeclarations`, dropping a declaration a later one overrides where no target is named. (by @alexander-akait in
- Let `util.makeSerializable` take several requests, current one first. (by @alexander-akait in
- Emit the source map `scopes` field, so a debugger resolves imported ESM bindings by name. (by @alexander-akait in
- Add `library.entryExports: "all"` to expose the exports of every entry module. (by @alexander-akait in
- Recognize a required `const` binding assigned to `exports` as a re-export. (by @hai-x in
- Accept glob patterns in more path, module and file filter options. (by @hai-x in
- Bundle a run of inline `<script>` tags into one chunk the page can inline. (by @alexander-akait in
### 5.111.0 (2026-09-14) [source](https://github.com/webpack/webpack/blob/main/CHANGELOG.md#51110)
- Enable `output.module` by default with `futureDefaults` on ESM-capable targets. (by @alexander-akait in
- Add `output.copy` to copy files and directories into the output directory. (by @alexander-akait in
- (216 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 31 releases; 10 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 5.112.2, 5.112.1, 5.111.1, 5.110.3, 5.110.2, 5.110.1, 5.109.2, 5.109.1, 5.108.4, 5.108.3, 5.108.2, 5.108.1 and 9 more.
- 10 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/webpack/webpack/main/CHANGELOG.md; registry (npm) for dates.
