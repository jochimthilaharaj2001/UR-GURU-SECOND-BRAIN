# Relationships and cardinalities — proposed

Notation `Parent (1) → Child (0..N/1..N)` describes expected logical relationship; a candidate nullable FK is not proof of a mandatory business association.

## Candidate foreign keys

| Child FK | Parent PK | Required | Logical cardinality |
|---|---|---|---|
| `UserRole.UserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `UserRole` 0..N |
| `StudentProfile.UserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `StudentProfile` 0..N |
| `StudentProfile.StreamId` | `AcademicStream.AcademicStreamId` | Required | `AcademicStream` 1 → `StudentProfile` 0..N |
| `TeacherProfile.UserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `TeacherProfile` 0..N |
| `TeacherVerification.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `TeacherVerification` 0..N |
| `TeacherVerification.EvidenceAssetId` | `MediaAsset.MediaAssetId` | Optional | `MediaAsset` 1 → `TeacherVerification` 0..N |
| `TeacherVerification.ReviewerUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `TeacherVerification` 0..N |
| `GuardianContact.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `GuardianContact` 0..N |
| `ConsentRecord.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `ConsentRecord` 0..N |
| `ConsentRecord.GuardianContactId` | `GuardianContact.GuardianContactId` | Optional | `GuardianContact` 1 → `ConsentRecord` 0..N |
| `ConsentRecord.EvidenceAssetId` | `MediaAsset.MediaAssetId` | Optional | `MediaAsset` 1 → `ConsentRecord` 0..N |
| `IdentityCheck.UserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `IdentityCheck` 0..N |
| `StreamSubject.StreamId` | `AcademicStream.AcademicStreamId` | Required | `AcademicStream` 1 → `StreamSubject` 0..N |
| `StreamSubject.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `StreamSubject` 0..N |
| `SyllabusVersion.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `SyllabusVersion` 0..N |
| `Topic.SyllabusVersionId` | `SyllabusVersion.SyllabusVersionId` | Required | `SyllabusVersion` 1 → `Topic` 0..N |
| `Topic.ParentTopicId` | `Topic.TopicId` | Optional | `Topic` 1 → `Topic` 0..N |
| `StudentSubject.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `StudentSubject` 0..N |
| `StudentSubject.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `StudentSubject` 0..N |
| `TeacherSubject.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `TeacherSubject` 0..N |
| `TeacherSubject.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `TeacherSubject` 0..N |
| `ClassOffering.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `ClassOffering` 0..N |
| `ClassOffering.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `ClassOffering` 0..N |
| `ClassBatch.ClassOfferingId` | `ClassOffering.ClassOfferingId` | Required | `ClassOffering` 1 → `ClassBatch` 0..N |
| `ClassSchedule.BatchId` | `ClassBatch.ClassBatchId` | Required | `ClassBatch` 1 → `ClassSchedule` 0..N |
| `LiveSession.BatchId` | `ClassBatch.ClassBatchId` | Required | `ClassBatch` 1 → `LiveSession` 0..N |
| `Enrollment.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `Enrollment` 0..N |
| `Enrollment.BatchId` | `ClassBatch.ClassBatchId` | Required | `ClassBatch` 1 → `Enrollment` 0..N |
| `Enrollment.OrderLineId` | `OrderLine.OrderLineId` | Optional | `OrderLine` 1 → `Enrollment` 0..N |
| `Attendance.LiveSessionId` | `LiveSession.LiveSessionId` | Required | `LiveSession` 1 → `Attendance` 0..N |
| `Attendance.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `Attendance` 0..N |
| `DemoVideo.ClassOfferingId` | `ClassOffering.ClassOfferingId` | Required | `ClassOffering` 1 → `DemoVideo` 0..N |
| `DemoVideo.MediaAssetId` | `MediaAsset.MediaAssetId` | Required | `MediaAsset` 1 → `DemoVideo` 0..N |
| `DemoVideo.ReviewerUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `DemoVideo` 0..N |
| `ContentReviewEvent.MediaAssetId` | `MediaAsset.MediaAssetId` | Optional | `MediaAsset` 1 → `ContentReviewEvent` 0..N |
| `ContentReviewEvent.ReviewerUserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `ContentReviewEvent` 0..N |
| `MediaAsset.CreatedByUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `MediaAsset` 0..N |
| `LearningResource.ClassOfferingId` | `ClassOffering.ClassOfferingId` | Required | `ClassOffering` 1 → `LearningResource` 0..N |
| `ResourceVersion.LearningResourceId` | `LearningResource.LearningResourceId` | Required | `LearningResource` 1 → `ResourceVersion` 0..N |
| `ResourceVersion.MediaAssetId` | `MediaAsset.MediaAssetId` | Required | `MediaAsset` 1 → `ResourceVersion` 0..N |
| `OrderHeader.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `OrderHeader` 0..N |
| `OrderLine.OrderId` | `OrderHeader.OrderHeaderId` | Required | `OrderHeader` 1 → `OrderLine` 0..N |
| `PaymentAttempt.OrderId` | `OrderHeader.OrderHeaderId` | Required | `OrderHeader` 1 → `PaymentAttempt` 0..N |
| `PaymentProviderEvent.PaymentAttemptId` | `PaymentAttempt.PaymentAttemptId` | Required | `PaymentAttempt` 1 → `PaymentProviderEvent` 0..N |
| `Entitlement.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `Entitlement` 0..N |
| `Entitlement.OrderLineId` | `OrderLine.OrderLineId` | Required | `OrderLine` 1 → `Entitlement` 0..N |
| `LedgerEntry.OrderId` | `OrderHeader.OrderHeaderId` | Required | `OrderHeader` 1 → `LedgerEntry` 0..N |
| `LedgerEntry.RelatedEntryId` | `LedgerEntry.LedgerEntryId` | Optional | `LedgerEntry` 1 → `LedgerEntry` 0..N |
| `Refund.OrderLineId` | `OrderLine.OrderLineId` | Required | `OrderLine` 1 → `Refund` 0..N |
| `Refund.PaymentAttemptId` | `PaymentAttempt.PaymentAttemptId` | Required | `PaymentAttempt` 1 → `Refund` 0..N |
| `TeacherEarning.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `TeacherEarning` 0..N |
| `TeacherEarning.OrderLineId` | `OrderLine.OrderLineId` | Required | `OrderLine` 1 → `TeacherEarning` 0..N |
| `TeacherPayout.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `TeacherPayout` 0..N |
| `PayoutItem.TeacherPayoutId` | `TeacherPayout.TeacherPayoutId` | Required | `TeacherPayout` 1 → `PayoutItem` 0..N |
| `PayoutItem.TeacherEarningId` | `TeacherEarning.TeacherEarningId` | Required | `TeacherEarning` 1 → `PayoutItem` 0..N |
| `PastPaperSource.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `PastPaperSource` 0..N |
| `SourceRightsRecord.PastPaperSourceId` | `PastPaperSource.PastPaperSourceId` | Required | `PastPaperSource` 1 → `SourceRightsRecord` 0..N |
| `SourceRightsRecord.EvidenceAssetId` | `MediaAsset.MediaAssetId` | Optional | `MediaAsset` 1 → `SourceRightsRecord` 0..N |
| `SourceRightsRecord.ApprovedByUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `SourceRightsRecord` 0..N |
| `QuestionConcept.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `QuestionConcept` 0..N |
| `QuestionConcept.SyllabusVersionId` | `SyllabusVersion.SyllabusVersionId` | Required | `SyllabusVersion` 1 → `QuestionConcept` 0..N |
| `QuestionConcept.PrimaryTopicId` | `Topic.TopicId` | Required | `Topic` 1 → `QuestionConcept` 0..N |
| `QuestionConcept.SourceId` | `PastPaperSource.PastPaperSourceId` | Optional | `PastPaperSource` 1 → `QuestionConcept` 0..N |
| `QuestionOption.QuestionConceptId` | `QuestionConcept.QuestionConceptId` | Required | `QuestionConcept` 1 → `QuestionOption` 0..N |
| `QuestionTranslation.QuestionConceptId` | `QuestionConcept.QuestionConceptId` | Required | `QuestionConcept` 1 → `QuestionTranslation` 0..N |
| `QuestionOptionTranslation.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `QuestionOptionTranslation` 0..N |
| `QuestionOptionTranslation.QuestionOptionId` | `QuestionOption.QuestionOptionId` | Required | `QuestionOption` 1 → `QuestionOptionTranslation` 0..N |
| `AnswerKeyVersion.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `AnswerKeyVersion` 0..N |
| `AnswerKeyVersion.QuestionOptionId` | `QuestionOption.QuestionOptionId` | Required | `QuestionOption` 1 → `AnswerKeyVersion` 0..N |
| `QuestionReviewEvent.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `QuestionReviewEvent` 0..N |
| `QuestionReviewEvent.ReviewerUserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `QuestionReviewEvent` 0..N |
| `WrittenExplanationVersion.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `WrittenExplanationVersion` 0..N |
| `ExplanationVideo.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `ExplanationVideo` 0..N |
| `ExplanationVideo.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `ExplanationVideo` 0..N |
| `ExplanationVideo.MediaAssetId` | `MediaAsset.MediaAssetId` | Required | `MediaAsset` 1 → `ExplanationVideo` 0..N |
| `MockExam.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `MockExam` 0..N |
| `MockExam.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `MockExam` 0..N |
| `MockExam.SyllabusVersionId` | `SyllabusVersion.SyllabusVersionId` | Required | `SyllabusVersion` 1 → `MockExam` 0..N |
| `MockQuestionSnapshot.MockExamId` | `MockExam.MockExamId` | Required | `MockExam` 1 → `MockQuestionSnapshot` 0..N |
| `MockQuestionSnapshot.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `MockQuestionSnapshot` 0..N |
| `MockQuestionSnapshot.AnswerKeyVersionId` | `AnswerKeyVersion.AnswerKeyVersionId` | Required | `AnswerKeyVersion` 1 → `MockQuestionSnapshot` 0..N |
| `ExamAttempt.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `ExamAttempt` 0..N |
| `ExamAttempt.MockExamId` | `MockExam.MockExamId` | Optional | `MockExam` 1 → `ExamAttempt` 0..N |
| `ExamAttempt.AssignmentRecipientId` | `AssignmentRecipient.AssignmentRecipientId` | Optional | `AssignmentRecipient` 1 → `ExamAttempt` 0..N |
| `ExamAttempt.ScoringPolicyVersionId` | `ScoringPolicyVersion.ScoringPolicyVersionId` | Required | `ScoringPolicyVersion` 1 → `ExamAttempt` 0..N |
| `AttemptQuestionSnapshot.ExamAttemptId` | `ExamAttempt.ExamAttemptId` | Required | `ExamAttempt` 1 → `AttemptQuestionSnapshot` 0..N |
| `AttemptQuestionSnapshot.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `AttemptQuestionSnapshot` 0..N |
| `AttemptQuestionSnapshot.AnswerKeyVersionId` | `AnswerKeyVersion.AnswerKeyVersionId` | Required | `AnswerKeyVersion` 1 → `AttemptQuestionSnapshot` 0..N |
| `AttemptAnswer.ExamAttemptId` | `ExamAttempt.ExamAttemptId` | Required | `ExamAttempt` 1 → `AttemptAnswer` 0..N |
| `AttemptAnswer.AttemptQuestionSnapshotId` | `AttemptQuestionSnapshot.AttemptQuestionSnapshotId` | Required | `AttemptQuestionSnapshot` 1 → `AttemptAnswer` 0..N |
| `AttemptAnswer.SelectedQuestionOptionId` | `QuestionOption.QuestionOptionId` | Optional | `QuestionOption` 1 → `AttemptAnswer` 0..N |
| `ExamResult.ExamAttemptId` | `ExamAttempt.ExamAttemptId` | Required | `ExamAttempt` 1 → `ExamResult` 0..N |
| `TeacherPaper.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `TeacherPaper` 0..N |
| `TeacherPaper.SubjectId` | `Subject.SubjectId` | Required | `Subject` 1 → `TeacherPaper` 0..N |
| `TeacherPaperVersion.TeacherPaperId` | `TeacherPaper.TeacherPaperId` | Required | `TeacherPaper` 1 → `TeacherPaperVersion` 0..N |
| `TeacherPaperItem.TeacherPaperVersionId` | `TeacherPaperVersion.TeacherPaperVersionId` | Required | `TeacherPaperVersion` 1 → `TeacherPaperItem` 0..N |
| `TeacherPaperItem.QuestionTranslationId` | `QuestionTranslation.QuestionTranslationId` | Required | `QuestionTranslation` 1 → `TeacherPaperItem` 0..N |
| `TeacherPaperItem.AnswerKeyVersionId` | `AnswerKeyVersion.AnswerKeyVersionId` | Required | `AnswerKeyVersion` 1 → `TeacherPaperItem` 0..N |
| `Assignment.TeacherPaperVersionId` | `TeacherPaperVersion.TeacherPaperVersionId` | Required | `TeacherPaperVersion` 1 → `Assignment` 0..N |
| `Assignment.TeacherId` | `TeacherProfile.TeacherProfileId` | Required | `TeacherProfile` 1 → `Assignment` 0..N |
| `AssignmentRecipient.AssignmentId` | `Assignment.AssignmentId` | Required | `Assignment` 1 → `AssignmentRecipient` 0..N |
| `AssignmentRecipient.StudentId` | `StudentProfile.StudentProfileId` | Required | `StudentProfile` 1 → `AssignmentRecipient` 0..N |
| `AssignmentRecipient.EnrollmentId` | `Enrollment.EnrollmentId` | Optional | `Enrollment` 1 → `AssignmentRecipient` 0..N |
| `NotificationDelivery.RecipientUserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `NotificationDelivery` 0..N |
| `AuditEvent.ActorUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `AuditEvent` 0..N |
| `SafetyReport.ReporterUserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `SafetyReport` 0..N |
| `SafetyReport.SubjectUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `SafetyReport` 0..N |
| `SafetyReport.AssignedToUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `SafetyReport` 0..N |
| `SupportTicket.RequesterUserId` | `UserAccount.UserAccountId` | Required | `UserAccount` 1 → `SupportTicket` 0..N |
| `SupportTicket.AssignedToUserId` | `UserAccount.UserAccountId` | Optional | `UserAccount` 1 → `SupportTicket` 0..N |

