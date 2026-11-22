# System Flow — End-to-End Journeys

**Document:** SYS-FLOW-01 | **Status:** DRAFT — extracted/mapped from BRD v6.2.2, sign-off pending | **Last reviewed:** 2026-11-19

## 1. Request lifecycle (conceptual)

1. Student/Teacher enters **responsive web** or a privileged user enters **Admin web** (BRD p. 1).
2. Browser communicates over TLS with the **proposed shared ASP.NET Core Modular Monolith API** (one backend deployment with in-process R0/R1/R2 modules). This is a candidate architecture only; final framework, hosting and database decisions remain **PENDING OD-20**.
3. Backend authenticates a session as applicable and **authorizes role + ownership/membership**, regardless of which UI elements are visible (BRD p. 4).
4. Relevant logical module validates approved policy, performs transactional data operations and, where appropriate, initiates guarded provider integrations.
5. Response carries only content authorized for the caller. Event delivery, ledger reconciliation and media processing must be auditable and retry-safe where specified (pp. 6–9).
6. Error states explicitly distinguish rejected, unavailable, interrupted and retryable operations. No unsafe assumption of success from browser redirects.

## 2. Student account and subject selection — SJ-01

`Register → verify contact → choose Grade 12/13 → choose available Bio/Maths stream + medium → choose eligible subjects → complete consent (if legally required) → dashboard`

- Validate grade, active stream/subject combinations and availability on server (BR-01; p. 5).
- Persist selected subject(s) through proposed `StudentSubject` with student/subject/year uniqueness. **A subject selection is not class enrollment** (pp. 3, 5).
- Account states and recovery path are recorded; **NIC policy is not finalized** and a well-formed NIC does not mean government-verified identity (p. 5; OD-19).
- Guardian consent, when required, records purpose/policy version and is revocable (p. 5; OD-15).
- Negative states: invalid verification code, duplicate account, suspended account, invalid stream-subject selection (SJ-01, p. 8).

## 3. Teacher onboarding and discovery — SJ-02/SJ-03

`Teacher creates account → submits evidence → reviewer verifies → Approved → eligible classes/public profiles can be listed`

- Teacher lifecycle: Draft, Submitted, Needs Information, Approved, Rejected, Suspended; track actor, reason and timestamps (p. 5).
- Only **approved active** teachers/classes are visible publicly; private identity, banking and student roster data are excluded (pp. 4–5).
- Discovery filters: subject, medium, time, price and availability of an **approved optional demo**. Ratings remain disabled without future approval (p. 5).

## 4. Optional FREE recorded demo — SJ-04 (BR-04)

`Open approved teacher/class page → [WATCH approved published prerecorded demo OR SKIP] → class batch selection / checkout`

**Critical rules** (BRD pp. 5–6 and 12):

- Demo is class-linked **prerecorded** media; **not** a live trial, a seat reservation or attendance.
- `ClassOffering 1 → 0..N DemoVideo` is a **proposed** ERD link; demo is linked to media asset and moderation approval.
- Only approved teachers submit demos; separate authorized reviewer approves/publishes; no teacher self-approval.
- Public preview is free, subject to yet-to-be-approved viewer account/consent policy (OD-02).
- If absent, rejected, processing, withdrawn or playback fails, **direct enrollment remains possible**.
- Demo playback must not create `TrialBooking`, `Enrollment`, `PaymentAttempt` or an `Entitlement`, nor gate checkout on completion.

## 5. Paid class enrollment — SJ-05, live session — SJ-06

`Select batch → create order → payment gateway → verified payment/callback → authorized entitlement + transactional seat/enrollment → session join token in valid window`

- Capacity and paid access must be checked and updated safely with duplicate/overbooking protection (BRD pp. 5–6).
- **Payment provider** response and webhooks require server validation and **idempotent processing**; never trust client redirect alone (p. 6; AC-12/13).
- Only authorized enrolled students receive short-lived live join credentials. Record attendance join/leave; any manual correction is audited (pp. 5–6).
- Provider outage, delayed payment callback, insufficient seats, cancellation/reschedule produce explicit states and notices (SJ-05/06, p. 9).
- **Order of seat reservation and payment handling is conceptual here** and needs an approved concrete transaction design (OD-04/05/20).

## 6. Materials and refunds — SJ-07/SJ-08

- **Materials:** enrolled student → resource access request → backend entitlement/class authorization → short-lived signed asset URL; virus/media validation and resource versioning applied (p. 6).
- **Refund:** authorized request → review/decision → provider processing → linked **append-only** ledger corrections, earnings and entitlement adjustments. Partial refunds do not always revoke full access (p. 6).
- Refund time limits, fees and payouts remain **PENDING OD-03/04/05**; do not infer them.

## 7. XACT practice, custom mock, assignment — SJ-09 to SJ-13

- **Practice:** select paper/year/subject/medium → approved question version → answer/autosave → submit → server scoring → authorized explanation/result.
- **Custom mock:** selected topics/all topics + approved difficulty/count/time presets → server constructs eligible unique canonical question set → immutable question/key snapshot → attempt → submit/expire → score and topic breakdown.
- **Teacher assigned paper:** authorized teacher selects approved questions → drafts and versions paper → assigns specified students → per-recipient authorized attempt → teacher sees only authorized results.
- **Explanation video:** authorized teacher uploads rights-cleared video → processing → separate academic/content review → approved publication → entitlement-gated signed playback; written explanation fallback.
- No translation fallback across Tamil/Sinhala/English without independently approved content. No question whose rights/key/version/translation are unapproved (pp. 3, 6–7).
- Autosave and deadline are server-authoritative; duplicate submits are idempotent; exact duration, retakes and grace policy **PENDING OD-10** (pp. 6–7, 10).

## 8. Admin, notifications and safety — SJ-14 to SJ-16

- Admin or scoped academic/finance reviewer performs approval/moderation/refund/exception action → authorization check → auditable decision → notification event (pp. 4, 7, 9).
- Notification delivery retries independently (outbox/consumer retries are in proposed reliability verification method, p. 8).
- Safety reports go to authorized owners with confidentiality; do not leak case evidence into general alerts.
- Guardian contact applies only to legally required consent/communications, **not a standalone guardian portal**.

## 9. Release / scope matrix

| Lane | Primary flows | Status |
|---|---|---|
| R0 | Identity, curriculum, subject selection, safeguarding, notifications/audit foundations | Proposed gate; BRD p. 3 |
| R1 | Teacher marketplace, free demo, batch/enrollment, live classes, materials, payments/refunds/earnings | Proposed gate; BRD p. 3 |
| R2 | XACT content, practice, mocks, assignment, versioned scoring/explanations | Proposed gate; BRD p. 3 |
| Later | Transcription, AI notes/study support, ExamPilot, DataSmart | Not a launch commitment |

**Refs:** BRD v6.2.2 pp. 2–10 (especially sections 2, 5–9, 12–13), Appendix C p. 12.
