# Business Rule Decision Gates

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Pending decisions (BRD §14 pp.10–11)

All entries below are **open / PENDING APPROVAL**, not implied decisions. No fixed financial amounts, thresholds, timers, SLA values or providers should be asserted in implementation contracts.

| Decision | Subject requiring approval | Named role / owner | Impact |
|---|---|---|---|
| OD-01 | Teacher evidence and screening policy | Product / Legal / Operations | StudentTeacher |
| OD-02 | Demo rights/ownership, upload/approval SLA, public preview access, free availability, duration/count policy and optional analytics/consent | Product / Legal / Operations | Marketplace / PrivacyContent |
| OD-03 | Commission rate/base, taxes, charges and revenue recognition | Sponsor / Finance | Finance |
| OD-04 | Refund/partial refund, dispute, earnings and payout policy | Finance / Legal | Marketplace / Finance |
| OD-05 | Payment provider, settlement, callbacks, recurring capability and quotation | Finance / Engineering | Finance |
| OD-06 | Live classroom, prerecorded demo and video/CDN provider, recording policy and cost envelope | Engineering / Product / Finance | Marketplace |
| OD-07 | Question reproduction/translation, adaptation and teacher video rights | Legal / Academic | XACT / PrivacyContent |
| OD-08 | Five-year inventory by subject/topic/language/diagram coverage | Academic Lead | XACT |
| OD-09 | Academic key reviews, video QA and correction/regrade SLA | Academic Lead | XACT |
| OD-10 | Mock timers, marks, attempt limit, negative marks, expiration and answer reveal | Academic / Product | XACT |
| OD-11 | Difficulty/topic quotas and translated-option QA | Academic | XACT |
| OD-12 | Teacher explanation-video pay, ownership, withdrawal and revenue share | Finance / Legal | XACT |
| OD-13 | XACT free allowance, packs/subscriptions and prices | Sponsor / Finance | XACT / Finance |
| OD-14 | Future native apps, institutions and teacher Pro | Sponsor / Product | Out of launch scope |
| OD-15 | Minor thresholds, guardian permissions, PDPA and retention | Legal / Safeguarding | PrivacyContent |
| OD-16 | Staffing, release dates, cloud budget, capacity and NFR SLA | Sponsor / PM / Engineering | Operations |
| OD-17 | Brand XACT and Bio/Maths first; later streams | Product Owner | StudentTeacher / XACT |
| OD-18 | R1/R2 live order versus current XACT pilot | Sponsor / Product Owner | Release sequencing |
| OD-19 | NIC necessity, official verification route, alternatives and retention | Product / Legal | StudentTeacher / PrivacyContent |
| OD-20 | Final web/backend/database choices, target environments and ERD v1.2 schema approval | Engineering / Sponsor | Architecture & implementation |

## Control procedure
1. Record decision ID, chosen option, approving person/role, effective date, approved policy/version and relevant evidence.
2. Evaluate implementation impact on BRD, business rules, architecture, API, database and UAT.
3. Update this folder only after formal decision; preserve prior versions and history.
4. Mark affected rules and related tests as **approval-required** until resolved.
