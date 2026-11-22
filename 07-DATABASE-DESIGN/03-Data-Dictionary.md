# Data dictionary — standards and critical definitions

**Status:** Proposed logical vocabulary, not signed-off data types. For all individual candidate fields see [`Column-Dictionary.csv`](./Column-Dictionary.csv).

## Core type conventions (conditional on OD-20)

| Logical type | Proposed representation | Important caveat |
|---|---|---|
| Entity identifier | UUID/Guid | Native type/provider and ID generation need sign-off |
| Time instant | UTC timestamp | Keep source time zone + IANA/Windows mapping as appropriate; do not store local time as UTC |
| Local schedule | LocalTime + TimeZoneId | Class sessions need a resolved UTC instant around DST changes |
| Monetary amount | `DECIMAL(19,4)` candidate | Final scale, tax rounding and LKR currency policy need Finance sign-off |
| Status, reason | Stable code/string or lookup | Never use free text as authorization logic |
| Language/medium | Controlled `MediumCode` | Tamil/Sinhala/English approvals independent; no fallback |
| External-provider ID | Provider + merchant + unique reference | Composite uniqueness and webhook replay prevention |
| Version | Positive sequential integer + immutable published state | Historical XACT scoring must reference exact version |
| Storage link | Opaque protected storage key | Do not save public signed URLs as canonical file identity |
| PII/evidence | Encrypted or restricted reference | Retention and access purpose legal review pending |

## Mandatory domain distinctions

- `StudentSubject`: educational preference. **Never automatically grants `Enrollment`, `Entitlement`, or `PaymentAttempt`**. BRD p3/p5, AC-32.
- `DemoVideo`: free, optional prerecorded class preview. **No StudentId, TrialId or EnrollmentId** and **no playback requirement for checkout**. BRD p5, AC-07/31/33.
- `Enrollment`: actual authorized `ClassBatch` seat, not trial booking.
- `Entitlement`: server-verified right to paid content; do not base access on browser redirect.
- `QuestionConcept` is stable across mediums; `QuestionTranslation`/`QuestionOptionTranslation` and `AnswerKeyVersion` have independent review/versions.
- `MockQuestionSnapshot` captures the generated mock definition; `AttemptQuestionSnapshot` captures each student's exact presented item for both student mock and teacher-assigned paper; future edits cannot alter historical score.
- `DemoVideo` and `ExplanationVideo` have distinct rights/review/publication/access policies.
- `LedgerEntry`: append-only. Refund/chargeback reversals use new correcting entries.

## Data lineage and ownership

Use the normalized logical names in [`Table-Inventory.csv`](./Table-Inventory.csv). For each physical column, the DB design reviewer must add classification (public/private/restricted), owner, masking requirement, retention, nullability, defaults and examples to `Column-Dictionary.csv` before migrations. The provisional CSV supplies module + field + suggested type + provenance; it does **not** claim business approvals.
