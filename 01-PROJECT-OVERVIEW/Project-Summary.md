# UR GURU — Project Summary

| Field | Value |
|---|---|
| Document ID | `OV-01` |
| Version / prepared | Draft 1.0 / 19 November 2026 |
| Approval | **DRAFT — NOT SIGNED OFF** |
| Document owner | Project Manager / Product Owner — **owner to confirm** |
| Source baseline | [BRD V6.1 corrected review baseline](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md), sections 1–6, 8, 12–15 |
| Supporting sources | [Decision register](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md), [project memory](../19-CHAT-MEMORY/CONSOLIDATED_PROJECT_MEMORY_2026-11-17.md) (historical context only) |

> **Use rule:** This overview summarizes the repository's reviewed requirements; it is **not** a signed requirements baseline. If this page differs from an approved BRD or a signed decision, escalate the discrepancy. Do not implement unresolved policy based on this overview alone.

## 1. Executive summary

**UR GURU** is a Sri Lankan **G.C.E. Advanced Level (A/L)-only** learning and tuition marketplace for **Grade 12 and Grade 13** students. Its current product direction is a **responsive web application** for students and teachers, plus a separate administrator web portal connected to a shared backend.

The product combines two service areas:

1. **Live tuition marketplace (Phase 1):** students discover administrator-verified teachers, find A/L subject offerings, use eligible trials, enroll/pay, attend authorized live classes, receive learning resources and notifications, and view their own learning activity.
2. **Exam Munnodi (Phase 2):** students practise curated A/L past-paper MCQs, configure topic- or all-topic mock exams, view server-scored results and explanations; verified teachers build and assign papers from an approved question bank. Teacher-created video explanations require academic/content approval before publication.

The platform's tuition model distinguishes **gross student tuition receipts (GMV)** from **UR GURU earned commission**. Additional Exam Munnodi monetization proposals are subject to approval.

## 2. Problem and opportunity

The product addresses needs identified in the BRD (these are product premises, **not yet quantified market research findings**):

- A/L students need a coherent way to discover appropriately verified teachers by subject, medium, timetable and price.
- Students and teachers need reliable scheduling, enrolment, permission-controlled classroom access and transparent payment states.
- A/L exam preparation needs structured MCQ practice with reviewed answer keys, explanations, historical attempt tracking and topic-level feedback.
- Teachers need authorized tools to reuse approved questions and distribute assessments to multiple learners without exposing other students' private results.
- Operations need auditable teacher verification, safeguarding, content review, payment/refund handling and administrative controls.

## 3. Target audience and curriculum

| Dimension | Current project direction |
|---|---|
| Country / curriculum | Sri Lanka, G.C.E. Advanced Level |
| Student grades | 12 and 13 only |
| Stream groups | Science, Commerce, Arts, Technology |
| Language mediums | Tamil, Sinhala and English (with approved subject/content availability) |
| Main application roles | Student, Teacher, Administrator |
| Guardian | Contact/consent touchpoints where required; **no stand-alone guardian dashboard at launch** |
| Client platforms | Responsive browser web; **no native mobile application in current delivery scope** |

Do not treat legacy O/L/Grade 10–11 content, mobile-app designs or a guardian portal as current launch requirements.

## 4. Product pillars

| Pillar | What users can do | Requirement references |
|---|---|---|
| Trustworthy educator marketplace | Teacher onboarding, verification, subject/medium discovery, public approved profiles | `BR-02`, `BR-03` |
| Tuition operations | Trials, course/class offerings, capacity, scheduled sessions, enrolment and attendance | `BR-04`, `BR-05` |
| Financial integrity | Orders, server-verified payments, refunds, commission, earnings and payout visibility | `BR-06` |
| Learning content & communication | Authorized class resources and essential notifications | `BR-07`, `BR-13` |
| Safe administration | Catalog control, moderation, consent, safeguarding, audit and support | `BR-14`, `BR-21` |
| Exam Munnodi | Approved MCQs, multilingual/question-version safeguards, mocks, results, teacher papers and reviewed explanation videos | `BR-11`, `BR-18`–`BR-20` |

## 5. Representative journeys

**Student tuition:** register/login → choose Grade 12/13 and A/L stream/subjects/medium → discover approved teacher → inspect class/trial → book and pay where required → receive authorized class access → attend session → access approved resources.

**Teacher tuition:** apply and submit verification evidence → administrator approves → create class/batch and timetable → manage authorized students → conduct sessions → manage resources → view earnings/payout statuses.

**Exam Munnodi student:** choose subject/medium → topics or all topics and difficulty → start valid mock → answer/submit → see server-scored result and topic breakdown → review approved written/video explanations.

**Teacher assessment:** find approved read-only question bank items → draft/preview paper → publish → assign multiple authorized students → view separate submissions and permitted results.

Detailed rules are in [BRD §7–9](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) and [Exam Munnodi specification](../17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md).

## 6. Business value and measures (definitions proposed; numerical targets TBD)

| Value objective | Candidate measure | Owner / target status |
|---|---|---|
| Increase qualified educator supply | Number and share of verified, active teachers with published A/L classes | Product/Operations — **TBD** |
| Convert discovery into tuition | Search → class detail → trial/booking → paid enrollment funnel | Product/Finance — **TBD** |
| Deliver dependable live teaching | Authorized join success; session completion; attendance recording reliability | Engineering/Operations — **TBD** |
| Support exam learning | Successful mock completions; valid question coverage; topic-level review usage | Academic/Product — **TBD** |
| Maintain financial control | Reconciliation exceptions; verified payment-to-entitlement accuracy; refund/payout audit coverage | Finance — **TBD** |
| Protect learners | Teacher review compliance; safeguarding handling and role-based-access test results | Legal/Operations/Engineering — **TBD** |

These are **measurement suggestions**, not pre-approved performance targets or guaranteed outcomes.

## 7. Key delivery boundaries

- **Phase 1:** trusted marketplace and safety/payment essentials.
- **Phase 2:** Exam Munnodi question bank, mocks, papers, scoring and moderated video explanations.
- **Later:** consent- and budget-gated lecture transcription, teacher-reviewed AI notes and academic assistance.
- **Future / not committed:** expanded ExamPilot, offline/DataSmart, institutions, guardian dashboard, native apps.

See [Project Scope](Project-Scope.md) and [Release Roadmap](Release-Roadmap.md).

## 8. Major dependencies and open questions

Formal decisions are still needed on the commission rate, refund/payout rules, payment gateway, live video provider, academic content rights, teacher video compensation, exam rules, safeguarding/legal reviews, database/vendor selection and release date. Treat these as **PENDING APPROVAL**, not coding defaults. Refer to [OD-01–OD-16](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md).

## 9. What this document does not claim

- It is **not** evidence that the market size or adoption funnel has been validated.
- It is **not** a sign-off on pricing, refunds, legal compliance or provider selection.
- It is **not** an assertion that all listed features are already implemented or tested.
- It does **not** override the BRD V6.1 corrected review baseline or the final approved specification once signed.
