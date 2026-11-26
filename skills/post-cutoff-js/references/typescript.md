# typescript (npm): changes after 2025-06-01

- Latest stable on the registry: **7.0.2** (2026-07-08). Built 2026-11-25.
- 5 stable releases after the cut-off: 5.9.2 (2025-07-31) to 7.0.2 (2026-07-08).
- New major versions since the cut-off: 6.0.2 (2026-03-23), 7.0.2 (2026-07-08).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 6.0.2 (2026-03-23) [source](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript%206.0.md)
- TypeScript 6.0 arrives as a significant transition release, designed to prepare developers for TypeScript 7.0, the upcoming native port of the TypeScript compiler. […]
- In the two years since TypeScript 5.0, we've seen ongoing shifts in how developers write and ship JavaScript
- Virtually every runtime environment is now "evergreen". True legacy environments (ES5) are vanishingly rare.
- Bundlers and ESM have become the most common module targets for new projects, though CommonJS remains a major target. AMD and other in-browser userland module systems are much rarer than they were in 2012.
- Almost all packages can be consumed through some module system. UMD packages still exist, but virtually no new code is available *only* as a global variable.
- `tsconfig.json` is nearly universal as a configuration mechanism.
- Appetite for "stricter" typing continues to grow.
- TypeScript build performance is top of mind. Despite the gains of TypeScript 7, performance must always remain a key goal, and options which can't be supported in a performant way need to be more strongly justified.
- Up-Front Adjustments: We'll cover specific adjustments below, but we have to note that some deprecations and behavior changes do not necessarily have an error message that directly points to the underlying issue. […]
- Set the `"types"` array in tsconfig, typically to `"types": ["node"]`.
- Set `"rootDir": "./src"` if you were previously relying on this being inferred
- Simple Default Changes: Several compiler options now have updated default values that better reflect modern development practices.
### 5.9.2 (2025-07-31) [source](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript%205.9.md)
- lib.d.ts Changes: Types generated for the DOM may have an impact on type-checking your codebase.
- (8 more in this category not shown; see the changelog.)

## Deprecated
### 6.0.2 (2026-03-23) [source](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript%206.0.md)
- The ECMAScript 5 target was important for a long time to support legacy browsers; but its successor, ECMAScript 2015 (ES6), was released over a decade ago, and all modern browsers have supported it for many years. […]
- TypeScript's lowest target will now be ES2015, and the `target: es5` option is deprecated. If you were using `target: es5`, you'll need to migrate to a newer target or use an external compiler. […]
- `--downlevelIteration` only has effects on ES5 emit, and since `--target es5` has been deprecated, `--downlevelIteration` no longer serves a purpose.
- Subtly, using `--downlevelIteration false` with `--target es2015` did not error in TypeScript 5.9 and earlier, even though it had no effect. […]
- `--moduleResolution node` encoded a specific version of Node.js's module resolution algorithm that most-accurately reflected the behavior of Node.js 10. […]
- In TypeScript 6.0, `--moduleResolution node` (specifically, `--moduleResolution node10`) is deprecated. Users who were using `--moduleResolution node` should usually migrate to `--moduleResolution nodenext` if they plan on […]
- The following flag values are no longer supported
- `--module amd`
- (21 more in this category not shown; see the changelog.)

## New APIs and features
### 6.0.2 (2026-03-23) [source](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript%206.0.md)
- Less Context-Sensitivity on this-less Functions: When parameters don't have explicit types written out, TypeScript can usually infer them based on an expected type, or even through other arguments in the same function call.
- Subpath Imports Starting with #/: When Node.js added support for modules, it added a feature called "subpath imports". This is basically a field called `imports` which allows packages to create internal aliases for modules within […]
- Combining --moduleResolution bundler with --module commonjs: TypeScript's `--moduleResolution bundler` setting was previously only allowed to be used with `--module esnext` or `--module preserve`; […]
- The --stableTypeOrdering Flag: As part of our ongoing work on TypeScript's native port, we've introduced a new flag called `--stableTypeOrdering` intended to assist with 6.0-to-7.0 migrations.
- es2025 option for target and lib: TypeScript 6.0 adds support for the `es2025` option for both `target` and `lib`. While there are no new JavaScript language features in ES2025, this new target adds new types for built-in APIs […]
- `getOrInsert`
- `getOrInsertComputed`
- RegExp.escape: When constructing some literal string to match within a regular expression, it is important to escape special regular expression characters like `*`, `+`, `?`, `(`, `)`, etc. […]
### 5.9.2 (2025-07-31) [source](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript%205.9.md)
- Minimal and Updated tsc --init: For a while, the TypeScript compiler has supported an `--init` flag that can create a `tsconfig.json` within the current directory. […]
- Support for import defer: TypeScript 5.9 introduces support for ECMAScript's deferred module evaluation proposal using the new `import defer` syntax. […]
- Support for --module node20: TypeScript provides several `node*` options for the `--module` and `--moduleResolution` settings. Most recently, `--module nodenext` has supported the ability to `require()` ECMAScript modules from […]
- Configurable Maximum Hover Length: Occasionally, quick info tooltips can become so long that TypeScript will truncate them to make them more readable. […]
- Optimizations
- Cache Instantiations on Mappers: When TypeScript replaces type parameters with specific type arguments, it can end up instantiating many of the same intermediate types over and over again. […]
- Avoiding Closure Creation in fileOrDirectoryExistsUsingSource: In JavaScript, a function expression will typically allocate a new function object, even if the wrapper function is just passing through arguments to another function […]
- Type Argument Inference Changes: In an effort to fix "leaks" of type variables during inference, TypeScript 5.9 may introduce changes in types and possibly new errors in some codebases. […]
- (2 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 2 releases; 2 had extractable items.
- 3 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Source not reachable in this build: github_releases microsoft/TypeScript: HTTP 403 cached
- Sources: https://raw.githubusercontent.com/microsoft/TypeScript-Website/v2/packages/documentation/copy/en/release-notes/TypeScript {mm}.md, https://github.com/microsoft/TypeScript/releases; registry (npm) for dates.
