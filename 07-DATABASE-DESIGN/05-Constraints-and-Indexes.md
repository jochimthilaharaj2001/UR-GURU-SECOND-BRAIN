# Constraints and indexes — database integrity plan

**Status: CANDIDATE / not executable DDL.** Exact partial indexes, lock modes and constraints depend on SQL Server vs PostgreSQL (OD-20).

## Unique and integrity candidates

| Entity | Proposed integrity rule | Test case / BRD |
|---|---|---|
| `UserAccount` | Email (subject to login/unique policy) | BR-01/02/14/21 |
| `UserRole` | UserId + RoleCode + active membership | BR-01/14 |
| `StudentProfile` | UserId | BR-01/21 |
| `TeacherProfile` | UserId | BR-02/03 |
| `StudentSubject` | StudentId + SubjectId + AcademicYear for active selections (partial/full unique decision pending) | BR-01 |
| `StreamSubject` | StreamId + SubjectId | BR-01 |
| `SyllabusVersion` | SubjectId + VersionCode | BR-18/23 |
| `TeacherSubject` | TeacherId + SubjectId + MediumCode (as approved) | BR-02/03 |
| `Enrollment` | StudentId + BatchId for active paid enrollment; seat cap transactional | BR-05/06 |
| `DemoVideo` | None required; ClassOffering 0..N demo videos | BR-04 |
| `OrderLine` | OrderId + line sequence (sequence column to add) | BR-06 |
| `PaymentProviderEvent` | ProviderCode + ProviderEventId | BR-06 |
| `Entitlement` | Verified order-line rights and no duplicate active grant | BR-06 |
| `PayoutItem` | TeacherPayoutId + TeacherEarningId | BR-06 |
| `QuestionOption` | QuestionConceptId + OptionCode | BR-18/23 |
| `QuestionTranslation` | QuestionConceptId + MediumCode + RevisionNumber | BR-18/23 |
| `QuestionOptionTranslation` | QuestionTranslationId + QuestionOptionId | BR-18/23 |
| `AnswerKeyVersion` | QuestionTranslationId + VersionNumber | BR-11/18 |
| `MockQuestionSnapshot` | MockExamId + DisplayOrder; no duplicate QuestionConceptId in same mock | BR-11/18 |
| `AttemptQuestionSnapshot` | ExamAttemptId + DisplayOrder; immutable, one per presented item | BR-11/18/19 |
| `AttemptAnswer` | ExamAttemptId + AttemptQuestionSnapshotId, safe upsert | BR-11/18 |
| `ExamResult` | ExamAttemptId + RegradeVersion | BR-11/18 |
| `TeacherPaperVersion` | TeacherPaperId + VersionNumber | BR-19 |
| `TeacherPaperItem` | TeacherPaperVersionId + ItemOrder | BR-19 |
| `AssignmentRecipient` | AssignmentId + StudentId | BR-19 |
| `OutboxMessage` | Event idempotency key (need explicit additional key) | BR-13/24 |

## Transactional invariants (enforce on server + database)

1. Only supported Bio/Maths subject combinations can be selected; stable subject master is language independent. `StudentSubject` active uniqueness must survive concurrent requests.
2. Paid seat reservation checks capacity **atomically**, detects duplicate purchase/enrollment, and handles delayed callbacks.
3. `PaymentProviderEvent` idempotency must be provider + merchant + event ID, not just client callback or redirect.
4. Financial ledger rows are immutable; refund creates linked correcting entries; multi-currency amounts never mixed implicitly.
5. Published question translations/keys are immutable; new revisions create new rows. Translation must have verified answer key + rights.
6. Backend generates mock and persists question order, selected option mapping and scoring rule revision; no duplicate canonical question per mock.
7. Autosaved answers implement safe idempotent upsert; final submission happens once; versioned regrades are audited.
8. Papers/assignments cannot expose unassigned student questions/results, including guessed foreign keys.
9. Video may publish only when rights, transcode, reviewer and approval are valid; withdrawn content remains historic.
10. Role/ownership authorization on read & write even if a row is linked by FK.

## Suggested index workload (subject to EXPLAIN/benchmark)

- `StudentSubject(StudentId, AcademicYear, Status)` + unique active selection.
- `ClassOffering(SubjectId, MediumCode, Status)` and `ClassBatch(ClassOfferingId, Status)`; batch capacity concurrency path.
- `Enrollment(BatchId, EnrollmentStatus)` and `(StudentId, BatchId)` unique active.
- `PaymentAttempt(ProviderCode, ProviderReference)`, `PaymentProviderEvent(ProviderCode, ProviderEventId)` unique.
- `QuestionConcept(SubjectId, SyllabusVersionId, PrimaryTopicId, DifficultyCode, Status)` + rights/translation joins.
- `QuestionTranslation(QuestionConceptId, MediumCode, RevisionNumber)` unique; review status lookup.
- `MockQuestionSnapshot(MockExamId, DisplayOrder)` unique; `AttemptQuestionSnapshot(ExamAttemptId, DisplayOrder)` unique; `AttemptAnswer(ExamAttemptId, AttemptQuestionSnapshotId)` unique.
- `AssignmentRecipient(StudentId, RecipientStatus)` and `Assignment(TeacherId, DueAt)`.
- `OutboxMessage(PublishedAt, RetryCount)` for worker scan; avoid heavy unbounded JSON scans.

**Readiness gate:** Concurrency, integrity, authorization and rollback tests must pass against the selected actual database provider (BRD AC-08, 12–14, 16–20, 23–25, 31–33).
