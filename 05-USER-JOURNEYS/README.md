# 05 — USER JOURNEYS | UR GURU

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

## Purpose

Explain **how users reach an outcome**, including entry conditions, happy paths, failure states, permissions and source traceability. This folder is a navigation layer for product, UI/UX, frontend, backend, QA and Codex; it is **not an API specification**.

## Current product baseline

- **Channel:** Responsive Student/Teacher web plus separate Admin web portal; native apps out of current release.
- **Grades:** Sri Lankan G.C.E. A/L Grade 12–13.
- **Initial curricular release:** Biological Science (Bio) and Physical Science (Maths), subject to catalogue approval. Commerce, Arts and Technology are future/uncommitted.
- **Assessments:** **XACT** is the current brand; *Exam Munnodi* is a legacy name.
- **Class previews:** Optional, free **prerecorded** demos. No live trial bookings; watching is never a requirement for enrollment.
- **Release lanes:** R0 foundation, R1 marketplace, R2 XACT. R1/R2 sequence change requires OD-18 approval.
- **BRD status:** Consolidated corrected **review candidate**, **not signed off**.

## Contents

| File | Covers |
|---|---|
| [User-Journey-Overview.md](User-Journey-Overview.md) | SJ-01–SJ-16 index, actors, source pages, releases |
| [Student-Journey.md](Student-Journey.md) | Student onboarding, discovery, class, XACT and safety |
| [Teacher-Journey.md](Teacher-Journey.md) | Verification, demo submission, classes, papers and videos |
| [Admin-Journey.md](Admin-Journey.md) | Admin, academic, finance and safeguarding review workflows |
| [Optional-Demo-Video-Journey.md](Optional-Demo-Video-Journey.md) | Free preview / skip / approval / direct enrollment |
| [Payment-and-Refund-Journey.md](Payment-and-Refund-Journey.md) | Paid class, payment verification, refund and ledger |
| [XACT-Journeys.md](XACT-Journeys.md) | Practice, mocks, assignments, paper authoring and explanations |
| [Guardian-Consent-Journey.md](Guardian-Consent-Journey.md) | Consent touchpoint only; no current guardian dashboard |
| [Exception-and-UI-States.md](Exception-and-UI-States.md) | Exception handling and proposed UI-state checklist |
| [Journey-Screen-Mapping.csv](Journey-Screen-Mapping.csv) | 16 SJ IDs, proposed screen families, **unverified actual screen IDs** |
| [Journey-Requirement-UAT-Matrix.csv](Journey-Requirement-UAT-Matrix.csv) | 16 SJ IDs, proposed BR and AC cross-references, decision blockers |
| [User-Journey-Flow.mmd](User-Journey-Flow.mmd) | Editable Mermaid flow overview |

## How to use these documents

1. Select a journey by its **SJ-xx ID**, and read the corresponding detailed flow.
2. Check source BRD sections and associated BR/AC links.
3. Identify UI state requirements and unresolved OD approvals.
4. Link **actual** approved UI screen IDs in `Journey-Screen-Mapping.csv` after prototype verification.
5. Only then link verified API endpoints, DB tables and test cases in Section 02 traceability documents.

## Source vs derived mapping

- **Exact BRD source:** SJ-01 to SJ-16 and their happy/exception paths — BRD pp. 8–9; BR register p. 4; UAT pp. 9–10.
- **Draft elaboration:** Screen-family labels, actor handoffs, derived BR↔SJ↔AC associations, and proposed UI-state checklist — review required.
- **No invented contracts:** No URLs, exact screen IDs, timer durations, refund SLAs, commission percentages, providers or deployment dates have been assumed.

## Release / approval gates

See BRD §2 (p. 3) and OD-01–OD-20 (pp. 10–11). In particular OD-02 demo access/rights, OD-04 refunds, OD-05 payment provider, OD-06 live/media provider, OD-07–11 content and exams, OD-15 minors and consent, OD-18 R1/R2 order, OD-20 technical stack/ERD.
