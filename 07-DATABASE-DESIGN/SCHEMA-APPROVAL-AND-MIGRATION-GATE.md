# Database implementation readiness — BRD v6.2.2

**Status: NOT APPROVED FOR PRODUCTION MIGRATION.** Existing DBML, column dictionary, table inventory and diagrams are design inputs, not executable EF Core migration evidence.

## Required sign-off sequence
1. Choose PostgreSQL or SQL Server, version, collation and backup policy (OD-20).
2. Reconcile actual entities and keys with BRD Appendix A, especially StudentSubject (unique student/subject/academic-year active selection), DemoVideo (0..N per ClassOffering), MediaAsset and entitlement rules.
3. Remove **active** TrialBooking, TrialAvailable, TrialCapacity and Enrollment.TrialId references; archive legacy records only under approved retention policy.
4. Model immutable QuestionConcept/QuestionTranslation/AnswerKeyVersion and exam snapshot, assignment version, append-only ledger, webhook idempotency, outbox and audit history.
5. Produce reviewed provider-specific EF Core migrations, rollback/restore drill, migration tests and seed data. Record approver, date, migration hash and PR.

**No executable migrations were fabricated as part of this documentation correction.**
