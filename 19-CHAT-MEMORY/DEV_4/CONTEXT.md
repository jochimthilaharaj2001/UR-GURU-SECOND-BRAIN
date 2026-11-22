# DEV_4: Database Specialist (SQL Server / EF Core) — Context & Starter

**Developer ID:** `DEV_4`  
**Role:** Database Developer / DBA  
**Primary Focus:** Relational data architecture, Microsoft SQL Server DDL migrations, Entity Framework Core mappings, index optimization, and concurrency controls.

---

## 1. My Core Responsibilities
- **26 Entities & 9 Modules:** Implement and maintain the normalized schema based on [UR_GURU_ERD_7_CRITICAL_BUGS_FIXED_V2.jpg](../../07-DATABASE-DESIGN/UR_GURU_ERD_7_CRITICAL_BUGS_FIXED_V2.jpg).
- **The 7 Critical Structural Fixes:**
  1. Separate `AdminProfile` from `TeacherProfile`.
  2. Direct `Trial` link to `StudentProfile` and `TuitionClass`.
  3. 5-Option `QuestionOption` (A to E) per `QuestionVersion`.
  4. One `ExamAttempt` per `PaperAssignment` per student.
  5. `PurchaseOrder` handles both `TuitionClass` and `ProductPlan`.
  6. Per-question language medium translations.
  7. History-safe `QuestionVersion` snapshotting.
- **EF Core Scaffolding:** Generate Entity configurations, constraints, composite FKs, and migration scripts.
- **Concurrency & Transactions:** Ensure transactional locking on class seat reservations to avoid overselling (`BR-05`).
- **Audit Trails:** Enforce `AuditLog` captures on sensitive mutations (payouts, refunds, approvals).

---

## 2. Key References I Must Read
1. [`07-DATABASE-DESIGN/README.md`](../../07-DATABASE-DESIGN/README.md)
2. [`07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql`](../../07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql) (45-table reference)
3. [`07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2.dbml`](../../07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2.dbml)
4. [`16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md`](../../16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md)
5. [`02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)

---

## 3. AI Starter Prompt (Copy-paste this when starting a new session)
```markdown
I am DEV_4 (Database Developer) working on the UR GURU Microsoft SQL Server relational database.
Workspace: D:\Unicom\UR_GURU_finalProject
Please read my context file:
UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_4\CONTEXT.md
And our 26-entity ERD documentation:
UR-GURU-SECOND-BRAIN\07-DATABASE-DESIGN\README.md

Today I am creating/optimizing [TABLE / MIGRATION / EF CORE CONFIG / QUERY].
Ensure all tables follow clean PK/FK constraints, proper indexing, transactional isolation, and strict A/L curriculum boundaries.
```

---

## 4. My Daily Work Log
Record daily activities in `WORK-LOG-YYYY-MM-DD.md`.
Log any schema modifications or index changes in `../SHARED-DECISIONS/CROSS-TEAM-LOG.md`.
