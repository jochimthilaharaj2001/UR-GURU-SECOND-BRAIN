# Optional free demo + student subject selection + paid enrollment

**Source:** BRD v6.2.2 pp3, 5, 8, 9–12; **AC-07, AC-08, AC-31, AC-32, AC-33**.

## Independent concepts

| Concept | Record required? | Grants paid class access? |
|---|---|---|
| Student chooses subject | `StudentSubject` | **No** |
| Student opens/watches demo | **No mandatory per-viewer/booking record** | **No** |
| Class has optional approved demo | `DemoVideo` referencing `ClassOffering` + `MediaAsset` | **No** |
| Student buys actual batch seat | `OrderHeader` / `PaymentAttempt` / `Enrollment` per approved reservation flow | Only after verified payment + entitlement |
| Paid enrollment | `Enrollment` + `Entitlement` | Access is checked at join/read time |

- `StudentSubject` columns must include StudentId, SubjectId, AcademicYear, SelectedAt and Status. Active uniqueness and stream eligibility need DB/integration tests.
- Demo is 0..N per ClassOffering, free, recorded and can be skipped. No `TrialBooking`, `TrialId`, `TrialCapacity`, `TrialAvailable`, or mandatory watch completion.
- `DemoVideo` candidate fields per BRD: DemoVideoId, ClassId/ClassOfferingId, MediaAssetId, optional ReviewerUserId, Title, MediumCode, ReviewStatus, DurationSeconds, CreatedAt, PublishedAt nullable, UpdatedAt.
- Only approved active published media is previewable. Reviewer should differ from creator; creator may not self-publish.
- Demo playback failure/missing demo keeps batch selection and checkout functional. Analytics per viewer require privacy/consent approval OD-02/15.
- A student can enroll directly without any demo record; enrollment shall not require demo fields in non-null FK path.

## Legacy migration warning

`TrialBooking` history is **not** `DemoVideo`: do not auto-convert. Archive historical trial records according to retention policy. Old PostgreSQL `bookings` rows require review against updated Enrollment/OrderLine semantics; never auto-upgrade by naming similarity.
