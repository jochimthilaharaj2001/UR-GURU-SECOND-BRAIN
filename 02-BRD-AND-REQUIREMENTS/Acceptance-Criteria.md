# Acceptance Criteria — BRD v6.2.2

> **UR GURU Second Brain — Development reference**  
> Source: [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](./UR_GURU_Full_Corrected_BRD_v6.2.2.pdf), consolidated corrected edition, 19 November 2026.  
> **Document status:** DRAFT EXTRACTION from BRD v6.2.2; source itself is a **review candidate pending stakeholder sign-off**.  
> **Use:** Requirements analysis / development planning; not independent approval or an executed test record.

The BRD defines **33 acceptance criteria (`AC-01`–`AC-33`)** across pp. 9–10. These are **specified acceptance conditions, not completed tests**. Wording below is faithful paraphrase for team readability; the controlling source is BRD §13.

## Account and curriculum

| Acceptance ID | Expected result | Execution status |
|---|---|---|
| AC-01 | Registration rejects non-A/L grade, invalid stream/subject combinations and duplicate active subject selections. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-02 | Unknown/duplicate accounts and password recovery do not reveal whether a user identity exists. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-03 | Passing an NIC-format check alone never establishes government-verified identity. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-04 | Required guardian consent stores purpose, policy/version and protected supporting evidence. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-32 | StudentSubject persists valid student/subject/year selections without granting paid enrollment/entitlement or duplicating active selections. | NOT EXECUTED / NO EVIDENCE SUPPLIED |

## Marketplace, free demos and classes

| Acceptance ID | Expected result | Execution status |
|---|---|---|
| AC-05 | Unapproved teachers cannot publish or appear in public discovery. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-06 | Teacher discovery returns approved active subject/medium matches without private information. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-07 | A free approved demo may be watched or skipped; absence/failure/skipping never blocks paid enrollment and creates no trial booking or seat reservation. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-08 | Paid enrollment and transactional seat reservation safely handle duplicate requests and delayed payments. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-09 | Only authorized students receive live-class join credentials; rescheduling triggers notifications. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-10 | Attendance corrections and state changes leave an audit trail. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-11 | Students outside a class cannot access its private learning resources, even with a copied URL. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-31 | Only authorized reviewers can approve and publish demos; withdrawn/rejected/unprocessed/rights-invalid demos cannot play publicly. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-33 | Demo preview does not create booking, Enrollment, PaymentAttempt or Entitlement and does not require completion before checkout. | NOT EXECUTED / NO EVIDENCE SUPPLIED |

## Payments and payouts

| Acceptance ID | Expected result | Execution status |
|---|---|---|
| AC-12 | A forged or unsigned payment gateway callback cannot grant entitlement. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-13 | Repeated valid gateway callbacks cause one entitlement and correct ledger posting. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-14 | Partial and full refunds reconcile corresponding line items and prevent duplicate reversal. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-15 | Teacher payouts reconcile with the approved commission basis and dispute holds. | NOT EXECUTED / NO EVIDENCE SUPPLIED |

## XACT question, mock and assessment integrity

| Acceptance ID | Expected result | Execution status |
|---|---|---|
| AC-16 | Question source rights, question version, translation and answer key must all be approved before use. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-17 | A question in an unavailable medium is not silently substituted with a different language. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-18 | Mock generation rejects insufficient eligible questions and duplicated canonical questions. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-19 | Autosaved answers survive retries; the server deadline blocks late edits. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-20 | Submitting or retrying yields one final result from the exact approved versioned answer key. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-21 | Unauthorized users cannot access unrelated student attempts or teacher reports. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-22 | Explanation reveal obeys approved publication, review and entitlement policy. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-23 | A teacher can assign the same versioned paper to multiple authorized students. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-24 | Reusing a teacher assignment preserves previous paper versions and results. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-25 | Withdrawal or correction of questions/keys is audited without altering recorded history. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-26 | Rejected or unprocessed XACT videos remain unpublished, with written explanation fallback. | NOT EXECUTED / NO EVIDENCE SUPPLIED |

## Safety, localization and platform reliability

| Acceptance ID | Expected result | Execution status |
|---|---|---|
| AC-27 | Safety reports reach the authorized owner and retain confidential evidence. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-28 | Target browsers render Tamil/Sinhala, equations, diagrams and long options correctly. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-29 | Outbox and notification processing survive worker crashes and provider retries. | NOT EXECUTED / NO EVIDENCE SUPPLIED |
| AC-30 | Backup/restore, concurrency, access-control and monitoring tests pass before release. | NOT EXECUTED / NO EVIDENCE SUPPLIED |

## Definition of Done (BRD §13, p. 10)

Before accepting a requirement, retain: mapped journey and UI states (**loading, empty, error, success**), authoritative access rule, API contract, database migration, positive and negative UAT, accessibility checks, operational logs, support path and sign-off evidence.

## Evidence capture format for QA

For each `AC-XX`, record: requirement ID; environment and test data; preconditions; steps; expected and actual outcome; screenshots/logs; pass/fail/block status; tester/date; bug/defect ID; approver/sign-off. Keep the actual execution records in `12-TESTING`; do not mark passing based on this Markdown file alone.

See [`Requirements-Traceability.csv`](./Requirements-Traceability.csv) for proposed requirement-to-UAT links and [`Open-Requirements.md`](./Open-Requirements.md) for policies that may block final test design.
