# UR GURU — Issues Register & Historical Changelog

**Last Updated:** `17 November 2026`  
**Purpose:** Maintain complete engineering traceability across requirement revisions, structural pivots, and resolved bugs.

---

## 1. Major Milestone Changelog & Scope Evolution

### Version 6.1 — Corrected Review Baseline (17 November 2026) — *Current Official Baseline*
- **Incorporated Critical Concerns Review (`C-01` to `C-07`):**
  - **C-01:** Detailed specifications for `BR-03` to `BR-07` and expanded Phase 1 Acceptance Criteria (`AC-03` to `AC-09`).
  - **C-02:** Locked launch modality to Responsive Web Application; native app IAP billing gated for future.
  - **C-03:** Minor safeguarding (`BR-21` Phase 1 Must), PDPA legal compliance, ban on personal contact sharing, 1:1 session recording prohibitions.
  - **C-04:** Canonical Question & Translation Model (`QuestionConcept` + `QuestionTranslation`). Zero silent language fallback.
  - **C-05:** Release gates and explicit dependency map across Phase 1, Phase 2, Later, and Future.
  - **C-06:** Payment gateway evaluation scorecard, separate tuition GMV vs Exam Munnodi ledgers, and teacher payout batch flow.
  - **C-07:** Video vendor criteria (HLS/DASH, 240p/360p low-bandwidth for Sri Lanka, signed URLs), complete review state machine; **Azure Media Services explicitly excluded (deprecated)**.
- **ERD Architecture Overhaul (26 Entities - 7 Critical Bugs Fixed):**
  1. `AdminProfile != TeacherProfile`: Complete role separation.
  2. `Trial` records directly to `Student` and `TuitionClass`.
  3. `QuestionOption` standardized to 5 options (A–E) for Sri Lankan A/L past papers.
  4. One attempt per paper, independent student evaluation (`PaperAssignment` -> `ExamAttempt`).
  5. `PurchaseOrder` handles both `TuitionClass` and `ProductPlan` (digital Exam Munnodi packs).
  6. Medium-aware question translations (`QuestionVersion`).
  7. History-safe question corrections via `QuestionVersion` snapshotting.
- **Requirements & Acceptance Expansion:**
  - Expanded Functional Requirements to `BR-01` through `BR-21`.
  - Expanded Acceptance Criteria to `AC-01` through `AC-20`.

---

### Version 6.0 / Baseline V5.0 (12–16 November 2026)
- **A/L Strict Focus Enforced:** Removed all Grade 10, Grade 11, and G.C.E. O/L references from active user journeys, search filters, and database schemas.
- **Modality Shift:** Pivot from hybrid mobile (Flutter) + web to **Responsive Web Application Only** across Student, Teacher, and Administrator portals.
- **Exam Munnodi Formalized:** Added complete product specification for 5-year past-paper MCQ bank, dual explanations (written + teacher-recorded video), topic/difficulty mock generator, and teacher multi-student paper assignment.
- **Guardian Entity Realignment:** Reclassified Parent/Guardian from a standalone full portal account to a streamlined contact record (`name`, `phone`, relationship) linked directly to the minor student profile.
- **Course vs. Class Reconciliation:** Clarified distinction between academic master catalog (`Subject`, `Topic`), teacher offering (`Course`), and scheduled lesson instances (`ClassSession`).
- **Revenue Recognition:** Clarified that full tuition fees paid by students represent Gross Merchandise Value (GMV); UR GURU revenue is strictly platform commission. Separated live tuition ledger from digital product (Exam Munnodi) ledger.

---

### Version 4.4 to 4.6 (2–9 November 2026)
- **Consolidated BRD V4.0:** Integrated 6 core USPs (Teacher matching, Tamil transcription notes, AI tutor, Gap2Growth, ExamPilot, DataSmart).
- **Teacher & Admin Portals Added:** Merged initial student-only prototypes into unified responsive prototypes (`MergedScreens2.html`, `UR_GURU_Admin_Web_Only_Updated.html`).
- **45-Table Relational Schema:** Generated unified PostgreSQL/SQL Server database design (`UR_GURU_A_L_ONLY_V2_PostgreSQL.sql`, `UR_GURU_A_L_ONLY_V2.dbml`).
- **168 API Endpoint Specification:** Consolidated comprehensive endpoint matrix (`UR_GURU_API_List_V6_0.xlsx`).

