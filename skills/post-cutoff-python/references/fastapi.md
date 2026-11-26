# fastapi (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.165.0** (2026-11-18). Built 2026-11-25.
- 150 stable releases after the cut-off: 0.115.13 (2025-06-17) to 0.165.0 (2026-11-18).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 0.162.0 (2026-10-23) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01620-2026-10-23)
- 🐛 Restore default handling for omitted boolean form fields. PR
### 0.160.0 (2026-10-22) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01600-2026-10-22)
- 🐛 Apply each parameter model's `extra` configuration to sibling fields. PR
### 0.155.0 (2026-10-20) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01550-2026-10-20)
- 🔥 Remove deprecated `extra` from request parameters. PR
### 0.151.0 (2026-10-20) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01510-2026-10-20)
- 🐛 Distinguish JSON null from omitted body values. PR
### 0.150.0 (2026-10-19) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01500-2026-10-20)
- 🐛 Treat unselected browser file inputs as missing. PR
### 0.149.0 (2026-10-19) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01490-2026-10-19)
- 🐛 Treat empty scalar values as missing in form models. PR
### 0.148.0 (2026-10-19) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01480-2026-10-19)
- 🐛 Fix default handling for request parameters and models. PR
### 0.147.0 (2026-10-19) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01470-2026-10-19)
- 🐛 Treat omitted boolean form fields as False. PR
### 0.146.0 (2026-10-18) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01460-2026-10-18)
- 🗑️ Deprecate the `root_path` parameter in `FastAPI`. PR
### 0.145.0 (2026-10-18) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01450-2026-10-18)
- 🔥 Remove deprecated `openapi_prefix` and unused `extra` from `FastAPI`. PR
### 0.143.0 (2026-10-08) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01430-2026-10-08)
- 💥 Require opt-in for automatic OpenTelemetry exporter setup. PR
### 0.137.0 (2026-06-14) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01370-2026-06-14)
- ♻️ Refactor internals to preserve `APIRouter` and `APIRoute` instances. PR
- Unblocks ✨ SO MANY THINGS ✨
- Before this, `router.include_router(other_router)` would take each path operation from `other_router` and "clone" it, or recreate it from scratch.
- Non Objectives: Dependencies for 404: previously I intended to support dependencies that would be executed even for 404, but that would conflict with the fact that a router could _not_ find a match, but the next router _did_ find […]
- Now `router.routes` is no longer a plain list of `APIRoute` objects, it can contain these intermediate objects that can contain additional routers, forming a tree.
- Any logic that depended on iterating on the `router.routes` directly would be affected, that logic cannot expect to be able to extract data from a plain list of routes, as it's no longer a plain list but a tree.
### 0.132.0 (2026-02-23) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01320-2026-02-23)
- 🔒️ Add `strict_content_type` checking for JSON requests. PR
### 0.131.0 (2026-02-22) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01310-2026-02-22)
- 🗑️ Deprecate `ORJSONResponse` and `UJSONResponse`. PR
### 0.128.0 (2025-12-27) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01280-2025-12-27)
- ➖ Drop support for `pydantic.v1`. PR
### 0.127.0 (2025-12-21) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01270-2025-12-21)
- 🔊 Add deprecation warnings when using `pydantic.v1`. PR
### 0.125.0 (2025-12-17) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01250-2025-12-17)
- This would actually not be a _breaking_ change as no code would really break. Any Python 3.8 installer would just refuse to install the latest version of FastAPI and would only install 0.124.4. […]

## Minimum versions and platform support
### 0.162.6 (2026-11-13) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01626-2026-11-13)
- 💥 Drop support for Python 3.10. PR
### 0.129.0 (2026-02-12) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01290-2026-02-12)
- ➖ Drop support for Python 3.9. PR
### 0.125.0 (2025-12-17) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01250-2025-12-17)
- 🔧 Drop support for Python 3.8. PR

## New APIs and features
### 0.165.0 (2026-11-18) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01650-2026-11-18)
- ✨ Add configurable form parsing limits. PR
### 0.164.0 (2026-11-18) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01640-2026-11-18)
- ✨ Add configurable request body size limits. PR
### 0.163.0 (2026-11-14) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01630-2026-11-14)
- ✨ Add dependency concurrency limits with `Depends(max_concurrency=...)`. PR
### 0.161.0 (2026-10-22) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01610-2026-10-22)
- ✨ Add support for combining unions of form models. PR
### 0.159.0 (2026-10-21) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01590-2026-10-21)
- ✨ Add support for optional query, header, and cookie parameter models. PR
### 0.158.0 (2026-10-21) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01580-2026-10-21)
- ✨ Add support for combining form models. PR
### 0.157.0 (2026-10-21) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01570-2026-10-21)
- ✨ Add support for combining query, header, and cookie parameter models. PR
### 0.154.0 (2026-10-20) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01540-2026-10-20)
- ✨ Add Pydantic validation options to request parameters. PR
### 0.144.0 (2026-10-18) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01440-2026-10-18)
- ✨ Add WebSocket support to security dependencies. PR
### 0.142.0 (2026-09-29) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01420-2026-09-29)
- ✨ Add native OpenTelemetry support. PR
### 0.141.0 (2026-07-29) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01410-2026-07-29)
- ✨ Add `app.frontend(check_dir="auto")`, to make local development more convenient with `fastapi dev`. PR
### 0.139.0 (2026-07-01) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01390-2026-07-01)
- ✨ Support dependencies in `app.frontend()`, e.g. for automatic cookie authentication for the frontend. PR
### 0.138.0 (2026-06-20) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01380-2026-06-20)
- ✨ Add support for `app.frontend("/", directory="dist")` and `router.frontend("/", directory="dist")`. PR
### 0.137.0 (2026-06-14) [source](https://github.com/fastapi/fastapi/blob/master/docs/en/docs/release-notes.md#01370-2026-06-14)
- Adding routes (path operations) after a router is included now works, they are reflected as they are not copied.
- Including `subrouter` in `mainrouter` can be done before adding routes (path operations) to `subrouter`, because now the entire object is stored instead of copying the routes.
- As routes are not copied, in some cases that might save some memory.
- Custom `APIRoute` subclasses (undocumented, but already works as described above)
- Custom `APIRouter` subclasses (undocumented, but already works as described above)
- (28 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 151 releases; 49 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.163.2, 0.163.1, 0.162.7, 0.162.5, 0.162.4, 0.162.3, 0.162.2, 0.162.1, 0.161.1, 0.158.1, 0.156.8, 0.156.7 and 90 more.
- Sources: https://raw.githubusercontent.com/fastapi/fastapi/master/docs/en/docs/release-notes.md; registry (pypi) for dates.
