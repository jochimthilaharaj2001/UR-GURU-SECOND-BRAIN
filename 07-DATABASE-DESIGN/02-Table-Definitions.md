# Proposed table definitions (logical)

**All identifiers, types, and entity boundaries below are design CANDIDATES**. Do not create production tables from this document before OD-20.

Common candidate columns: `<Entity>Id` UUID PK; `CreatedAt`, `UpdatedAt` where lifecycle requires; sensitive evidence/logs have explicit retention classification.

## Identity

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `UserAccount` | `UserAccountId` | Email, Phone, PasswordHash, AccountStatus, CreatedAt | — |
| `UserRole` | `UserRoleId` | UserId, RoleCode, GrantedAt, RevokedAt | `UserId` → `UserAccount` |
| `StudentProfile` | `StudentProfileId` | UserId, GradeLevel, StreamId, PreferredMediumCode, Status | `UserId` → `UserAccount`, `StreamId` → `AcademicStream` |
| `TeacherProfile` | `TeacherProfileId` | UserId, PublicName, Bio, VerificationStatus, Status | `UserId` → `UserAccount` |
| `TeacherVerification` | `TeacherVerificationId` | TeacherId, ReviewStatus, EvidenceAssetId, ReviewerUserId, ReviewedAt | `TeacherId` → `TeacherProfile`, `EvidenceAssetId` → `MediaAsset`, `ReviewerUserId` → `UserAccount` |
| `GuardianContact` | `GuardianContactId` | StudentId, ContactName, ContactPhone, RelationshipCode, ContactStatus | `StudentId` → `StudentProfile` |
| `ConsentRecord` | `ConsentRecordId` | StudentId, GuardianContactId, PurposeCode, PolicyVersion, GrantedAt, RevokedAt, EvidenceAssetId | `StudentId` → `StudentProfile`, `GuardianContactId` → `GuardianContact`, `EvidenceAssetId` → `MediaAsset` |
| `IdentityCheck` | `IdentityCheckId` | UserId, MethodCode, ProviderReference, VerificationStatus, VerifiedAt | `UserId` → `UserAccount` |

## Catalogue

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `AcademicStream` | `AcademicStreamId` | StreamCode, Name, LaunchStatus | — |
| `Subject` | `SubjectId` | SubjectCode, Name, Status | — |
| `StreamSubject` | `StreamSubjectId` | StreamId, SubjectId, EligibilityStatus | `StreamId` → `AcademicStream`, `SubjectId` → `Subject` |
| `SyllabusVersion` | `SyllabusVersionId` | SubjectId, VersionCode, EffectiveFrom, Status | `SubjectId` → `Subject` |
| `Topic` | `TopicId` | SyllabusVersionId, ParentTopicId, TopicCode, TopicName, Status | `SyllabusVersionId` → `SyllabusVersion`, `ParentTopicId` → `Topic` |
| `CatalogueTranslation` | `CatalogueTranslationId` | EntityType, EntityId, MediumCode, DisplayText, ReviewStatus | — |
| `StudentSubject` | `StudentSubjectId` | StudentId, SubjectId, AcademicYear, SelectedAt, Status | `StudentId` → `StudentProfile`, `SubjectId` → `Subject` |
| `TeacherSubject` | `TeacherSubjectId` | TeacherId, SubjectId, MediumCode, AuthorizationStatus | `TeacherId` → `TeacherProfile`, `SubjectId` → `Subject` |

