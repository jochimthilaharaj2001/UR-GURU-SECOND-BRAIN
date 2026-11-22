> **HISTORICAL AUDIT — SUPERSEDED 22 NOV 2026.** See root `SECOND-BRAIN-CORRECTION-AUDIT-2026-11-22.md`.

# UR GURU — Second Brain: Full ZIP Content Audit
**Audited:** 18 November 2026  
**Input:** `UR-GURU-SECOND-BRAIN.zip`  
**Scope:** This is a source-content/documentation consistency audit, not an execution test of the application, an external legal opinion, or proof of production readiness.

## 1. Verified archive inventory
- **65 files** across **19 top-level modules**; archive data is approximately 9.58 MiB uncompressed.
- Contents: 41 Markdown, 7 CSV, 7 SVG, 2 JPG, 2 HTML, 1 each PDF, DOCX, XLSX, SQL, DBML and PNG.
- The BRD PDF was text-extracted and 15 pages rendered for visual overview; DOCX rules extracted including tables; Excel sheets examined; SQL/DBML and SVG entity labels inspected; both HTML prototypes analyzed, including decoded embedded Student/Teacher/Admin UI payloads.

## 2. Confirmed positive coverage
- A/L Grade 12–13 scope, student/teacher/admin roles and responsive-web direction are documented in BRD, root readme and project memory.
- Corrected BRD V6.1 has 21 functional requirement records and 20 acceptance criteria, with C-01 to C-07 concerns explicitly discussed, but is *not signed off*.
- Business Rules V2.0 DOCX enumerates BR-001 to BR-077 (with BR-076/077 presented out of numerical order).
- Exam Munnodi specification covers approved question selection, mock attempts, versioned scoring, video approvals, teacher paper assignment and result boundaries.
- API workbook includes an explicit Change Log and a Deferred Guardian APIs sheet; documentation maintains open decisions OD-01 to OD-16.
- Six role-based developer context folders plus shared blockers/decision protocols exist.

## 3. High priority corrections with evidence
### 1. [CRITICAL] Approval/source authority
**Evidence:** `02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md` and its PDF say corrected review draft / not approved; `15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md`, `19-CHAT-MEMORY/DEV_1/WORK-LOG-2026-11-17.md` and `18-SOURCES/SOURCE_REGISTRY.md` use official/ratified/governing language. Chat memory should not outrank approved signed decisions.

**Required action:** Mark V6.1 *Working Review Baseline* until signed off; define approved-document precedence, owners and decision record.

### 2. [CRITICAL] ERD counting mismatch
**Evidence:** `07-DATABASE-DESIGN/README.md` repeatedly says *26 entities* but its 9-module catalog explicitly names **38 distinct entities**. Separate PostgreSQL SQL and DBML each define **45 tables**, a different older model.

**Required action:** Count and version the conceptual model correctly; choose a single approved logical/physical database model and document mapping.

### 3. [CRITICAL] Guardian role still in physical schema
**Evidence:** `07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql` defines `guardian_profiles`, `student_guardians` referencing account entities, and seeds GUARDIAN role; latest BRD limits guardian to contact/consent touchpoints with no active guardian portal.

**Required action:** Revise SQL/DBML to the decided guardian contact/consent model only after policy approval; update screens and roles.

### 4. [CRITICAL] Exam Munnodi physical schema absent
**Evidence:** BRD V6.1 asks canonical `QuestionConcept`, `QuestionTranslation`, versioned answer key, mocks, paper assignments, video explanations and entitlements; SQL has only generic `assessments`, `assessment_questions`, `student_submissions`, `submission_answers`, `assessment_results`.

**Required action:** Write approved domain model including medium- and version-aware question tables, individual assignment/attempt history, approvals, entitlements and migrations.

### 5. [HIGH] Database engine mismatch
**Evidence:** The only provided DDL is explicitly PostgreSQL (`gen_random_uuid`, `timestamptz`); BRD, DEV_4 and task plan target Microsoft SQL Server / EF Core. `T4-01` incorrectly asks to run a 26-entity DDL on SQL Server.

**Required action:** Approve database engine; create matching SQL Server EF Core migration or approve PostgreSQL and update tasks.

### 6. [HIGH] Stream catalogue inconsistent
**Evidence:** BRD uses **four core streams** (Science, Commerce, Arts, Technology); SQL seeds **five rows** (`Physical Science`, `Biological Science`, `Commerce`, `Arts`, `Technology`).