---

### Version 1.0 to 2.0 (Late October – Early November 2026)
- Initial conceptualization as Grade 10–13 tuition marketplace.
- 30 student journeys, 200 steps, and 77 screen design inventory established.
- Initial HTML/CSS UI prototype produced.

---

## 2. Historical Defects & Resolution Log

### BUG-001: Unvalidated Form Submission Navigating to Next Screen
- **Module:** Authentication (`AU-04` Login, `AU-02` Registration, `AU-03` OTP, `EN-02` Enrollment)
- **Severity:** High (Integrity Violation)
- **Reported:** 2 November 2026
- **Root Cause:** In the initial standalone UI prototype (`MergedScreens.html`), action buttons utilized a generic handler `action(label, to, style)` which invoked `go(to)` unconditionally, bypassing client-side validation and navigating to dashboard even on blank form submissions.
- **Resolution Applied:**
  1. Replaced generic action handler with `attempt(to, event, style)`.
  2. Implemented `checkFields(current)` on all form screens to enforce mandatory inputs, valid Sri Lankan phone patterns (`07XXXXXXXX` or `+947XXXXXXXX`), minimum password lengths, and required terms checkboxes.
  3. Form errors now highlight invalid fields inline, present summary banners, retain user-entered values, and shift focus to the first invalid field.
  4. Explicitly blocked local navigation from `PY-02` (Pending) to `PY-03` (Success), enforcing that payment confirmations can ONLY occur via server-verified webhook callbacks.
- **Verification:** 27/27 automated Playwright test assertions passed on local Chromium test suite.

---

### DEF-002: Redundant Guardian Portal in API & Database Schemas
- **Module:** User Management & API Surface
- **Severity:** Medium (Architectural Bloat)
- **Observed:** 16 November 2026
- **Issue:** Early API and ERD specifications contained 7 separate guardian endpoints (registration, login, guardian-student linking, dedicated dashboard) which contradicted the revised decision to limit guardians to contact information during Phase 1.
- **Resolution Applied:** Deprecated the 7 standalone guardian endpoints from `UR_GURU_API_List_V6_0.xlsx` (moved to Sheet 3 / Deprecated). Reduced active endpoints to 161 core endpoints. Guardian attributes migrated as fields on `student_guardians` table.

---

### DEF-003: Subject Catalog vs. Teacher Offering Overlap
- **Module:** Academic Catalog (`07-DATABASE-DESIGN`)
- **Severity:** Medium (Data Integrity Risk)
- **Issue:** Early discussions had teachers creating arbitrary subjects, creating potential catalog chaos and breaking standard A/L syllabus categorization.
- **Resolution Applied:** Master `subjects` and `topics` tables are strictly administrator-managed based on official Sri Lankan syllabi. Teachers can only create offerings (`courses` / `class_schedules`) referencing approved subject catalog IDs.

---

## 3. Active Known Issues & Technical Debt Watchlist

| Issue ID | Area | Description | Severity | Target Milestone |
|---|---|---|---|---|
| **ISS-001** | UI Prototypes | Disconnect between standalone HTML files (`MergedScreens2.html`) and upcoming production frontend framework. | Medium | Phase 1 Frontend Setup |
| **ISS-002** | Database Migrations | Schema currently defined in PostgreSQL SQL and DBML; need official Microsoft SQL Server / Entity Framework Core migration scripts. | High | Phase 1 Backend Setup |
| **ISS-003** | Concurrency Control | Seat capacity validation on popular class sessions requires pessimistic locking or database transaction isolation to prevent overbooking. | High | Phase 1 Core Booking |
| **ISS-004** | Past-Paper Digitization | Question bank requires systematic digitizing of mathematical formulas and chemical equations (LaTeX) from physical past papers. | Medium | Phase 2 Ingestion |
