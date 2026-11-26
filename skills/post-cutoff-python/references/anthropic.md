# anthropic (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.14.0** (2026-11-24). Built 2026-11-25.
- 129 stable releases after the cut-off: 0.52.2 (2025-06-02) to 2.14.0 (2026-11-24).
- New major versions since the cut-off: 1.0.0 (2026-08-20), 2.0.0 (2026-10-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 2.10.0 (2026-11-17) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2100-2026-11-17)
- internal: don't report moved classes as breaking changes
### 2.0.0 (2026-10-21) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#200-2026-10-21)
- api: add support for new API version 2026-10-21
### 1.15.0 (2026-10-15) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#1150-2026-10-15)
- ci: speed up breaking change detection
### 1.4.0 (2026-09-04) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#140-2026-09-04)
- internal: fix mypy unreachable error in detect-breaking-changes script
### 1.3.0 (2026-09-01) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#130-2026-09-01)
- ci: don't hard-wrap detect-breaking-changes output
### 1.2.0 (2026-08-27) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#120-2026-08-27)
- ci: resolve assignment aliases in detect-breaking-changes
### 1.0.0 (2026-08-20) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#100-2026-08-20)
- client: upgrade to httpx2 and some minor breaking changes. See MIGRATION.md for details
### 0.122.0 (2026-08-13) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#01220-2026-08-13)
- ci: run breaking-change detection as a ci.yml job on every push
### 0.77.0 (2026-01-29) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0770-2026-01-29)
- remove class causing breaking change
### 0.65.0 (2025-09-02) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0650-2025-09-02)
- internal: improve breaking change detection
### 0.63.0 (2025-08-12) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0630-2025-08-12)
- internal: detect breaking changes when removing endpoints
### 0.56.0 (2025-07-01) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0560-2025-07-01)
- internal: add breaking change detection

## Removed or renamed
### 1.2.0 (2026-08-27) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#120-2026-08-27)
- Beta Messages type `BetaSkill` (container skill reference with `skill_id`, `type`, `version`) is renamed `BetaContainerSkill`; the request-side `BetaSkillParams` keeps its name. […]

## Deprecated
### 1.12.0 (2026-10-07) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#1120-2026-10-07)
- api: add display_name to RBAC roles and deprecate name
### 1.7.0 (2026-09-18) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#170-2026-09-18)
- api: add group with display_name to rate limits, deprecate group_type
### 0.106.0 (2026-06-05) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#01060-2026-06-05)
- api: mark Claude Opus 4.1 as deprecated
### 0.95.0 (2026-04-14) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0950-2026-04-14)
- api: mark Sonnet and Opus 4 as deprecated
### 0.59.0 (2025-07-23) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#0590-2025-07-23)
- api: removed older deprecated models

## New APIs and features
### 2.14.0 (2026-11-24) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2140-2026-11-24)
- api: add Google-managed data controls for Google Cloud projects
- api: add Google-managed data controls for user profiles
- api: add support for compliance review cases, notices, and items
### 2.13.0 (2026-11-23) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2130-2026-11-23)
- api: add an error code to Message Batches creation
- api: add External Storage to the Admin API beta
- api: add webhook events for external storage failure and recovery
### 2.12.0 (2026-11-20) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2120-2026-11-20)
- api: add the image_dimensions_too_large error code
### 2.11.0 (2026-11-19) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2110-2026-11-19)
- api: add Claude Code managed settings to the Admin API
- api: add the sandbox_egress_restricted error to Admin API plugin methods
### 2.10.0 (2026-11-17) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#2100-2026-11-17)
- api: add beta support for the billing_policy request parameter
- api: add contract_spend_limit_reached error code to messages
- api: add error codes for linked billing refusals
- api: add the user_profile_billing_not_authorized error code
- api: add webhook events for external key failure and recovery
### 2.9.0 (2026-11-16) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#290-2026-11-16)
- api: add source and error codes to the RBAC Role read endpoints
- api: add Update Bundle, which sets a Claude Tag Bundle's instructions, and return instructions on Bundle
### 2.8.0 (2026-11-10) [source](https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md#280-2026-11-10)
- api: add Claude Tag metrics to the analytics summaries and users reports
- api: add reply_mode to Claude Tag Slack channel settings
- (192 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 130 releases; 106 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 1.12.1, 0.120.2, 0.120.1, 0.117.1, 0.115.1, 0.109.2, 0.109.1, 0.107.1, 0.105.2, 0.105.1, 0.104.1, 0.103.1 and 12 more.
- Sources: https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/CHANGELOG.md; registry (pypi) for dates.
