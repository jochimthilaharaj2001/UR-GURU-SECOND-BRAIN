# Functional Requirements — BRD v6.2.2

> **UR GURU Second Brain — Development reference**  
> Source: [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](./UR_GURU_Full_Corrected_BRD_v6.2.2.pdf), consolidated corrected edition, 19 November 2026.  
> **Document status:** DRAFT EXTRACTION from BRD v6.2.2; source itself is a **review candidate pending stakeholder sign-off**.  
> **Use:** Requirements analysis / development planning; not independent approval or an executed test record.

## Baseline boundaries

- Initial implementation: Sri Lankan G.C.E. A/L **Grades 12–13**, **Biological Science (Bio)** and **Physical Science (Maths)** only (BRD pp. 1–3). Commerce, Arts and Technology are later/uncommitted.
- Delivery: **responsive Student/Teacher web** and **separate Admin web portal**; no native mobile app in the current release (pp. 1, 3).
- Assessments: **XACT**, formerly called *Exam Munnodi*; use XACT in active implementation artifacts (pp. 1–2, 11–12).
- **Free optional prerecorded DemoVideo** replaces all active scheduled live-trial bookings. Demo is not an Enrollment or paid entitlement prerequisite (pp. 5, 8, 12).
- Sequence: **R0 Foundation → R1 Marketplace → R2 XACT** is the working release baseline; XACT-first pilot is an open decision (p. 3; OD-18).
- This document is an organized extract. Where implementation detail is unspecified, see [`Open-Requirements.md`](./Open-Requirements.md); do not invent policies or claim release approval.

## Complete requirements register (24 IDs)

| ID | Name | Release | Priority | Source |
|---|---|---|---|---|
| BR-01 | Student onboarding, login, recovery, grade/stream/medium and subject selection | R0 | Must | p4–5 |
| BR-02 | Teacher onboarding, identity/qualification verification and suspension | R1 | Must | p4–5 |
| BR-03 | A/L teacher discovery, search and authorized public profiles | R1 | Must | p4–5 |
| BR-04 | Optional free prerecorded Demo Video Management | R1 | Must | p4–5 |
| BR-05 | Classes, batches, schedules, live sessions, attendance and cancellation | R1 | Must | p4–6 |
| BR-06 | Orders, payments, refunds, commissions, teacher earnings and payouts | R1 | Must | p4, p6 |
| BR-07 | Protected class learning-resource library with media versions | R1 | Must | p4, p6 |
| BR-08 | Lecture transcription with explicit recording permission | Later | Should | p3–4 |
| BR-09 | Teacher-reviewed AI revision notes | Later | Should | p3–4 |
| BR-10 | Personalized age-appropriate AI study assistance | Later | Should | p3–4 |
| BR-11 | Assessment scoring, history and topic progress | R2 | Must | p4, p6–7 |
| BR-12 | ExamPilot planning and reminders | Future | Future | p3–4 |
| BR-13 | Essential events and notifications | R0–R2 | Must | p4, p7 |
| BR-14 | Admin, academic, finance and operations review controls | R0–R2 | Must | p4, p7 |
| BR-15 | Academic counselling | Future | Future | p3–4 |
| BR-16 | Guardian dashboard | Future | Future | p3–4 |
| BR-17 | DataSmart offline/low-data improvements | Future | Future | p3–4, p8 |
| BR-18 | XACT question bank, practice and customizable mocks | R2 | Must | p4, p6–7 |
| BR-19 | Teacher paper drafts, versions and multi-student assignment | R2 | Must | p4, p7 |
| BR-20 | Teacher question-explanation videos with academic moderation | R2 staged | Must | p4, p7 |
| BR-21 | Age/guardian consent, child safety, complaints and case audit | R0–R1 | Must | p4–5, p7 |
| BR-22 | Identity assurance and NIC policy decision (if required) | R0–R1 | Must to define; verification conditional | p4–5 |
| BR-23 | Localization, scientific accessibility and content ingestion QA | R0–R2 | Must | p3–4, p8 |
| BR-24 | Customer support, operational exceptions and auditability | R1–R2 | Must | p4, p7 |

## Requirement details and implementation interpretation

