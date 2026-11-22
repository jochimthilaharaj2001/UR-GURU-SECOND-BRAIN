# User Journey Overview — SJ-01 to SJ-16

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.


## Catalogue (source paths reproduce BRD §12, pp. 8–9)

| ID | Journey | Primary actors | Release | Source page |
|---|---|---|---|---|
| SJ-01 | Student account | Student | R0 | 8 |
| SJ-02 | Teacher onboarding | Teacher;Academic reviewer;Admin | R1 | 8 |
| SJ-03 | Teacher discovery | Student | R1 | 8 |
| SJ-04 | Optional free demo | Student/Prospective viewer;Teacher;Reviewer | R1 | 8 |
| SJ-05 | Paid class | Student;Finance;Teacher | R1 | 9 |
| SJ-06 | Live class | Student;Teacher | R1 | 9 |
| SJ-07 | Material | Student;Teacher | R1 | 9 |
| SJ-08 | Refund | Student;Finance reviewer;Admin | R1 | 9 |
| SJ-09 | XACT practice | Student | R2 | 9 |
| SJ-10 | XACT custom mock | Student | R2 | 9 |
| SJ-11 | Assigned paper | Teacher;Student | R2 | 9 |
| SJ-12 | Teacher paper | Teacher;Academic reviewer | R2 | 9 |
| SJ-13 | Teacher explanation video | Teacher;Academic reviewer;Student | R2 staged | 9 |
| SJ-14 | Admin operations | Admin;Academic reviewer;Finance reviewer | R0–R2 | 9 |
| SJ-15 | Help and safety | Student;Teacher;Admin;Safeguarding owner | R0–R2 | 9 |
| SJ-16 | Guardian touchpoint | Student;Guardian contact;Authorized operator | R0–R1 | 9 |

## Canonical happy paths and negative states

### SJ-01 — Student account
- **Source happy path:** Register → verify contact → choose grade/stream/medium/subjects → consent if required → dashboard.
- **Source exceptions:** Invalid code; guardian decision required; duplicate account; suspended state; invalid subject/stream.
- **Requirement IDs (derived mapping):** BR-01, BR-21, BR-22, BR-23.
- **UAT IDs (derived mapping):** AC-01, AC-02, AC-03, AC-04, AC-32.
- **Open decisions affecting detail:** OD-15, OD-19.

### SJ-02 — Teacher onboarding
- **Source happy path:** Register → provide evidence → submit → academic/admin review → approval → publish.
- **Source exceptions:** Needs information; rejected/suspended; expired evidence.
- **Requirement IDs (derived mapping):** BR-02, BR-14, BR-21.
- **UAT IDs (derived mapping):** AC-03, AC-05.
- **Open decisions affecting detail:** OD-01, OD-19.

### SJ-03 — Teacher discovery
- **Source happy path:** Filter subject/medium/time/fee → teacher/class detail → optional approved demo → choose batch.
- **Source exceptions:** No match; inactive teacher; class withdrawn; demo absent/failed (direct enrollment remains available).
- **Requirement IDs (derived mapping):** BR-03, BR-04, BR-05.
- **UAT IDs (derived mapping):** AC-05, AC-06, AC-07.
- **Open decisions affecting detail:** OD-02, OD-06.

### SJ-04 — Optional free demo
- **Source happy path:** Open teacher/class page → watch approved free recording OR skip → proceed directly to batch/checkout.
- **Source exceptions:** Unapproved/withdrawn/failed demo hidden/unavailable; no booking/payment/enrollment gate.
- **Requirement IDs (derived mapping):** BR-04, BR-03, BR-05.
- **UAT IDs (derived mapping):** AC-07, AC-31, AC-33.
- **Open decisions affecting detail:** OD-02, OD-06, OD-15.

### SJ-05 — Paid class
- **Source happy path:** Select batch (with or without demo) → order → gateway → verified payment → entitlement → authorized class join.
- **Source exceptions:** Cancelled payment; delayed/duplicate callback; insufficient seats.
- **Requirement IDs (derived mapping):** BR-05, BR-06.
- **UAT IDs (derived mapping):** AC-08, AC-09, AC-12, AC-13, AC-33.
- **Open decisions affecting detail:** OD-03, OD-04, OD-05, OD-06.

### SJ-06 — Live class
- **Source happy path:** Schedule → reminder → authorized join → session → attendance.
- **Source exceptions:** Provider outage; late join; rescheduled/cancelled.
- **Requirement IDs (derived mapping):** BR-05, BR-13.
- **UAT IDs (derived mapping):** AC-09, AC-10, AC-29.
- **Open decisions affecting detail:** OD-04, OD-06.

