# XACT — canonical content, language versions, paper snapshots and attempts

**BRD:** v6.2.2 pp6–7, 9–10, 11. Status: proposed logical model; no DB/migration approval.

## Content version path

`PastPaperSource + SourceRightsRecord → QuestionConcept → QuestionTranslation → QuestionOptionTranslation + AnswerKeyVersion → WrittenExplanationVersion / ExplanationVideo`.

- QuestionConcept is stable logical identity across Tamil, Sinhala and English. **Option identity is canonical** (`QuestionOption`); its translated text and displayed order are per `QuestionTranslation` revision.
- Do not assume all three mediums exist. Every medium/version/key must be approved **independently**.
- Key version must unambiguously identify the correct canonical option for a specific approved translation. No update of answer key in place after an attempt.
- Teacher explanation video requires rights and review, and is different from free pre-enrollment ClassOffering DemoVideo.

## Student mock & attempt

1. Backend validates stream, subject, syllabus, requested medium, topic, difficulty, inventory, published rights and scoring preset.
2. Backend selects approved questions **without duplicate canonical concepts** and persists question/option order and immutable version references in `MockQuestionSnapshot` (or equivalent immutable content snapshot). Each started `ExamAttempt` also freezes its own `AttemptQuestionSnapshot`, including assigned-paper attempts.
3. `ExamAttempt` is server-started, with server deadline and one authoritative submission state. Student client timer is display-only.
4. Each answer save uses idempotent persistence on `AttemptAnswer`; intermittent connectivity must not erase server-confirmed saved answers.
5. Backend scores with frozen `AnswerKeyVersion` and `ScoringPolicyVersion`, then writes `ExamResult` once, recording controlled regrades as later versions.
6. Historical attempt stays visible after a question correction/withdrawal; review access follows approved policy.

## Teacher paper & assignment

`TeacherPaper → TeacherPaperVersion → TeacherPaperItem`, and `Assignment → AssignmentRecipient → ExamAttempt`.

A teacher may reuse the same published paper version in multiple assignments without mutating old recipients/results. Each recipient's permissions are independent. `ExamAttempt.MockExamId` vs `AssignmentRecipientId` must be modeled with an approved discriminated union/check constraint (or separate exam context) before migrations.

## Explicit missing approvals

OD-07 content rights; OD-08 inventory; OD-09 review/regrade policy; OD-10 exam time/mark/retakes/reveal; OD-11 quotas/translation checks; OD-12 video terms; OD-13 monetization. These are **not** implementation defaults.

**Security tests:** AC-16–26, AC-28. Subject medium mismatch must not silently fall back. Old 45-table SQL assessment tables are not an equivalent XACT model.
