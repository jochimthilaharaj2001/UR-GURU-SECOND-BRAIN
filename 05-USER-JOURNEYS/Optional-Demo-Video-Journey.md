# Optional Free Prerecorded Demo Video — End-to-End Journey

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

**Primary sources:** BRD §6.3 p. 5; §10 pp. 7–8; SJ-03/SJ-04/SJ-05 pp. 8–9; AC-07/31/33 pp. 9–10; Appendix C pp. 11–12.

## The central rule

A free demo is a **prerecorded, moderated ClassOffering preview** that a prospective student may **watch or skip**. It is neither a live trial nor a reservation. **Watching is never a condition for checkout, enrollment or a live class join.**

## Viewer journey (SJ-03 → SJ-04 → SJ-05)

1. Browse teacher/class results for supported subject and medium.
2. On class detail, show a **Watch free demo** action *only if* an approved/published/active preview exists.
3. Always show **Choose batch / Enroll** for otherwise eligible classes, regardless of demo presence or status.
4. Viewer may play the demo or choose to skip. Playback failure shows retry/unavailable while batch and checkout actions remain.
5. Viewer chooses ClassBatch and enters the **normal paid enrollment journey**; payment, seat checks and entitlement creation happen only there.

### Required alternative branches

- **No demo:** class information and direct enrollment remain accessible.
- **Rejected, processing, withdrawn or rights-invalid demo:** hide/block playback; class path remains available subject to its own eligibility.
- **Viewer skips:** must navigate directly; no watch percentage, completion flag or recording required.
- **Playback fails:** informative error + retry; no loss of enrollment option.
- **Viewer not logged in:** public access/login and tracking rules are pending OD-02/15; do not silently require login without approval.

## Teacher and review journey

1. Only approved teachers can submit a demo linked to their own `ClassOffering`.
2. Capture title, medium/language, duration, creator, media reference, dates and evidence of ownership/right to distribute.
3. Validate uploaded file; process to approved preview delivery form in media storage.
4. Separate authorized reviewer checks academic/content and rights compliance, then approves/publishes or requests changes/rejects.
5. Log review/publication/withdrawal actor, timestamp, reason and content version.

## Data and access boundaries (proposed ERD v1.2)

- `ClassOffering (1) → DemoVideo (0..N)`; `DemoVideo → MediaAsset`; optional reviewer reference to `UserAccount`.
- Do **not** require StudentId, TrialId, SessionId or EnrollmentId in DemoVideo.
- Demo must not trigger `TrialBooking`, `OrderHeader`, `PaymentAttempt`, `Enrollment`, `Entitlement` or reserve a `ClassBatch` seat.
- Class preview and XACT explanation videos have different access/rights models.
- Viewer analytics require separate privacy/consent decision; no silent per-viewer tracking assumption.

## Acceptance criteria

| AC | Expected result |
|---|---|
| AC-07 | Watch OR skip; absent/failed demo never prevents otherwise valid enrollment; no trial booking/seat reservation |
| AC-31 | Only authorized reviewer publishes approved demo; no rejected/withdrawn/unprocessed/rights-invalid video available publicly |
| AC-33 | Playback never creates booking/enrollment/payment/entitlement and completion never gates checkout |

## Explicitly superseded live-trial concepts

Do **not** implement scheduled trial-class booking, trial capacity, trial attendance, trial no-show, `TrialBooking`, `ClassBatch.TrialCapacity`, `ClassOffering.TrialAvailable`, `Enrollment.TrialId` in the active design. Historical trial data is a separate retention/migration decision; it **must not** be converted into DemoVideo.

## Decisions pending

OD-02 demo access/count/duration/analytics/rights; OD-06 hosting and media provider; OD-15 minors/consent/analytics; OD-20 ERD/schema approval.
