# Technical Decisions & Implementation Gates

**Status:** Open decisions register for 04 section. **Not proof of approval.**  
**Canonical decisions:** BRD v6.2.2 §14, OD-01–OD-20; this file lists technical impacts, not substitute sign-off.

## 1. Required sign-off before implementation choices become mandatory

| BRD decision | Technical implication | Owner specified by BRD | Status |
|---|---|---|---|
| **OD-20** | Modular Monolith vs other topology; frontend/backend frameworks, SQL engine, physical ERD/migrations, environments | Engineering / Sponsor | **PENDING** |
| **OD-18** | Marketplace-first R1 vs XACT pilot/alternate release order | Sponsor / Product Owner | **PENDING** |
| **OD-02** | Demo rights/public access/login policy/length/review SLA/analytics consent | Product / Legal / Operations | **PENDING** |
| **OD-05** | Gateway, merchant/callback protocol, supported refunds/recurring/payout reconciliation | Finance / Engineering | **PENDING** |
| **OD-06** | Live class, VOD/CDN, recording and operational/cost constraints | Engineering / Product / Finance | **PENDING** |
| **OD-15** | Minor and guardian consent, PDPA/retention rules | Legal / Safeguarding | **PENDING** |
| **OD-19** | NIC necessity, actual government verification route and alternatives | Product / Legal | **PENDING** |
| **OD-16** | Staffing, environments/cloud spend, benchmark SLO, DR targets | Sponsor / PM / Engineering | **PENDING** |
| **OD-07–11** | XACT past-paper rights, translations, academic approval, scoring and timers | Legal / Academic / Product | **PENDING** |
| **OD-03/04/12/13** | Commission/refund/teacher video payments and optional XACT pricing | Sponsor / Finance / Legal | **PENDING** |

## 2. Safe engineering work before gates close

- Organize documentation, source inventory, ADR proposals and module ownership diagrams.
- Draft proof-of-concept services against fake/test gateways and synthetic data.
- Establish basic coding/quality guidelines and test architecture.
- Validate multilingual rendering and browser responsiveness using synthetic content.
- Implement **no production migration/payment policy/identity legal process** on an invented decision.

## 3. Approval record template

```text
Decision ID:
Title:
BRD / requirement link:
Options considered:
Final decision / approved scope:
Approver name and role:
Approval date and effective date:
Contracts/policies and version:
Implementation + migration impact:
Risks and fallback:
Related API/DB/test modifications:
```

## 4. Current inconsistencies to reconcile

1. Older V6.1 docs refer to **Exam Munnodi**, 4 streams and **live trials**; current v6.2.2 uses **XACT**, **Bio/Maths first** and **free optional prerecorded demos**.
2. Older physical SQL may use **PostgreSQL** while task plans discuss **SQL Server**; resolve in OD-20 before migrations.
3. Proposed ERD v1.2 (DemoVideo and StudentSubject) is **not** an approved physical DDL; cross-map with API/DB documentation.
4. Unapproved payment provider/commission/refund values must not appear as finalized implementation rules.
5. API inventory may be stale; no auto-generated route contract should claim a production endpoint until API review.

## 5. How to approve and update Second Brain

1. Create a dated Architecture Decision Record (ADR) under [`../13-DECISION-LOG/`](../13-DECISION-LOG/).
2. Update [`Technology-Stack.md`](./Technology-Stack.md) and affected documents with approved values.
3. Update [`../03-SYSTEM-ARCHITECTURE/`](../03-SYSTEM-ARCHITECTURE/) and [`../07-DATABASE-DESIGN/`](../07-DATABASE-DESIGN/) diagrams and contracts.
4. Update [`../08-API-DOCUMENTATION/`](../08-API-DOCUMENTATION/) and [`../12-TESTING/`](../12-TESTING/) and make traceability explicit.
5. Only then prepare/apply code changes with review and tests.

**Remember:** This folder is a **technical proposal**. It does not amend BRD V6.2.2 or grant product/legal sign-off.
