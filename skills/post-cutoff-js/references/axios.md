# axios (npm): changes after 2025-06-01

- Latest stable on the registry: **1.21.1** (2026-11-09). Built 2026-11-25.
- 36 stable releases after the cut-off: 0.30.1 (2025-08-04) to 1.21.1 (2026-11-09).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.21.0 (2026-10-27) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1210--october-21-2026)
- Header Defaults: Only plain objects, null-prototype maps, and compatible `AxiosHeaders` instances are treated as common or method-specific defaults; literal headers such as `Link` are now preserved. […]

## Deprecated
### 1.16.0 (2026-05-02) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1160--may-2-2026)
- Deprecated `unescape()` replaced with modern UTF-8 encoding. Non-ASCII URL handling is now spec-correct; consumers depending on legacy `unescape()` quirks may see different output bytes. (#7378)

## New APIs and features
### 1.21.0 (2026-10-27) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1210--october-21-2026)
- Response Timing: Added `response.duration`, in milliseconds, including on `error.response` when present. Timing measures adapter execution and excludes interceptors and transforms; […]
- UTF-8 Basic Authentication: Added `transitional.encodeBasicAuthUsername: true` to support Unicode usernames in XHR and Fetch requests. The option defaults to `false`, preserving existing authentication behavior; […]
### 1.19.0 (2026-07-29) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1190--july-22-2026)
- Configuration Extensibility: Preserved own-enumerable symbol-keyed fields through mergeConfig and added a generic params type across public TypeScript declarations, responses, errors, adapters, and serializers.
- Header Parameter Parsing: Added the opt-in AxiosHeaders.parseParameters() parser for quote-aware, RFC-style HTTP parameter parsing while preserving legacy parsing behavior.
- HTTP Status Codes: Added the missing Cloudflare 520 WebServerReturnsAnUnknownError status and matching ESM/CJS declarations.
### 1.17.0 (2026-06-03) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1170--june-1-2026)
- HTTP Compression: Added Node HTTP adapter support for zstd response decompression, with `transitional.advertiseZstdAcceptEncoding` controlling whether `zstd` is advertised in `Accept-Encoding`. (#6792, #10920)
### 1.16.0 (2026-05-02) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1160--may-2-2026)
- QUERY HTTP Method: Added support for the QUERY HTTP method across adapters and type definitions. (#10802)
- ECONNREFUSED Error Constant: Exposed `ECONNREFUSED` as a constant on `AxiosError` so callers can match connection-refused failures without comparing string literals. (#10680)
- Encode Helper Export: Exported the internal `encode` helper from `buildURL` so userland param serializers can reuse the same encoding logic that axios uses internally. (#6897)
### 1.15.0 (2026-04-08) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1150---april-7-2026)
- Deno & Bun Runtime Support: Added full smoke test suites for Deno and Bun, with CI workflows that run both runtimes before any release is cut. (#10652)
### 1.13.0 (2025-10-27) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#1130-2025-10-27)
- http: add HTTP2 support
### 1.12.0 (2025-09-11) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#1120-2025-09-11)
- adapter: surface low‑level network error details; attach original error via cause
- fetch: add fetch, Request, Response env config variables for the adapter
- support reviver on JSON.parse (2a97634), closes
- types: extend AxiosResponse interface to include custom headers type
### 1.10.0 (2025-06-14) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#1100-2025-06-14)
- types: improved fetchOptions interface
### 1.15.2 (2026-04-21) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1152---april-21-2026)
- `allowedSocketPaths` Config Option: New request config option (and TypeScript types) to allowlist Unix domain socket paths used by the Node http adapter; backwards compatible when unset. (#10777)
### 1.15.1 (2026-04-19) [source](https://github.com/axios/axios/blob/v1.x/CHANGELOG.md#v1151---april-19-2026)
- AI-Based Docs Translations: Initial scaffold for AI-assisted translations of the documentation site. (#10705)
- (10 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 22 releases; 13 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 1.18.0, 1.16.1, 1.14.0, 1.13.4, 1.13.2, 1.13.1, 1.12.2, 1.12.1, 1.11.0.
- 14 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/axios/axios/v1.x/CHANGELOG.md; registry (npm) for dates.
