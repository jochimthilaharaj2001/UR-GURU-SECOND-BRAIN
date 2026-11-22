# Modular Monolith — Proposed System Architecture

**Document ID:** SYS-ARCH-02  
**Project:** UR GURU  
**Source baseline:** `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf` (19 November 2026)  
**Status:** **PROPOSED / PENDING ARCHITECTURE APPROVAL (OD-20)**  
**Scope:** R0 Foundation, R1 Marketplace, R2 XACT

## 1. Architectural decision candidate

UR GURU can use a **C# ASP.NET Core modular monolith** as its initial backend architecture. This is an **engineering proposal**, not a technology/deployment commitment approved by BRD v6.2.2. The BRD defines logical business modules, roles and flows but leaves final web/backend/database technology and schema approval to **OD-20**.

The design uses:

- **Two web entry points:** responsive **Student/Teacher Web** and a **separate Admin Web Portal**.
- **One modular backend deployable:** one ASP.NET Core application hosting multiple business modules in-process.
- **Strict module boundaries:** explicit module interfaces, ownership of business logic and data; no cross-module direct repository access.
- **One logical relational database (proposed):** module-owned tables/schemas or equivalent boundary rules; final DB engine, physical ERD, migrations and deployment **pending OD-20**.
- **External dependencies behind adapters:** payment, live classroom, private object storage/media/CDN and messaging providers remain unselected (**OD-02/05/06**).
- **Async work where needed:** outbox-backed notification delivery and media processing; separate worker deployment is an optional later technical decision, not a microservice requirement.

**What it is NOT:** a microservices architecture, one database per service, a suite of independently deployed backends, a mandate for a message broker, or confirmation that the existing SQL/ERD is approved.

## 2. Logical module boundaries (in-process)

| Group | Module | Owns business responsibility | BRD mapping |
|---|---|---|---|
| R0 Foundation | Identity & Access | Accounts, authentication, role/object authorization, consent and identity-policy hooks | BR-01/21/22 |
| R0 Foundation | Academic Catalogue | Grade/stream/subject/medium/syllabus and `StudentSubject` selection validation | BR-01/23 |
| R1 Marketplace | Teacher & Discovery | Teacher approval, public profiles, eligible class discovery | BR-02/03 |
| R1 Marketplace | Demo Video | Optional **free**, approved, prerecorded demo linked to `ClassOffering`; no live trial booking | BR-04 |
| R1 Marketplace | Class, Batch & Enrollment | Batch capacity, scheduling, enrollment, attendance and authorized live access | BR-05 |
| R1 Marketplace | Orders, Payments & Finance | Payment attempts, server-verified entitlement, append-only ledger, refund, earnings/payout controls | BR-06 |
| R1 Marketplace | Learning Resources | Protected media resources, revisions, entitlement-based access | BR-07 |
| R2 XACT | Question & Content Governance | Rights, canonical questions, translations, answer-key versions and academic review | BR-18/20/23 |
| R2 XACT | Exam Engine & Results | Generated immutable attempts, autosave, deadlines, idempotent submit and server-side scoring | BR-11/18 |
| R2 XACT | Teacher Papers & Assignments | Versioned papers, scoped recipient assignments, individually authorized results | BR-19 |
| Cross-cutting | Notifications, Audit & Safety | Outbox and retries, audit trails, safety escalations, moderation activities | BR-13/14/21/24 |

Logical groupings may be implemented as modules inside one host. Their **names** are proposed architecture vocabulary, not newly approved BRD requirements.

## 3. In-process communication rules

1. Each module exposes explicit **application interfaces/contracts** to other modules.
2. Dependencies flow through approved interfaces or events; do not read/write another module's persistence tables directly.
3. Transactions remain local where practical. For payment/enrollment/entitlements, design verified idempotency, capacity invariants and ledger integrity; exact payment/seat reservation sequence is **PENDING OD-04/05/20**.
4. Publish reliable events via a **transactional outbox design candidate**; consumers must be idempotent. The BRD expects retry-safe notifications, but broker/worker technology is **not chosen**.
5. Server-side authorization checks both caller **role** and **object ownership/membership**.
6. External systems are integration adapters with timeouts, retries, safe callbacks, and audited decisions.

## 4. Critical user journeys

- **Subject selection:** Student → Identity → Catalogue → `StudentSubject`. **No `Enrollment`/payment/entitlement.**
- **Optional demo:** Teacher uploads class-linked free media → review → approved public preview; student can watch **or skip** and enroll directly. No scheduled trial booking, trial capacity or watch-completion prerequisite.
- **Paid class:** Student selects batch → order/payment → authenticated and verified gateway result → protected enrollment/entitlement → valid-time live join. Capacity/payment ordering requires design sign-off.
- **XACT:** Approved question/translation/key → immutable exam snapshot → autosave/submit → server scoring → authorized results and explanation access.
- **Teacher paper:** Authorized teacher → approved question bank → versioned paper → recipients → separate student attempts and scoped reporting.

## 5. Deployment boundaries (proposal)

```text
Student + Teacher Responsive Web       Separate Admin Web
                \                    /
                 \      HTTPS       /
               One ASP.NET Core API Host
          (Modular Monolith: R0 / R1 / R2)
                   |            |
       Relational Database     Object Storage
       [engine pending]       [provider pending]
                   |
  External adapters -> Payment / Live / Media / Messaging
                     [vendor decisions pending]
```

**Single backend deployment** means the business modules are released together. It does **not** prohibit multiple web frontends or external managed services.

## 6. Open decisions and review gates

- **OD-20:** Sponsor/engineering sign-off for modular monolith, concrete web/backend/DB choices, hosting strategy, migration/ERD and module contracts.
- **OD-18:** Initial production R1 vs R2 rollout sequence, while prototypes can proceed independently.
- **OD-02/05/06:** Demo rights/access, payment and classroom/video providers.
- **OD-07–11:** Rights, translation approvals, XACT configuration/scoring/content ownership.
- **OD-15/19:** Guardian consent, minor safeguards, NIC/identity process.
- **OD-16:** Availability, capacity targets, security and release operations.

## 7. Related docs

- [`README.md`](./README.md)
- [`System-Architecture-Diagram.png`](./System-Architecture-Diagram.png)
- [`Data-Flow-Diagram.png`](./Data-Flow-Diagram.png)
- [`Module-Interaction.md`](./Module-Interaction.md)
- [`System-Flow.md`](./System-Flow.md)
- [`Authentication-and-Access-Flow.md`](./Authentication-and-Access-Flow.md)
- [`External-Integrations.md`](./External-Integrations.md)

**Source references:** BRD v6.2.2 pp. 1–4 (channels, scope, roles, requirements), pp. 5–8 (marketplace, XACT, data/privacy, NFR), pp. 10–12 (OD-18, OD-20, architecture mapping, change register).
