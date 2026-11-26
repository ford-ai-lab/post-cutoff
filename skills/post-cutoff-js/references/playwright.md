# playwright (npm): changes after 2025-06-01

- Latest stable on the registry: **1.65.1** (2026-11-13). Built 2026-11-25.
- 26 stable releases after the cut-off: 1.53.0 (2025-06-10) to 1.65.1 (2026-11-13).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.65 (2026-11-05) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-165)
- TypeScript class fields now follow `useDefineForClassFields` from your `tsconfig.json`, the same as `tsc`. It is enabled for `ES2022` and later targets, and when `target` is not specified. […]
- Actions such as [`method: Locator.click`], [`method: Locator.check`], [`method: Locator.tap`], [`method: Locator.fill`], [`method: Locator.clear`] and [`method: Locator.selectOption`] now wait for the element to be not inert. […]
- A sharded run now fails with "No tests found" when no tests match across all shards. Pass `--pass-with-no-tests` to allow this. An empty shard still passes when other shards have tests.
- Cookie matching now follows RFC 6265. With a URL, [`method: BrowserContext.cookies`] and [`method: APIRequestContext.cookies`] no longer return host-only cookies for subdomains or `Path=/api` cookies for `/apiv2`, and a […]
- Proxy credentials are no longer sent to websites. The credentials in the [`option: BrowserType.launch.proxy`] option now answer only proxy challenges. […]
- Text that the browser does not render, such as text that is not assigned to a slot or text directly inside a closed `<details>`, is no longer part of accessible names and aria snapshots. […]
- String and `URLSearchParams` values of the `params` option in [APIRequestContext] requests are now appended to the query that the URL already has, instead of replacing it.
- [APIRequestContext] now matches `application/json` content types case-insensitively and with parameters, such as `application/json;charset=UTF-8`, when serializing string `data`. […]
- `.css`, `.less` and `.scss` imports in test files now load as empty modules instead of being removed, so the imported file must exist.
- The blob reporter again deletes the content of its output directory before it writes the report. Playwright 1.64 kept reports with other names.
- Test locations of imported calls such as `test(` in CommonJS output now point to the start of the callee, for example `a.spec.ts:3:7` instead of `a.spec.ts:3:11`. This is the same as in ESM.
- ⚠️ Playwright no longer tests on Node.js 20. Use Node.js 22, 24 or 26, as listed in the system requirements.
### 1.64 (2026-10-07) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-164)
- `screen` property is now forwarded from the device descriptors. If you use `...devices['Desktop Chrome']` and alike, `window.screen` and media queries now see the emulated screen size. […]
- JSX in your test files now follows your `tsconfig.json`. Playwright compiles JSX in test files according to the `jsx`, `jsxFactory`, `jsxFragmentFactory` and `jsxImportSource` tsconfig options, and defaults to the automatic […]
- `--update-snapshots=missing` now passes the test run. Tests that only create missing snapshots now pass in the `'missing'` mode of [`property: TestConfig.updateSnapshots`], so that CI can generate new snapshots and verify the […]
- Elements inside hidden iframes are considered hidden. Elements inside an iframe that is not visible, for example with `visibility: hidden`, are now considered hidden by actions, [`method: Locator.isVisible`] and [`method […]
### 1.63 (2026-09-04) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-163)
- ⚠️ The experimental `@playwright/experimental-ct-react`, `@playwright/experimental-ct-react17` and `@playwright/experimental-ct-vue` packages will no longer be updated. […]
- ⚠️ Ubuntu 20.04 is not supported anymore.
### 1.62 (2026-07-24) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-162)
- ⚠️ Debian 11 is not supported anymore.
### 1.60 (2026-05-11) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-160)
- Removed long-deprecated APIs: `Locator.ariaRef()` — use the standard [`method: Locator.ariaSnapshot`] pipeline.
### 1.59 (2026-04-01) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-159)
- Removed macOS 14 support for WebKit. We recommend upgrading your macOS version, or keeping an older Playwright version.
- Removed `@playwright/experimental-ct-svelte` package.
- `junit` test reporter now differentiates between types of errors, so some of the previous `<failure>`s are now reported as `<error>`s.
### 1.58 (2026-01-23) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-158)
- Removed `_react` and `_vue` selectors. See locators guide for alternatives.
- (6 more in this category not shown; see the changelog.)

## Removed or renamed
### 1.54 (2025-07-10) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-154)
- Option `-gv` has been removed from the `npx playwright test` command. Use `--grep-invert` instead.

## Deprecated
### 1.64 (2026-10-07) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-164)
- New [`option: Screencast.showActions.style`] option takes CSS declarations for the `point` marker, the target `highlight` and the action `title`. It replaces the `fontSize` option, which is now deprecated.
### 1.60 (2026-05-11) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-160)
- [`method: ConsoleMessage.location`] now exposes `line` / `column` properties (`lineNumber` / `columnNumber` are deprecated).

## New APIs and features
### 1.65 (2026-11-05) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-165)
- New options [`option: CDPSession.send.timeout`] and [`option: CDPSession.send.signal`] in [`method: CDPSession.send`].
- New [`method: TestRun.mode`] returns the execution mode of a suite during [`method: Reporter.preprocess`].
### 1.64 (2026-10-07) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-164)
- New `fps` option in [`property: TestOptions.video`], [`option: Browser.newContext.recordVideo`] and [`method: Screencast.start`]. Firefox and WebKit currently capture up to 25 frames per second.
- New [`method: Page.getByRef`] locates an element by its aria ref, such as `e2`, reported by [`method: Page.ariaSnapshot`] in the `'ai'` mode.
- New option [`option: Page.content.includeShadow`] in [`method: Page.content`] and [`method: Frame.content`] serializes open shadow roots as declarative shadow DOM.
- New option [`option: Credentials.create.signCount`] sets the initial signature counter of a virtual credential. [`method: Credentials.create`] and [`method: Credentials.get`] return the current `signCount`, and it is saved and […]
- New [`property: FullConfig.filteredProjects`] lists the projects that were selected to run after applying the `--project` filter. It is available in global setup and reporters.
- New [`method: APIRequestContext.addCookies`], [`method: APIRequestContext.cookies`] and [`method: APIRequestContext.clearCookies`] manage cookies of a request context, mirroring the [BrowserContext] methods
### 1.63 (2026-09-04) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-163)
- Browser and Context
- [`option: Browser.newContext.httpCredentials`] now also accepts an array of credentials. The first entry matching the request origin is used, and entries without an origin match any request.
- New option [`option: BrowserContext.storageState.opfs`] includes the origin private file system in the storage state, so it can be persisted and restored into later contexts.
- New events [`event: Page.dialogClosed`] and [`event: BrowserContext.dialogClosed`] are emitted when a JavaScript dialog is accepted, dismissed or closed by the user.
- New [`method: Locator.ariaSnapshotJSON`] and [`method: Page.ariaSnapshotJSON`] return the aria snapshot as a JSON value instead of YAML markup, with `mode`, `depth` and `boxes` options.
- [`method: APIRequestContext.get`] and other request methods accept a type argument that types the response `json()`
- Command line
- `npx playwright install --no-remove` keeps the browsers of other Playwright installations instead of removing them.
### 1.62 (2026-07-24) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-js.md#version-162)
- Browser and Context
- New option [`option: BrowserContext.storageState.credentials`] includes the context's virtual WebAuthn [Credentials] (passkeys) in the storage state, so they can be persisted and re-seeded into later contexts.
- (60 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 13 releases; 13 had extractable items.
- 13 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/release-notes-js.md; registry (npm) for dates.