### BR-01 — Student onboarding, login, recovery, grade/stream/medium and subject selection

- **Release / priority:** R0 / Must.
- **Source-based requirement summary:** Create secure student accounts and session recovery; capture Grade 12/13, available Bio/Maths stream, medium and valid subjects. Preserve StudentSubject independently of paid enrollment.
- **Journey reference(s):** SJ-01.
- **UAT reference(s):** AC-01, AC-02, AC-32.
- **Pending decision link(s):** OD-15, OD-19, OD-20.
- **BRD location:** p4–5 (register on p. 4).

### BR-02 — Teacher onboarding, identity/qualification verification and suspension

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Support Draft → Submitted → Needs Information → Approved/Rejected/Suspended with evidence, actor, time, reason. Only approved teachers become public and can publish.
- **Journey reference(s):** SJ-02.
- **UAT reference(s):** AC-05.
- **Pending decision link(s):** OD-01.
- **BRD location:** p4–5 (register on p. 4).

### BR-03 — A/L teacher discovery, search and authorized public profiles

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Show only approved active teacher/class listings; filter by available subject, medium, slot, price and optional demo availability. Keep private identity, bank and rosters hidden; ratings disabled without policy.
- **Journey reference(s):** SJ-03.
- **UAT reference(s):** AC-05, AC-06.
- **Pending decision link(s):** OD-01, OD-02.
- **BRD location:** p4–5 (register on p. 4).

### BR-04 — Optional free prerecorded Demo Video Management

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Teacher can submit class-linked prerecorded DemoVideo for moderation; approved active videos are free previews. Students may watch or skip; no booking, trial seat, payment, demo completion or enrollment prerequisite. Video failure cannot block direct purchase.
- **Journey reference(s):** SJ-03, SJ-04.
- **UAT reference(s):** AC-07, AC-31, AC-33.
- **Pending decision link(s):** OD-02, OD-06, OD-15.
- **BRD location:** p4–5 (register on p. 4).

### BR-05 — Classes, batches, schedules, live sessions, attendance and cancellation

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Approved offerings/batches contain subject, medium, syllabus, price, capacity, timezone and schedule. Enrollment reserves real seats transactionally; authorized short-lived live join credentials, attendance audit, cancellation/reschedule notifications.
- **Journey reference(s):** SJ-05, SJ-06.
- **UAT reference(s):** AC-08, AC-09, AC-10.
- **Pending decision link(s):** OD-04, OD-06.
- **BRD location:** p4–6 (register on p. 4).

### BR-06 — Orders, payments, refunds, commissions, teacher earnings and payouts

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Separate GMV from earned revenue; order line items and payment attempts; authenticated/idempotent gateway callbacks; append-only ledger; partial refund, earnings and payout review; entitlements only after verified payment.
- **Journey reference(s):** SJ-05, SJ-08.
- **UAT reference(s):** AC-08, AC-12, AC-13, AC-14, AC-15.
- **Pending decision link(s):** OD-03, OD-04, OD-05.
- **BRD location:** p4, p6 (register on p. 4).

### BR-07 — Protected class learning-resource library with media versions

- **Release / priority:** R1 / Must.
- **Source-based requirement summary:** Teachers upload class-bound PDFs/slides/notes/media with version and visibility; validate/scan files and protect private objects with authorized short-lived links. Keep provenance and revoke outdated resources.
- **Journey reference(s):** SJ-07.
- **UAT reference(s):** AC-11.
- **Pending decision link(s):** OD-06, OD-15.
- **BRD location:** p4, p6 (register on p. 4).

### BR-08 — Lecture transcription with explicit recording permission

- **Release / priority:** Later / Should.
- **Source-based requirement summary:** Conditional future transcription, requiring approved permissions and recording safeguards. Not a committed initial release capability.
- **Journey reference(s):** —.
- **UAT reference(s):** —.
- **Pending decision link(s):** OD-06, OD-15, OD-16.
- **BRD location:** p3–4 (register on p. 4).

### BR-09 — Teacher-reviewed AI revision notes

- **Release / priority:** Later / Should.
- **Source-based requirement summary:** Conditional future revision-note functionality with human teacher review and approved source/consent controls.
- **Journey reference(s):** —.
- **UAT reference(s):** —.
- **Pending decision link(s):** OD-15, OD-16.
- **BRD location:** p3–4 (register on p. 4).

