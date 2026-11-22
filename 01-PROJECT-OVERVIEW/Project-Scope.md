# UR GURU — Project Scope and Boundaries

| Field | Value |
|---|---|
| Document ID | `OV-03` |
| Version / prepared | Draft 1.0 / 19 November 2026 |
| Approval | **DRAFT — SCOPE REVIEW REQUIRED** |
| Proposed owner | Product Owner / Business Analyst (confirm) |
| Source | [BRD V6.1 §§3–5, 8, 11–15](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) |

## 1. Purpose

Define the current product boundary, phase-specific work, explicit exclusions, dependencies and change process for the UR GURU responsive-web implementation. **In scope** does not mean **already built**, **funded** or **approved for production**.

## 2. Overall product boundary

| Area | Current direction | Notes |
|---|---|---|
| Audience | Sri Lankan G.C.E. A/L students, Grade 12 and 13 | O/L / Grades 10–11 excluded |
| Academic streams | Science, Commerce, Arts, Technology | Subject/medium coverage is catalogue-dependent |
| Content mediums | Tamil, Sinhala and English | Only approved translations published |
| Primary actors | Student, Teacher, Administrator | Academic Reviewer has delegated moderation permissions, not necessarily a separate account type |
| Parent/guardian | Contact and legally required consent/assisted-payment touchpoints | No standalone guardian dashboard at Phase 1 |
| Application delivery | Responsive Student/Teacher web experience and separate Admin web portal | No native Flutter app in current delivery |
| Backend | Shared C# ASP.NET Core API direction | Actual service decomposition and environment details require technical sign-off |
| Database/provider | Relational DB needed; SQL Server is proposed in BRD | ZIP includes PostgreSQL SQL; **technology conflict pending resolution** |

## 3. Included — Phase 1 core marketplace (BRD release intent)

| Requirement | Included capability | Operational constraints |
|---|---|---|
| `BR-01` | Student registration, login/recovery, A/L profile, subjects, medium | Validation, consent, role-limited access |
| `BR-02` | Teacher application, qualification evidence and admin verification | Unapproved teacher cannot publish paid classes |
| `BR-03` | Teacher search/filter, verified profiles, published offering details | Do not expose sensitive teacher documents |
| `BR-04` | Eligible trial configuration, reservation, status/notification | Trial limits/no-shows remain open policy `OD-02` |
| `BR-05` | Class/batch setup, schedule, seat capacity, enrollment, sessions, attendance, reschedule/cancel | Only entitled students may join; provider/gate pending |
| `BR-06` | Orders, payment attempts, server verification, refunds, commission, earnings and payout accounting | Rates, eligibility, provider and settlement rules pending |
| `BR-07` | Class-linked uploaded resources and authorized access | Malware/file-type checks, restricted media access |
| `BR-13` | Essential booking/class/payment/safety notifications | Delivery provider/operational channels to decide |
| `BR-14` | Admin verification, catalog, moderation, finance exception review, audit | Privileged actions logged |
| `BR-21` | Consent, safety reporting, complaint handling and safeguarding | Legal/PDPA review required before public launch |

## 4. Included — Phase 2 Exam Munnodi (BRD release intent)

| Requirement | Included capability | Key gate |
|---|---|---|
| `BR-11` | Assessment and progress tracking | Meaningful/confidence-aware topic feedback |
| `BR-18` | Five-year A/L past-paper MCQ target, approved medium-specific question bank, topic/all-topic mocks, scoring, review | Content licensing, rights, translations and exam policy |
| `BR-19` | Teacher paper draft/preview/publish from approved read-only questions, multi-student assignment, results | Authorized subjects/students and independent per-student attempts |
| `BR-20` | Teacher-created explanation video production, academic review, publication and playback | Reviewer approval, IP/compensation, secure delivery |

The **five-year past-paper bank** is a **target**; the exact years, rights-cleared scope, mediums and completeness must be inventoried (`OD-07`, `OD-08`). It is not an assertion that all content already exists.

