# Data design approval gates — OPEN

| Decision | Why database work is blocked | Evidence to obtain |
|---|---|---|
| OD-20 — relational engine, ERD v1.2, schema conventions | Cannot safely issue SQL Server/PostgreSQL migrations; source ERD v1.2 physical DDL is not provided | Chosen engine/provider, signed logical & physical ERD, nullability, indexes |
| OD-02 — demo rights, publishing/public access | Public-preview authorization, data retention and viewer analytics unresolved | Signed demo access/moderation policy |
| OD-03/04/05 — commission, refunds, provider | Monetary schema, idempotency, payouts and ledger posting rules not fully determined | Finance policy + provider callback/settlement contract |
| OD-07/08/09/10/11 — question rights/content/scoring | Which version/medium is allowed, mark/timer/retake policies | Academic and legal sign-off |
| OD-12/13 — teacher videos and XACT monetization | Rights/payment linkage for videos and entitlements pending | Signed creator contracts / product pricing |
| OD-15/19 — guardian, minors, NIC | Consent evidence, identity retention and restricted PII | Legal approval/retention schedule |
| OD-16/18 — release dates and R1/R2 order | Seed/migration sequencing and environment strategy depends on release | PM/Sponsor release decision |

## Schema design checklist (for approvers)

- [ ] Entity list validated against canonical v1.2 ERD, scope, table count and actual DTOs
- [ ] Every table has owner, PK, FK, unique, nullability, indexes, data classification and retention
- [ ] StudentSubject/Enrollment separation & demo optionality tested
- [ ] No trial booking constraints or guardian portal assumptions
- [ ] Medium-wise XACT key approval, immutable snapshot and answer correction model signed
- [ ] Payments and refunds reconcile with approved append-only ledger policy
- [ ] Engine/provider selected; baseline migrations generated and reversible
- [ ] Authorized UI/teacher/admin scope and consent requirements covered in tests

**Decision status:** Pending. This pack does not mark any OD item as closed or any new entity name as officially adopted.
