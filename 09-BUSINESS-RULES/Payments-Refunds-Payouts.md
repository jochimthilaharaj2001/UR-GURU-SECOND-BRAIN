# Payments, Refunds, Teacher Earnings and Payout Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Commercial principle
Gross class payments = **GMV**, not platform revenue. Paid access depends on **server-verified gateway success**. An append-only ledger records adjustments. There is no approved final 15% commission in BRD V6.2.2.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-030 | Student tuition receipts are GMV; recognize UR GURU revenue separately as approved commission/direct fees only. | BRD §7 p.6 | AC-15 | Review baseline |
| UG-RULE-031 | Checkout must disclose total/currency, charges, description, access period and applicable renewal/cancellation/refund terms before purchase. | BRD §7 p.6 | AC-12 | Review baseline |
| UG-RULE-032 | An order contains auditable line items and payment attempts; client-side success redirect alone cannot grant paid access. | BRD §7 p.6 | AC-12, AC-13 | Review baseline |
| UG-RULE-033 | Gateway notifications must be authenticated, server-verified, replay/idempotency protected before any entitlement is created. | BRD §7 p.6 | AC-12, AC-13 | Review baseline |
| UG-RULE-034 | Repeated valid callbacks must result in one entitlement and correct, nonduplicated ledger postings. | BRD §7 p.6 | AC-13 | Review baseline |
| UG-RULE-035 | Financial ledger is append-only; refunds, chargebacks and payout reversals create linked correcting entries, not silent edits. | BRD §7 p.6 | AC-14, AC-15 | Review baseline |
| UG-RULE-036 | Teacher earnings derive only from eligible paid enrollments using the approved commission base; reserves/disputes affect payout status. | BRD §7 p.6 | AC-15 | Pending policy OD-03/OD-04 |
| UG-RULE-037 | Partial refunds must reconcile only relevant entitlement and earning portions under the approved policy, not invariably revoke an entire class. | BRD §7 p.6 | AC-14 | Pending policy OD-04 |
| UG-RULE-038 | Refund requests, authorized decisions, provider processing and resulting balance adjustments must be traceable. | BRD §7 p.6, §12 p.9 | AC-14 | Review baseline |
| UG-RULE-039 | Free demo previews cannot be sold as paid products or trigger order, payment attempt or paid entitlement. | BRD §7 p.6 | AC-33 | Review baseline |
| UG-RULE-040 | Payout approval/reconciliation must be auditable; actual gateway payout and recurring capabilities depend on approved provider contracts. | BRD §7 p.6, §14 p.10 | AC-15 | Pending policy OD-04/OD-05 |
| UG-RULE-041 | Exact tuition commission percentage, calculation base, taxes, fees and recognition policy are not fixed. | BRD §14 p.10 | AC-15 | Pending policy OD-03 |
| UG-RULE-042 | XACT paid packs or subscriptions are proposals only; do not activate charges, prices or entitlements until sign-off. | BRD §7 p.6, §14 p.10 | AC-12 | Pending policy OD-13 |

## Must-verify conditions
- Forged/duplicate callbacks cannot activate multiple entitlements.
- Partial refunds produce linked ledger/earning adjustments rather than deleting history.
- Demo preview never creates a payment or entitlement.
- Payout authorization and segregation of duties are enforced where approved.

## Open financial decisions
**OD-03** commission, taxes, revenue base; **OD-04** refunds/disputes/payouts; **OD-05** payment provider, settlement and recurring capability; **OD-13** XACT monetization. Do not hard-code amounts, percentages, processing timelines or guaranteed payouts.
