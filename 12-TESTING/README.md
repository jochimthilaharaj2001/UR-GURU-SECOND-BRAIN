> **22 Nov 2026 correction notice:** Refer to root README and BRD v6.2.2 for active scope. Earlier counts, approvals and legacy references below are historical until reconciled.

# 12-TESTING

**Purpose:** Test cases, environments, QA results and sign-off.

**Status:** Required deliverables checklist — filenames are proposed; create each real file after its owner starts work.

| Needed file | Minimum contents | Status |
|---|---|---|
| `Test-Strategy.md` | Unit, integration, end-to-end, accessibility, security, performance | ☐ Not supplied / verify |
| `Test-Case-Register.csv` | Test ID, linked requirement, steps, expected/actual, status | ☐ Not supplied / verify |
| `API-and-Database-Tests.md` | RBAC, constraints, duplicate submission, payment callback tests | ☐ Not supplied / verify |
| `Critical-User-Flow-Tests.md` | Student booking and teacher assignment, mock exam and admin approvals | ☐ Not supplied / verify |
| `UAT-and-Signoff.md` | Acceptance checklist, owner, actual evidence, decision | ☐ Not supplied / verify |
| `Regression-and-Bug-Reports.md` | Re-test high risk payment, exams, access and class flows | ☐ Not supplied / verify |

## Rules for this folder

- Do not mark a planned document as completed until its actual content is reviewed and version-controlled.
- Add owner, approval status, version/date and cross-references to the appropriate BRD requirements.
- Link to the canonical document instead of creating conflicting copies.
- When a policy or provider is pending, write `PENDING APPROVAL` rather than assuming a final value.


## 104-API MVP testing alignment
The 33 BRD acceptance checks remain requirements-level coverage and are NOT evidence of passed tests. Derive API test cases from the 104 rows in `08-API-DOCUMENTATION/API-REGISTER.csv`, then map each to relevant BRD acceptance checks and exception scenarios. Mark unsupported BRD capabilities deferred with owner approval; do not silently remove UAT requirements.
