# UR GURU — Task Assignment by Developer (6 Members)

**Sprint Window:** 17 November 2026 – 29 November 2026 (12 Days)  
**Lead:** Jochim (`DEV_1`)

---

## 👨‍💻 DEV_1: Jochim (Project Lead & System Architect)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T1-01 | Scaffold ASP.NET Core 8.0 Clean Architecture Solution | M1 (Days 1–3) | NFR-12 | `Planned` |
| T1-02 | Define shared ApiResponse envelope & Exception Middleware | M1 (Days 1–3) | NFR-11 | `Planned` |
| T1-03 | Code Review & PR approvals for Milestone 1 | M1 (Days 1–3) | - | `Planned` |
| T1-04 | Coordinate MediatR commands/queries & DI registrations | M2 (Days 4–6) | NFR-12 | `Planned` |
| T1-05 | Implement Dual Ledger segregation logic (Tuition vs Digital) | M3 (Days 7–9) | BR-06, MOD-FIN | `Planned` |
| T1-06 | Idempotency filter for payment & attempt submissions | M3 (Days 7–9) | NFR-03, AC-07 | `Planned` |
| T1-07 | Dockerize API & Web App, Environment config management | M4 (Days 10–12)| NFR-12, MOD-DEP| `Planned` |
| T1-08 | Final Release Candidate RC-1 Sign-off & Architecture review | M4 (Days 10–12)| AC-20 | `Planned` |

---

## 👨‍💻 DEV_2: Backend Developer (C# ASP.NET Core API)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T2-01 | Student & Teacher Registration Endpoints | M1 (Days 1–3) | BR-01, BR-02 | `Planned` |
| T2-02 | Password hashing & JWT Authentication Service | M1 (Days 1–3) | NFR-01 | `Planned` |
| T2-03 | Student Academic Profile & Stream selection API | M2 (Days 4–6) | BR-01 | `Planned` |
| T2-04 | Teacher Document Upload & Verification Status API | M2 (Days 4–6) | BR-02, BR-14 | `Planned` |
| T2-05 | Class & ClassSession creation & schedule API | M2 (Days 4–6) | BR-05 | `Planned` |
| T2-06 | Free Trial booking & eligibility check API | M3 (Days 7–9) | BR-04, AC-04 | `Planned` |
| T2-07 | Paid Class Booking & Payment Webhook Handler | M3 (Days 7–9) | BR-06, AC-07 | `Planned` |
| T2-08 | Live Session Join Token & Attendance logging | M3 (Days 7–9) | BR-05, AC-06 | `Planned` |
| T2-09 | Safeguarding & Abuse reporting API | M4 (Days 10–12)| BR-21, AC-10 | `Planned` |
| T2-10 | Essential Notifications Service (Email/In-App) | M4 (Days 10–12)| BR-13 | `Planned` |

---

## 👨‍💻 DEV_3: Frontend Developer (Responsive Web App)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T3-01 | Responsive Web Shell, Navbars, Indigo/Violet Theme tokens | M1 (Days 1–3) | NFR-08, NFR-09 | `Planned` |
| T3-02 | Registration & Login Forms with inline error validation | M1 (Days 1–3) | BR-01, BUG-001 | `Planned` |
| T3-03 | Student Academic Setup Wizard (Grade 12/13, Stream, Medium)| M2 (Days 4–6) | BR-01, PF-01 | `Planned` |
| T3-04 | Teacher Dashboard & Class Creation Wizard | M2 (Days 4–6) | BR-05, DS-01 | `Planned` |
| T3-05 | Admin Teacher Verification Portal UI | M2 (Days 4–6) | BR-14 | `Planned` |
| T3-06 | Class Booking, Checkout Review & Payment Status UI | M3 (Days 7–9) | BR-06, PY-01..03| `Planned` |
| T3-07 | Live Room Pre-Join Check & Waiting Room UI | M3 (Days 7–9) | BR-05, CL-04..05| `Planned` |
| T3-08 | Exam Munnodi Mock Taking UI (LaTeX math, timer, autosave) | M3 (Days 7–9) | BR-18, AS-02 | `Planned` |
| T3-09 | Student Safety Report & Complaint Modal | M4 (Days 10–12)| BR-21, FB-02 | `Planned` |
| T3-10 | Responsive HLS/DASH Video Player with written fallback | M4 (Days 10–12)| BR-20, C-07 | `Planned` |

---

