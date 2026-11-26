# @anthropic-ai/sdk (npm): changes after 2025-06-01

- Latest stable on the registry: **1.14.0** (2026-11-24). Built 2026-11-25.
- 122 stable releases after the cut-off: 0.53.0 (2025-06-05) to 1.14.0 (2026-11-24).
- New major versions since the cut-off: 1.0.0 (2026-10-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.0.0 (2026-10-21) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#100-2026-10-21)
- api: add support for new API version 2026-10-21
### 0.135.0 (2026-10-15) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01350-2026-10-15)
- ci: speed up breaking change detection
### 0.124.0 (2026-09-04) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01240-2026-09-04)
- internal: bundle the mock server spec and update breaking-change detection
### 0.117.0 (2026-08-13) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01170-2026-08-13)
- ci: run breaking-change detection as a ci.yml job on every push
### 0.72.0 (2026-01-29) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#0720-2026-01-29)
- ci: add breaking change detection workflow
### 0.57.0 (2025-07-21) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#0570-2025-07-21)
- client: add breaking change detection to CI

## Removed or renamed
### 0.122.0 (2026-08-27) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01220-2026-08-27)
- Beta Messages type `BetaSkill` (the `{type, skill_id, version}` entry in `BetaContainer.skills`) is renamed `BetaContainerSkill`; the request-side `BetaSkillParams` keeps its name. […]

## Deprecated
### 0.132.0 (2026-10-07) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01320-2026-10-07)
- api: add display_name to RBAC roles and deprecate name
### 0.127.0 (2026-09-18) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#01270-2026-09-18)
- api: add group with display_name to rate limits, deprecate group_type
### 0.89.0 (2026-04-14) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#0890-2026-04-14)
- api: mark Sonnet and Opus 4 as deprecated
### 0.58.0 (2025-08-05) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#0580-2025-08-05)
- api: removed older deprecated models

## New APIs and features
### 1.14.0 (2026-11-24) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#1140-2026-11-24)
- api: add Google-managed data controls for Google Cloud projects
- api: add Google-managed data controls for user profiles
- api: add support for compliance review cases, notices, and items
### 1.13.0 (2026-11-23) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#1130-2026-11-23)
- api: add an error code to Message Batches creation
- api: add External Storage to the Admin API beta
- api: add webhook events for external storage failure and recovery
### 1.12.0 (2026-11-20) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#1120-2026-11-20)
- api: add the image_dimensions_too_large error code
### 1.11.0 (2026-11-19) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#1110-2026-11-19)
- api: add Claude Code managed settings to the Admin API
- api: add the sandbox_egress_restricted error to Admin API plugin methods
### 1.10.0 (2026-11-17) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#1100-2026-11-17)
- api: add beta support for the billing_policy request parameter
- api: add contract_spend_limit_reached error code to messages
- api: add error codes for linked billing refusals
- api: add the user_profile_billing_not_authorized error code
- api: add webhook events for external key failure and recovery
### 1.9.0 (2026-11-16) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#190-2026-11-16)
- api: add source and error codes to the RBAC Role read endpoints
- api: add Update Bundle, which sets a Claude Tag Bundle's instructions, and return instructions on Bundle
### 1.8.0 (2026-11-10) [source](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CHANGELOG.md#180-2026-11-10)
- api: add Claude Tag metrics to the analytics summaries and users reports
- api: add reply_mode to Claude Tag Slack channel settings
- (184 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 124 releases; 100 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.132.1, 0.117.1, 0.112.5, 0.112.4, 0.112.3, 0.112.2, 0.112.1, 0.109.1, 0.104.2, 0.104.1, 0.100.1, 0.98.1 and 12 more.
- Sources: https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/CHANGELOG.md; registry (npm) for dates.