**Required action:** Define whether science subdivisions are stream groups/substreams and align schema, UI, APIs and seed data.

### 7. [HIGH] API totals wrong in multiple documents
**Evidence:** `08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx` has 168 populated API Register V6 rows (157 carried + 11 proposed), 7 separate deferred guardian rows. Root README, team memory and change log claim 161 active.

**Required action:** Reconcile 168 proposed/non-deployed endpoints versus 7 deferred, then freeze/approve the active contract. Add request-response/error schemas and OpenAPI.

### 8. [HIGH] Unapproved refund rules presented as facts
**Evidence:** `16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md` specifies 7-day teacher-cancellation window, 24h student cutoff, <2h no-refund and >50% disruption thresholds. BRD V6.1 `OD-04` explicitly holds refunds/cancellation policies open. The finance doc labels its architecture Approved.

**Required action:** Mark these examples as unapproved proposals, remove automatic workflow assumptions and seek Finance/Product/Legal approval.

### 9. [HIGH] Acceptance-criterion IDs clash
**Evidence:** `17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md` maps AC-03 to question bank, AC-04 to topic mock, AC-07 to shortage, AC-08 to grading. In BRD V6.1 AC-03 is teacher discovery, AC-04 trial, AC-07 payment and AC-08 refund/payout.

**Required action:** Rebuild feature-to-BRD AC map using V6.1 IDs. Use clearly distinct rule IDs: functional BR-01..21 versus business BR-001..077.

### 10. [HIGH] Design prototypes out of scope/incomplete
**Evidence:** `06-UI-UX-DESIGN/MergedScreens2.html` decoded metadata contains **78 student / 37 teacher / 22 admin screens** (137 listings). On-screen marketing text claims 77 student and 139 total. The admin prototype offers active Guardian account-management sample data; neither HTML has an explicitly named *Exam Munnodi* feature. Both are local demo prototypes, not live applications.

**Required action:** Create real screen inventory, remove/defer Guardian modules, add Exam Munnodi dedicated flows and validate every screen against BRD.

### 11. [HIGH] Missing developer instructions and critical content
**Evidence:** No root `AGENTS.md`; folders `01`, `03`, `04`, `10`, `12`, `14` contain only README checklists; the traceability, journey mapping, screen inventory, backlog, test-case, decisions, bugs CSV files have headers only.

**Required action:** Create AGENTS.md, architecture, guidelines, test strategy, deployment files and evidence-based mapping rows. Do not invent gaps.

### 12. [MEDIUM] Nonportable links and unavailable source artifacts
**Evidence:** Five Markdown links use `file:///D:/Unicom/...` and fail outside a single machine. `18-SOURCES/SOURCE_REGISTRY.md` references an external student screen JSON and UI theme docx not included in this archive and a differently named API workbook. Two ERD JPG files have identical SHA256.

**Required action:** Use relative links; mark missing external source references, reconcile filenames and remove redundant duplicate after confirming references.

### 13. [HIGH] Timeline conflicts with staged scope
**Evidence:** BRD Phase 1 is marketplace and Phase 2 is Exam Munnodi. `11-SPRINT-AND-TASKS/12-DAY-MILESTONE-PLAN.md` expects both plus 20 UAT criteria in release candidate by 29 Nov 2026; `13-DECISION-LOG` explicitly says 30 Nov aspirational, no signed SLA; history cites 3–5 developers while task plan allocates six.

**Required action:** Approve team capacity, MVP scope and realistic milestone gates before marking date committed.

### 14. [MEDIUM] QA success not demonstrated by bundled tests
**Evidence:** `15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md` says 27/27 Playwright checks passed on a previous UI, but this ZIP includes no Playwright test source or run artifact; `12-TESTING/Test-Case-Register.csv` is empty.

**Required action:** Label result historical/unverified by this bundle until test scripts, reports and run evidence are attached.

### 15. [MEDIUM] Mixed question option representation
**Evidence:** BRD/ERD narrative standardizes A/L MCQs at five options (A-E); `17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md` defines `options_json` with **4 or 5** options.

**Required action:** Define accepted option cardinality per syllabus/exam configuration and update data/API/UI constraints consistently.

