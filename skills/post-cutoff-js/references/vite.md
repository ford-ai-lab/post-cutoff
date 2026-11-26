# vite (npm): changes after 2025-06-01

- Latest stable on the registry: **8.3.8** (2026-11-11). Built 2026-11-25.
- 87 stable releases after the cut-off: 5.4.20 (2025-09-08) to 8.3.8 (2026-11-11).
- New major versions since the cut-off: 7.0.0 (2025-06-24), 8.0.0 (2026-03-12).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 8.0.0 (2026-03-12) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#800-2026-03-12)
- remove `import.meta.hot.accept` resolution fallback
- update default browser target
- the epic `rolldown-vite` merge
### 7.0.0 (2025-06-24) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24)
- ssr: don't access `Object` variable in ssr transformed code
- remove `experimental.skipSsrTransform` option
- remove `HotBroadcaster`
- css: always use sass compiler API
- bump `build.target` and name it `baseline-widely-available`
- css: remove sass legacy API support
- remove deprecated `HotBroadcaster` related types
- remove deprecated no-op type only properties
- remove node 18 support
- remove deprecated hook-level `enforce`/`transform` from `transformIndexHtml` hook
- remove deprecated splitVendorChunkPlugin

## Deprecated
### 7.1.0 (2025-08-07) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#710-2025-08-07)
- add `removeServerPluginContainer` future deprecation
- add `removeServerReloadModule` future deprecation
- add `server.warmupRequest` to future deprecation
- add `ssrFixStacktrace` / `ssrRewriteStacktrace` to `removeSsrLoadModule` future deprecation
- implement `removePluginHookSsrArgument` future deprecation
- implement `removeServerHot` future deprecation

## Minimum versions and platform support
### 7.0.0 (2025-06-24) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24)
- bump required node version to 20.19+, 22.12+ and remove cjs build

## New APIs and features
### 8.3.0 (2026-09-10) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#830-2026-09-10)
- build: avoid settling seen preload dependencies for performance
- devtools: enable dev server integration
- accept Rolldown watch options in `server.watch`
- add closeServer and closePreviewServer hooks
- add top-level `tsconfig` option
- add warning for unsupported hooks in plugin returned from `applyToEnvironment` hook
- cli: support naming the CPU profile via --profile [name]
- config: warn on named imports from JSON modules
### 8.2.0 (2026-07-30) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#820-2026-07-30)
- add `input` to `server.fs.allow`
- bundled-dev: reload once after rebuild instead of via the fallback page
- bundled-dev: support worker file update accepted by HMR
- config: include column in config incompatibility location
- dev: resolve interface name for explicit host in network URLs
- add `input` option
- config: warn features incompatible with native loader in bundle loader
- css: export PostCSS config type for type-safe configs
### 8.1.0 (2026-06-23) [source](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#810-2026-06-23)
- extend `server.fs.deny` list with common files
- update rolldown to 1.1.2
- (111 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 64 releases; 26 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 8.3.8, 8.3.7, 8.3.6, 8.3.5, 8.3.3, 8.3.2, 8.3.1, 8.2.1, 8.1.5, 8.1.3, 8.1.2, 8.0.16 and 26 more.
- 24 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/vitejs/vite/main/packages/vite/CHANGELOG.md; registry (npm) for dates.
