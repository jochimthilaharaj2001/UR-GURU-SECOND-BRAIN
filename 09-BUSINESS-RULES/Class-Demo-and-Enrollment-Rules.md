# Classes, Optional Demo and Enrollment Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Critical scope correction
**BR-04 = optional free prerecorded DemoVideo, not scheduled live trial.** Replace any earlier `TrialBooking`, `TrialCapacity`, trial no-show or trial-to-paid policies as active requirements. Retain old terms only in the historical rule reconciliation and migration notes.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-014 | Class demo is an optional free prerecorded preview linked to a teacher-owned ClassOffering, not a scheduled live trial booking. | BRD §6.3 p.5, §10 p.8 | AC-07, AC-33 | Review baseline |
| UG-RULE-015 | Students may watch an approved demo or skip it; neither viewing nor completion can gate checkout, enrollment or live-class joining. | BRD §6.3 p.5 | AC-07, AC-33 | Review baseline |
| UG-RULE-016 | A ClassOffering may contain zero or more demo videos; missing, failed, withdrawn or pending demos must not block direct enrollment. | BRD §6.3 p.5 | AC-07 | Review baseline |
| UG-RULE-017 | Approved, published, active demo media may be publicly previewed free; rejected, withdrawn or processing demos must not be playable. | BRD §6.3 p.5 | AC-31 | Review baseline |
| UG-RULE-018 | Only approved teachers submit class-linked demos; content must record title, language/medium, media reference, duration, rights attestation and creator. | BRD §6.3 p.5 | AC-31 | Review baseline |
| UG-RULE-019 | A demo uploader cannot approve their own demo; review and publish/withdraw actions require authorized reviewers and audit history. | BRD §6.3 p.5 | AC-31 | Review baseline |
| UG-RULE-020 | Demo video storage and preview delivery must be isolated from paid class resources and XACT explanation media. | BRD §6.3 p.5 | AC-11, AC-31 | Review baseline |
| UG-RULE-021 | Demo preview must not create TrialBooking, OrderHeader, Enrollment, PaymentAttempt, paid Entitlement or reserve a batch seat. | BRD §6.3 p.5, §7 p.6, §10 p.8 | AC-07, AC-33 | Review baseline |
| UG-RULE-022 | Public demo viewer login requirement, viewing analytics, duration and rights policy are unresolved; do not require or track these without approval. | BRD §6.3 p.5, §14 p.10 | AC-07 | Pending policy OD-02 |
| UG-RULE-023 | Transactional seat capacity applies only to actual paid enrollment; prevent duplicate seats, overbooking and double charges. | BRD §6.4 p.5 | AC-08 | Review baseline |
| UG-RULE-024 | Each class offering/batch must carry authorized teacher, subject, medium, syllabus, price, capacity, timezone, schedule, lifecycle window and status. | BRD §6.4 p.5 | AC-08 | Review baseline |
| UG-RULE-025 | Join credentials for live provider must be short-lived and issued only to authorized users within configured join windows. | BRD §6.4 p.5 | AC-09 | Review baseline |
| UG-RULE-026 | Attendance records join/leave details; authorized corrections require an audit trail. | BRD §6.4 p.6 | AC-10 | Review baseline |
| UG-RULE-027 | Class cancellation/rescheduling must notify affected students and apply an approved credit/refund policy; do not promise automatic refunds. | BRD §6.4 p.6 | AC-09, AC-14 | Pending policy OD-04 |
| UG-RULE-028 | Class resources require validation/scanning and authorized class-linked access; revoked content must stop new distribution. | BRD §6.5 p.6 | AC-11 | Review baseline |
| UG-RULE-029 | Private learning media must use protected object storage and short-lived backend-authorized links; guessed URLs must not bypass access. | BRD §6.5 p.6 | AC-11 | Review baseline |

## Negative-path tests
- User skips demo and still reaches batch selection and checkout.
- Demo is absent, processing, rejected or fails playback; direct enrollment remains available.
- Repeated enrollment/payment callback does not overbook a full batch.
- Unauthorized learner cannot join live provider session.

## Policy boundaries
Demo login/analytics/duration/rights: **OD-02**. Refund/cancellation: **OD-04**. Live/video provider: **OD-06**. No automatic refund deadline or trial seat-hold duration should be invented.