## Highest-risk invariants

- `ClassOffering (1) → DemoVideo (0..N)`; demo absent/failed does not block enrollment.
- `StudentProfile (1) → StudentSubject (0..N)`; independent of `ClassBatch (1) → Enrollment (0..N)`.
- `QuestionConcept (1) → QuestionTranslation (0..N)`; **approved medium required**.
- `QuestionTranslation (1) → AnswerKeyVersion (0..N)`; eligible published key must be selected.
- `MockExam (1) → MockQuestionSnapshot (1..N)` when generated; **each `ExamAttempt` has immutable `AttemptQuestionSnapshot` items** whether sourced from a mock or teacher-assigned paper.
- `Assignment (1) → AssignmentRecipient (1..N)`; each student can independently attempt their assigned paper.
- `OrderHeader (1) → OrderLine (1..N)` and `PaymentAttempt (0..N)`; no paid rights until verified callback.
- `ExamAttempt.MockExamId` and `ExamAttempt.AssignmentRecipientId` are conditional; validate exactly one assessment source under a finalized schema.
- `OrderLine.ProductType/ProductRefId` is a polymorphic logical product reference; choose a safe physical pattern before production.

**References note:** These are *proposed* design edges. Physical FK constraints may be within module-owned schema; cross-module ownership must use explicit contracts.
