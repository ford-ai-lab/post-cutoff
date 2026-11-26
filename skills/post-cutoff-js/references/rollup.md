# rollup (npm): changes after 2025-06-01

- Latest stable on the registry: **4.68.8** (2026-11-21). Built 2026-11-25.
- 95 stable releases after the cut-off: 2.80.0 (2026-02-22) to 4.68.8 (2026-11-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 4.44.0 (2025-06-19) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4440)
- Remove limit on `maxParallelFileOps` as this could break watch mode with the commonjs plugin

## Deprecated
### 4.57.0 (2026-01-27) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4570)
- Deprecate returning import attributes from `load` or `transform` hooks as that will no longer be supported with rollup 5

## New APIs and features
### 4.68.0 (2026-11-06) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4680)
- Use the directory name instead of "index" for dynamic chunks of `index.js` files
- Support tree-shaking of namespace members through default exports
- Use cached sourcemaps if available when reading cached files
### 4.66.0 (2026-10-28) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4660)
- Support `null` sources in plugin-generated sourcemaps
- Support plugin-generated "index" sourcemaps
### 4.65.0 (2026-10-22) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4650)
- Support synthetic named exports in namespaces when preserving modules
### 4.64.0 (2026-10-02) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4640)
- Improve try-catch deoptimization to cover calling methods on objects
### 4.63.0 (2026-08-25) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4630)
- Allow to analyze function return values in many more cases
### 4.62.0 (2026-06-13) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4620)
- Ensure that shared dependencies between manual chunks and entry points receive a serparate chunk
### 4.61.0 (2026-06-01) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4610)
- Sort entry modules to make chunk hashes deterministic
### 4.60.0 (2026-03-22) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4600)
- Support source phase imports as long as they are external
### 4.59.0 (2026-02-22) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4590)
- Throw when the generated bundle contains paths that would leave the output directory
### 4.58.0 (2026-02-20) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4580)
- Also support `NO_SIDE_EFFECTS` annotation before variable declarations declaring function expressions
### 4.57.0 (2026-01-27) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4570)
- Add import attributes to all plugin hooks that did not provide them yet
### 4.56.0 (2026-01-22) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4560)
- Track object property inclusions of dynamic namespace members
### 4.54.0 (2025-12-20) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4540)
- Enable tree-shaking for `Symbol.hasInstance`, `Symbol.dispose` and `Symbol.asyncDispose` properties if unused
### 4.53.0 (2025-11-07) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4530)
- Improve rendering performance by caching generated variable names
### 4.52.0 (2025-09-19) [source](https://github.com/rollup/rollup/blob/master/CHANGELOG.md#4520)
- Add option `output.onlyExplicitManualChunks` to turn off merging additional dependencies into manual chunks
- (12 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 93 releases; 26 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 4.68.8, 4.68.7, 4.68.6, 4.68.5, 4.68.4, 4.68.3, 4.68.2, 4.68.1, 4.67.5, 4.67.4, 4.67.3, 4.65.1 and 55 more.
- 2 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/rollup/rollup/master/CHANGELOG.md; registry (npm) for dates.
