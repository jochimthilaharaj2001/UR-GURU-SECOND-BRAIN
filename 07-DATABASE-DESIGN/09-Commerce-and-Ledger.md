# Marketplace commerce, refunds and accounting — proposed data flow

**BRD:** v6.2.2 p6, p9–10, p11. No rate, provider, refund window or payout timing is final (OD-03/04/05).

## Approved principles, proposed data model

`OrderHeader → OrderLine → PaymentAttempt → PaymentProviderEvent → Entitlement / Enrollment`.

- Create order lines for each chargeable item; XACT subscriptions/packs are **R2 proposals**, not a fixed launch billing feature.
- Gateway callback must be authenticated, independently verified, idempotent, and auditable. A client redirect is insufficient.
- Enforce provider-scoped event uniqueness. Delayed or duplicated provider notifications must not create duplicate paid access.
- `LedgerEntry` is append-only: debit/credit postings, corrections and refunds are **new linked rows**, not value overwrites.
- `Refund` can be partial by line/payment; eligibility and entitlement adjustment policy require Finance sign-off. No promised default refund timeline.
- TeacherEarning is calculated using an approved commission base and may be reserved, held for disputes or settled via `TeacherPayout` and `PayoutItem`.
- Tuition GMV is not UR GURU revenue; only approved commission/direct revenue counts as platform revenue.
- Demo video never creates an order, payment attempt or entitlement.

## Critical physical decisions before code

- Invoice/order-line numbering, currency/tax rounding, multi-currency treatment, immutable journal entry pairing, failed webhook retry policy, provider merchant uniqueness, capacity vs reservation timing, payout aggregation and reconciliation statuses.
- Define role/permission rights for Finance reviewer; all manual adjustments require audit and reversible financial correction entry.

**UAT:** AC-08, AC-12–15, AC-33 and recovery/load tests.
