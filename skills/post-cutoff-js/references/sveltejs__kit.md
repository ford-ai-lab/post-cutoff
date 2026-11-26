# @sveltejs/kit (npm): changes after 2025-06-01

- Latest stable on the registry: **3.4.0** (2026-11-18). Built 2026-11-25.
- 137 stable releases after the cut-off: 2.21.2 (2025-06-03) to 3.4.0 (2026-11-18).
- New major versions since the cut-off: 3.0.0 (2026-10-01).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 3.0.0 (2026-10-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#300)
- breaking: move remote function types to `$app/server`
- breaking: remove `experimental.handleRenderingErrors` flag
- breaking: make `getRequest` and `setResponse` synchronous
- breaking: TypeScript 6 is now the minimum required version
- breaking: refresh all load functions/queries when clicking a link to the current URL
- breaking: upgrade to `cookie` v2. Cookie names must now contain only ASCII characters
- major: error when a client-requested single-flight mutation isn't respected by the server, allow the server to explicitly ignore refreshes
- breaking: remove the `preloadStrategy` option. `modulepreload` will always be used
- breaking: default the cookie `path` option to `'/'`
- breaking: remove `@sveltejs/kit/node/polyfills`
- breaking: add `config.kit.output.linkHeaderPreload` to preload using the `Link` header
- breaking: require `@sveltejs/vite-plugin-svelte` v7
### 2.61.0 (2026-05-22) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2610)
- breaking: the `.run()` method has been removed from remote queries on both the client and the server. Use `await query()` directly instead — it now works everywhere
### 2.59.0 (2026-05-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2590)
- breaking: on the server, make the promise returned from `refresh` represent adding the refresh to the map, not the time it takes to run the remote function
### 2.58.0 (2026-04-23) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2580)
- breaking: require `limit` in `requested` (as originally intended)
- breaking: `requested` now yields `{ arg, query }` entries instead of the validated argument
### 2.56.0 (2026-04-03) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2560)
- breaking: rework client-driven refreshes
- breaking: stabilize remote function caching by sorting object keys
- breaking: add `run()` method to queries, disallow awaiting queries outside render
- breaking: isolate command-triggered query refresh failures per-query
### 2.50.0 (2026-01-17) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2500)
- breaking: remove `buttonProps` from experimental remote form functions; use e.g. `<button {...myForm.fields.action.as('submit', 'register')}>Register</button>` button instead
### 2.44.0 (2025-10-05) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2440)
- breaking: update experimental `form` API
### 2.42.0 (2025-09-16) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2420)
- breaking: remote form functions get passed a parsed POJO instead of a `FormData` object now
- (60 more in this category not shown; see the changelog.)

## Deprecated
### 3.0.0 (2026-10-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#300)
- feat: add shallow routing to `goto` and deprecate `pushState` and `replaceState`
- feat: reinstate `$env/static/private`, `$env/dynamic/private`, `$env/static/public`, `$env/dynamic/public` and `$app/environment` as deprecated aliases for `$app/env/private` `$app/env/public` and `$app/env`
- chore: deprecate `Response` helpers in favor of platform-provided alternatives
- chore: deprecate `export const snapshot` in favour of the `snapshot` helper

## Minimum versions and platform support
### 3.0.0 (2026-10-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#300)
- breaking: require Node 22 or newer
- breaking: require Node 22.17

## New APIs and features
### 3.4.0 (2026-11-18) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#340)
- feat: allow adapters to disable SvelteKit's Node preview server with `vite.customPreview: true` when providing their own preview implementation
- feat: add `sveltekit.remote.call.file` attribute to remote function tracing spans
### 3.3.0 (2026-11-17) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#330)
- feat: support the Vite DevTools dock in dev
### 3.2.0 (2026-11-10) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#320)
- feat: Add clickable links to remote function invocation in dev server logs
### 3.1.0 (2026-10-14) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#310)
- feat: support `report-sha256`/`report-sha384`/`report-sha512` CSP hash-reporting keywords
- feat: emit a `sveltekit.endpoint` span for `+server` handlers when server tracing is enabled
### 3.0.0 (2026-10-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#300)
- feat: allow hyphens in param and matcher names
- feat: add `$app/manifest` module with `immutable`, `assets`, `prerendered`, and `routes` exports
- feat: ignore files with + prefix if they contain test/spec/stories
- feat: add `ErrorProps` to generated types
- feat: support sourcemaps in production
- feat: return the list of compressed files from `builder.compress`
- feat: better response logging
- feat: warn when tsconfig doesn't exclude service worker
### 2.70.0 (2026-07-17) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2700)
- feat: move `defineEnvVars` to `@sveltejs/kit/env`
### 2.69.0 (2026-07-01) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2690)
- feat: expose `submitted` property of remote forms
### 2.68.0 (2026-06-24) [source](https://github.com/sveltejs/kit/blob/main/packages/kit/CHANGELOG.md#2680)
- feat: expose `RemoteFormEnhanceInstance` and `RemoteFormEnhanceCallback` types
- feat: set value of `submit` fields when form is submitted
- (83 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 136 releases; 54 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.3.1, 3.2.1, 3.1.1, 3.0.1, 2.70.3, 2.70.2, 2.70.1, 2.69.3, 2.69.2, 2.69.1, 2.65.2, 2.65.1 and 70 more.
- 1 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/sveltejs/kit/main/packages/kit/CHANGELOG.md; registry (npm) for dates.
