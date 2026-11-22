# UR GURU — Release Roadmap and Delivery Gates

| Field | Value |
|---|---|
| Document ID | `OV-06` |
| Version / prepared | Draft 1.0 / 19 November 2026 |
| Approval | **DRAFT — NO COMMITTED LAUNCH DATES** |
| Accountable owner | Sponsor / Product Owner / Project Manager — confirm |
| Requirements source | [BRD V6.1 §5, §8, §13–15](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) |
| Planning context | [12-Day Milestone Plan](../11-SPRINT-AND-TASKS/12-DAY-MILESTONE-PLAN.md) (**aspirational**, not an approved SLA) |

## 1. Roadmap policy

This is a **capability-and-gate roadmap**, not a promise of launch on a named date. The BRD allocates features by Phase 1, Phase 2, Later and Future. It explicitly leaves dates, staffing, budget and targets to `OD-16`. The ZIP's **17–29 November 2026 / 12-day** plan is a draft and must not be re-labelled an approved delivery schedule.

`Must` = required for the release it belongs to. `Should` = desired, may be deferred with documented approval. `Future` = outside current committed release.

## 2. Phase overview

| Phase | Intended outcome | Included requirements | Exit criterion / gate |
|---|---|---|---|
| **Foundation & readiness** *(recommended internal workstream, not an extra BRD product release)* | Approved scope, consistent data/API contracts, repo/CI/test setup, legal/vendor decisions ready | Cross-cutting `NFR-01`–`NFR-12`; design work | No unresolved critical conflicts for the selected feature slice |
| **Phase 1 — Core Marketplace** | Student and teacher A/L web marketplace with authorized live tuition | `BR-01`–`BR-07`, `BR-13`, `BR-14`, `BR-21` | Approved teacher publishing, safe trials/booking, verified payment and access, consent/safety, support/operations UAT |
| **Phase 2 — Exam Munnodi** | Versioned/question-medium-aware mocks, results, teacher papers and staged reviewed videos | `BR-11`, `BR-18`–`BR-20` | Rights/answer/translation reviews; mock and paper assignment integrity; video moderation and entitlement UAT |
| **Later — Learning Intelligence** | Transcription, reviewed AI notes and academic assistance when feasible | `BR-08`–`BR-10` | Legal consent, quality, human review, cost and safety approval |
| **Future** | ExamPilot extension, DataSmart, full guardian portal, institutional/native app or counselling initiatives | `BR-12`, `BR-15`–`BR-17`, plus separately approved opportunities | Separate business case, roadmap update and sponsor sign-off |

**Native mobile applications are not in the current delivery scope.**

## 3. Phase 1 workstreams and release gates

| Workstream | Dependency | Required validation / evidence |
|---|---|---|
| A/L identity/profile | Approved scope and consent | `AC-01`, secure auth/authorization tests |
| Teacher eligibility & discovery | Teacher screening policy `OD-01`; active verification | `AC-02`, `AC-03`; no unverified public offering |
| Classes, capacity, trials & live sessions | Timetable/seat rules `OD-02`; classroom vendor `OD-06` | `AC-04`–`AC-06`, authorized room joins, failure handling |
| Payments, refunds, teacher economics | Rate `OD-03`, policy `OD-04`, provider `OD-05` | `AC-07`, `AC-08`, server confirmation, financial reconciliation |
| Learning resources & notifications | Valid enrollment + approved storage/notification controls | `AC-09`, session/trial/payment messaging validation |
| Admin/safeguarding | Consent and privacy `OD-15` | `AC-10`, least privilege, report/escalation, audit log checks |
| Production readiness | Capacity, recovery, browser/device and operational sign-off `OD-16` | `AC-19`, `AC-20`, monitored service, backups/restore evidence |

**Release blocked if:** privileged roles or records leak across users, teacher vetting bypasses checks, payment success is client-forged, class access is unauthorized, privacy/legal controls lack approval, or monitoring/recovery requirements fail.

## 4. Phase 2 workstreams and release gates