## Marketplace

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `ClassOffering` | `ClassOfferingId` | TeacherId, SubjectId, Title, MediumCode, PriceAmount, CurrencyCode, DemoPreviewEnabled, Status | `TeacherId` → `TeacherProfile`, `SubjectId` → `Subject` |
| `ClassBatch` | `ClassBatchId` | ClassOfferingId, Capacity, StartAt, EndAt, TimeZoneId, Status | `ClassOfferingId` → `ClassOffering` |
| `ClassSchedule` | `ClassScheduleId` | BatchId, DayOfWeek, LocalStartTime, DurationMinutes, TimeZoneId | `BatchId` → `ClassBatch` |
| `LiveSession` | `LiveSessionId` | BatchId, ScheduledStartAt, ScheduledEndAt, ProviderSessionRef, Status | `BatchId` → `ClassBatch` |
| `Enrollment` | `EnrollmentId` | StudentId, BatchId, OrderLineId, EnrollmentStatus, EnrolledAt | `StudentId` → `StudentProfile`, `BatchId` → `ClassBatch`, `OrderLineId` → `OrderLine` |
| `Attendance` | `AttendanceId` | LiveSessionId, StudentId, JoinedAt, LeftAt, AttendanceStatus | `LiveSessionId` → `LiveSession`, `StudentId` → `StudentProfile` |
| `DemoVideo` | `DemoVideoId` | ClassOfferingId, MediaAssetId, ReviewerUserId, Title, MediumCode, ReviewStatus, DurationSeconds, CreatedAt, PublishedAt, UpdatedAt | `ClassOfferingId` → `ClassOffering`, `MediaAssetId` → `MediaAsset`, `ReviewerUserId` → `UserAccount` |

## Media

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `MediaAsset` | `MediaAssetId` | StorageKeyRef, ContentType, ByteSize, ProcessingStatus, RightsStatus, CreatedByUserId | `CreatedByUserId` → `UserAccount` |
| `ContentReviewEvent` | `ContentReviewEventId` | MediaAssetId, ReviewObjectType, ReviewObjectId, ReviewerUserId, DecisionCode, RecordedAt | `MediaAssetId` → `MediaAsset`, `ReviewerUserId` → `UserAccount` |
| `LearningResource` | `LearningResourceId` | ClassOfferingId, Title, MediumCode, VisibilityStatus | `ClassOfferingId` → `ClassOffering` |
| `ResourceVersion` | `ResourceVersionId` | LearningResourceId, MediaAssetId, VersionNumber, PublishedAt, Status | `LearningResourceId` → `LearningResource`, `MediaAssetId` → `MediaAsset` |

## Commerce

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `OrderHeader` | `OrderHeaderId` | StudentId, CurrencyCode, GrossAmount, OrderStatus, CreatedAt | `StudentId` → `StudentProfile` |
| `OrderLine` | `OrderLineId` | OrderId, ProductType, ProductRefId, Quantity, UnitAmount, TotalAmount | `OrderId` → `OrderHeader` |
| `PaymentAttempt` | `PaymentAttemptId` | OrderId, ProviderCode, ProviderReference, Amount, VerificationStatus, CreatedAt | `OrderId` → `OrderHeader` |
| `PaymentProviderEvent` | `PaymentProviderEventId` | PaymentAttemptId, ProviderCode, ProviderEventId, PayloadHash, ReceivedAt, HandledAt | `PaymentAttemptId` → `PaymentAttempt` |
| `Entitlement` | `EntitlementId` | StudentId, OrderLineId, ResourceType, ResourceRefId, ValidFrom, ValidTo, Status | `StudentId` → `StudentProfile`, `OrderLineId` → `OrderLine` |
| `LedgerEntry` | `LedgerEntryId` | OrderId, EntryType, Amount, CurrencyCode, Direction, RelatedEntryId, RecordedAt | `OrderId` → `OrderHeader`, `RelatedEntryId` → `LedgerEntry` |
| `Refund` | `RefundId` | OrderLineId, PaymentAttemptId, RefundAmount, DecisionStatus, ProviderReference, CreatedAt | `OrderLineId` → `OrderLine`, `PaymentAttemptId` → `PaymentAttempt` |
| `TeacherEarning` | `TeacherEarningId` | TeacherId, OrderLineId, GrossBase, CommissionAmount, NetAmount, EarningStatus | `TeacherId` → `TeacherProfile`, `OrderLineId` → `OrderLine` |
| `TeacherPayout` | `TeacherPayoutId` | TeacherId, PayoutAmount, CurrencyCode, Status, ApprovedAt, ProviderReference | `TeacherId` → `TeacherProfile` |
| `PayoutItem` | `PayoutItemId` | TeacherPayoutId, TeacherEarningId, AllocatedAmount | `TeacherPayoutId` → `TeacherPayout`, `TeacherEarningId` → `TeacherEarning` |