## 👨‍💻 DEV_4: Database Developer (SQL Server / EF Core)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T4-01 | Execute 26-Entity DDL Script on Microsoft SQL Server | M1 (Days 1–3) | MOD-07, ERD-26 | `Planned` |
| T4-02 | Scaffold EF Core Entity Configurations & DbContext | M1 (Days 1–3) | NFR-12 | `Planned` |
| T4-03 | Seed 4 A/L Streams, Standard Subjects & Topic Hierarchy | M1 (Days 1–3) | BO-01 | `Planned` |
| T4-04 | Add Indexes for Teacher Discovery filters | M2 (Days 4–6) | BR-03, NFR-04 | `Planned` |
| T4-05 | Implement Class Capacity Reservation Concurrency Lock | M2 (Days 4–6) | BR-05, AC-06 | `Planned` |
| T4-06 | Create Dual-Ledger Financial Views (Tuition GMV vs Digital) | M3 (Days 7–9) | BR-06, MOD-FIN | `Planned` |
| T4-07 | Implement Teacher Payout batching & Earnings aggregation | M3 (Days 7–9) | BR-06 | `Planned` |
| T4-08 | Configure Database Audit Triggers on sensitive mutations | M4 (Days 10–12)| NFR-01, AC-18 | `Planned` |
| T4-09 | Database Backup & Point-in-time Recovery Rehearsal | M4 (Days 10–12)| NFR-07 | `Planned` |

---

## 👨‍💻 DEV_5: Exam Munnodi Specialist (Assessment Engine)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T5-01 | Question Bank Entities (QuestionConcept, Translation, Options)| M1 (Days 1–3) | BR-18, C-04 | `Planned` |
| T5-02 | 5-Year Past-Paper MCQ Seed Ingestion Script | M1 (Days 1–3) | OD-08 | `Planned` |
| T5-03 | Mock Exam Generator Algorithm (Selected-topic & All-topics) | M2 (Days 4–6) | BR-18, AC-13 | `Planned` |
| T5-04 | Question Shortage Handler (No fake questions) | M2 (Days 4–6) | AC-07 | `Planned` |
| T5-05 | Mock Exam Start & Question Snapshotting (Version isolation) | M3 (Days 7–9) | AC-18 | `Planned` |
| T5-06 | Attempt Autosave & Server-Side Scoring Engine | M3 (Days 7–9) | AC-08, AC-14 | `Planned` |
| T5-07 | Teacher Paper Builder API (Curate & assemble custom papers)| M3 (Days 7–9) | BR-19, AC-15 | `Planned` |
| T5-08 | Multi-Student Paper Assignment & independent attempt tracking| M4 (Days 10–12)| BR-19, AC-16 | `Planned` |
| T5-09 | Teacher Explanation Video Review & Publishing Pipeline | M4 (Days 10–12)| BR-20, C-07 | `Planned` |

---

## 👨‍💻 DEV_6: QA Lead (Test Automation & Acceptance)
| Task ID | Task Description | Target Milestone | BR / NFR Ref | Status |
|---|---|---|---|---|
| T6-01 | Setup Postman / REST API Automated Test Collection | M1 (Days 1–3) | NFR-12 | `Planned` |
| T6-02 | Setup Playwright Browser Test Suite for Auth & Forms | M1 (Days 1–3) | BUG-001 | `Planned` |
| T6-03 | Test AC-01 (A/L Scope Only) & AC-02 (Teacher Verification) | M2 (Days 4–6) | AC-01, AC-02 | `Planned` |
| T6-04 | Test AC-03 (Discovery) & AC-11 (Question Bank Filters) | M2 (Days 4–6) | AC-03, AC-11 | `Planned` |
| T6-05 | Test AC-04 (Trial eligibility & double-booking block) | M3 (Days 7–9) | AC-04 | `Planned` |
| T6-06 | Test AC-06 (Capacity overflow) & AC-07 (Payment Webhook) | M3 (Days 7–9) | AC-06, AC-07 | `Planned` |
| T6-07 | Test AC-08 (Server scoring anti-cheat) & AC-15 (Teacher paper)| M3 (Days 7–9) | AC-08, AC-15 | `Planned` |
| T6-08 | Security Test AC-19 (Cross-student access, replay attacks) | M4 (Days 10–12)| AC-19 | `Planned` |
| T6-09 | Mobile Viewport 390px & Network Throttling Test (240p video)| M4 (Days 10–12)| AC-20, NFR-09 | `Planned` |
| T6-10 | Full Regression Run & Definition of Done Sign-off Report | M4 (Days 10–12)| DoD, AC-01..20| `Planned` |
