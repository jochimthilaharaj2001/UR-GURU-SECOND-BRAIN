# UR GURU — 104 API MVP Second Brain Alignment
Date: 22 November 2026

## Verified inventory
- Active API register: **104 endpoint rows**, **15 modules**.
- Per-API Markdown files: **104 / 104** present.
- Historical `11-SPRINT-AND-TASKS/Product-Backlog.csv`: **292 rows** (retained, not active).
- Active backlog: `11-SPRINT-AND-TASKS/ACTIVE-MVP-104-API-BACKLOG.csv` (104 rows).

## Changed
- Added active MVP scope notices to root, architecture, technical, database, UI, business rules, testing and sprint README files.
- Added 104-row active backlog, with owner and DTO approval explicitly pending.
- Preserved historical specifications and BRD without rewriting facts.

## Still requires human engineering review
1. Confirm 104 endpoint coverage against BRD R0/R1/R2 requirements and 33 UAT checks. **104 APIs do not automatically satisfy the full BRD**.
2. Complete request/response DTOs, error/status contracts, RBAC, object-level permissions and database mappings.
3. Verify screen-to-API mapping against actual prototype and mark unsupported flows.
4. Confirm ERD/migrations, transaction boundaries, gateway webhook idempotency, LiveKit authorization, XACT scoring snapshots and data retention.
5. Approve community/forum scope separately: BRD v6.2.2 does not expressly specify it.
6. Obtain pending BRD OD-01–OD-20 approvals and release decisions.

## Authority
BRD v6.2.2 is the full business baseline. 104 APIs are a reduced *implementation planning* baseline, not a replacement BRD or proof of feature completeness.

## Archive handling
Older references to 292, 469 or 521 APIs and old sprint allocations remain as historical records. Do not use them as the active build list.