## 4. Folder-level readiness
- **01 PROJECT OVERVIEW:** Checklist only. Project overview documents missing; root has a synopsis.
- **02 BRD & REQUIREMENTS:** Substantive / unapproved. BRD V6.1 PDF/Markdown present, traceability CSV empty.
- **03 SYSTEM ARCHITECTURE:** Checklist only. No provided architecture design/flow diagram in this ZIP folder.
- **04 TECHNICAL ARCHITECTURE:** Checklist only. No backend/frontend/security architecture specifications.
- **05 USER JOURNEYS:** Checklist only. Journey mapping CSV empty, though UI bundles contain embedded journeys.
- **06 UI/UX:** Demo assets present. Two HTML prototypes, no approved inventory or production component library.
- **07 DATABASE:** Conflicting models. 38 named entities incorrectly called 26 vs 45-table old physical model; backend target mismatch.
- **08 API:** Inventory only. 168-row proposed endpoint workbook, no OpenAPI or DTO/error contracts.
- **09 BUSINESS RULES:** Substantive / proposed. 77 rules in DOCX, still awaiting cross-version mapping/approvals.
- **10 DEVELOPMENT GUIDELINES:** Checklist only. No coding standard, repo policy, local setup or AGENTS.md.
- **11 SPRINT & TASKS:** Substantive / unapproved. 12-day schedule and six assignments, product backlog CSV empty.
- **12 TESTING:** Checklist only. Only README and empty test-case CSV, no executable tests.
- **13 DECISION LOG:** Substantive / unresolved. 14 ADR claims and OD-01..16, register CSV empty.
- **14 DEPLOYMENT:** Checklist only. No CI/CD/backup/runbook/configuration artifact.
- **15 ISSUES & CHANGELOG:** Substantive / claims unverified. Historical narrative, bug CSV empty, test evidence absent.
- **16 FINANCE:** Substantive / approval conflict. Ledger concepts useful, but proposed refund thresholds presented as established.
- **17 EXAM MUNNODI:** Substantive / version mismatch. Functional blueprint exists; AC references outdated vs BRD V6.1.
- **18 SOURCES:** Substantive / inaccuracies. Sources hierarchy gives memory undue authority; external Windows paths and missing assets.
- **19 CHAT MEMORY:** Useful context / not authoritative. 6 developer context folders and shared logs; fixed machine paths, unverified approval claims.

## 5. Minimal safe execution order for Codex
1. Import this audit as evidence, preserve all original source files, and create root `AGENTS.md` plus an approval-aware source hierarchy.
2. Reconcile approved BRD, functional IDs, business rule IDs and all 20 ACs; register conflicts instead of silently deciding.
3. Choose the relational database engine and define a single coherent Exam Munnodi + live class + guardian-safe data model. Generate proposed migrations only after approval.
4. Reconcile 168 API candidates and 7 deferred guardian endpoints; derive formal OpenAPI contracts from approved requirements.
5. Decode existing UI metadata into a real screen inventory; mark demo-only, out-of-scope and missing exam screens.
6. Populate traceability and user journey CSVs from verified sources; draft developer standards, deployment/testing strategies.
7. Run Markdown relative-link and consistency checks. Record missing source artifacts and approvals.
8. Then select one end-to-end vertical slice for implementation; do not claim all phases are ready.

