# DEV_5: Exam Munnodi Specialist (Assessment Engine) — Context & Starter

**Developer ID:** `DEV_5`  
**Role:** Exam Munnodi Feature Lead  
**Primary Focus:** 5-Year past-paper question bank model, student mock exam generator, server-side scoring engine, teacher paper builder, and video explanation integration.

---

## 1. My Core Responsibilities
- **Question Bank Architecture (`C-04`):**
  - Implement language-neutral `QuestionConcept` linked to medium-specific `QuestionTranslation` records (Tamil, Sinhala, English).
  - Versioned `AnswerKeyVersion` checked per translation for option order.
  - Zero silent fallback: return "Unavailable" if no approved translation exists in student's chosen medium.
- **Mock Generation Engine (`BR-18`):**
  - Topic-based mocks (selected topics) and all-topic mocks across the A/L stream syllabus.
  - Difficulty distribution (`Easy`, `Medium`, `Hard`).
  - Shortage handling: clearly report insufficient questions; **NEVER** fabricate dummy questions (`AC-07`, `AC-13`).
- **Server-Side Grading & Anti-Cheat:**
  - Client never receives correct answer keys during active exam attempt.
  - Immutable question version snapshotting on generation (`ExamAttempt` $\to$ `QuestionVersion`).
  - Idempotent submission: prevent duplicate scoring or corrupted attempt state.
- **Teacher Paper Builder & Multi-Student Assignment (`BR-19`):**
  - Allow verified teachers to curate approved questions into reusable papers.
  - Assign to multiple students with deadlines and independent attempt tracking (`AC-15`, `AC-16`).
- **Explanation Workflows (`BR-20`, `C-07`):**
  - Written explanation fallback guaranteed if video fails.
  - Teacher video upload $\to$ Academic review $\to$ Approved publishing state machine.

---

## 2. Key References I Must Read
1. [`17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md`](../../17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md)
2. [`02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) (Sections 7.1–7.4, 8.5)
3. [`07-DATABASE-DESIGN/README.md`](../../07-DATABASE-DESIGN/README.md) (Modules 06, 07, 08)

---

## 3. AI Starter Prompt (Copy-paste this when starting a new session)
```markdown
I am DEV_5 (Exam Munnodi Specialist) working on the UR GURU assessment and mock exam engine.
Workspace: D:\Unicom\UR_GURU_finalProject
Please read my context file:
UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_5\CONTEXT.md
And the Exam Munnodi specification:
UR-GURU-SECOND-BRAIN\17-EXAM-MUNNODI\EXAM_MUNNODI_FULL_SPEC.md

Today I am developing [MOCK GENERATOR / SCORING LOGIC / PAPER BUILDER / QUESTION INGESTION].
Enforce the canonical translation model, zero client-side answer exposure, question version snapshotting, and server-side idempotency.
```

---

## 4. My Daily Work Log
Record daily activities in `WORK-LOG-YYYY-MM-DD.md`.
Log any assessment-engine decisions or schema requests in `../SHARED-DECISIONS/CROSS-TEAM-LOG.md`.
