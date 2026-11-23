> **SUPERSEDED — HISTORICAL PLAN ONLY (2026-11-23).** The 3-backend/3-frontend pair allocation below is no longer active. Use `CURRENT-6-DEVELOPER-EXECUTION-PLAN.md` and `../07-DEVELOPMENT-PLANNING/TEAM-RESPONSIBILITIES-v2.md`. The companion XLSX is retained unchanged for traceability and must not be used to assign current owners.

# UR GURU — MVP Development Team & API Ownership Plan

**Status:** Proposed execution baseline (not signed off)  
**Date:** 2026-11-23  
**Source of truth:** `UR_GURU_104_API_3_Backend_3_Frontend_Pair_Plan.xlsx`  
**Requirements baseline:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`  
**Scope:** 104 MVP APIs, 6 developers, Angular frontend + ASP.NET Core backend.

## 1. Team allocation

| Pair | Backend owner | Frontend owner | API count | Module ownership |
|---|---|---|---:|---|
| Pair 1 | Dev 1 | Dev 2 | 36 | Identity, Curriculum, Discovery, Classes, Notifications |
| Pair 2 | Dev 3 | Dev 4 | 34 | Demo Videos, Live Classes, Payments, Resources, Community |
| Pair 3 | Dev 5 | Dev 6 | 34 | XACT Source, XACT Exams, XACT Teacher, Admin, Support Safety |
| **Total** | **3** | **3** | **104** | **15 modules** |

**Ownership rule:** Every API has exactly one backend owner and one frontend integration owner. Frontend ownership does not imply one distinct screen per API. The exact per-API assignment, ID, method, endpoint, role, and priority is maintained in the companion Excel workbook; do not copy or manually renumber the 104 endpoints.

## 2. Responsibilities

**Backend owner:** Implement endpoint, request/response DTOs, validation, role and object-level authorization, domain rules, database changes, safe error handling, automated tests, and OpenAPI documentation.

**Frontend owner:** Map the API to the approved Student / Teacher / Admin prototype, implement Angular page/service/state handling, client-side validation, loading/empty/error/success states, responsive behavior, and integration tests. Work against agreed mock payloads while backend is being developed.

**Both owners:** Agree API contract before coding; integrate and test success, failure and permission-denied paths; review each other's PR where appropriate; update task status and document blockers.

## 3. Development workflow

1. Confirm requirement, API ID, method, path, access role and prototype screen.
2. Agree request/response DTOs, HTTP codes, authorization, example payloads and error shape.
3. Implement backend and frontend in parallel using mock responses.
4. Integrate against development environment and test user journeys end-to-end.
5. Review security, regression, accessibility, logs and documentation; mark done only after acceptance evidence.

**Suggested statuses:** Not Started → Contract Ready → In Progress → Integration → QA → Done; use Blocked when a dependency prevents progress.

## 4. Proposed 7-day coordination plan

| Day | Backend focus | Frontend focus | Joint checkpoint |
|---|---|---|---|
| 1 | Auth, curriculum, database foundations | Auth, onboarding screens | DTO agreement and login flow |
| 2 | Teacher discovery, classes, admin review | Teacher/class listing and admin screens | Teacher approval and class discovery |
| 3 | Payment sandbox, enrollment and webhook | Checkout, payment status | Idempotent paid enrollment |
| 4 | Demo, LiveKit, resources | Demo, class join and materials | Authorized class access |
| 5 | XACT question bank, attempts and scoring | Practice, exam and results | Autosave, scoring and exam resume |
| 6 | Assignments, notifications, forum and safety | Teacher assignments, forum, notifications | Cross-pair integration |
| 7 | Security, regression, bug fixes | Responsive QA, error handling | End-to-end demo and signoff |

These are **suggested coordination checkpoints**, not validated effort estimates or a guarantee of full BRD delivery in seven days. Workstreams can run in parallel; cross-pair dependencies must be reviewed daily.

## 5. Cross-pair dependencies and safeguards

- Pair 1 owns authentication, user roles, subject catalogue and class foundations used by Pairs 2 and 3. Publish contracts and test accounts early.
- Pair 2 owns payment and enrollment integration. Do not grant paid entitlements before a verified, idempotently processed payment callback; enforce class capacity and access checks.
- Pair 3 owns XACT assessment workflows and admin review. Scoring, autosave and attempts must be server-authoritative, and exam versions must be immutable.
- Approved optional prerecorded demo viewing must **never** be required for checkout; demo video is not a live trial booking.
- BRD v6.2.2 limits initial curriculum to A/L Grades 12–13 Bio and Maths streams; future features are not automatically included merely because an endpoint exists.
- Community is present in the MVP API tracker; verify its approved MVP boundaries separately against the BRD before implementation.
- Use shared error-response conventions, database migration review, API contract review and PR approvals to prevent integration conflicts.

## 6. Definition of done for each API

- [ ] Contract approved: DTOs, HTTP codes, auth, errors, sample requests/responses
- [ ] Backend implementation and database migration reviewed
- [ ] Authorization, validation and negative tests pass
- [ ] Frontend mapped to approved prototype screen or documented as non-UI endpoint
- [ ] Frontend integration handles loading, empty, error and success states
- [ ] Pair integration and regression tests pass
- [ ] API docs, ownership/status and acceptance evidence updated

## 7. Second Brain usage and change control

**Recommended path:** `12-DEVELOPMENT-PLANNING/DEVELOPMENT_TEAM_104_API_PAIR_PLAN.md` (create folder if missing), or place under the repository's existing development-planning folder. Store the companion workbook alongside it or link to its controlled location.

The Excel workbook is the **authoritative per-API task assignment**; this Markdown file is the team policy and summary. Do not replace BRD, architecture, API contracts or ERD with this plan. Changes to API IDs, scope, ownership, contracts or schema must be reviewed and logged. Assign named people to Dev 1–6 and confirm approval before calling this plan final.
