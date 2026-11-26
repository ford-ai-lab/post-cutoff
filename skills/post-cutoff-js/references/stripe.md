# stripe (npm): changes after 2025-06-01

- Latest stable on the registry: **23.2.0** (2026-11-19). Built 2026-11-25.
- 42 stable releases after the cut-off: 18.2.1 (2025-06-02) to 23.2.0 (2026-11-19).
- New major versions since the cut-off: 19.0.0 (2025-09-30), 20.0.0 (2025-11-18), 21.0.0 (2026-03-26), 22.0.0 (2026-04-03), 23.0.0 (2026-10-01).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 23.0.0 (2026-10-01) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2300---2026-09-30)
- ⚠️ #2856 Remove V1-only fields from V2 list response types
- ⚠️ #2862 Remove Stripe.constructEventWithoutVerification
- ⚠️ Generate operation-specific address parameters for V2 requests
- ⚠️ #2865 Remove `ErrorType` export
- ⚠️ #2868 Classify incomplete response bodies as connection errors
- ⚠️ #2876 Update verifyHeader and verifyHeaderAsync methods to use DEFAULT_TOLERANCE
- ⚠️ #2832 Update generated code
- ⚠️ Change type of `AccountRejectParams.reason` from `string` to `enum`
- ⚠️ Add support for new values `invalid_address_cmra_address` and `invalid_address_registered_agent_address` on enums `Account.future_requirements.errors[].code`, `Account.requirements.errors[].code` […]
- ⚠️ Add support for new value `other` on enum `Reserve.Plan.status`
- ⚠️ Add support for new values `manual_release` and `other` on enum `Reserve.Plan.type`
- ⚠️ Add support for new value `hold_expired` on enum `Reserve.Release.reason`
### 22.6.0 (2026-08-27) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2260---2026-08-26)
- ⚠️ #2801 Add discriminatedUnion kind to V2RuntimeSchema coercion
- ⚠️ Throws when serializing a discriminated union parameter whose discriminator is missing or is not a string. This avoids skipping coercion entirely which could silently truncate `int64` fields above `Number.MAX_SAFE_INTEGER`.
- ⚠️ #2812 Update generated code
- ⚠️ Remove support for `cryptogram` on `PaymentAttemptRecord.payment_method_details.card.three_d_secure` and `PaymentRecord.payment_method_details.card.three_d_secure`
### 22.3.0 (2026-06-24) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2230---2026-06-24)
- ⚠️ #2748 Update generated code
- ⚠️ Add support for new value `tax_fund` on enum `BalanceTransaction.type`
- ⚠️ Add support for new value `sui` on enums `Charge.payment_method_details.crypto.network`, `PaymentAttemptRecord.payment_method_details.crypto.network`, and `PaymentRecord.payment_method_details.crypto.network`
- ⚠️ Add support for new value `usdsui` on enums `Charge.payment_method_details.crypto.token_currency`, `PaymentAttemptRecord.payment_method_details.crypto.token_currency`, and […]
- ⚠️ Add support for new value `mastercard_compliance` on enum `Dispute.enhanced_eligibility_types`
- ⚠️ Add support for new value `validated` on enum `Identity.VerificationSession.redaction.status`
- ⚠️ Add support for new value `satispay` on enums `Invoice.payment_settings.payment_method_types` and `Subscription.payment_settings.payment_method_types`
- ⚠️ Remove support for `stored_credential_usage` on `PaymentAttemptRecord.payment_method_details.card` and `PaymentRecord.payment_method_details.card`
- (88 more in this category not shown; see the changelog.)

## Removed or renamed
### 22.0.0 (2026-04-03) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2200---2026-04-02)
- Removed top-level “stripe” ambient module. This allows import aliasing for the stripe package.
### 20.4.0 (2026-02-25) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2040---2026-02-25)
- Remove support for unused `card_issuer_decline` on `Radar.PaymentEvaluation.insights`
### 20.3.0 (2026-01-28) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2030---2026-01-28)
- Remove the `qs` dependency, addressing Issue
- Remove support for `bgn` on `Terminal.Configuration.tipping`, `Terminal.ConfigurationCreateParams.tipping`, and `Terminal.ConfigurationUpdateParams.tipping`
### 19.0.0 (2025-09-30) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1900---2025-09-30)
- Remove support for `link` and `pay_by_bank` on `PaymentMethodUpdateParams`
- Remove support for `iterations` on `InvoiceCreatePreviewParams.schedule_details.phases[]`, `SubscriptionScheduleCreateParams.phases[]`, and `SubscriptionScheduleUpdateParams.phases[]`
### 18.4.0 (2025-07-30) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1840---2025-07-30)
- Remove support for value `disabled` from enum `Capability.status`

## Deprecated
### 22.4.0 (2026-07-29) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2240---2026-07-29)
- Remove support for `proof_of_registration` on `AccountCreateParams.documents`. This field was limited-use and is being deprecated.
- Remove support for `dynamic_tax_rates` on `Checkout.SessionCreateParams.line_items[]`. This field was limited-use and is being deprecated.
### 22.2.0 (2026-05-27) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2220---2026-05-27)
- Adds `V2List` and `V2ListPromise` types to represent API v2 list responses. These types include deprecated fields from the previously returned list shapes. These fields will be removed in the next major release.
### 19.1.0 (2025-10-03) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1910---2025-10-03)
- #2447 Update param in deprecation docs link
### 19.0.0 (2025-09-30) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1900---2025-09-30)
- Node 16 support is deprecated and will be removed in the next scheduled major release (March 2026)

## Minimum versions and platform support
### 23.0.0 (2026-10-01) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2300---2026-09-30)
- ⚠️ Drop support for Node 18
### 21.0.0 (2026-03-26) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#2100---2026-03-25)
- ⚠️ #2609 Drop support for Node 16
### 19.0.0 (2025-09-30) [source](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1900---2025-09-30)
- ⚠️ #2432 Drop support for Node < 16 & clarify policy
- ⚠️ Drop support for Node versions < 16

## Coverage
- Release notes read for 42 releases; 14 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 23.2.0, 23.1.0, 23.0.1, 22.6.2, 22.6.1, 22.5.0, 22.3.2, 22.3.1, 22.2.3, 22.2.2, 22.2.1, 22.1.1 and 16 more.
- Sources: https://raw.githubusercontent.com/stripe/stripe-node/master/CHANGELOG.md; registry (npm) for dates.
