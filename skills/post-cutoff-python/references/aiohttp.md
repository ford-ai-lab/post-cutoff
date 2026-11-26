# aiohttp (pypi): changes after 2025-06-01

- Latest stable on the registry: **3.14.5** (2026-10-11). Built 2026-11-25.
- 21 stable releases after the cut-off: 3.12.7 (2025-06-02) to 3.14.5 (2026-10-11).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 3.14.4 (2026-10-05) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- The WebSocket receive queue now only holds a weak reference to the `WebSocketReader` while parsing is stalled; code constructing a reader directly and passing it to `set_parser()` must keep its own strong reference to it, or […]
- Removed the internal writer proxy used for upload progress accounting. `AbstractStreamWriter` gained an optional `on_body_write` callback that `write()` / `write_eof()` implementations must invoke with each accepted body chunk's […]
- Increased minimum yarl version to 1.25.1 -- by.
- Changed `Set-Cookie` parsing to create exactly one cookie per field, as RFC 6265 and browsers do. Later `name=value` pairs and unknown attributes no longer create extra cookies, a leading pair such as `Path=/` or `$Version=1` is […]
### 3.14.0 (2026-06-01) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Stopped calling `socket.getfqdn` as the fallback for `aiohttp.web.BaseRequest.host`. `socket.getfqdn` performs blocking reverse DNS resolution on the event loop thread and can stall a worker for many seconds when the system […]
- Tightened outbound header serialization to reject all ASCII control characters forbidden by `9110#section-5.5` and `9112#section-4` (`0x00`\-`0x08`, `0x0A`\-`0x1F`, `0x7F`) in status lines, header field-names, and field-values. […]
### 3.13.3 (2026-01-03) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- `Brotli` and `brotlicffi` minimum version is now 1.2. Decompression now has a default maximum output size of 32MiB per decompress call -- by.

## Removed or renamed
### 3.14.4 (2026-10-05) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Deprecated `ClientResponse.output_size` and `ClientResponse.upload_complete`; use `aiohttp.UploadTracker` instead -- by.
### 3.14.0 (2026-06-01) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Deprecated `aiohttp.BasicAuth` and the `auth` / `proxy_auth` parameters. They will be removed in aiohttp 4.0. Use the new `aiohttp.encode_basic_auth` helper together with `headers={"Authorization":...}` (or […]
- Added deprecation warning to `aiohttp.pytest_plugin`, please switch to `pytest-aiohttp` -- by.

## Deprecated
### 3.14.0 (2026-06-01) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Added `aiohttp.encode_basic_auth` for encoding HTTP Basic Authentication credentials. Replaces the now-deprecated `aiohttp.BasicAuth` -- by.

## Minimum versions and platform support
### 3.14.0 (2026-06-01) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Dropped support for Python 3.9 -- by.

## New APIs and features
### 3.14.0 (2026-06-01) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Added `RequestKey` and `ResponseKey` classes, which enable static type checking for request & response context storages in the same way that `AppKey` does for `Application` -- by.
- Started accepting `asynchronous context managers` for cleanup contexts. Legacy single-yield `asynchronous generator` cleanup contexts continue to be supported; […]
- Added `aiohttp.CookieJar.cookies` and `aiohttp.CookieJar.host_only_cookies` read-only properties to `aiohttp.CookieJar` exposing the stored cookies with their full attributes -- by.
- Added `aiohttp.web.TCPSite.port` accessor for dynamic port allocations in `aiohttp.web.TCPSite` -- by and.
- Added `decode_text` parameter to `aiohttp.ClientSession.ws_connect` and `aiohttp.web.WebSocketResponse` to receive WebSocket TEXT messages as raw bytes instead of decoded strings, enabling direct use with high-performance JSON […]
- Large overhaul of parser/decompression code.
- Added explicit APIs for bytes-returning JSON serializer: `JSONBytesEncoder` type, `JsonBytesPayload`, `aiohttp.web.json_bytes_response`, `aiohttp.web.WebSocketResponse.send_json_bytes` and […]
- Added `ClientResponse.output_size` and `ClientResponse.upload_complete` -- by.
### 3.13.0 (2025-10-06) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Added support for Python 3.14.
- Added support for free-threading in Python 3.14+ -- by.
- Added support for Zstandard (aka Zstd) compression -- by.
- Added `StreamReader.total_raw_bytes` to check the number of bytes downloaded -- by.
### 3.14.4 (2026-10-05) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Added `aiohttp.UploadTracker` for observing a client request's upload progress -- by.
- Switched `application/x-www-form-urlencoded` parsing in `aiohttp.web.BaseRequest.post` to the faster `yarl.query_to_pairs` parser and added the `client_max_fields` argument to `aiohttp.web.Application` (default `1000`) to cap the […]
- Added constants to `aiohttp.hdrs` for widely used headers: those that browsers send on every request (`Sec-Fetch-*`, `Sec-CH-UA*`, `Sec-GPC`, `Upgrade-Insecure-Requests`, `Priority`), W3C trace context (`traceparent` […]
### 3.13.4 (2026-03-28) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Added `max_headers` parameter to limit the number of headers that should be read from a response -- by.
- Added a `dns_cache_max_size` parameter to `TCPConnector` to limit the size of the cache -- by.
### 3.13.1 (2025-10-17) [source](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- Make configuration options in `AppRunner` also available in `run_app()` -- by.
- (3 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 21 releases; 9 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.14.5, 3.14.3, 3.14.2, 3.14.1, 3.13.5, 3.13.2, 3.12.15, 3.12.13, 3.12.12, 3.12.10, 3.12.9, 3.12.7.
- Sources: https://raw.githubusercontent.com/aio-libs/aiohttp/master/CHANGES.rst; registry (pypi) for dates.
