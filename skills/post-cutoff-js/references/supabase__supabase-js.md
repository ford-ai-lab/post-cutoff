# @supabase/supabase-js (npm): changes after 2025-06-01

- Latest stable on the registry: **2.119.2** (2026-11-19). Built 2026-11-25.
- 123 stable releases after the cut-off: 2.49.9 (2025-06-02) to 2.119.2 (2026-11-19).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Deprecated
### 2.117.0 (2026-09-22) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21170-2026-09-22)
- auth: enable passkey API by default and deprecate experimental passkey opt-in

## Minimum versions and platform support
### 2.79.0 (2025-11-04) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#2790-2025-11-04)
- repo: remove node-fetch dependency, require Node.js 20+

## New APIs and features
### 2.119.0 (2026-11-04) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21190-2026-11-04)
- postgrest: expose query builder options to.from method - custom fetch per request
### 2.118.0 (2026-10-15) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21180-2026-10-15)
- postgrest: leave computed fields out of select('*') and resolve no-argument rpc overloads for postgrest-typegen output
### 2.116.0 (2026-09-07) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21160-2026-09-07)
- auth: add MFA recovery codes API
### 2.115.0 (2026-09-03) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21150-2026-09-03)
- postgrest: add getOpenApiSpec()
### 2.112.0 (2026-08-03) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21120-2026-08-03)
- supabase: move OpenTelemetry tracing to opt-in /tracing subpath
### 2.110.0 (2026-06-30) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21100-2026-06-30)
- repo: drop Node.js 20 support
### 2.107.0 (2026-06-02) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21070-2026-06-02)
- auth: remove navigator.locks-based mutex; introduce commit guard + dispose()
- supabase: update X-Client-Info to structured metadata format
- realtime: allow httpSend to send binary payload
### 2.106.0 (2026-05-18) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21060-2026-05-18)
- supabase: W3C/OpenTelemetry trace context propagation
### 2.105.0 (2026-04-27) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21050-2026-04-27)
- auth: add passkey support with WebAuthn registration, authentication, and management
- realtime: Realtime deferred disconnect
### 2.102.0 (2026-04-07) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#21020-2026-04-07)
- supabase: export PostgrestFilterBuilder and StorageApiError from supabase-js
- postgrest: add automatic retries for transient errors
### 2.95.0 (2026-02-05) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#2950-2026-02-05)
- supabase: add canonical CORS headers export for edge functions
### 2.94.0 (2026-02-03) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#2940-2026-02-03)
- postgrest: add URL length validation and timeout protection
### 2.93.0 (2026-01-26) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#2930-2026-01-26)
- supabase: add missing HTTP headers for client platform and runtime detection
### 2.89.0 (2025-12-18) [source](https://github.com/supabase/supabase-js/blob/master/packages/core/supabase-js/CHANGELOG.md#2890-2025-12-18)
- supabase: export DatabaseWithoutInternals utility type
- (6 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 93 releases; 20 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.119.2, 2.119.1, 2.117.3, 2.117.2, 2.117.1, 2.114.0, 2.113.0, 2.112.4, 2.112.3, 2.112.2, 2.112.1, 2.111.0 and 61 more.
- 30 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/supabase/supabase-js/master/packages/core/supabase-js/CHANGELOG.md; registry (npm) for dates.
