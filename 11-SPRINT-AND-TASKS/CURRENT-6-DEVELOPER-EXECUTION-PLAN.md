# Current 104-API MVP execution plan — 2026-11-23

**Status:** Team role assignments confirmed; endpoint ownership and release sign-off pending.

## Confirmed developer responsibilities

| Developer | Responsibility |
|---|---|
| DEV 1 | Backend — identity, profiles, curriculum, discovery (proposed modules) |
| DEV 2 | Backend — classes, payments, live, XACT, operations (proposed modules) |
| DEV 3 | Student frontend — onboarding, account, subjects, discovery (proposed screens) |
| DEV 4 | Student frontend — enrollment, payment, live, resources, XACT (proposed screens) |
| DEV 5 | Teacher frontend — teacher workflows |
| DEV 6 | Admin frontend — operations, academic and finance review workflows |

The exact module splits are **proposals**, not confirmed per-endpoint assignments. DEV 1 and DEV 2 must agree one backend owner for each of the 104 API register entries. DEV 3–6 should map frontend integration to student/teacher/admin journeys; an API may serve multiple portals. Do not use the superseded 3-pair workbook's owner columns as current assignments.

## Execution gates

1. Freeze the 104-API register against BRD v6.2.2, recording explicitly deferred requirements and owner decisions.
2. Agree DTOs, status codes, object authorization, validation, example payloads and error shape before implementation.
3. Confirm MySQL schema, constraints, migrations and DbContext mappings against the actual backend repository; Second Brain alone cannot prove they are implemented.
4. Build frontend using agreed contracts and mocks; integrate with DEV 1/2 services.
5. Verify authentication, paid enrollment/webhook idempotency, demo optionality, protected LiveKit join, XACT scoring/autosave and admin permissions.
6. Run UAT, backup/restore, security and deployment checks; collect sign-off evidence.

**Non-negotiable BRD rules:** initial Grades 12–13 Bio/Maths only; demo is an optional free prerecorded preview, never a trial booking; payment entitlement only after verified processing; server-authoritative exam timer and scoring. Community/forum scope requires explicit approval against the BRD.

**Schedule:** The previous seven-day schedule is a historical planning target, not evidence of completed delivery. Agree new checkpoints and actual task owners in the live tracker.

**Document control:** DEV 2 reviews controlled baseline changes (excluding chat memory), subject to repository branch protection and stakeholder sign-off where required.
