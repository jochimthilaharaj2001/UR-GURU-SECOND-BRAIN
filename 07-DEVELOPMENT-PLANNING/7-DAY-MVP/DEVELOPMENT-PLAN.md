# 7-Day MVP Development Plan — Team Allocation Update (23 Nov 2026)

**Status:** Working plan, not proof of implementation. The original blueprint remains attached as historical source. Confirm actual start date, task capacity and 104-API ownership before committing delivery dates.

**Confirmed:** DEV 1 + DEV 2 backend; DEV 3 + DEV 4 student frontend; DEV 5 teacher frontend; DEV 6 admin frontend. Specific backend API and student screen splits below are proposed, not yet signed off.

| Day | DEV 1 / DEV 2 Backend | DEV 3 / DEV 4 Student | DEV 5 Teacher | DEV 6 Admin | Gate |
|---|---|---|---|---|---|
| 1 | Auth, roles, curriculum, migrations | Auth, onboarding, subjects | Verification/profile | Admin shell, login | Contract and auth checks |
| 2 | Discovery, approval, class/batch | Discovery, class details | Class and batch management | Teacher approvals | Approved class visible |
| 3 | Checkout, payment callback, enrollment | Checkout, enrolled classes | Enrollment visibility | Payment oversight | Verified payment and no duplicate enrollment |
| 4 | Live, attendance, resources, demos | Live join and resources | Live sessions, demo upload | Demo moderation | Authorization and playback gates |
| 5 | XACT practice and scoring | Practice, mocks, results | Paper builder UI | XACT review | Deterministic score |
| 6 | Assignments, notifications, finance/audit | Assigned papers, notifications | Assignment and earnings | Finance, audit | Cross-role integration |
| 7 | Integration tests, fixes, deployment checks | Student regression/mobile QA | Teacher regression | Admin regression | Internal demo and gap log |

**Scope caution:** These are illustrative workstreams, not a claim that all BRD requirements fit seven days. Track deferred/gap items explicitly. The previously documented migration proposal remains subject to database owner approval; do not create or modify migrations based on this schedule alone.

## Tracking
For each selected MVP API: endpoint ID, backend owner, frontend consumer(s), screen, DTO, migration dependency, test, status, evidence and blocker. See `../API-OWNERSHIP-MATRIX.md`.
