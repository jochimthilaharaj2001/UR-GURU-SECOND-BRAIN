# XACT Assessment Journeys — Student, Teacher and Reviewers

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

**Current brand:** **XACT**; former documentation may say *Exam Munnodi*. **Release:** R2, with R1/R2 pilot priority requiring OD-18 approval. **Sources:** BRD §8 pp. 6–7, §12 p. 9, UAT pp. 9–10.

## Eligibility, approval and provenance (all XACT paths)

- Question concept has stable canonical identity and syllabus/subject/topic/difficulty provenance.
- Only approved **source rights + concept + translation + answer-key version** yield eligible questions.
- Each Tamil/Sinhala/English variant has independent approval; no fallback to an unapproved medium.
- Question translations/answer keys/scoring policy are snapshotted or immutably version-referenced for each attempt; corrections cannot rewrite history.
- Formulas, scientific units, diagrams and long options must remain accessible on target devices.

## SJ-09 — Past-paper practice (Student)

1. Open XACT and choose approved paper/year, subject, syllabus and available medium.
2. Load only eligible questions for that source selection.
3. Start authorized practice, select answers, persist autosaves and show state/status.
4. Server applies approved timing, submission and grading policy; one final result per valid attempt.
5. Display total/correct/incorrect/unanswered, topic context and **approved** written/video explanation according to reveal/entitlement policy.

**Exceptions:** Desired translation absent, answer edit locked by deadline, interrupted autosave, duplicate submit, unavailable explanation video (written fallback). **Refs:** BR-11/18/23; candidate AC-16/17/19/20/22/25/28.

## SJ-10 — Configurable mock (Student)

1. Choose subject, syllabus and approved medium.
2. Choose **selected topics or all topics**, approved difficulty selection, available question count and time presets.
3. Backend constructs eligible pool with **no duplicate canonical question**; verify sufficient coverage.
4. Store immutable question/option order, question translation, answer key and scoring-policy version at generation.
5. Student attempts questions. Server owns start/deadline, autosave, resumption rules and submission.
6. Score on server; present result and topic-wise evidence (avoid overclaiming with low sample sizes).

**Exceptions:** Insufficient eligible pool → clear shortage and valid options, no invented question; expiry → block late edit; repeat submit → one result; lost connectivity → retry-safe save subject to approved grace/resume rules.

**Open:** OD-10 timers, marks, attempts, negative grading, review; OD-11 difficulty quotas; OD-07/08 content rights/coverage.

## SJ-11 — Teacher-assigned paper (Student)

1. Teacher assigns a **versioned paper** to individually authorized student recipients/class members with approved open/due windows and attempt limits.
2. Each assigned student receives notification and may open **only own** permitted assignment.
3. Each student has an independent attempt and result; expired/unauthorized recipient is denied.
4. Authorized teacher sees only assigned/enrolled learners' results.

**Exceptions:** Closed window, unauthorized recipient, retake limit, teacher suspension or prior paper correction. Follow approved continuity and regrade rules.

## SJ-12 — Teacher paper authoring

1. Verified teacher filters the predefined, approved **read-only** bank by authorized subject/topic/medium.
2. Creates ordered paper draft and previews.
3. Publishes immutable paper version once validation succeeds.
4. Assigns to multiple selected authorized students. Reassigning creates separate assignment records, never overwrites old results.
5. Views scoped completion and results; question withdrawal/correction is audited, never silently rewritten.

**Source:** BRD §8.3 p. 7; BR-19; candidate AC-21/23/24/25.

## SJ-13 — Explanation video

Teacher submits original/licensed question- and approved-medium-linked video with compensation declaration → upload/processing → independent academic/content review → approved publication → authorized signed playback. Rejected/failed/withdrawn videos cannot publish; approved written fallback remains.

**Distinct from** free ClassOffering demo preview. **Open:** OD-07/09/12.

## Security and tests

- Backend owns score; UI cannot modify score/key.
- No other student/unauthorized teacher may read attempts, assignments or full results.
- AC-16 to AC-26 and AC-28 are key checkpoints; exact scenario traceability is a **draft mapping** in `Journey-Requirement-UAT-Matrix.csv`.
- Never generate AI-authored answer keys or mark unreviewed content as official.
