# 08-API-DOCUMENTATION — UR GURU MVP

**Tracker baseline:** 104 endpoints in 15 modules.  
**BRD baseline:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf` (review candidate, not signed).  
**Status:** Documentation scaffold / DTO contracts unapproved.

## How to use

1. Start at [API-MASTER-INDEX.md](API-MASTER-INDEX.md).
2. Each module directory contains one Markdown document per tracker API ID.
3. Preserve API IDs, methods, paths and feature labels from tracker; do not rename without change control.
4. Backend lead finalizes exact request/response DTOs, authorization, persistence, integration and UAT links before development sign-off.
5. Add UI prototype screenshots only after actual screen mapping verification.

## Scope and warnings

- **Community** endpoints are in the tracker, but BRD v6.2.2 does not expressly define a community forum as a functional requirement. Treat as an MVP scope exception requiring approval.
- **DemoVideo** is free, optional, prerecorded and never a live trial booking or paid-access gate.
- **StudentSubject** selection is not a paid Enrollment or Entitlement.
- **NIC** format checks do not constitute official identity verification.
- The BRD's 20 open decisions, ERD approval and specific contract details must be resolved before marking documentation implementation-ready.
- Tracker-specific product choices (e.g., batch size or payment vendor) must be reconciled against signed business decisions.

## Deliverables

- `104` individual API documents
- `API-MASTER-INDEX.md`
- `API-REGISTER.csv`
- `CONTRACT-APPROVAL-CHECKLIST.md`
