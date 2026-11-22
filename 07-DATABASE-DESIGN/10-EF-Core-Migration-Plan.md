# EF Core migrations / schema generation — blocked until OD-20

**Do not run the legacy `UR_GURU_A_L_ONLY_V2_PostgreSQL.sql` against a new or production database.** The old file targets PostgreSQL and predates v6.2.2 optional-demo/XACT requirements.

## Proposed sequence

1. Get stakeholder approval of BRD v6.2.2 scope and technical OD-20: exact database engine, runtime, naming, collation, ID/time/money representation.
2. Approve canonical ERD v1.2 mapping and identify exact physical table/column types, required/nullable and stable keys.
3. Confirm data classifications, consent/retention, rights and finance audit requirements.
4. Choose EF Core provider and review compatibility; define module-owned `DbContext` boundaries (or approved single context with owned schemas) **within one modular-monolith backend deployable**.
5. Generate baseline migration from approved model **into a disposable empty database first**.
6. Add foreign-key/unique/index checks; use filtered uniqueness only with selected provider's correct syntax.
7. Run concurrency and idempotency integration tests on actual provider. Test student subject duplicates, seat-capacity races, order/webhook retries, key immutability, assignment authorization, partial refund, and demo watch-or-skip.
8. Plan legacy transition: classify old trial/guardian/assessment data, retention/legal archive, backfill; no mechanical TrialBooking→DemoVideo conversion.
9. Document forward migration, reversible operations, backups/restore, data reconciliation and release gate. Have migration reviewed before staging/production.

## Suggested project migration ownership (illustrative)

- Identity/Catalogue: R0 migrations; controlled academic seeds **only Bio/Maths launch flags**.
- Marketplace/Media/Commerce: R1 changes; signed provider integrations staged separately.
- XACT Content/Assessments/Assignments: R2; immutable versioned question base and attempt engine.
- Operations: Outbox, notifications, audit/safety from R0 onward.

**Do not run `dotnet ef database update` against shared/prod environments until approval and tested rollback.** No completed or runnable EF migration is claimed by this pack.
