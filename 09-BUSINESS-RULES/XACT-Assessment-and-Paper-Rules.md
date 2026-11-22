# XACT Assessment, Question Bank and Assignment Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Naming and scope
**XACT** is the active name. **Exam Munnodi** is legacy naming. Supported media/subjects are only those with approved rights, translation, versioned answer key and available curriculum coverage.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-043 | XACT is the current assessment product name; Exam Munnodi is historical terminology, not a separate active product. | BRD §1–2 p.2, Appendix B p.11 | — | Review baseline |
| UG-RULE-044 | Question catalogue must retain source paper/year, subject, medium, rights evidence and attribution for each candidate source. | BRD §8.1 p.6 | AC-16 | Review baseline |
| UG-RULE-045 | Canonical question concept is distinct from approved translation/option/answer-key versions; stable option identifiers survive display reordering. | BRD §8.1 p.6 | AC-16, AC-17 | Review baseline |
| UG-RULE-046 | Each Tamil, Sinhala and English translation requires independent academic approval and must not silently fall back to another medium. | BRD §3 p.3, §8.1 p.6 | AC-16, AC-17 | Review baseline |
| UG-RULE-047 | Only rights-cleared, approved, active concept, translation and answer-key combinations may be used in practice and exams. | BRD §8.1 p.6 | AC-16 | Review baseline |
| UG-RULE-048 | Question/key corrections create versioned records; previously attempted snapshots remain immutable and changes are auditable. | BRD §8.1–8.2 pp.6–7 | AC-20, AC-25 | Review baseline |
| UG-RULE-049 | Students may practice by approved paper/year/subject/medium or configure mocks by available topics, difficulty, count and time presets. | BRD §8.2 p.6 | AC-18 | Review baseline |
| UG-RULE-050 | Mock generation selects from eligible approved pool without duplicate canonical questions and explains insufficient inventory. | BRD §8.2 p.6 | AC-18 | Review baseline |
| UG-RULE-051 | Generated attempt snapshot retains question/option order, translation/key versions, scoring-policy version, time limit and source references. | BRD §8.2 p.6 | AC-20 | Review baseline |
| UG-RULE-052 | Backend is authoritative for exam start, deadline, autosave, submission and grading; client timer is display-only. | BRD §8.2 pp.6–7 | AC-19, AC-20 | Review baseline |
| UG-RULE-053 | Attempt state is one of NotStarted, InProgress, Submitted, AutoSubmitted, Expired or Invalidated; resumability/grace requires configuration and audit. | BRD §8.2 p.7 | AC-19 | Pending policy OD-10 |
| UG-RULE-054 | Autosave retries must not lose server-confirmed answers; duplicate submission must create only one final result. | BRD §8.2 p.6, §13 p.10 | AC-19, AC-20 | Review baseline |
| UG-RULE-055 | Results show approved score, correct/incorrect/unanswered, topic progress and history; answer reveal follows review policy. | BRD §8.2 p.7 | AC-20, AC-22 | Pending policy OD-10 |
| UG-RULE-056 | Do not infer topic mastery where sample size is insufficient; coverage and limitations must be transparent. | BRD §8.2 p.7 | — | Review baseline |
| UG-RULE-057 | Only authorized approved teachers may build, preview, version, publish and assign papers from a read-only approved bank. | BRD §8.3 p.7 | AC-23, AC-24 | Review baseline |
| UG-RULE-058 | Each assignment references immutable teacher paper version and authorized recipients; each recipient has a separate attempt/result. | BRD §8.3 p.7 | AC-21, AC-23 | Review baseline |
| UG-RULE-059 | Paper reuse creates a new assignment; historical paper versions, recipient attempts and scores are preserved. | BRD §8.3 p.7 | AC-24 | Review baseline |
| UG-RULE-060 | Teacher score/answer-level access requires ownership or authorized assignment membership; regrades are audited. | BRD §8.3 p.7 | AC-21, AC-25 | Review baseline |
| UG-RULE-061 | XACT explanation video passes secure processing, academic/rights review and authorized publication; rejected/unprocessed media cannot publish. | BRD §8.4 p.7 | AC-26 | Review baseline |
| UG-RULE-062 | Written explanation fallback remains when video is unavailable; XACT video entitlement differs from free class demo media. | BRD §8.4 p.7 | AC-22, AC-26 | Review baseline |
| UG-RULE-063 | Question count, duration, retries, marking, negative marks, reveal/grace and difficulty quotas require approved configuration. | BRD §14 p.10 | AC-18, AC-19 | Pending policy OD-10/OD-11 |

## Integrity-sensitive scenarios
- Two translated displays of the same canonical question cannot create duplicate canonical items in one mock.
- Incorrect-medium content must not silently substitute another translation.
- Repeated submit returns one final versioned score.
- Teacher paper reused for new cohort must not change earlier records.
- Expired/failed explanation video retains approved written fallback.

## Open academic decisions
**OD-07–OD-12** include content rights, inventory, answer corrections, timing/negative marking, difficulty distribution and explanation video compensation. **OD-13** applies if XACT becomes paid.
