# express (npm): changes after 2025-06-01

- Latest stable on the registry: **5.3.0** (2026-10-09). Built 2026-11-25.
- 7 stable releases after the cut-off: 4.22.0 (2025-12-01) to 5.3.0 (2026-10-09).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 5.2.1 (2025-12-01) [source](https://github.com/expressjs/express/blob/master/History.md#521)
- The prior release (5.2.0) included an erroneous breaking change related to the extended query parser. There is no actual security vulnerability associated with this behavior (CVE-2024-51999 has been rejected). […]

## Deprecated
### 5.2.0 (2025-12-01) [source](https://github.com/expressjs/express/blob/master/History.md#520)
- A deprecation warning was added when using `res.redirect` with undefined arguments, Express now emits a warning to help detect calls that pass undefined as the status or URL and make them easier to fix.

## New APIs and features
### 5.3.0 (2026-10-09) [source](https://github.com/expressjs/express/blob/master/History.md#530)
- Allow conditional revalidation for QUERY requests. `req.fresh` previously only validated freshness for GET and HEAD requests, so QUERY responses never returned 304 despite a matching validator. […]

## Coverage
- Release notes read for 3 releases; 3 had extractable items.
- 4 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/expressjs/express/master/History.md; registry (npm) for dates.
