# Technology Stack — Decision Register

**Status:** **PROPOSED**; **BRD v6.2.2 OD-20** requires final technology and environment approval.  
**Scope:** Responsive web only, Grade 12/13 Bio & Maths initial release, single backend modular-monolith proposal.

## 1. Separate what is required from what is proposed

| Layer | Required by current BRD / prior architecture | Engineering candidate | Final status / gate |
|---|---|---|---|
| Student + Teacher client | Responsive browser experience | TypeScript web SPA (Angular is an older baseline, **not confirmed by v6.2.2**) | **PENDING OD-20** |
| Admin client | Separate responsive Admin Web portal | Separate TypeScript web deployment/app; shared design primitives only | **PENDING OD-20** |
| Backend | Server-authoritative workflows, protected APIs | **C# ASP.NET Core Web API, modular monolith, one backend deployable** | **PROPOSED — OD-20** |
| Internal architecture | Isolated domain boundaries for R0/R1/R2 | Feature modules + Application/Domain/Infrastructure slices | **PROPOSED — OD-20** |
| Relational DB | Transactional, auditable data + versioned XACT | **SQL Server OR PostgreSQL**; decide one before migrations | **PENDING OD-20** |
| ORM + migrations | Controlled, tested schema changes | Entity Framework Core with selected database provider | **PROPOSED — OD-20** |
| Media / documents | Private object storage; controlled public demo preview | Object storage + processing pipeline + CDN as appropriate | **PENDING OD-02/06/20** |
| Live classrooms | Authorized join credentials and availability controls | **LiveKit Build — team preference recorded**, provider capability/security/cost and OD-06 approval pending | **PENDING OD-06** |
| Payment gateway | Signed/verified callbacks, reconciliation and refunds | **PayHere Lite — team preference recorded**, settlement/refund/webhook capability and OD-05 approval pending | **PENDING OD-03/04/05** |
| Messaging | Retryable event notification + outbox | Provider-neutral email/SMS/in-app adapters | **PENDING OD-16/20** |
| Background processing | Durable media/notification tasks | In-host `BackgroundService` initially or separate worker when required | **PROPOSED — OD-20** |
| Hosting / CI/CD | Controlled environments and deployments | Any approved cloud/container + CI pipeline | **PENDING OD-16/20** |
| Observability | Auditable and monitored critical actions | Structured logs, metrics, traces, alerts | **PROPOSED — OD-16** |
| AI / speech-to-text | Later/conditional scope only | **Not a launch dependency** | Separate future decision |

**Do not write specific versions as already approved.** Record runtime version, provider driver, framework version, DB collation, infrastructure SKUs and browser matrix only after selection and compatibility tests.

## 2. Why modular monolith first? (engineering rationale)

- The R0 foundation, R1 marketplace, and R2 XACT workflows share authorization, academic catalogue, notification and audit concerns.
- One backend deployment reduces initial operations overhead while **module ownership** preserves the ability to isolate logic.
- Critical enrollment/payment transactions benefit from one relational transaction boundary, but external gateways are not transactional participants.
- A monolith may scale to multiple identical host replicas; a worker can be a separate *process* without becoming a domain microservice.
- Future extraction is possible **only if** interfaces and data ownership remain separate. It is not a guaranteed zero-cost migration.

## 3. Explicit non-decisions

- No approved PostgreSQL-vs-SQL-Server engine; do not turn older SQL text into production migrations.
- No approved Angular/React web selection from v6.2.2 alone; existing prototype HTML is not framework approval.
- LiveKit Build and PayHere Lite were selected in project discussion, but no signed provider contract, verified integration capability, pricing or release approval is evidenced here.
- No approved public demo tracking/login gate; user may skip demo.
- No approval of NIC government identity checks, broad guardian portal, recording, biometric verification, or XACT monetization.
- No approved production NFR/SLA numbers; p95/API, uptime and recovery values in BRD §11 are **candidates**.

## 4. Conditions before locking stack

1. Sign off **OD-20** with exact frameworks, LTS/runtime versions, DB engine/driver, migrations and architecture diagram.
2. Resolve **OD-18** (R1 vs XACT pilot release order).
3. Evaluate legal/finance/integration constraints **OD-02/05/06/07/15/19**.
4. Benchmark Tamil/Sinhala scientific text, mobile-browser experience, realistic Sri Lankan network conditions.
5. Update [`Technical-Decisions-and-Gates.md`](./Technical-Decisions-and-Gates.md), repository build instructions and support matrix.

**Sources:** BRD v6.2.2 pp. 1–4 (scope/R0–R2), pp. 5–8 (functional/consent/XACT), pp. 8–11 (candidate NFR, decisions). See [`../03-SYSTEM-ARCHITECTURE/Modular-Monolith-Architecture.md`](../03-SYSTEM-ARCHITECTURE/Modular-Monolith-Architecture.md).
