# uvicorn (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.54.0** (2026-09-25). Built 2026-11-25.
- 27 stable releases after the cut-off: 0.35.0 (2025-06-28) to 0.54.0 (2026-09-25).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 0.51.0 (2026-07-08) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0510-july-8-2026)
- Remove `colorama` from the `standard` extra
### 0.43.0 (2026-04-03) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0430-april-3-2026)
- Drop cast in ASGI types

## Deprecated
### 0.50.0 (2026-07-04) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0500-july-4-2026)
- Deprecate the legacy `websockets` implementation; use `websockets-sansio` or `wsproto` instead

## Minimum versions and platform support
### 0.40.0 (2025-12-21) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0400-december-21-2025)
- Drop support for Python 3.9

## New APIs and features
### 0.54.0 (2026-09-25) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0540-september-24-2026)
- Add HTTP/2 response trailers through the ASGI `http.response.trailers` extension. Clients must send `TE: trailers` to receive them
- Add HTTP/2 `103 Early Hints` through the ASGI `http.response.early_hint` extension
### 0.53.0 (2026-09-14) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0530-september-14-2026)
- Add experimental HTTP/2 support through `zttp`
- Add support for `zuvloop`
### 0.52.0 (2026-07-29) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0520-july-29-2026)
- Add an experimental `zttp` HTTP/1.1 implementation, selectable with `--http zttp`
### 0.51.0 (2026-07-08) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0510-july-8-2026)
- Restart workers one at a time on `SIGHUP`, bringing each replacement up before retiring the old worker, so reloads no longer drop requests
### 0.47.0 (2026-05-14) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0470-may-14-2026)
- Add `ssl_context_factory` for custom `SSLContext` configuration
### 0.46.0 (2026-04-23) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0460-april-23-2026)
- Support `ws_max_size` in `wsproto` implementation
- Support `ws_ping_interval` and `ws_ping_timeout` in `wsproto` implementation
### 0.45.0 (2026-04-21) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0450-april-21-2026)
- Add `--reset-contextvars` flag to isolate ASGI request context
- Accept `os.PathLike` for `log_config`
- Accept `log_level` strings case-insensitively
### 0.44.0 (2026-04-06) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0440-april-6-2026)
- Implement websocket keepalive pings for websockets-sansio
### 0.41.0 (2026-02-16) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0410-february-16-2026)
- Add `--limit-max-requests-jitter` to stagger worker restarts
- Add socket path to `scope["server"]`
### 0.38.0 (2025-10-18) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0380-october-18-2025)
- Support Python 3.14
### 0.37.0 (2025-09-23) [source](https://github.com/Kludex/uvicorn/blob/main/CHANGELOG.md#0370-september-23-2025)
- Add `--timeout-worker-healthcheck` option
- Add `os.PathLike[str]` type to `ssl_ca_certs`
- (3 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 27 releases; 16 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.52.4, 0.52.3, 0.52.2, 0.52.1, 0.50.2, 0.50.1, 0.49.0, 0.48.0, 0.42.0, 0.39.0, 0.36.1.
- Sources: https://raw.githubusercontent.com/Kludex/uvicorn/main/CHANGELOG.md; registry (pypi) for dates.
