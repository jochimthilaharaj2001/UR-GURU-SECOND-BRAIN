> **22 Nov 2026 correction notice:** Refer to root README and BRD v6.2.2 for active scope. Earlier counts, approvals and legacy references below are historical until reconciled.

# 02 — BRD AND REQUIREMENTS

> **Current document baseline:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf` (19 November 2026) — **consolidated review candidate; not yet signed off**.
> **Important:** Do not use old BRD V6.1 or the legacy Exam Munnodi / live-trial requirements as current implementation authority. Preserve older versions separately as historical references if your main repository already has them.

## Contents

| File | Purpose | Status |
|---|---|---|
| [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](./UR_GURU_Full_Corrected_BRD_v6.2.2.pdf) | Primary uploaded consolidated source | Review candidate — SIGN-OFF PENDING |
| [`Functional-Requirements.md`](./Functional-Requirements.md) | Complete BR-01–BR-24 register + grouped details and constraints | Prepared from V6.2.2, review pending |
| [`Non-Functional-Requirements.md`](./Non-Functional-Requirements.md) | Security, performance, recovery, accessibility, reliability and verification targets | Prepared; numeric targets NOT APPROVED |
| [`Acceptance-Criteria.md`](./Acceptance-Criteria.md) | AC-01–AC-33 acceptance catalogue + QA evidence requirements | Specified, NOT EXECUTED |
| [`Open-Requirements.md`](./Open-Requirements.md) | OD-01–OD-20 unresolved decisions + questions | PENDING APPROVAL |
| [`Requirements-Traceability.csv`](./Requirements-Traceability.csv) | 24 BR rows, proposed journey/UAT crosswalk; UI/API/DB not mapped without evidence | PARTIAL — requires reconciliation |

## Active scope from V6.2.2

- Target: Sri Lankan A/L **Grades 12–13**, first implementation **Biological Science and Physical Science/Maths** only. Commerce/Arts/Technology remain later/uncommitted.
- Channel: **responsive Student/Teacher web** and a **separate Admin web portal**.
- Assessments: **XACT** (legacy name: Exam Munnodi).
- `BR-04`: **Optional, approved, free prerecorded DemoVideo** linked to a class. Watching is **never required** before checkout. **No scheduled live-trial booking flow**.
- `StudentSubject` is persistent subject selection, **not** purchased `Enrollment`.
- Working releases: **R0 Foundation**, **R1 Marketplace**, **R2 XACT**; ordering changes need approval.

## How Codex should use these files

1. Read the source BRD and relevant requirement ID.
2. Check unresolved decisions before generating UI/DB/API behavior.
3. Use mapping CSV only as a **partial proposed crosswalk**; do not invent unknown UI screen IDs, API paths, migration IDs or test results.
4. For each implementation feature, verify owner, approved decision, business rule, API contract, database design and actual acceptance evidence.
5. Record and resolve conflicts with legacy Second Brain docs via a controlled decision; do not silently overwrite source documents.

## Migration note for older Second Brain folders

A V6.1-based `01-PROJECT-OVERVIEW`, UI prototype, API list, data schema or business-rule document may now be outdated. Review each for: Bio/Maths first release, XACT branding, removal of live-trial fields, optional free DemoVideo, StudentSubject distinct from paid enrollment, AC-31–AC-33 additions and revised OD-01–OD-20 approvals.

**Approval footer:** Source remains **CONTROLLED REVIEW COPY — NOT YET SIGNED** (BRD p. 12).