## XACT Content

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `PastPaperSource` | `PastPaperSourceId` | SubjectId, PaperYear, PaperCode, MediumCode, Attribution, ReviewStatus | `SubjectId` → `Subject` |
| `SourceRightsRecord` | `SourceRightsRecordId` | PastPaperSourceId, RightsCode, EvidenceAssetId, ApprovedByUserId, ValidUntil | `PastPaperSourceId` → `PastPaperSource`, `EvidenceAssetId` → `MediaAsset`, `ApprovedByUserId` → `UserAccount` |
| `QuestionConcept` | `QuestionConceptId` | SubjectId, SyllabusVersionId, PrimaryTopicId, SourceId, DifficultyCode, Status | `SubjectId` → `Subject`, `SyllabusVersionId` → `SyllabusVersion`, `PrimaryTopicId` → `Topic`, `SourceId` → `PastPaperSource` |
| `QuestionOption` | `QuestionOptionId` | QuestionConceptId, OptionCode, Status | `QuestionConceptId` → `QuestionConcept` |
| `QuestionTranslation` | `QuestionTranslationId` | QuestionConceptId, MediumCode, RevisionNumber, QuestionText, ReviewStatus, IsActive | `QuestionConceptId` → `QuestionConcept` |
| `QuestionOptionTranslation` | `QuestionOptionTranslationId` | QuestionTranslationId, QuestionOptionId, DisplayText, DisplayOrder, ReviewStatus | `QuestionTranslationId` → `QuestionTranslation`, `QuestionOptionId` → `QuestionOption` |
| `AnswerKeyVersion` | `AnswerKeyVersionId` | QuestionTranslationId, QuestionOptionId, VersionNumber, ReviewStatus, ApprovedAt | `QuestionTranslationId` → `QuestionTranslation`, `QuestionOptionId` → `QuestionOption` |
| `QuestionReviewEvent` | `QuestionReviewEventId` | QuestionTranslationId, ReviewerUserId, DecisionCode, Notes, RecordedAt | `QuestionTranslationId` → `QuestionTranslation`, `ReviewerUserId` → `UserAccount` |
| `WrittenExplanationVersion` | `WrittenExplanationVersionId` | QuestionTranslationId, RevisionNumber, Body, ReviewStatus, PublishedAt | `QuestionTranslationId` → `QuestionTranslation` |
| `ExplanationVideo` | `ExplanationVideoId` | QuestionTranslationId, TeacherId, MediaAssetId, ReviewStatus, RightsStatus, PublishedAt | `QuestionTranslationId` → `QuestionTranslation`, `TeacherId` → `TeacherProfile`, `MediaAssetId` → `MediaAsset` |

