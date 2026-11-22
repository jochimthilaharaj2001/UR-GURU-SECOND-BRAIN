# Legacy 45-table schema vs BRD v6.2.2 — controlled gap analysis

**Inspected sources:** `UR_GURU_A_L_ONLY_V2.dbml` and `UR_GURU_A_L_ONLY_V2_PostgreSQL.sql` in the original Second Brain. Both list **45 physical table declarations**. Old README uses inconsistent entity counts and obsolete absolute `file:///D:/...` links.

| Legacy model observed | v6.2.2 business requirement | Action |
|---|---|---|
| `guardian_profiles`, `student_guardians` model a guardian user account | Guardian **contact + purpose/versioned consent**, no current guardian dashboard | Decide archive/migration; DO NOT imply guardian login (BR-21, OD-15) |
| `bookings`, generic `class_types` and no explicit `DemoVideo` | Optional free prerecorded demo with no trial-booking gate; `ClassOffering`/`ClassBatch` and real paid Enrollment | Replace trial logic with candidate model; preserve legally required legacy records (BR-04/05, AC-07/31/33) |
| `student_subjects` links academic detail/stream | Explicit StudentSubject(StudentId, SubjectId, AcademicYear, Status) and eligibility unique selection | Map keys and academic year semantics before migration (BR-01, AC-32) |
| Generic `assessments`, `assessment_questions`, `student_submissions`, `submission_answers`, `assessment_results` | XACT: five-year sources, rights, canonical concept, medium-specific translations, immutable keys, mock snapshots | Create dedicated approved versioned model; old tables not a substitute (BR-18) |
| No dedicated TeacherPaperVersion, AssignmentRecipient and per-student paper version reference | Teacher issues paper to several individually authorized students | Design versioned paper + assignment + per-recipient record (BR-19) |
| No dedicated `ExplanationVideo` or `DemoVideo` separated by authorization | Free class demos versus moderated XACT explanation content | Separate entities and access/rights status (BR-04/20) |
| `payments`, `payment_transactions`, `refunds`, `teacher_earnings`, etc | Auditable order lines/payment attempts/provider event dedupe/append-only ledger | Full finance reconciliation and immutable journal missing (BR-06) |
| PostgreSQL DDL (`pgcrypto`, `timestamptz`, quoted identifiers) | Engine SQL Server/PostgreSQL undecided OD-20 | Do not execute as chosen database DDL |
| Historic models include 4 streams, or split scientific groupings inconsistently | First release **Bio/Maths only**; others future | Separate master catalogue from launch availability; confirm subject sets (BRD p3) |

## Important

This file is a comparison **not** an automated migration diff and not a claim of 1-to-1 mapping for all 45 legacy rows. Request actual ERD v1.2 file and migration stakeholder approval for final table count, change strategy and retention of protected data. Do not rename legacy files in place or silently claim they match BRD v6.2.2.
