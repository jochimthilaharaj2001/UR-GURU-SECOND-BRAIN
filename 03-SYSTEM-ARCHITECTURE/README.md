# 03 — SYSTEM ARCHITECTURE (UR GURU)

> **Status:** Architecture documentation draft based on **UR GURU Full Corrected BRD v6.2.2 (19 November 2026)**. The BRD is a **consolidated review candidate — stakeholder sign-off pending**. Diagrams here are *logical views*, **not** a production infrastructure approval or finalized ERD.

## Contents

| File | What it explains | Status |
|---|---|---|
| [`System-Architecture-Diagram.png`](./System-Architecture-Diagram.png) | Users/web channels, logical backend boundaries, stores and external providers | Draft visualization |
| [`System-Architecture-Diagram.dot`](./System-Architecture-Diagram.dot) | Editable Graphviz source of diagram | Draft visualization |
| [`System-Architecture-Diagram.svg`](./System-Architecture-Diagram.svg) | Scalable diagram for zooming/embedding | Draft visualization |
| [`System-Flow.md`](./System-Flow.md) | Primary end-to-end journeys, branches and failure states | Source-grounded draft |
| [`Module-Interaction.md`](./Module-Interaction.md) | Module responsibilities, permissions and inter-module events | Proposed decomposition; validate implementation |
| [`External-Integrations.md`](./External-Integrations.md) | Payment, live sessions, media, messaging, conditional identity and provider risks | Interfaces conceptual; vendors pending |
| [`Authentication-and-Access-Flow.md`](./Authentication-and-Access-Flow.md) | Identity lifecycle, role + ownership access, guardian consent and data boundaries | Policy/implementation pending |
| [`Data-Flow-Diagram.png`](./Data-Flow-Diagram.png) | Conceptual information movement through UR GURU | Draft visualization |
| [`Data-Flow-Diagram.dot`](./Data-Flow-Diagram.dot) | Editable Graphviz source of data-flow diagram | Draft visualization |
| [`Data-Flow-Diagram.svg`](./Data-Flow-Diagram.svg) | Scalable data-flow diagram for zooming/embedding | Draft visualization |

## Architecture style — explicit proposal

**Proposed:** one C# ASP.NET Core **Modular Monolith** backend, with R0/R1/R2 business modules in-process and two browser entry points (Student/Teacher responsive web and separate Admin web). **Not approved:** BRD v6.2.2 OD-20 leaves final stack, physical deployment and database choice for sign-off. This is **not** a microservices diagram. See [`Modular-Monolith-Architecture.md`](./Modular-Monolith-Architecture.md).

## Current scope and exclusions

- Channels: **responsive Student/Teacher web** and a **separate Admin web portal**; **no native mobile app** in current release (BRD pp. 1–3).
- Initial curriculum: **Grade 12–13 Biological Science and Physical Science/Maths**. Commerce, Arts and Technology are **future/uncommitted** (pp. 2–3).
- Assessments are **XACT** (formerly “Exam Munnodi”); avoid legacy brand in new UI/API specification (pp. 1–2, 6–7).
- `BR-04` = **optional, free, approved prerecorded class DemoVideo**. **No scheduled live-trial booking**. Watching a demo is **not** required for checkout (pp. 5, 12).
- `StudentSubject` records selected subjects, **not** paid `Enrollment` (pp. 3, 5, 7).
- Work lanes: **R0 Foundation**, **R1 Marketplace**, **R2 XACT**. Release sequencing is **not finally signed off** (p. 3, OD-18).

## Architecture decisions not yet approved

- **OD-05** payment gateway and capabilities; **OD-06** live/VOD/CDN providers and recording policy.
- **OD-15 / OD-19** minor/guardian consent and NIC/identity validation routes.
- **OD-16** production environment, capacity and NFR SLA; **OD-20** web/backend/database stack, schema and infrastructure choices.
- **OD-07/08/09** question rights/academic review and content completeness; **OD-10/11** exam scoring/timer rules.
- **ERD v1.2 is proposed**; no physical database schema or migration is approved solely by these diagrams.

## How to use

1. Read the relevant BRD requirement (BR-01 … BR-24) in [`../02-BRD-AND-REQUIREMENTS/`](../02-BRD-AND-REQUIREMENTS/).
2. Use this folder to understand **flows and logical components**, not concrete routes/tables or deployment wiring.
3. Before implementation, validate the proposed components with `04-TECHNICAL-ARCHITECTURE`, `07-DATABASE-DESIGN`, `08-API-DOCUMENTATION`, the Decision Log and actual source code.
4. Do **not** turn dotted/“PENDING” vendor interfaces into hard-coded products, prices or authentication policies.
5. Update both diagram sources (`.dot`) and rendered `.png` when modifying an approved flow.

**Source:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`, especially sections 2–14 and Appendix A/C. Original should live in `02-BRD-AND-REQUIREMENTS/`.

## Modular Monolith specific readme

- [`Modular-Monolith-Architecture.md`](./Modular-Monolith-Architecture.md) — proposed single-backend-deployable, module responsibilities, boundaries, interactions and explicit approval gates.