### BR-10 — Personalized age-appropriate AI study assistance

- **Release / priority:** Later / Should.
- **Source-based requirement summary:** Conditional future AI study assistance subject to consent, budget and human-review controls.
- **Journey reference(s):** —.
- **UAT reference(s):** —.
- **Pending decision link(s):** OD-15, OD-16.
- **BRD location:** p3–4 (register on p. 4).

### BR-11 — Assessment scoring, history and topic progress

- **Release / priority:** R2 / Must.
- **Source-based requirement summary:** Preserve versioned answer/key and scoring snapshots, calculate marks server-side, expose authorized results/history/topic accuracy and explain low-data uncertainty.
- **Journey reference(s):** SJ-09, SJ-10, SJ-11.
- **UAT reference(s):** AC-19, AC-20, AC-21, AC-25.
- **Pending decision link(s):** OD-09, OD-10, OD-11.
- **BRD location:** p4, p6–7 (register on p. 4).

### BR-12 — ExamPilot planning and reminders

- **Release / priority:** Future / Future.
- **Source-based requirement summary:** Future academic planning/reminder capability; no committed R0–R2 implementation.
- **Journey reference(s):** —.
- **UAT reference(s):** —.
- **Pending decision link(s):** OD-14, OD-16.
- **BRD location:** p3–4 (register on p. 4).

### BR-13 — Essential events and notifications

- **Release / priority:** R0–R2 / Must.
- **Source-based requirement summary:** Deliver retry-safe verification, demo-review, enrollment, class, financial, assignment and safeguarding notifications without leaking unnecessary personal details.
- **Journey reference(s):** SJ-01, SJ-05, SJ-06, SJ-11, SJ-14.
- **UAT reference(s):** AC-09, AC-29.
- **Pending decision link(s):** OD-15, OD-16.
- **BRD location:** p4, p7 (register on p. 4).

### BR-14 — Admin, academic, finance and operations review controls

- **Release / priority:** R0–R2 / Must.
- **Source-based requirement summary:** Apply least-privilege approvals for teachers, demos, questions, keys, translations, payments and sensitive operations; every privileged change audited.
- **Journey reference(s):** SJ-14.
- **UAT reference(s):** AC-05, AC-16, AC-21, AC-27, AC-31.
- **Pending decision link(s):** OD-01, OD-07, OD-09.
- **BRD location:** p4, p7 (register on p. 4).

### BR-15 — Academic counselling

- **Release / priority:** Future / Future.
- **Source-based requirement summary:** Possible future capability; excluded from initial committed scope.
- **Journey reference(s):** —.
- **UAT reference(s):** —.
- **Pending decision link(s):** OD-14.
- **BRD location:** p3–4 (register on p. 4).

### BR-16 — Guardian dashboard

- **Release / priority:** Future / Future.
- **Source-based requirement summary:** Full guardian dashboard is explicitly future/uncommitted. Current scope includes only legally applicable guardian consent/contact touchpoints.
- **Journey reference(s):** SJ-16 (touchpoint only).
- **UAT reference(s):** AC-04 (consent only).
- **Pending decision link(s):** OD-15.
- **BRD location:** p3–4 (register on p. 4).

### BR-17 — DataSmart offline/low-data improvements

- **Release / priority:** Future / Future.
- **Source-based requirement summary:** Advanced low-data/offline features are future/uncommitted. Initial responsive-browser/low-bandwidth usability still applies.
- **Journey reference(s):** —.
- **UAT reference(s):** AC-28 (browser only).
- **Pending decision link(s):** OD-14, OD-16.
- **BRD location:** p3–4, p8 (register on p. 4).

### BR-18 — XACT question bank, practice and customizable mocks

- **Release / priority:** R2 / Must.
- **Source-based requirement summary:** Five-year past-paper rights and per-medium translations/keys require approval. Practice or configurable topics/difficulty/count/time; no duplicate canonical questions, immutable snapshots, autosave, controlled timers and server-side scoring.
- **Journey reference(s):** SJ-09, SJ-10.
- **UAT reference(s):** AC-16, AC-17, AC-18, AC-19, AC-20, AC-25.
- **Pending decision link(s):** OD-07, OD-08, OD-09, OD-10, OD-11.
- **BRD location:** p4, p6–7 (register on p. 4).

