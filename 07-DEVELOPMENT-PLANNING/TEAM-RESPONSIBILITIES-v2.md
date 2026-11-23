# Team Responsibilities v2 — 23 November 2026

**Confirmed allocation:** DEV 1 and DEV 2 = backend; DEV 3 and DEV 4 = student frontend; DEV 5 = teacher frontend; DEV 6 = admin frontend.

| Developer | Ownership | Coordination |
|---|---|---|
| DEV 1 | Backend — proposed identity, profiles, curriculum, discovery | Coordinate shared API contracts and migrations with DEV 2 |
| DEV 2 | Backend — proposed classes, payments, live, XACT, operations | Coordinate cross-module transactions and integrations with DEV 1 |
| DEV 3 | Student frontend — proposed onboarding, account, subject selection, discovery | Share student app with DEV 4 |
| DEV 4 | Student frontend — proposed enrollment, payment, live, resources, XACT | Share student app with DEV 3 |
| DEV 5 | Teacher frontend — teacher workflows | Consume backend contracts from DEV 1/2 |
| DEV 6 | Admin frontend — admin/reviewer/finance workflows | Consume backend contracts from DEV 1/2 |

**Important:** Only the six role assignments above are confirmed. Specific module/API ownership is a proposal until the 104-API MVP tracker and developer capacity are reviewed. Backend ownership is not necessarily a 50/50 endpoint count; prioritize complexity and dependencies. Assign one migration integrator and one shared frontend library maintainer by team agreement.

**BRD boundary:** Student and Teacher share a responsive web channel; Admin is a separate portal. Distinct developer ownership does not require three independently deployed Angular applications. Preserve BRD v6.2.2 requirements and signed decisions.