### SJ-07 — Material
- **Source happy path:** Open enrolled class → resource → permission check → download/play.
- **Source exceptions:** Expired entitlement; revoked resource; failed virus scan.
- **Requirement IDs (derived mapping):** BR-07, BR-05.
- **UAT IDs (derived mapping):** AC-11.
- **Open decisions affecting detail:** OD-06, OD-15.

### SJ-08 — Refund
- **Source happy path:** Request → review → decision → provider processing → ledger/entitlement adjustments.
- **Source exceptions:** Partial refund; rejection; gateway failure; dispute.
- **Requirement IDs (derived mapping):** BR-06, BR-14, BR-24.
- **UAT IDs (derived mapping):** AC-14, AC-15.
- **Open decisions affecting detail:** OD-03, OD-04, OD-05.

### SJ-09 — XACT practice
- **Source happy path:** Choose paper/year/subject/medium → answer → save → submit → review.
- **Source exceptions:** Translation unavailable; answer lock; interrupted save.
- **Requirement IDs (derived mapping):** BR-11, BR-18, BR-23.
- **UAT IDs (derived mapping):** AC-16, AC-17, AC-19, AC-20, AC-22, AC-25, AC-28.
- **Open decisions affecting detail:** OD-07, OD-08, OD-09, OD-10.

### SJ-10 — XACT custom mock
- **Source happy path:** Choose topics/difficulty/count/time → eligible pool → attempt → server score.
- **Source exceptions:** Insufficient questions; expired attempt; duplicate submit.
- **Requirement IDs (derived mapping):** BR-11, BR-18, BR-23.
- **UAT IDs (derived mapping):** AC-16, AC-17, AC-18, AC-19, AC-20, AC-22, AC-28.
- **Open decisions affecting detail:** OD-08, OD-09, OD-10, OD-11.

### SJ-11 — Assigned paper
- **Source happy path:** Teacher assignment → student notification → independent student attempt → result.
- **Source exceptions:** Unauthorized recipient; due date; attempt limits.
- **Requirement IDs (derived mapping):** BR-11, BR-19, BR-13.
- **UAT IDs (derived mapping):** AC-20, AC-21, AC-23, AC-24.
- **Open decisions affecting detail:** OD-09, OD-10, OD-11.

### SJ-12 — Teacher paper
- **Source happy path:** Filter approved bank → draft → preview → version → publish → assign → analyze.
- **Source exceptions:** Withdrawn question; invalid subject; correction/regrade.
- **Requirement IDs (derived mapping):** BR-18, BR-19, BR-11.
- **UAT IDs (derived mapping):** AC-16, AC-21, AC-23, AC-24, AC-25.
- **Open decisions affecting detail:** OD-07, OD-09, OD-10, OD-11.

### SJ-13 — Teacher explanation video
- **Source happy path:** Upload → processing → review → approved → signed playback.
- **Source exceptions:** Processing failure; rejection; rights complaint.
- **Requirement IDs (derived mapping):** BR-20, BR-18, BR-23.
- **UAT IDs (derived mapping):** AC-22, AC-26.
- **Open decisions affecting detail:** OD-07, OD-09, OD-12.

### SJ-14 — Admin operations
- **Source happy path:** Moderate teacher/demo/content/safety → decision → audit → notify.
- **Source exceptions:** Privilege denied; escalation breach; rollback.
- **Requirement IDs (derived mapping):** BR-02, BR-04, BR-14, BR-21, BR-24.
- **UAT IDs (derived mapping):** AC-05, AC-25, AC-27, AC-31.
- **Open decisions affecting detail:** OD-01, OD-02, OD-09, OD-15.

### SJ-15 — Help and safety
- **Source happy path:** Report concern → triage → restrict if necessary → owner review → outcome.
- **Source exceptions:** Emergency escalation; confidential evidence; abusive report.
- **Requirement IDs (derived mapping):** BR-21, BR-24, BR-13.
- **UAT IDs (derived mapping):** AC-27, AC-29.
- **Open decisions affecting detail:** OD-15.

### SJ-16 — Guardian touchpoint
- **Source happy path:** Request needed permission → verify guardian → protect evidence → controlled decision.
- **Source exceptions:** No consent; revoked consent; unreachable guardian.
- **Requirement IDs (derived mapping):** BR-21, BR-01, BR-22.
- **UAT IDs (derived mapping):** AC-04.
- **Open decisions affecting detail:** OD-15, OD-19.

## Journey-wide invariants

- Demo viewing is optional and free; no trial booking or demo completion prerequisite.
- Subject selection is a persistent preference; it does not create paid Enrollment or Entitlement.
- The backend, not the UI, enforces authorization, payment verification, exam timer/deadline and grading.
- Unapproved question translations/videos and private class resources must not be accessible.
- Guardian is a limited consent touchpoint; no current guardian dashboard.
- Release order and actual screen IDs still require review.
