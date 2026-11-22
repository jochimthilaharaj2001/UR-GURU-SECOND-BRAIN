# Database baseline, scope, and evidence

**Status:** DESIGN PROPOSAL; stakeholder sign-off pending. **Date:** 19 Nov 2026.

## Verified from BRD v6.2.2

- **p1, p3:** Bio/Maths are the initial A/L streams; native apps, Commerce, Arts and Technology not in first release.
- **pp3, 5, 8, 12:** `StudentSubject` is a persistent academic selection independent of paid `Enrollment`.
- **pp5, 8, 12:** `DemoVideo` linked to `ClassOffering` and media is optional and free; no `TrialBooking`, trial seat, trial attendance or demo-to-payment prerequisite.
- **p6:** order line/payment attempts, server-verified callbacks, append-only ledger, partial refunds, earnings/payouts.
- **pp6–7:** XACT canonical question concepts, separately approved translations, immutable answer-key versions, autosaved server-scored attempts, per-student assignments and two different kinds of videos.
- **pp7–8:** media rights, consent, private resources, version retention and operational audit.
- **p11 Appendix A:** illustrative entity names and module mapping. **p11 OD-20:** database/ERD/technology decision remains open.

## Source precedence

1. Approved/controlled signed-off BRD + actual approved decisions (not available yet).
2. **BRD v6.2.2 consolidated corrected REVIEW CANDIDATE** as current working baseline.
3. Section 03/04 architecture **proposals**, not vendor or DDL approval.
4. Old V6.1/45-table SQL/old ERD only as historical reference. They may conflict.

## Provisional design convention

Proposed logical entity names in PascalCase. Surrogate `Id` columns shown as candidate UUIDs. `timestamp` in DBML means intended UTC instant; exact physical type/precision, names, collations and money storage await OD-20. Columns generated here are **not** a final authoritative table specification. Proposed relationships indicate intended logical ownership, not always suitable FK implementation across bounded contexts.

**Boundary:** No new Student/Teacher/Admin portal roles are implied by `AcademicReviewer`/`FinanceReviewer`; they are permission sets. Guardian is contact and conditional consent, not a dashboard/account by default.

**Not modeled as release-committed:** Future Commerce/Arts/Technology rollout, native apps, AI tutoring/notes/transcription, institution portal or Guardian dashboard, XACT monetization without OD-13 sign-off.
