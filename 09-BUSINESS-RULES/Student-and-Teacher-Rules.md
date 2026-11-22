# Student and Teacher Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Scope
G.C.E. A/L Grades 12–13; launch curriculum is **Biological Science (Bio)** and **Physical Science (Maths)** only. The historical V2 register's generic Science/Commerce/Arts/Technology launch statement is superseded. There is no native application or standalone guardian portal in the current release.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-001 | Student registration must support only G.C.E. A/L Grades 12 and 13; reject unsupported grades. | BRD §2–3 pp.3, §5 p.4 | AC-01 | Review baseline |
| UG-RULE-002 | Initial selectable curriculum is Biological Science and Physical Science (Maths) only; other streams are future/uncommitted, not selectable as launch-available. | BRD §2–3 p.3 | AC-01 | Review baseline |
| UG-RULE-003 | Students may choose one or more supported subjects only if the stream, syllabus availability and academic year permit them. | BRD §3 p.3, §6.1 p.5 | AC-01, AC-32 | Review baseline |
| UG-RULE-004 | Persist each student/subject/academic-year choice in StudentSubject with a uniqueness control against duplicate active selections. | BRD §3 p.3, §6.1 p.5, §10 p.7 | AC-01, AC-32 | Review baseline |
| UG-RULE-005 | Subject selection is not paid class enrollment, and must never itself issue class access or an entitlement. | BRD §3 p.3, §10 p.8 | AC-32 | Review baseline |
| UG-RULE-006 | Account states include Pending Verification, Active, Locked, Suspended and Closed; recovery and logout must invalidate applicable sessions. | BRD §6.1 p.5 | AC-02 | Review baseline |
| UG-RULE-007 | Registration and recovery must not reveal the existence of another person’s account through identity-enumeration responses. | BRD §13 p.9 | AC-02 | Review baseline |
| UG-RULE-008 | Only approved, active teachers and their eligible public class offerings appear in discovery. | BRD §6.2 p.5 | AC-05, AC-06 | Review baseline |
| UG-RULE-009 | Teacher verification follows Draft → Submitted → Needs Information → Approved/Rejected/Suspended, recording actor, timestamp and reason for decisions. | BRD §6.2 p.5 | AC-05 | Review baseline |
| UG-RULE-010 | Teachers cannot self-approve identity/qualification verification or publish paid offerings before approval. | BRD §4 p.4, §6.2 p.5 | AC-05 | Review baseline |
| UG-RULE-011 | Teacher listings may expose authorized subjects, medium, schedules, price and approved demo availability, not private evidence, rosters, payments or contacts. | BRD §6.2 p.5 | AC-06 | Review baseline |
| UG-RULE-012 | Ratings remain disabled until a moderation, eligibility and anti-fraud policy is approved. | BRD §6.2 p.5 | — | Pending policy OD-01 |
| UG-RULE-013 | Teacher suspension prevents unauthorized new publishing; treatment of existing paid students requires an approved continuity policy. | BRD §6.2 p.5 | AC-05 | Pending policy OD-01/OD-04 |

## Validation cases to implement later
- Student cannot select a future/unavailable stream or duplicate active subject/year.
- StudentSubject selection cannot create Enrollment or Entitlement.
- Suspended/unverified teacher cannot publish or expose private verification evidence.
- An unknown email address should not be disclosed through account recovery messages.

## Open decisions
Teacher screening and ratings: **OD-01**. Guardian consent and NIC policy: **OD-15, OD-19**.
