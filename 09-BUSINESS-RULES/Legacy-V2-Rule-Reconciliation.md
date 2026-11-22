# Legacy Business Rules V2.0 Reconciliation

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Authority and scope
The original `UR_GURU_Business_Rules_V2_0.docx` contains **BR-001 through BR-077** against an older BRD baseline. These identifiers must not be confused with the **BRD V6.2.2 requirements `BR-01` through `BR-24`** or the new **`UG-RULE-###`** IDs.

The old DOCX is retained **unchanged as historical evidence**. The table below is a *migration/review aid*, not a blanket approval or a claim of one-to-one mapping.

| Legacy ID | Original rule summary | V6.2.2 disposition / check |
|---|---|---|
| BR-001 | Allow A/L students only to register | MODIFIED: launch Bio/Maths only, Grade 12–13 |
| BR-002 | Validate email address format | REVALIDATE: Legacy source; check current BRD/approval |
| BR-003 | Prevent duplicate accounts with the same email | REVALIDATE: Legacy source; check current BRD/approval |
| BR-004 | Validate Sri Lankan mobile phone format | REVALIDATE: Legacy source; check current BRD/approval |
| BR-005 | Require password length of at least eight characters; complexity to be approved | REVALIDATE: Legacy source; check current BRD/approval |
| BR-006 | Require selection of an A/L stream | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-007 | Present only subjects valid for selected A/L stream | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-008 | Require teacher registration profile data | REVALIDATE: Legacy source; check current BRD/approval |
| BR-009 | Require qualifications and teaching subject details | REVALIDATE: Legacy source; check current BRD/approval |
| BR-010 | Teacher public visibility requires admin verification | REVALIDATE: Legacy source; check current BRD/approval |
| BR-011 | Restrict teacher teaching subjects to A/L catalogue | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-012 | Allow teacher management of own pricing and schedule under policy | REVALIDATE: Legacy source; check current BRD/approval |
| BR-013 | Only approved teachers may publish paid classes | REVALIDATE: Legacy source; check current BRD/approval |
| BR-014 | Book only available classes | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-015 | Never exceed confirmed class seat capacity | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-016 | Prevent duplicate booking for same student/class schedule | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-017 | Confirm paid booking only after successful verified payment | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-018 | Limit individual class to one learner | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-019 | Enforce teacher-set group class capacity | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-020 | Disallow bookings to cancelled classes | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-021 | Verify payment before confirming paid booking | REVALIDATE: Legacy source; check current BRD/approval |
| BR-022 | Verify gateway responses securely on backend | REVALIDATE: Legacy source; check current BRD/approval |
| BR-023 | Do not confirm failed-payment booking | REVALIDATE: Legacy source; check current BRD/approval |
| BR-024 | Record successful payment transaction | REVALIDATE: Legacy source; check current BRD/approval |
| BR-025 | Use initial 15% tuition commission as working configuration subject to finance approval | NOT APPROVED: working 15% commission superseded by OD-03 pending |
| BR-026 | Commission rate configurable by authorized admin | REVALIDATE: Legacy source; check current BRD/approval |
| BR-027 | Adjust teacher earnings when payment/refund status changes | REVALIDATE: Legacy source; check current BRD/approval |
| BR-028 | Identify affected confirmed bookings when teacher cancels class | REVALIDATE: Legacy source; check current BRD/approval |
| BR-029 | Process policy-eligible student refunds | MODIFIED: finance; details OD-03/04/05 |
| BR-030 | Prevent total pending/completed refunds exceeding refundable balance | MODIFIED: finance; details OD-03/04/05 |
| BR-031 | Track refund request, approval, processing and final status | MODIFIED: finance; details OD-03/04/05 |
| BR-032 | Notify student after completed refund | MODIFIED: finance; details OD-03/04/05 |
| BR-033 | Allow student to access assessments for own A/L subjects | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-034 | Define start time and duration for timed exams | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-035 | Score auto-gradable exams by configured marking rules | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-036 | Allow teacher manual grading where applicable | OUT OF CURRENT XACT MCQ SCOPE: manual grading unspecified |
| BR-037 | Verify payment prior to granting paid mock exam access (if launched) | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-038 | Protect private assessment results across students | REVALIDATE: Legacy source; check current BRD/approval |
| BR-039 | Capture parent/guardian name as one text field on student profile only | MODIFIED: guardian contact/consent subject to OD-15; no full guardian dashboard |
| BR-040 | Capture and validate one Sri Lankan parent/guardian phone contact field | MODIFIED: guardian contact/consent subject to OD-15; no full guardian dashboard |
| BR-041 | Save parent contact details on corresponding student profile; prevent disclosure to other students | MODIFIED: guardian contact/consent subject to OD-15; no full guardian dashboard |
| BR-042 | Do not provide guardian registration, login, dashboard, attendance, results or payment view | MODIFIED: guardian contact/consent subject to OD-15; no full guardian dashboard |
| BR-043 | Admin may approve/reject teacher applications | REVALIDATE: Legacy source; check current BRD/approval |
| BR-044 | Admin may review refund requests | REVALIDATE: Legacy source; check current BRD/approval |
| BR-045 | Require admin verification before teacher payout processing | REVALIDATE: Legacy source; check current BRD/approval |
| BR-046 | Allow authorized admin to configure commission | REVALIDATE: Legacy source; check current BRD/approval |
| BR-047 | Allow admin to manage A/L streams and subjects | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-048 | Audit important financial actions | REVALIDATE: Legacy source; check current BRD/approval |
| BR-049 | Only approved, active, rights-cleared question versions may enter student mocks or teacher papers | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-050 | Question selection must match stream, subject, syllabus version, chosen topics and difficulty | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-051 | Selected-topic mocks use selected eligible topics only; all-topics mocks use configured syllabus scope | MODIFIED: current Bio/Maths, syllabus/medium availability and translation eligibility |
| BR-052 | Prevent duplicate questions within a generated mock and persist its question set | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-053 | When eligible questions are insufficient, return shortage and valid options; never fabricate items | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-054 | Preserve immutable question/answer-key version references or snapshots for historical attempts | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-055 | Corrected or withdrawn questions require versioned approval and controlled regrade decision | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-056 | Auto-grade submitted MCQs on server only; never expose correct answers before allowed review | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-057 | Save answers with ownership, attempt-state, timer and idempotency controls | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-058 | Make final submission idempotent and prevent duplicate final attempts | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-059 | Show total marks, correct/incorrect/unanswered and topic breakdown after permitted submission | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-060 | Only approved teachers can build/publish papers from approved predefined questions | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-061 | Allow draft, preview, validation, publish and immutable paper-version records | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-062 | Permit multi-student assignment only to authorized selected students or owned cohorts | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-063 | Enforce assignment opening/closing windows, due dates and configured attempt limits | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-064 | Keep separate attempt/result record for each assigned student and each assignment instance | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-065 | Restrict assignment and result access to assigned student, assigning authorized teacher and admins | REVALIDATE AS XACT: BRD §8, exact exam rules OD-10/11 |
| BR-066 | Require creator/question linkage, metadata and review status for submitted explanation video | MODIFIED: academic rights/approved explanation; separately class DemoVideo vs XACT video |
| BR-067 | Publish video only after academic, quality, rights and safeguarding review | MODIFIED: academic rights/approved explanation; separately class DemoVideo vs XACT video |
| BR-068 | Provide written explanation fallback when approved video is unavailable | MODIFIED: academic rights/approved explanation; separately class DemoVideo vs XACT video |
| BR-069 | Activate paid Exam Munnodi entitlement only on server-verified payment success | CONDITIONAL: paid XACT future pricing OD-13 |
| BR-070 | Prevent duplicate payment orders/entitlements under repeated callbacks and idempotency keys | CONDITIONAL: paid XACT future pricing OD-13 |
| BR-071 | Keep tuition commission/ledger separate from digital-product revenue/entitlements | CONDITIONAL: paid XACT future pricing OD-13 |
| BR-072 | Use approved separately defined pricing, limits, refunds and teacher-video compensation for exam products | CONDITIONAL: paid XACT future pricing OD-13 |
| BR-073 | Payout creation, approval and settlement must be audited and reconciled; maker-checker thresholds pending | MODIFIED: finance; details OD-03/04/05 |
| BR-074 | Seat holds, reschedule/no-show windows and booking races must follow approved policy and atomic capacity control | MODIFIED: enrollment/batch controls; do not apply trial booking logic |
| BR-075 | Role- and resource-level checks required on all protected student, teacher and admin operations | REVALIDATE: Legacy source; check current BRD/approval |
| BR-076 | Past-paper reproduction, explanations and videos require verified use rights before publication | MODIFIED: academic rights/approved explanation; separately class DemoVideo vs XACT video |
| BR-077 | Collect parent name/phone only; necessity, consent, retention and access must be approved | MODIFIED: guardian contact/consent subject to OD-15; no full guardian dashboard |

## Specific legacy hazards
- Historic BR-025 says **15% working commission**. BRD V6.2.2 OD-03 has no approved rate; do **not** code 15% as signed-off.
- BR-074 concerns old seat-hold/reschedule policies. In current BR-04 no scheduled trial booking exists. Paid batch capacity still needs transactional control.
- Generic four-stream launch mentions from older V2 have been superseded by the Bio/Maths first release.
- BR-039 to BR-042 name/phone-only language does not remove the newer consent-event and safeguarding requirements.
- Old BRD `Exam Munnodi` name is now `XACT`; numbering is not reused as current BRD requirement IDs.
- All 77 rows are historical; current `UG-RULE-###` entries are traceable proposed interpretation of V6.2.2, pending sign-off.
