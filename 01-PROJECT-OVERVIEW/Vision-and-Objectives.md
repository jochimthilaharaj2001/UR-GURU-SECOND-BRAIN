# UR GURU — Vision and Business Objectives

| Field | Value |
|---|---|
| Document ID | `OV-02` |
| Version / prepared | Draft 1.0 / 19 November 2026 |
| Approval | **DRAFT — NOT SIGNED OFF** |
| Proposed accountable owner | Product Owner / Sponsor (confirm) |
| Main source | [BRD V6.1 §2](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) (business objectives `BO-01`–`BO-07`) |

## 1. Product vision

> Enable Sri Lankan G.C.E. A/L students to find trustworthy online teachers, take part in authorized live learning, and improve examination preparation through reviewed, meaningful assessment practice.

This statement is a concise restatement of the BRD vision; it is not a newly approved marketing promise.

## 2. Mission

Build a responsive-web A/L learning marketplace that connects verified teachers and Grade 12–13 students, supports dependable class booking and participation, and extends into **Exam Munnodi** practice backed by governed question content, transparent results and safe student data handling.

## 3. Approved-for-review business objective register

The IDs and intent below follow the **BRD V6.1 corrected review baseline**. Candidate KPIs are proposed for future owner approval; no target percentages or deadlines have been fabricated.

| ID | Business objective (BRD-aligned) | Expected product outcome | Proposed evidence/KPI | Priority/release |
|---|---|---|---|---|
| `BO-01` | A/L-only journey and valid curriculum catalogue | Grade 12/13, four stream groups, authorized subject/medium content; no O/L UI | Scope coverage audit, invalid content-filter results, onboarding acceptance pass | Foundation / Phase 1 |
| `BO-02` | Verified teacher discovery | Students can find eligible verified A/L teachers with appropriate public information | Active verified teachers, discoverability and filter correctness, discovery-to-detail funnel | Phase 1 |
| `BO-03` | Reliable, authorized live tuition | Students can enroll/pay where required, join entitled sessions, view attendance and materials | Verified enrolment success, authorized join test pass, session/access failures | Phase 1 |
| `BO-04` | Approved MCQ practice and explanations | Students can access reviewed A/L questions with written and approved video explanations where available | Approved question coverage by subject/medium, answer review pass, explanation availability | Phase 2 |
| `BO-05` | Trustworthy scores and topic progress | Server-side scoring, topic breakdown and historical progress without unjustified certainty | Score accuracy test pass, completed attempts, topic coverage/sufficiency checks | Phase 2 |
| `BO-06` | Teacher paper drafting and assignments | Authorized teachers build papers from approved items and assign them to multiple students | Paper publish/assign success, independent student result correctness, access control tests | Phase 2 |
| `BO-07` | Auditable sustainable revenue | Separate tuition GMV and platform commission; support approved digital offerings | Ledger reconciliation pass, accurate platform revenue reporting, refund/payout traceability | Phase 1 + approved Phase 2 offers |

**KPI governance:** For every KPI, the Product Owner should approve numerator/denominator or event definition, data source, reporting cadence, accountable owner, target, baseline and interpretation safeguards. Until approved, use `TBD`.

## 4. Strategic priorities

1. **Scope discipline:** serve A/L Grade 12–13 only, with Science, Commerce, Arts and Technology and appropriate subject/medium mappings.
2. **Trust and safety first:** teacher verification, role-scoped access, reporting/escalation, recording/contact boundaries and privacy/legal review before public launch (`BR-02`, `BR-21`).
3. **Reliable learning experience:** clear trial, class, capacity, enrollment, payment, attendance and resource journeys (`BR-03`–`BR-07`).
4. **Content correctness:** only approved, rights-cleared question material; explicit translation approval and version-safe attempts (`BR-18`, `BR-20`).
5. **Fair and auditable commerce:** server-verified payments, idempotency, finance reconciliation and written rules for refunds/payouts (`BR-06`).
6. **Measured expansion:** add Exam Munnodi, AI and advanced tools only after their specified gates, staffing and costs are accepted.

## 5. User and stakeholder value

| Stakeholder | Intended value | Boundary |
|---|---|---|
| Student | Find verified teachers; attend entitled classes; practise and review approved MCQs | No guaranteed exam score or official certification |
| Teacher | Publish authorized class offerings, manage learning and assessments, see transparent earnings | Cannot bypass verification or edit approved question-source records |
| Administrator / Academic Reviewer | Maintain catalogue, review identities/content, handle exceptions and audit changes | Least privilege and action logs apply |
| Parent/Guardian | Supply contact/consent or assist payment where lawful/required | No general learner-activity dashboard in current scope |
| Project sponsor | Evidence-backed acquisition, quality and sustainable commercial control | Pricing/commission assumptions require explicit approval |

## 6. Success criteria and acceptance evidence

Objectives are evidenced by **testable flows**, not documents alone. The BRD lists Phase 1 criteria `AC-01`–`AC-10`, Phase 2 criteria `AC-11`–`AC-18`, plus security and release readiness `AC-19`–`AC-20`. Exact scope/gates need owner sign-off.

- Validate user journeys through approved screen states, backend authorization and negative testing.
- Validate payment entitlement against a server-verified callback and accurate ledger events.
- Validate mock question eligibility, language, version snapshots and independent per-student assignment results.
- Record accessibility, low-bandwidth, performance, recovery and safety evidence prior to production.

## 7. Targets and decisions awaiting sign-off

| Item | Current status | Source |
|---|---|---|
| Revenue commission rate / basis | **PENDING APPROVAL** | `OD-03` |
| Refund/cancellation and teacher payout rules | **PENDING APPROVAL** | `OD-04` |
| Live classroom / video providers | **PENDING APPROVAL** | `OD-06` |
| Question rights, review and coverage | **PENDING APPROVAL / inventory in progress** | `OD-07`–`OD-09` |
| Exam timers, count, difficulty and retakes | **PENDING APPROVAL** | `OD-10`–`OD-11` |
| Minor consent, privacy and safeguarding details | **PENDING LEGAL REVIEW** | `OD-15` |
| MVP delivery date, performance targets, staffing | **PENDING APPROVAL** | `OD-16` |

## 8. Document connections

- [Project Summary](Project-Summary.md)
- [Project Scope](Project-Scope.md)
- [Modules and Features](Modules-and-Features.md)
- [Release Roadmap](Release-Roadmap.md)
- [BRD V6.1 corrected review baseline](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)