| Workstream | Required inputs | Release evidence |
|---|---|---|
| Approved question bank | Rights/translation policy `OD-07`; coverage inventory `OD-08`; academic approval `OD-09` | `AC-11`, `AC-12`; only approved active medium-accurate questions |
| Mock creation & scoring | Counts, timers, retakes `OD-10`; difficulty/topic selection `OD-11` | `AC-13`, `AC-14`; no duplicate/unauthorized questions, backend scores/history |
| Teacher papers/assignments | Approved question sets, authorized student/teacher relationships | `AC-15`, `AC-16`; independent per-student attempts and results |
| Written and video explanations | Review workflow `OD-09`, rights and payment `OD-12`, video vendor `OD-06` | `AC-17`, `AC-18`; no unapproved video, written fallback |
| Digital monetization, if enabled | Product prices/free allowance `OD-13`, payment entitlement handling | Server-verified access, clearly disclosed terms and reconciled ledger |

A teacher video may be staged while textual MCQ functions are tested, but **any revised phase acceptance and launch decision must be formally recorded**; don't silently remove `BR-20` from its agreed phase.

## 5. Suggested sequence for a small development team

This is **implementation planning advice**, not an approved date or staffing plan:

1. Resolve scope, source-of-truth hierarchy, database vendor and critical entity/API conflicts.
2. Set up authentication, roles, master A/L catalogue, migrations, CI and reproducible test environment.
3. Build one thin, testable vertical slice: **student register → profile/subject selection → teacher listing**.
4. Extend to teacher verification, class publication, trials, booking and attendance.
5. Integrate real gateway/provider only after procurement and approval; validate entitlements and recovery.
6. Complete Phase 1 UAT, safeguarding and operational controls before declaring a release candidate.
7. Build Exam Munnodi question governance/translation versioning before mocks and teacher assignments; stage content and video production with approval.

Do not equate prototypes, documentation or endpoint counts with completed functionality.

## 6. Readiness gates and sign-off record

| Gate | Required decision/evidence | Suggested approver | Status |
|---|---|---|---|
| G0 Scope and requirements | Correct approved BRD version and resolved critical conflicts | Product Owner | **PENDING** |
| G1 Architecture | Approved DB/client/provider direction, ERD/API contract consistency | Tech Lead | **PENDING** |
| G2 Safety & content | Legal/privacy/teacher checks; question/video rights and review | Legal, Academic Lead | **PENDING** |
| G3 Financial control | Commission/refund/payout policies, gateway, reconciliation checks | Finance/Owner | **PENDING** |
| G4 QA and reliability | UAT pass, negative tests, low-bandwidth support, backup/restore, monitoring | QA + Engineering | **PENDING** |
| G5 Release authorization | Named owner, environment readiness, budget, support and explicit go/no-go | Sponsor / PM | **PENDING** |

The `PENDING` statuses are **default placeholders because approval evidence is not in the inspected sources**; replace with approver name/date/reference when available.

## 7. Risks and constraints

- **Planning mismatch:** the 12-day plan aims at broad Phase 1 + Exam Munnodi delivery; the BRD phases and decision register do not confirm that this is achievable or signed off.
- **Content risk:** five-year past-paper coverage, medium-specific answer accuracy and reproduction rights must be established before public mocks.
- **Financial risk:** example commission/refund numbers in supporting files must not be treated as approved production policy.
- **Technology risk:** PostgreSQL schema exists in the ZIP, but BRD proposes SQL Server; frontend framework and cloud/video vendor choices are not fully ratified.
- **Safeguarding risk:** recording, guardian consent, private contact sharing and complaint escalation require approved operational/legal rules.
- **Capacity risk:** the 3–5 developer estimate is historical planning context, not verified current staffing or throughput.

## 8. Roadmap change procedure

When scope/date changes: document request → assess requirement/financial/academic/safeguarding impact → obtain required approval → update BRD/dependency map/sprints/tests → communicate release scope clearly. Keep a dated decision log and do not remove a Must requirement without an explicit change approval.

## 9. Source links

- [BRD V6.1 corrected baseline](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)
- [Requirements register and acceptance criteria](../02-BRD-AND-REQUIREMENTS/README.md)
- [Decision register](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md)
- [12-day planning artifact](../11-SPRINT-AND-TASKS/12-DAY-MILESTONE-PLAN.md)
- [Project Scope](Project-Scope.md)
- [Modules and Features](Modules-and-Features.md)
