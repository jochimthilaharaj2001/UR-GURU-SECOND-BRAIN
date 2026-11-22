> **MySQL update (22 Nov 2026):** User selected MySQL 8.4 LTS for engineering planning. Treat SQL Server/PostgreSQL references below as historical alternatives. No physical schema, migration, driver, collation or index design is approved until MySQL-specific tests and OD-20 sign-off. [Alignment details](./TECHNICAL-ARCHITECTURE-BASELINE-2026-11-22.md).

# Database Access, Ownership & Migrations

**Status:** PROPOSED; physical relational engine, naming, ERD v1.2 implementation and migrations **PENDING OD-20**.  
**BRD source:** v6.2.2 pp. 3, 5, 7–8, 11–12, Appendices A/C.

## 1. What is fixed by business rules

| Concept | Required invariant |
|---|---|
| `StudentSubject` | Student-subject-academic-year uniqueness/eligibility; **not** enrollment, payment or entitlement |
| `ClassOffering` + `DemoVideo` | 0..N approved **optional free** previews; no trial booking, watch-gate or demo seat reservation |
| `ClassBatch` + `Enrollment` | Paid enrollment/access governed by verified payment/entitlement and capacity rules |
| Financial ledger | Append-only posting, auditable correcting entries for refunds/chargebacks/settlements |
| XACT content | Rights-approved `QuestionConcept`, separately approved `QuestionTranslation`, immutable `AnswerKeyVersion` |
| XACT attempt | Immutable generated question/option/rules snapshot; durable autosave and server result |
| Teacher assignment | `TeacherPaperVersion`, `Assignment`, `AssignmentRecipient` with separate student attempts |
| Media | Separate `DemoVideo`, `ExplanationVideo`, `MediaAsset`, independent publishing/review control |

Entity names reflect **illustrative ERD v1.2** mappings; they are **not** a confirmed physical DDL.

## 2. Modular data boundaries

- One **logical relational database** is the initial design option; module-owned schemas or clear table naming and separate EF Core contexts are **candidates**, not approved schema.
- A module owns its aggregate business rules and its persistence write surface. Other modules call approved contracts; no cross-module direct `DbContext` or repository reference.
- Cross-module reports use permitted read models/projections with explicit authorization; do not join all tables indiscriminately.
- Shared transactions across tightly-coupled in-process commands may be justified; external providers remain outside the DB transaction. Use outbox and idempotency for eventual effects.

## 3. Representative uniqueness and integrity checks (proposal)

- `StudentSubject(StudentId, SubjectId, AcademicYear)` must prevent duplicate **active** selections. Decide full/filtered unique index and retention semantics during schema sign-off.
- `Enrollment(StudentId, BatchId)` enforces approved duplicate/capacity behavior; capacity uses transaction-safe concurrency controls, not a client-side count.
- Payment external reference + webhook/inbox dedupe key is unique within provider/merchant boundary.
- Attempt final submission idempotency and immutable question/answer snapshot references must prevent duplicate grading.
- Rights approval, medium-specific translation and key version validity are explicit referential checks, not display-name matching.
- Soft deletion/archival vs physical deletion follows legal retention and financial/audit constraints.

## 4. Provider-specific migrations are blocked until OD-20

Existing historical material may use PostgreSQL syntax while development plans mention SQL Server. Do not run mixed SQL or issue incompatible migrations.

Approval sequence:

1. Agree precise data dictionary and ERD v1.2 correction (including DemoVideo replacing trial fields and StudentSubject).
2. Select relational engine, driver, schema namespace, timestamp/timezone conventions, numeric money precision, ID type and collation/localization rules.
3. Baseline and review **module-owned migrations** and constraints with data governance requirements.
4. Add integration tests for constraints, payment dedupe, capacity races, exam snapshot immutability, partial refund and content withdrawals.
5. Test migration against clean DB and **controlled legacy data**. `TrialBooking` history must be archived by policy; never converted to `DemoVideo`.
6. Record migration compatibility/rollback plan and obtain migration approval before staging/production.

## 5. Example persistence interface pattern (not implementation)

```text
Catalogue: SelectStudentSubject(studentId, subjectId, academicYear)
    -> validate launch stream + syllabus/medium eligibility
    -> enforce unique selection
    -> persist StudentSubject
    -> return selection status
    [DO NOT create an Enrollment]

Commerce: ProcessVerifiedGatewayEvent(providerRef, eventId)
    -> authenticate/validate source + idempotency
    -> apply approved financial/enrollment policy
    -> post immutable ledger entries + durable outbox
    -> return processing result
```

## 6. Schema-versioning risks

- Older ERDs, 45-table PostgreSQL SQL and legacy APIs may be **V6.1-era** and conflict with v6.2.2. Mark stale models as historical, do not silently erase them.
- Question translation/answer-key edits cannot mutate previously submitted scores.
- Demo `MediaAsset` must not expose private source keys; public preview delivery is a separate access policy.
- Guardian contact/consent is not a full Guardian account portal by default.

**Next source:** [`../07-DATABASE-DESIGN/`](../07-DATABASE-DESIGN/) for approved physical definitions when ready; [`Module-Contracts.md`](./Module-Contracts.md) for module access boundaries.