### BR-19 — Teacher paper drafts, versions and multi-student assignment

- **Release / priority:** R2 / Must.
- **Source-based requirement summary:** Approved subject teachers can compose from read-only approved question bank, publish immutable versions, assign to authorized students, track independent attempts and history.
- **Journey reference(s):** SJ-11, SJ-12.
- **UAT reference(s):** AC-21, AC-23, AC-24.
- **Pending decision link(s):** OD-09, OD-10.
- **BRD location:** p4, p7 (register on p. 4).

### BR-20 — Teacher question-explanation videos with academic moderation

- **Release / priority:** R2 staged / Must.
- **Source-based requirement summary:** Separate XACT explanation media from free ClassOffering demos; enforce licensing, upload/processing/review states, approved publication, signed playback and written fallback.
- **Journey reference(s):** SJ-13.
- **UAT reference(s):** AC-22, AC-26.
- **Pending decision link(s):** OD-07, OD-09, OD-12.
- **BRD location:** p4, p7 (register on p. 4).

### BR-21 — Age/guardian consent, child safety, complaints and case audit

- **Release / priority:** R0–R1 / Must.
- **Source-based requirement summary:** Purpose-specific revocable consent with policy/version evidence when legally required; safeguard minors, report/escalation and confidential case audit.
- **Journey reference(s):** SJ-01, SJ-15, SJ-16.
- **UAT reference(s):** AC-04, AC-27.
- **Pending decision link(s):** OD-15.
- **BRD location:** p4–5, p7 (register on p. 4).

### BR-22 — Identity assurance and NIC policy decision (if required)

- **Release / priority:** R0–R1 / Must to define; verification conditional.
- **Source-based requirement summary:** NIC-format match is not official identity verification. Product/legal must decide necessity, minor exemptions, alternatives, process and retention before implementation.
- **Journey reference(s):** SJ-01.
- **UAT reference(s):** AC-03.
- **Pending decision link(s):** OD-19.
- **BRD location:** p4–5 (register on p. 4).

### BR-23 — Localization, scientific accessibility and content ingestion QA

- **Release / priority:** R0–R2 / Must.
- **Source-based requirement summary:** Tamil/Sinhala/English only where approved content exists; separate review for each translation; ensure scientific diagrams/equations/options and responsive interfaces render accessibly.
- **Journey reference(s):** SJ-09, SJ-10.
- **UAT reference(s):** AC-17, AC-28.
- **Pending decision link(s):** OD-07, OD-08, OD-11.
- **BRD location:** p3–4, p8 (register on p. 4).

### BR-24 — Customer support, operational exceptions and auditability

- **Release / priority:** R1–R2 / Must.
- **Source-based requirement summary:** Accessible help/report paths, retry/error escalation, privacy-protected case evidence and operational event audit.
- **Journey reference(s):** SJ-14, SJ-15.
- **UAT reference(s):** AC-27, AC-29.
- **Pending decision link(s):** OD-15, OD-16.
- **BRD location:** p4, p7 (register on p. 4).

## Implementation guardrails

1. Subject selection (`StudentSubject`) **does not** imply a paid enrollment; the classroom purchase/entitlement flow is independent.
2. Public `DemoVideo` is not the same as private XACT `ExplanationVideo`. Do not implement active `TrialBooking`, `TrialAvailable`, `TrialCapacity`, or `Enrollment.TrialId`. Historical trial data, if any, requires an archival policy (BRD p. 8, 12).
3. Do not publish questions, answer keys, language translations or explanations without required rights and academic approval.
4. Class pricing, fees, rates, provider availability, exam presets, consent thresholds and NIC checks require explicit sign-off.
5. The illustrative ERD v1.2 entities in the BRD are **proposed**, not an approved physical SQL schema.
6. For detailed UAT criteria and mapped tests, consult [`Acceptance-Criteria.md`](./Acceptance-Criteria.md) and [`Requirements-Traceability.csv`](./Requirements-Traceability.csv).
