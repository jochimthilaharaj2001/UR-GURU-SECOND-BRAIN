# Teacher Journeys — UR GURU

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

## SJ-02 — Teacher onboarding and verification (R1)

**Source:** BRD §6.2 p. 5, §12 p. 8. **BR-02/14; candidate AC-05.**

1. Teacher creates an account and starts a verification application.
2. Teacher uploads required identity/qualification evidence and declares subjects/medium, following an **approved** evidence standard (OD-01).
3. Review transitions through `Draft → Submitted → Needs Information / Approved / Rejected / Suspended` as appropriate.
4. Reviewer action records actor, timestamp and reason; teacher cannot approve self.
5. Only an **approved active** teacher can publish classes or submit publishable approved-content assets.

**Exceptions:** Expired/missing evidence, needs information, rejection, suspension. Suspension requires existing paid learners' continuity policy; do not silently remove live obligations.

## SJ-04 — Teacher submits optional demo (R1)

**Source:** BRD §6.3 p. 5. **BR-04; candidate AC-31/33.**

1. Approved teacher selects a teacher-owned `ClassOffering` and submits a **free prerecorded preview** (title, medium, duration, media reference, creator and rights attestation).
2. Media is uploaded, validated and processed into controlled distribution form.
3. An **independent authorized reviewer** evaluates rights, quality and safeguarding before approval/publication.
4. Only approved + published + active demos appear on public class/teacher pages.
5. A rejected/withdrawn/processing/rights-invalid demo is not public; teacher can follow an approved correction workflow.

**Never:** Scheduled trial booking, trial seat, demo fee, compulsory watch for enrollment, or teacher self-approval.

## Class offering, batches and delivery — SJ-06 (R1)

**Source:** BRD §§6.4–6.5 pp. 5–6, §12 p. 9. **BR-05/07.**

- An approved teacher publishes valid class offering details, including subject, medium, syllabus, price, schedule, capacity and time zone under admin policies.
- Delivery uses approved live provider; only authorized participants receive short-lived join credentials.
- Attendance is recorded by join/leave and audited on correction; session rescheduling/cancellation notifies enrolled students.
- Teacher uploads class-linked resources with version and visibility; resources remain private and authorized.

**Exceptions:** Teacher suspension, session outage, cancelled classes, full seats, resource processing/scan failure. Refund continuity must follow OD-04, not an invented SLA.

## SJ-12 — XACT paper builder and assignments (R2)

**Source:** BRD §8.3 p. 7 and §12 p. 9. **BR-19; candidate AC-21/23/24/25.**

1. Approved teacher filters **read-only approved** question bank for authorized subjects/medium.
2. Selects eligible questions and prepares draft paper.
3. Previews, versions and publishes a stable paper version; source question/answer keys cannot be silently rewritten.
4. Assigns one versioned paper to individually authorized students/class recipients, each with own attempt and result.
5. Reviews authorized student outcomes; reuse creates a **new assignment**, preserving earlier results.

**Exceptions:** Withdrawn item, invalid subject/recipient, expired assignment, failed authorization, version corrections and controlled regrade.

## SJ-13 — Teacher-created XACT explanation video (R2 staged)

**Source:** BRD §8.4 p. 7 and §12 p. 9. **BR-20; candidate AC-26.**

Submit original/licensed question- and medium-linked video → Uploaded → Processing → SubmittedForReview → ChangesRequested / Rejected / Approved → Published (or Withdrawn). Independent academic/content review is required. Only approved content can be delivered via signed access; approved written explanation remains fallback. Copyright and compensation terms OD-07/09/12 pending.

**Do not confuse** XACT explanation video with a free ClassOffering demo.

## Proposed teacher screen families — NOT approved screen IDs

Teacher registration/evidence; verification status; class management; optional demo submission/status; batch calendar and attendance; resource upload/version; XACT paper draft/preview/assign; assignment results; explanation video submission/review outcome.

## Open approvals

OD-01 teacher evidence; OD-02 demo terms; OD-04 continuity/refunds; OD-06 live/media provider; OD-07/09/12 content rights/QA/pay; OD-10/11 paper/exam policies; OD-20 technical design.
