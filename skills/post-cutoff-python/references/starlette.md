# starlette (pypi): changes after 2025-06-01

- Latest stable on the registry: **1.10.0** (2026-10-24). Built 2026-11-25.
- 28 stable releases after the cut-off: 0.47.1 (2025-06-21) to 1.10.0 (2026-10-24).
- New major versions since the cut-off: 1.0.0 (2026-03-22).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 0.50.0 (2025-11-01) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#0500-november-1-2025)
- Drop Python 3.9 support

## Deprecated
### 1.10.0 (2026-10-24) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#1100-october-24-2026)
- Deprecate `starlette.formparsers.FormMessage`, which is no longer used
### 0.51.0 (2026-01-10) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#0510-january-10-2026)
- Increase warning stacklevel on `DeprecationWarning` for wsgi module

## Minimum versions and platform support
### 1.8.0 (2026-10-13) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#180-october-13-2026)
- Require Python 3.11 or later, dropping support for Python 3.10

## New APIs and features
### 1.8.0 (2026-10-13) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#180-october-13-2026)
- Add `Request.send_early_hints()` for HTTP 103 Early Hints through the ASGI `http.response.early_hint` extension
### 1.7.0 (2026-09-23) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#170-september-23-2026)
- Add experimental `OpenTelemetryMiddleware` for HTTP server spans, with URL exclusions and custom tracer providers #3438, #3463, and
- Expose the matched route through `scope["route"]`
- Support the `QUERY` HTTP method in `HTTPEndpoint`, CORS, and OpenAPI 3.2 schema generation
- Capture HTTP response trailers in `TestClient` and expose them through `response.extensions["http.response.trailers"]`
- Support partitioned cookies in `SessionMiddleware`
- Add `partitioned` to `Response.delete_cookie()` on Python 3.14 and later
- Support IPv6 hosts in `TrustedHostMiddleware` and `TestClient`
- Support Python 3.15
### 1.6.0 (2026-08-08) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#160-august-8-2026)
- Add `max_body_size` to `Starlette` and route classes
- Expose `http.response.debug` information via response extensions
### 1.5.0 (2026-08-08) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#150-august-8-2026)
- Add `exclude_content_types` parameter to `GZipMiddleware`
### 1.4.0 (2026-08-05) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#140-august-5-2026)
- Offload large GZip compression to a worker thread, keeping the event loop responsive. `GZipMiddleware` accepts a new `thread_minimum_size` parameter (default 128 KiB) controlling the minimum body chunk size compressed in a thread
### 1.3.0 (2026-06-11) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#130-june-11-2026)
- Add `httpx2` to the `full` extra
- Annotate the `URLPath` `protocol` parameter with `Literal`
### 1.2.0 (2026-05-28) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#120-may-28-2026)
- Support httpx2 in the test client
### 1.1.0 (2026-05-23) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#110-may-23-2026)
- Use `"application/octet-stream"` as the `FileResponse` media type fallback
### 1.0.0 (2026-03-22) [source](https://github.com/Kludex/starlette/blob/main/docs/release-notes.md#100-march-22-2026)
- Track session access and modification in `SessionMiddleware`
- (6 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 28 releases; 14 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 1.9.0, 1.5.1, 1.4.1, 1.3.1, 1.2.1, 1.0.1, 0.52.1, 0.52.0, 0.49.3, 0.49.2, 0.49.1, 0.47.3 and 2 more.
- Sources: https://raw.githubusercontent.com/Kludex/starlette/main/docs/release-notes.md; registry (pypi) for dates.