## 5. Later or future (not launch commitments)

| Requirement / area | Current release status |
|---|---|
| `BR-08` Tamil lecture transcription | Later; recording consent, budget and quality gated |
| `BR-09` Teacher-reviewed AI revision notes | Later; human review and safe data use required |
| `BR-10` Personalized AI learning assistant | Later; provider, safety and budget pending |
| `BR-12` ExamPilot academic journey | Future |
| `BR-15` Academic counselling | Future |
| `BR-16` Full guardian dashboard | Future; **distinct from Phase 1 consent** |
| `BR-17` DataSmart/offline and low-data features | Future, except reasonable low-bandwidth web quality testing |
| Native Android/iOS app | Not in current web-only delivery |
| Institute licensing, institutional portal, teacher paid Pro tier | Future/business case or pending decision |

## 6. Explicitly out of scope for current releases

- O/L/Grade 10/11 content, profiles, workflows and reporting.
- Public editing of reviewed source question-bank items by arbitrary teachers.
- Publishing unreviewed answer keys, AI-created official answers or unapproved explanation videos.
- Claiming mock scores are official examination results or guaranteeing exam performance.
- Native mobile apps, full guardian portal, student lending/EMI products, and unapproved institution features.
- Automatically enabled live recording or unrestricted exchange of personal contact details.
- Changing payment, commission, refunds, consent, content rights or exam scoring assumptions without approved decisions.

## 7. Non-functional requirements that apply across scope

From BRD `NFR-01`–`NFR-12`: TLS/security, privacy and safeguarding, financial/exam integrity, performance on low-data networks, reliability/resume handling, scale, backups/recovery, browser support, accessibility across Tamil/Sinhala/English, content quality, monitoring and maintainable/versioned APIs. Numeric targets and browser matrices require `OD-16` approval.

## 8. Phase dependencies and boundary rules

1. Approved teacher (`BR-02`) is a prerequisite for discovery/publication (`BR-03`, `BR-05`).
2. Capacity/session information (`BR-05`) informs trial (`BR-04`) and paid enrollment (`BR-06`).
3. Server-verified payments are prerequisite for entitlements; UI redirects alone never prove access rights.
4. Question rights, medium-specific academic approval and question-version safeguards precede Phase 2 mocks (`BR-18`).
5. Teacher paper assignment (`BR-19`) requires approved question bank and scoped learner authorization.
6. Explanation videos (`BR-20`) require review, content rights and delivery/provider setup.
7. AI features require a distinct release gate; **do not fold them into Phase 1 by implication**.

## 9. Scope decisions not yet resolved

| ID | Pending issue |
|---|---|
| `OD-01`–`OD-02` | Teacher vetting policy, trial eligibility and limits |
| `OD-03`–`OD-05` | Commission, refund/payout and gateway |
| `OD-06`–`OD-09` | Live/video provider, content rights, inventory and question governance |
| `OD-10`–`OD-13` | Exam defaults, difficulty, teacher video agreements and monetization |
| `OD-15` | Consent/PDPA/safeguarding legal sign-off |
| `OD-16` | Staffing, dates, budget, release/SLO targets |
| Technical decision | Database vendor and actual frontend framework require reconciliation with artifacts |

See [Open Decisions](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md). The 12-day planning document is a **draft target**, not a signed contract.

## 10. Change control and acceptance

For an added/changed requirement: (1) log request and business reason; (2) map affected `BR-xx`/`AC-xx`; (3) assess UI/DB/API/test, cost and data/privacy impact; (4) obtain Product Owner and relevant legal/finance/technical approval; (5) update governing documents and traceability; (6) implement only after the relevant approval. Verify test evidence and acceptance before declaring complete.

## Related files

[Project Summary](Project-Summary.md) · [User Roles](User-Roles.md) · [Modules and Features](Modules-and-Features.md) · [Release Roadmap](Release-Roadmap.md) · [BRD](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)