## 6. Exact archived file inventory
- `01-PROJECT-OVERVIEW/README.md` — 1,431 bytes
- `02-BRD-AND-REQUIREMENTS/README.md` — 1,460 bytes
- `02-BRD-AND-REQUIREMENTS/Requirements-Traceability.csv` — 82 bytes
- `02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1.pdf` — 109,652 bytes
- `02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md` — 39,881 bytes
- `03-SYSTEM-ARCHITECTURE/README.md` — 1,384 bytes
- `04-TECHNICAL-ARCHITECTURE/README.md` — 1,400 bytes
- `05-USER-JOURNEYS/Journey-Screen-Mapping.csv` — 76 bytes
- `05-USER-JOURNEYS/README.md` — 1,469 bytes
- `06-UI-UX-DESIGN/MergedScreens2.html` — 8,819,863 bytes
- `06-UI-UX-DESIGN/README.md` — 1,383 bytes
- `06-UI-UX-DESIGN/Screen-Inventory.csv` — 87 bytes
- `06-UI-UX-DESIGN/UR_GURU_Admin_Web_Only_Updated.html` — 252,906 bytes
- `07-DATABASE-DESIGN/README.md` — 8,030 bytes
- `07-DATABASE-DESIGN/TABLE-SPEC-TEMPLATE.md` — 431 bytes
- `07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2.dbml` — 10,712 bytes
- `07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql` — 17,367 bytes
- `07-DATABASE-DESIGN/UR_GURU_ERD_7_CRITICAL_BUGS_FIXED.jpg` — 99,197 bytes
- `07-DATABASE-DESIGN/UR_GURU_ERD_7_CRITICAL_BUGS_FIXED_V2.jpg` — 99,197 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_01_Users_Roles.svg` — 27,165 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_02_A_L_Academic_Verification.svg` — 29,438 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_03_Courses_Classes_Bookings.svg` — 34,153 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_04_Payments_Refunds_Payouts.svg` — 29,485 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_05_Assessments.svg` — 19,745 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_06_Communication_Admin.svg` — 25,920 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_BRD_Scope_Review.md` — 3,498 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_Full_45_Tables.svg` — 192,237 bytes
- `07-DATABASE-DESIGN/UR_GURU_V2_Module_Overview.png` — 53,165 bytes
- `08-API-DOCUMENTATION/API-ENDPOINT-TEMPLATE.md` — 434 bytes
- `08-API-DOCUMENTATION/README.md` — 1,497 bytes
- `08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx` — 16,724 bytes
- `09-BUSINESS-RULES/README.md` — 1,446 bytes
- `09-BUSINESS-RULES/UR_GURU_Business_Rules_V2_0.docx` — 41,579 bytes
- `10-DEVELOPMENT-GUIDELINES/README.md` — 1,396 bytes
- `11-SPRINT-AND-TASKS/12-DAY-MILESTONE-PLAN.md` — 9,600 bytes
- `11-SPRINT-AND-TASKS/Product-Backlog.csv` — 95 bytes
- `11-SPRINT-AND-TASKS/README.md` — 1,427 bytes
- `11-SPRINT-AND-TASKS/Task-Assignment.md` — 7,149 bytes
- `12-TESTING/README.md` — 1,403 bytes
- `12-TESTING/Test-Case-Register.csv` — 91 bytes
- `13-DECISION-LOG/Business-Decision-Register.csv` — 76 bytes
- `13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md` — 7,851 bytes
- `13-DECISION-LOG/OPEN-DECISIONS-STARTER.md` — 1,208 bytes
- `13-DECISION-LOG/README.md` — 1,157 bytes
- `14-DEPLOYMENT/README.md` — 1,383 bytes
- `15-ISSUES-AND-CHANGELOG/Bug-Tracker-Export.csv` — 88 bytes
- `15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md` — 7,808 bytes
- `15-ISSUES-AND-CHANGELOG/README.md` — 1,223 bytes
- `16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md` — 5,517 bytes
- `17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md` — 10,177 bytes
- `18-SOURCES/SOURCE_REGISTRY.md` — 4,330 bytes
- `19-CHAT-MEMORY/CONSOLIDATED_PROJECT_MEMORY_2026-11-17.md` — 9,952 bytes
- `19-CHAT-MEMORY/DEV_1/CONTEXT.md` — 2,958 bytes
- `19-CHAT-MEMORY/DEV_1/WORK-LOG-2026-11-17.md` — 2,102 bytes
- `19-CHAT-MEMORY/DEV_2/CONTEXT.md` — 2,501 bytes
- `19-CHAT-MEMORY/DEV_3/CONTEXT.md` — 2,740 bytes
- `19-CHAT-MEMORY/DEV_4/CONTEXT.md` — 2,701 bytes
- `19-CHAT-MEMORY/DEV_5/CONTEXT.md` — 2,966 bytes
- `19-CHAT-MEMORY/DEV_6/CONTEXT.md` — 2,569 bytes
- `19-CHAT-MEMORY/README.md` — 4,229 bytes
- `19-CHAT-MEMORY/SHARED-DECISIONS/BLOCKERS-REGISTER.md` — 1,132 bytes
- `19-CHAT-MEMORY/SHARED-DECISIONS/CROSS-TEAM-LOG.md` — 1,517 bytes
- `19-CHAT-MEMORY/SHARED-DECISIONS/decisions/TEMPLATE.md` — 338 bytes
- `19-CHAT-MEMORY/WORK-LOG-TEMPLATE.md` — 664 bytes
- `README.md` — 4,214 bytes

## Verification boundaries
- The PDF, DOCX, XLSX, Markdown, SQL/DBML, vector diagram text labels and decoded prototype screens were inspected offline. No external vendor claims, legal status, student data or actual production systems were independently verified.
- Neither runnable backend/frontend application source, SQL Server migrations, CI configuration nor executable test suite is included in this ZIP. Screenshot/demo interactions do not establish production behavior.