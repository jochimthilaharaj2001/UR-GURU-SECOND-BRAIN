# Student Journeys — UR GURU

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

## Audience and scope

A/L Grade 12/13 students in the **initial Bio / Maths curricular release**. Subject choices depend on approved academic catalogue and medium availability. Exact screen IDs and route names are **not verified**.

## SJ-01 — Student registration and subject selection (R0)

**Source:** BRD §6.1 pp. 5 and §12 p. 8. **BR-01/21/22/23; candidate AC-01–04, AC-32.**

1. Student opens registration and provides minimum required account/contact information.
2. System performs contact verification using the approved process; invalid or expired codes show a retry/recovery path without leaking account existence.
3. Student selects Grade 12 or 13 and one currently available stream: Biological Science or Physical Science (Maths).
4. Student chooses medium and one or more eligible subjects; backend validates stream/subject/year combinations.
5. If legally/policy required, route to purpose-specific guardian consent before completing the protected action; do not assume every minor must supply NIC.
6. Persist valid selections via **StudentSubject** with uniqueness by student, subject and academic year.
7. Student reaches their account/dashboard when approved access conditions are satisfied.

**Not allowed:** O/L/Grades 10–11; future streams advertised as available; subject selection creating enrollment, payment or class access.

**Exceptions:** Duplicate account, invalid OTP, invalid stream-subject, duplicate active subject/year selection, locked/suspended account, pending consent, interrupted verification. Show actionable status; avoid account enumeration.

**Proposed UI states:** Registration form; code confirmation; grade/stream/medium selector; subject picker; conditional consent; verification pending/blocked; dashboard. These are **screen concepts**, not approved IDs.

## SJ-03 + SJ-04 — Discovery and optional demo (R1)

**Source:** BRD §§6.2–6.3 p. 5 and §12 pp. 8–9. **BR-03/04; candidate AC-05–07, AC-31, AC-33.**

1. Filter approved teachers/classes by eligible subject, medium, time, fee and approved demo availability.
2. Open authorized public teacher/class details (private teacher bank and learner roster fields must not appear).
3. If a public, approved, published demo exists, student **may watch** it for free; otherwise **skip**.
4. Continue to select a batch **either way**, even when demo media is unavailable or playback fails.

**Never create** TrialBooking, trial attendance/capacity, OrderHeader, PaymentAttempt, Enrollment or Entitlement merely for preview.

**Exceptions:** No matching classes; teacher suspended/inactive; withdrawn class; no demo; failed or unapproved demo; rights-invalid video. Always preserve route to eligible direct enrollment.

## SJ-05 — Paid class enrollment (R1)

**Source:** BRD §§6.4, 7 and §12 p. 9. **BR-05/06; candidate AC-08, AC-12, AC-13.**

1. Choose available `ClassBatch` without needing to watch a demo.
2. Review total/currency, class details, charges and **approved** refund/cancellation terms before checkout.
3. Create order and initiate payment through selected contracted gateway.
4. Backend verifies signed/authenticated provider result and handles duplicate/delayed callbacks idempotently.
5. Grant paid `Entitlement` / confirmed `Enrollment` only under approved seat/payment policy; join live class within authorized window.

**Exceptions:** Full batch, simultaneous enrollment, failed/cancelled payment, delayed provider callback, duplicate notification; no free demo can reserve a seat.

**Open decisions:** Commission/refund rules OD-03/04, gateway OD-05, provider OD-06.

## SJ-06 — Attend live class (R1)

**Source:** BRD §§6.4, 9, 12. **BR-05/13; candidate AC-09/10.**

Scheduled session → reminder → server-side membership/entitlement/join-window check → short-lived join credential → session → attendance join/leave tracking.

**Exceptions:** Provider outage, late join, teacher/session cancellation or reschedule; show meaningful state and notifications, follow **approved** continuity and refund policy. Do not promise automatic refunds or recording access.

## SJ-07 — Class materials (R1)

**Source:** BRD §6.5 and §12 p. 9. **BR-07; candidate AC-11.**

Open enrolled class → select approved resource version → backend checks permission → short-lived authorized access → download/play. No guessed/shared URL bypass. Handle expired entitlement, revoked resource and failed scan.

## SJ-09 / SJ-10 / SJ-11 — XACT (R2)

See [XACT-Journeys.md](XACT-Journeys.md). Student may practise approved five-year question sets, configure topic-based/all-topic mocks, and complete independently authorized teacher assignments. Per-medium question versions must be approved; no silent language fallback. Autosave, deadline and score are server-governed. Results and explanations follow approved policy.

## SJ-15 / SJ-16 — Report/safeguarding and conditional consent

Students need a protected support/escalation route. Guardian consent is conditional and purpose-specific, not a guardian dashboard. See [Guardian-Consent-Journey.md](Guardian-Consent-Journey.md) and [Exception-and-UI-States.md](Exception-and-UI-States.md).

## Student handoff checklist

- [ ] Actual screen IDs and prototype screenshots attached to journeys.
- [ ] Requirement-to-API/DB mapping verified against approved contracts.
- [ ] Empty, loading, success, failure, access-denied and retry states designed.
- [ ] Tamil/Sinhala content and maths notation tested on target browsers.
- [ ] All referenced policy/vendor decisions approved before release.
