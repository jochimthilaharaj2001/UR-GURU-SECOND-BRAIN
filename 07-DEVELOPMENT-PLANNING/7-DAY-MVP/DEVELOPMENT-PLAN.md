# 7-Day Development Plan

Source: Blueprint pages 18–23. Original plan assigns backend and frontend owners; adapt to the actual 3-backend/3-frontend pair model only after reviewing the API tracker and team assignments.

| Day | Backend focus | Frontend focus | Gate |
|---|---|---|---|
| 1 | Identity, roles, teacher evidence, curriculum, migration | Auth, profiles, onboarding, admin shell | Registration and contracts |
| 2 | Approval, discovery, classes/batches, pricing, seat hold | Discovery, class and batch forms, admin review | Approved class visible |
| 3 | Sandbox checkout, payment verification, enrollment | Checkout, status, enrolled classes | Exactly one enrollment per payment |
| 4 | Live sessions, attendance, protected files, demo uploads | Join, schedule, materials, demo | Unauthorized access denied |
| 5 | Exam Munnodi adapter, XACT attempts/scoring | Practice, mock, results | Scored attempt |
| 6 | Assignments, notifications, manual finance, moderation/audit | Assignments, admin finance, notifications | Operational flows |
| 7 | Support, community, testing/fixes | Support, forum, regression/mobile QA | Internal demo with gap log |

## Migration proposal (not verified against starter repo)
M001 IdentityAndCurriculum; M002 ClassesPricingAndEnrollment; M003 PaymentsMediaAndResources; M004 LiveAndXact; M005 AssignmentsNotificationsAndOperations. One migration owner; validate fresh DB and rollback.

## Tracking
For every selected feature record owner, feature ID, endpoint, screen, migration, test, status (`COMPLETE`, `PARTIAL`, `BLOCKED`, `NOT STARTED`), evidence and blocker.