## XACT Assessments

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `ScoringPolicyVersion` | `ScoringPolicyVersionId` | PolicyCode, VersionNumber, RuleJson, ApprovedAt, Status | — |
| `MockExam` | `MockExamId` | StudentId, SubjectId, SyllabusVersionId, MediumCode, SelectionConfigJson, DurationMinutes, CreatedAt | `StudentId` → `StudentProfile`, `SubjectId` → `Subject`, `SyllabusVersionId` → `SyllabusVersion` |
| `MockQuestionSnapshot` | `MockQuestionSnapshotId` | MockExamId, QuestionTranslationId, AnswerKeyVersionId, DisplayOrder, SnapshotHash | `MockExamId` → `MockExam`, `QuestionTranslationId` → `QuestionTranslation`, `AnswerKeyVersionId` → `AnswerKeyVersion` |
| `ExamAttempt` | `ExamAttemptId` | StudentId, MockExamId, AssignmentRecipientId, ScoringPolicyVersionId, StartedAt, DeadlineAt, FinalizedAt, AttemptStatus | `StudentId` → `StudentProfile`, `MockExamId` → `MockExam`, `AssignmentRecipientId` → `AssignmentRecipient`, `ScoringPolicyVersionId` → `ScoringPolicyVersion` |
| `AttemptQuestionSnapshot` | `AttemptQuestionSnapshotId` | ExamAttemptId, QuestionTranslationId, AnswerKeyVersionId, DisplayOrder, SnapshotHash | `ExamAttemptId` → `ExamAttempt`, `QuestionTranslationId` → `QuestionTranslation`, `AnswerKeyVersionId` → `AnswerKeyVersion` |
| `AttemptAnswer` | `AttemptAnswerId` | ExamAttemptId, AttemptQuestionSnapshotId, SelectedQuestionOptionId, SavedAt, MarksAwarded | `ExamAttemptId` → `ExamAttempt`, `AttemptQuestionSnapshotId` → `AttemptQuestionSnapshot`, `SelectedQuestionOptionId` → `QuestionOption` |
| `ExamResult` | `ExamResultId` | ExamAttemptId, Score, CorrectCount, IncorrectCount, UnansweredCount, GradedAt, RegradeVersion | `ExamAttemptId` → `ExamAttempt` |

## XACT Assignments

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `TeacherPaper` | `TeacherPaperId` | TeacherId, SubjectId, Title, Status | `TeacherId` → `TeacherProfile`, `SubjectId` → `Subject` |
| `TeacherPaperVersion` | `TeacherPaperVersionId` | TeacherPaperId, VersionNumber, CreatedAt, PublishedAt, Status | `TeacherPaperId` → `TeacherPaper` |
| `TeacherPaperItem` | `TeacherPaperItemId` | TeacherPaperVersionId, QuestionTranslationId, AnswerKeyVersionId, ItemOrder | `TeacherPaperVersionId` → `TeacherPaperVersion`, `QuestionTranslationId` → `QuestionTranslation`, `AnswerKeyVersionId` → `AnswerKeyVersion` |
| `Assignment` | `AssignmentId` | TeacherPaperVersionId, TeacherId, OpenAt, DueAt, AttemptLimit, Status | `TeacherPaperVersionId` → `TeacherPaperVersion`, `TeacherId` → `TeacherProfile` |
| `AssignmentRecipient` | `AssignmentRecipientId` | AssignmentId, StudentId, EnrollmentId, RecipientStatus, AssignedAt | `AssignmentId` → `Assignment`, `StudentId` → `StudentProfile`, `EnrollmentId` → `Enrollment` |

## Operations

| Candidate entity | PK | Core fields (proposed) | Relationships |
|---|---|---|---|
| `NotificationDelivery` | `NotificationDeliveryId` | RecipientUserId, EventType, ChannelCode, DeliveryStatus, SentAt | `RecipientUserId` → `UserAccount` |
| `OutboxMessage` | `OutboxMessageId` | EventType, AggregateType, AggregateId, PayloadJson, PublishedAt, RetryCount | — |
| `AuditEvent` | `AuditEventId` | ActorUserId, ActionCode, ObjectType, ObjectId, TimestampUtc, EventJson | `ActorUserId` → `UserAccount` |
| `SafetyReport` | `SafetyReportId` | ReporterUserId, SubjectUserId, CaseStatus, AssignedToUserId, OpenedAt | `ReporterUserId` → `UserAccount`, `SubjectUserId` → `UserAccount`, `AssignedToUserId` → `UserAccount` |
| `SupportTicket` | `SupportTicketId` | RequesterUserId, CategoryCode, TicketStatus, AssignedToUserId, CreatedAt | `RequesterUserId` → `UserAccount`, `AssignedToUserId` → `UserAccount` |

**Exceptions and gaps:** `UserRole` may need composite PK; `OrderLine` needs a line number; `MockQuestionSnapshot` needs immutable rendered question/option snapshot storage or immutable FK plus content hashes; enum values, money precision and physical FK strategy are unresolved. See constraints and approval gates.
