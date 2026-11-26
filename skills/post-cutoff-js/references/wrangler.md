# wrangler (npm): changes after 2025-06-01

- Latest stable on the registry: **4.168.0** (2026-11-24). Built 2026-11-25.
- 218 stable releases after the cut-off: 3.114.10 (2025-06-25) to 4.168.0 (2026-11-24).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 4.167.0 (2026-11-23) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41670)
- Remove the `wrangler dispatch-namespace rename` command
### 4.136.0 (2026-09-21) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41360)
- Remove the experimental Container image environment binding
### 4.132.0 (2026-09-15) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41320)
- Remove the gated Web Search binding and Wrangler command
### 4.131.0 (2026-09-10) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41310)
- Remove `wrangler preview settings` commands
### 4.117.0 (2026-07-31) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41170)
- Remove `containerEngine` from the worker options returned by `unstable_getMiniflareWorkerOptions`
### 4.111.0 (2026-07-15) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41110)
- Remove support for service environments and the `legacy_env` configuration field
### 4.107.0 (2026-07-02) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41070)
- A stale Node.js flag that caused unexpected behaviour on Node.js v26 has been removed.
### 4.103.0 (2026-06-19) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41030)
- Remove experimental autoconfig exports
### 4.98.0 (2026-06-04) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4980)
- Rename the `web_search` binding kind to `websearch`
### 4.96.0 (2026-06-01) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4960)
- Rename `pipeline` field to `stream` in pipeline bindings configuration
### 4.86.0 (2026-04-28) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4860)
- `BundlerController.teardown()` now runs the esbuild cleanup before removing the bundler's temporary directory, and aborts the in-flight bundle build so it cannot emit stale `bundleStart`/`bundleComplete` events after teardown. […]
### 4.84.0 (2026-04-20) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4840)
- Rename the documented containers SSH config option to `ssh`
### 4.52.0 (2025-12-02) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4520)
- Remove the `wrangler deploy`'s `--x-remote-diff-check` experimental flag
### 4.25.0 (2025-07-17) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4250)
- Added rename namespace command to Workers KV
- (1 more in this category not shown; see the changelog.)

## Deprecated
### 4.117.0 (2026-07-31) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41170)
- `/cdn-cgi/mf/scheduled` → `/cdn-cgi/local/scheduled` (Note `/cdn-cgi/mf/scheduled` is already deprecated)
### 4.96.0 (2026-06-01) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4960)
- Remove the deprecated `experimental.testMode` option from `unstable_dev`
### 4.90.0 (2026-05-07) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4900)
- Add deprecation warning for `delivery_delay` in queue producer bindings
### 4.73.0 (2026-03-13) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4730)
- Deprecate SSH passthrough flags in `wrangler containers ssh`
### 4.59.0 (2026-01-13) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4590)
- Users can now specify `constraints.tiers` for their container applications. `tier` is deprecated in favor of `tiers`. If left unset, we will default to `tiers: [1, 2]`. Note that `constraints` is an experimental feature.
### 4.57.0 (2026-01-07) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4570)
- Drop deprecated containers `observability.logging` field
### 4.39.0 (2025-09-23) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#4390)
- Rename Hyperdrive local connection string environment variable from `WRANGLER_HYPERDRIVE_LOCAL_CONNECTION_STRING_<BINDING_NAME>` to `CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_<BINDING_NAME>`. […]

## New APIs and features
### 4.168.0 (2026-11-24) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41680)
- Apply `images.url_transformations` when deploying a Worker
### 4.167.0 (2026-11-23) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41670)
- Support `--env-file` in the experimental `cf-wrangler dev` delegate
### 4.166.0 (2026-11-20) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41660)
- Show configured trigger targets during experimental `wrangler triggers deploy --dry-run`
- Add `images.url_transformations` to the Wrangler configuration
- Add `--show-diff` flag to `wrangler triggers deploy`
### 4.165.0 (2026-11-18) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41650)
- Add a new `--force` flag to `d1 migrations apply` which skips the interactive confirmation and applies any pending migrations non-interactively. This is useful for CI and automation.
### 4.164.0 (2026-11-17) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41640)
- Add custom CA and client certificate references to Workers VPC service TLS settings
### 4.163.0 (2026-11-16) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41630)
- Write Build Output to `.cloudflare/output/v1/` and record the producer
- Start local Workflows from Artifacts events
### 4.162.0 (2026-11-13) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41620)
- Use the local simulator for Artifacts bindings that omit `remote`
- Reject settings on a `workflows` binding to a Workflow declared in `exports`
- Upload Workflow export settings with the Worker
### 4.161.0 (2026-11-12) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41610)
- Write source maps in Build Output with `sources` relative to each source map file
### 4.160.0 (2026-11-10) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41600)
- Support forwarded Wrangler development server options in the experimental `cf-wrangler` delegate
- Add custom Cloudflare API headers through `CLOUDFLARE_API_HEADERS`
### 4.159.0 (2026-11-09) [source](https://github.com/cloudflare/workers-sdk/blob/main/packages/wrangler/CHANGELOG.md#41590)
- Store experimental `cf-wrangler dev` state in `.cloudflare/state`
- Add `--compatibility` flag to `wrangler d1 export`
- Support `CLOUDFLARE_AUTH_PROFILE` for shared authentication profile selection
- (374 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 210 releases; 150 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 4.160.1, 4.156.2, 4.156.1, 4.151.3, 4.151.2, 4.151.1, 4.143.1, 4.136.3, 4.136.2, 4.136.1, 4.131.2, 4.131.1 and 48 more.
- 8 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/cloudflare/workers-sdk/main/packages/wrangler/CHANGELOG.md; registry (npm) for dates.
