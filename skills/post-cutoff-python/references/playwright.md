# playwright (pypi): changes after 2025-06-01

- Latest stable on the registry: **1.65.2** (2026-11-14). Built 2026-11-25.
- 16 stable releases after the cut-off: 1.53.0 (2025-06-25) to 1.65.2 (2026-11-14).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.65 (2026-11-09) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-165)
- Actions such as [`method: Locator.click`], [`method: Locator.check`], [`method: Locator.tap`], [`method: Locator.fill`], [`method: Locator.clear`] and [`method: Locator.selectOption`] now wait for the element to be not inert. […]
- Cookie matching now follows RFC 6265. With a URL, [`method: BrowserContext.cookies`] and [`method: APIRequestContext.cookies`] no longer return host-only cookies for subdomains or `Path=/api` cookies for `/apiv2`, and a […]
- Proxy credentials are no longer sent to websites. The credentials in the [`option: BrowserType.launch.proxy`] option now answer only proxy challenges. […]
- Text that the browser does not render, such as text that is not assigned to a slot or text directly inside a closed `<details>`, is no longer part of accessible names and aria snapshots. […]
- String values of the `params` option in [APIRequestContext] requests are now appended to the query that the URL already has, instead of replacing it.
### 1.64 (2026-10-13) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-164)
- Elements inside hidden iframes are considered hidden. Elements inside an iframe that is not visible, for example with `visibility: hidden`, are now considered hidden by actions, [`method: Locator.isVisible`] and [`method […]
### 1.63 (2026-09-15) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-163)
- ⚠️ Ubuntu 20.04 is not supported anymore.
### 1.62 (2026-07-31) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-162)
- ⚠️ Debian 11 is not supported anymore.
### 1.60 (2026-05-18) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-160)
- Removed long-deprecated `handle` option on `BrowserContext.expose_binding` and `Page.expose_binding`.
### 1.59 (2026-04-29) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-159)
- Removed macOS 14 support for WebKit. We recommend upgrading your macOS version, or keeping an older Playwright version.
### 1.58 (2026-01-30) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-158)
- Removed `_react` and `_vue` selectors. See locators guide for alternatives.
- Removed `:light` selector engine suffix. Use standard CSS selectors instead.
- Option `devtools` from [`method: BrowserType.launch`] has been removed. Use `args=['--auto-open-devtools-for-tabs']` instead.
- Removed macOS 13 support for WebKit. We recommend to upgrade your macOS version, or keep using an older Playwright version.
### 1.57 (2025-12-09) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-157)
- After 3 years of being deprecated, we removed `page.accessibility` from our API. Please use other libraries such as Axe if you need to test page accessibility. See our Node.js guide for integration with Axe.
### 1.56 (2025-11-11) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-156)
- Event [`event: BrowserContext.backgroundPage`] has been deprecated and will not be emitted. Method [`method: BrowserContext.backgroundPages`] will return an empty list
### 1.55 (2025-08-28) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-155)
- ⚠️ Dropped support for Chromium extension manifest v2.

## Deprecated
### 1.64 (2026-10-13) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-164)
- New [`option: Screencast.showActions.style`] option takes CSS declarations for the `point` marker, the target `highlight` and the action `title`. It replaces the `font_size` option, which is now deprecated.
### 1.60 (2026-05-18) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-160)
- [`method: ConsoleMessage.location`] now exposes `line` / `column` properties (`line_number` / `column_number` are deprecated).

## New APIs and features
### 1.65 (2026-11-09) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-165)
- New option [`option: CDPSession.send.timeout`] in [`method: CDPSession.send`].
### 1.64 (2026-10-13) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-164)
- New [`option: Browser.newContext.recordVideoFps`] option and new [`option: Screencast.start.fps`] option in [`method: Screencast.start`]. Firefox and WebKit currently capture up to 25 frames per second.
- New [`method: Page.getByRef`] locates an element by its aria ref, such as `e2`, reported by [`method: Page.ariaSnapshot`] in the `"ai"` mode.
- New option [`option: Page.content.includeShadow`] in [`method: Page.content`] and [`method: Frame.content`] serializes open shadow roots as declarative shadow DOM.
- New option [`option: Credentials.create.signCount`] sets the initial signature counter of a virtual credential. [`method: Credentials.create`] and [`method: Credentials.get`] return the current `sign_count`, and it is saved and […]
- New [`method: APIRequestContext.addCookies`], [`method: APIRequestContext.cookies`] and [`method: APIRequestContext.clearCookies`] manage cookies of a request context, mirroring the [BrowserContext] methods
### 1.63 (2026-09-15) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-163)
- Browser and Context
- [`option: Browser.newContext.httpCredentials`] now also accepts an array of credentials. The first entry matching the request origin is used, and entries without an origin match any request.
- New option [`option: BrowserContext.storageState.opfs`] includes the origin private file system in the storage state, so it can be persisted and restored into later contexts.
- New events [`event: Page.dialogClosed`] and [`event: BrowserContext.dialogClosed`] are emitted when a JavaScript dialog is accepted, dismissed or closed by the user.
- Command line
- `playwright install --no-remove` keeps the browsers of other Playwright installations instead of removing them.
- `playwright codegen --http-credentials` records against pages behind HTTP authentication.
### 1.62 (2026-07-31) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-162)
- New `scroll` option (`"auto"` | `"none"`) on actions to opt out of Playwright's automatic scroll-into-view.
- New [`method: Locator.waitForFunction`] waits until a function — called with the matching element — returns a truthy value.
- New [`method: APIResponse.timing`] returns resource timing information for an API response.
### 1.61 (2026-06-29) [source](https://github.com/microsoft/playwright/blob/main/docs/src/release-notes-python.md#version-161)
- [`method: APIResponse.securityDetails`] and [`method: APIResponse.serverAddr`] mirror the browser-side [`method: Response.securityDetails`] and [`method: Response.serverAddr`].
- New option `artifacts_dir` in [`method: BrowserType.connectOverCDP`] controls where artifacts such as traces and downloads are stored when attached to an existing browser.
- (36 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 13 releases; 13 had extractable items.
- 3 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/release-notes-python.md; registry (pypi) for dates.
