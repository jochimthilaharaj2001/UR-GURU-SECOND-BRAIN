# Class Payment, Entitlement, Refund and Payout Journeys

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

**Primary sources:** BRD §7 p. 6; §6.4 pp. 5–6; §12 SJ-05/SJ-08 p. 9; AC-08, AC-12–15, p. 9. **Requirements:** BR-05, BR-06, BR-14, BR-24.

## SJ-05 — Paid enrollment

1. Student selects an eligible `ClassBatch`; demo is wholly optional.
2. Checkout discloses agreed class/course description, total, currency, charges, access period and **approved** cancellation/refund terms.
3. System creates a traceable order with line items and handles seat availability transactionally; no duplicate paid enrollment or overbooking.
4. User follows provider checkout (the **provider is not selected** under OD-05).
5. **Backend** verifies authenticated gateway callback/status and performs retry-safe, idempotent state change. Client redirect alone does **not** prove success.
6. Verified eligible payment activates the appropriate class entitlement and enrollment/join access under approved policy.
7. Financial ledger records gross tuition transaction (GMV) separately from platform-recognized commission/revenue.

**State examples (illustrative, not approved DTO enums):** OrderPending → PaymentPending → VerifiedPaid / Failed / Cancelled / ReconciliationRequired. Do not hardcode without approved contracts.

**Exceptions:** Full capacity, concurrent reservations, canceled/failed provider interaction, forged callback, delayed webhook, duplicate webhook, paid response with unconfirmed seat, mismatch requiring support. No duplicate entitlement or ledger postings.

## SJ-08 — Refund and dispute

1. Student or authorized support submits request with original purchase reference and reason.
2. Finance/operations checks payment history, applicable line items, eligibility and **approved** refund/partial-refund policy.
3. Authorized decision (approve, decline, request information, dispute hold) is audited with reviewer/reason.
4. Where approved and provider-capable, issue refund through selected gateway; handle asynchronous acknowledgement and retries.
5. Add correcting **append-only** ledger entries referencing original financial events. Update only relevant entitlements/earnings for partial refund according to policy.
6. Inform affected student/teacher/finance using privacy-safe notifications and reconcile settlement/payout impacts.

**Exceptions:** Partial amount, failed provider refund, gateway outage, duplicate request, chargeback, earnings held due to dispute, unsettled provider transaction. Never silently edit ledger balances or promise an automatic refund.

## Teacher earnings and payout oversight

Earnings derive from eligible paid enrollment and an **approved** commission base. Reserves, refunds and disputes alter payout eligibility; finance controls approval. GMV is not equal to platform revenue. Exact rates, payout cadence and tax rules are OD-03/04.

## Required QA outcomes

- AC-08 concurrent seat/idempotent enrollment.
- AC-12 forged gateway notice cannot grant access.
- AC-13 repeated valid notice leads to one entitlement and correct ledger posting.
- AC-14 partial/full refund ties back to original line items and cannot duplicate reversal.
- AC-15 payout matches approved commission/dispute holds.

## Open decisions that block final behavior

OD-03 commission/tax; OD-04 refund/disputes/payout; OD-05 provider and supported capabilities; OD-06 live provider; OD-13 proposed future XACT monetization. **Do not assume XACT subscription is live.**
