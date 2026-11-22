> **Latest technical design reference (22 Nov 2026):** [Full Technical Architecture v1.0](./UR_GURU_Complete_Technical_Architecture_v1.0.docx) and [MySQL/Hetzner alignment & open gates](./TECHNICAL-ARCHITECTURE-BASELINE-2026-11-22.md). These supersede earlier *engineering candidate choices* only, not the BRD or unsigned approvals.

# 04 — TECHNICAL ARCHITECTURE (UR GURU)

> **Document status:** **PROPOSED IMPLEMENTATION DESIGN — NOT APPROVED FOR PRODUCTION**  
> **Source baseline:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`, 19 November 2026 (12 pages). **Stakeholder sign-off pending.**  
> **Architecture reference:** [`../03-SYSTEM-ARCHITECTURE/Modular-Monolith-Architecture.md`](../03-SYSTEM-ARCHITECTURE/Modular-Monolith-Architecture.md) — single ASP.NET Core modular-monolith proposal.  
> **Primary approval gate:** BRD **OD-20** (final web/backend/database stack, environments and ERD schema). Separate commercial, legal and provider approvals remain open.  
> **Audience:** tech lead, frontend/backend engineers, QA, DevOps, security, Codex.

## What belongs here

Section 03 explains **WHAT connects to WHAT**. This section 04 explains **HOW the proposed system would be engineered**. No design below should be treated as an approved business rule or a finished physical schema.

| File | Contents | Status |
|---|---|---|
| [`Technology-Stack.md`](./Technology-Stack.md) | Confirmed business constraints vs proposed framework, platform and vendor options | Draft / OD-20 |
| [`Backend-Architecture.md`](./Backend-Architecture.md) | ASP.NET Core modular-monolith layering, module ownership, application flows, boundaries | Draft / OD-20 |
| [`Backend-Folder-Structure.md`](./Backend-Folder-Structure.md) | Proposed .NET solution/repository tree and file responsibilities | Draft / OD-20 |
| [`Frontend-Architecture.md`](./Frontend-Architecture.md) | Responsive Student/Teacher Web, separate Admin Web, routing, client/API/UX patterns | Draft / OD-20 |
| [`Security-Architecture.md`](./Security-Architecture.md) | Authentication, role + object authorization, privacy, safeguarding, webhook/media security | Draft / OD-15/19/20 |
| [`Integrations-Design.md`](./Integrations-Design.md) | Payment, live classroom, demo/VOD, object storage, notifications and their failure behavior | Draft / OD-02/05/06 |
| [`Infrastructure-Design.md`](./Infrastructure-Design.md) | Logical environments, deployment, pipeline, backup/restore and operations | Draft / OD-16/20 |
| [`Database-Access-and-Migrations.md`](./Database-Access-and-Migrations.md) | Module data ownership, transactions, proposed EF Core and migration discipline | Draft / OD-20 |
| [`Module-Contracts.md`](./Module-Contracts.md) | Proposed in-process module APIs, commands, events, cross-module boundaries | Draft / OD-20 |
| [`Reliability-Observability-and-Testing.md`](./Reliability-Observability-and-Testing.md) | NFR candidates, idempotency, outbox, logs, test layering and test matrix | Draft / OD-16/20 |
| [`Technical-Decisions-and-Gates.md`](./Technical-Decisions-and-Gates.md) | Approval checklist before physical implementation | Pending approval |

## Source-critical invariants: never change without BRD approval

1. Current channels: **responsive Student/Teacher Web** and **separate Admin Web portal**; no native app now.
2. Initial Grade 12/13 curriculum: **Biological Science (Bio)** and **Physical Science (Maths)** only. Future streams are not launched.
3. Assessment feature name: **XACT**; “Exam Munnodi” is the historical label.
4. **Optional, free, prerecorded DemoVideo**, linked to `ClassOffering`, may be watched **or skipped**; no live-trial booking or checkout prerequisite (BR-04, AC-07/31/33).
5. `StudentSubject` **is not** `Enrollment` and gives **no** paid entitlement (BR-01, AC-32).
6. Payment entitlements require authenticated, **server-verified** gateway status; financial ledger must be auditable and append-only (BR-06).
7. XACT scoring, timer/deadline and versioned question/key snapshot are **server-side**; no unsupported translation fallback (BR-18/19; AC-16–25).
8. No unapproved guardian dashboard, NIC verification route, recording or data policy.

## How a developer or Codex should use this folder

1. Read the applicable BRD requirements and status in [`../02-BRD-AND-REQUIREMENTS/`](../02-BRD-AND-REQUIREMENTS/).
2. Read the logical module/flow in [`../03-SYSTEM-ARCHITECTURE/`](../03-SYSTEM-ARCHITECTURE/).
3. Use the appropriate design file here as a **proposal**, not approval to invent policy.
4. Verify names and constraints against [`../07-DATABASE-DESIGN/`](../07-DATABASE-DESIGN/) and [`../08-API-DOCUMENTATION/`](../08-API-DOCUMENTATION/). Old V6.1 SQL/endpoint assumptions may be incompatible with V6.2.2.
5. Record disputed decisions under [`../13-DECISION-LOG/`](../13-DECISION-LOG/). Stop before applying irreversible database, payment or contract changes without owners' sign-off.
6. Implement in small reviewed vertical slices, with tests, audit/logging and documentation updates.

**Document owners (proposed):** Engineering Lead (technical architecture), Security Lead (security), DevOps Lead (infrastructure), Product/Academic/Finance (business gates). Names and sign-off dates: **PENDING**.


## 104-API MVP alignment
Use `../08-API-DOCUMENTATION/API-REGISTER.csv` as the active endpoint inventory. Finalize per-endpoint DTOs, permissions, persistence, idempotency, failure handling and provider integration before treating the 104 contracts as implementation-ready. Previous 292-endpoint references are historical.
