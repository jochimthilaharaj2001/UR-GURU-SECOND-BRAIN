# DEV_6: QA & Test Engineer — Context & Starter

**Developer ID:** `DEV_6`  
**Role:** QA Lead / Test Automation Engineer  
**Primary Focus:** Test plan execution, acceptance criteria validation (AC-01 to AC-20), automated Playwright UI tests, API contract testing, and Definition of Done sign-off.

---

## 1. My Core Responsibilities
- **Acceptance Criteria Verification:** Systematically test and verify `AC-01` through `AC-20` defined in BRD V6.1.
- **Form Validation & Regression (BUG-001):** Verify that empty or format-invalid inputs NEVER navigate to next screens across all 77 screens.
- **Security & Authorization Testing (`AC-19`):**
  - Verify that Student A cannot access Student B's exam attempts or results.
  - Verify that Teacher A cannot view Teacher B's student roster or earnings.
  - Verify that replay attacks or duplicate payment callbacks fail safely.
- **Low-Bandwidth & Device Testing (`AC-20`):** Validate UI responsiveness on 390px mobile viewports and video playback resilience under throttled network conditions.
- **Exam Integrity Tests:** Verify that questions cannot be duplicated in a single mock attempt and answer keys are not leaked in network payloads.
- **Definition of Done Enforcement:** Ensure no feature is merged without unit/integration tests and documented QA approval.

---

## 2. Key References I Must Read
1. [`02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) (Section 14: AC-01..20, DoD)
2. [`12-TESTING/Test-Case-Register.csv`](../../12-TESTING/Test-Case-Register.csv)
3. [`15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md`](../../15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md)

---

## 3. AI Starter Prompt (Copy-paste this when starting a new session)
```markdown
I am DEV_6 (QA & Test Automation Lead) working on the UR GURU education marketplace.
Workspace: D:\Unicom\UR_GURU_finalProject
Please read my context file:
UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_6\CONTEXT.md
And our Acceptance Criteria baseline:
UR-GURU-SECOND-BRAIN\02-BRD-AND-REQUIREMENTS\UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md

Today I am testing / writing test cases for [FEATURE / API / ACCEPTANCE CRITERION].
Generate comprehensive positive, negative, boundary, and security test scenarios adhering to our Definition of Done.
```

---

## 4. My Daily Work Log
Record daily activities in `WORK-LOG-YYYY-MM-DD.md`.
Log any verified defects or test failures in `../../15-ISSUES-AND-CHANGELOG/` and notify the team via `../SHARED-DECISIONS/CROSS-TEAM-LOG.md`.
