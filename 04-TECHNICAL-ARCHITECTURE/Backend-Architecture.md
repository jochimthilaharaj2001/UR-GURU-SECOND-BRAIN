# ASP.NET Core Backend Architecture — Modular Monolith Proposal

**Status:** PROPOSED / **OD-20 pending**. **Do not implement an entire source-code solution from this design until stack, DB schema and API contracts are approved.**  
**Source:** BRD v6.2.2 BR-01–BR-24 and Appendix A; System Architecture §03.

## 1. Deployment and logical layout

```text
Student/Teacher Responsive Web        Separate Admin Web
               \                     /
                HTTPS/JSON API calls
                       |
         [one ASP.NET Core API host]
                 API / Middleware
                       |
         Application / Module contracts
                       |
 R0: Identity, Catalogue, Consent, Notifications
 R1: Teacher, Demo, Class, Finance, Resources
 R2: XACT Content, Exams, Papers, Explanations
                       |
      Module-owned domain + persistence adapters
                       |
         [one relational database: TBD]
                       |
      Object media + external provider adapters
```

Single deployment **does not mean** one giant service class. No module may bypass another module's application layer by writing its owned tables directly.

## 2. Layer and dependency rules

| Layer | Owns | Must NOT own |
|---|---|---|
| Host/API | Authentication middleware, route wiring, input DTOs, auth/ownership enforcement, exception mapping, API versioning | Business pricing/score policy inline in controllers |
| Application per module | Use cases, authorization via policies, orchestration, consistency contracts, transactions, domain event dispatch | Framework-specific HTTP response types or vendor SDKs |
| Domain per module | Entities/value objects, invariants, state transitions, domain events | Direct SQL, external network, secrets |
| Infrastructure per module | Persistence mapping, approved EF Core provider, storage adapters, third-party clients | Changing cross-module business rules |
| Shared building blocks | Minimal result types, clock abstractions, IDs and safe telemetry utilities | Catch-all shared business services and cross-module entities |

A vertical use case follows: `Endpoint → DTO validation → Authentication & object authorization → Application command → Domain invariant → Transaction / outbox → standard response`.

## 3. R0, R1, R2 module boundaries

| Module (proposed) | BRD | Main responsibility |
|---|---|---|
| Identity & Safeguarding | BR-01/21/22 | Account lifecycle, sessions, role/object policy, consent events, optional identity policy |
| Academic Catalogue | BR-01/23 | Approved streams, subjects, medium, syllabus, `StudentSubject` eligibility |
| Teachers & Discovery | BR-02/03 | Verification, authorized public teacher/class profiles |
| Demo Media | BR-04 | Teacher-submitted **optional free** class preview, moderation, media state |
| Classes & Enrollment | BR-05 | Batches, schedules, seat constraints, authorized joins, attendance |
| Commerce & Finance | BR-06 | Orders, attempts, verified gateway processing, entitlement, refunds, append-only ledger |
| Learning Resources | BR-07 | Protected class-linked, versioned files |
| XACT Question Governance | BR-18/20/23 | Rights, concepts, translations, answer-key versions, academic review |
| XACT Exam Engine | BR-11/18 | Generate immutable attempt snapshots; autosave, deadline, score and review |
| XACT Teacher Assessments | BR-19 | Versioned teacher papers, scoped recipients and outcomes |
| Notifications/Audit/Support | BR-13/14/21/24 | Outbox, audit, operational notifications and safeguarding cases |

Prefer separate source folders or projects per module; protect boundaries via tests. Module names are design choices, not approved domain vocabulary.

## 4. Six crucial use-case specifications

### 4.1 Student subject selection (`BR-01`, `AC-01`, `AC-32`)

- Validate authenticated student, Grade 12/13, current Bio/Maths catalogue availability and eligible combinations.
- Persist `StudentSubject` with student/subject/year unique protection; reject duplicates or invalid combinations.
- **Never** create `Enrollment`, `OrderHeader`, `Entitlement` or paid access from this selection.
- Curriculum-year/timezone and history rules: **verify against approved ERD**, no assumption of hard deletion.

### 4.2 Optional free class DemoVideo (`BR-04`, `AC-07/31/33`)

- Teacher submits an approved class-linked media reference and rights metadata → processing → authorized independent review → publish or reject.
- Expose only approved, published, active public previews. Source files and moderation notes remain private.
- Demo playback creates **no** live trial seat, booking, enrollment, order, payment or entitlement.
- A student can skip the demo and proceed directly to class selection/checkout; failed demo must never block that action.
- Whether anonymous viewers may watch and viewer-analytics consent is **PENDING OD-02/15**.

### 4.3 Paid enrollment and payment (`BR-05/06`, `AC-08/12–15`)

- Proposed stages: `Validate batch → build order → reserve/hold seat under approved concurrency rule → gateway attempt → verify webhook/server status → grant enrollment/entitlement → ledger and notification`.
- The **exact** seat hold/expiration/confirmation/refund policy is not approved (OD-04/05/20): do not hardcode this sequence as a finalized state machine.
- Gateway callback is authenticated; duplicates are idempotent; redirect/success query param does **not** grant access.
- Financial balances must be posted via auditable correcting ledger entries, not direct silent edits.

### 4.4 Live class & resources (`BR-05/07`)

- Verify student's enrollment/entitlement, session membership and allowed join window **on every issuance** of short-lived provider credentials.
- Materials require backend authorization and short-lived signed URLs. Revocation/expiry should invalidate future link issue.
- Provider outage/rescheduling has an explicit state and notification/finance support path; recording is not implicitly allowed.

### 4.5 XACT (`BR-11/18`, `AC-16–22/25`)

- Query only active, rights-approved source content with approved independent medium translation and answer-key version.
- Generate **server-owned immutable** question/option order, answer-key reference, rules version, start/deadline and scoring snapshot.
- Autosave using idempotent sequence/version policy; enforce deadline on backend; server calculates deterministic result against original snapshot.
- No “silent fallback” to a different language; wrong-medium content returns a clear unavailable state.
- Revisions/regrades must create audited history; do not rewrite prior answers.

### 4.6 Teacher paper assignments (`BR-19`, `AC-23/24`)

- Teacher sees only authorized subject/approved items; can draft/preview/version a paper.
- Assignment references **immutable published paper version**, each recipient has separate authorization and attempt lifecycle.
- Reuse creates a new assignment; do not mutate old student results.

## 5. Endpoint/API patterns (proposed, not contracts)

- Use URI versioning (`/api/v1/...` is **illustrative**) and DTO request/response version discipline.
- Authentication and object authorization must be enforced server-side per endpoint/use case.
- Validation failure, forbidden resource, not-found resource, concurrency conflict and idempotent duplicate need differentiated error states.
- Correlation ID + request tracing across external callbacks; do not log passwords, tokens, raw minor identity data or payment secrets.
- API endpoint registry and exact request/response schemas belong to [`../08-API-DOCUMENTATION/`](../08-API-DOCUMENTATION/), **not** invented here.

## 6. Module-owned data and transactions

Use ORM and persistence abstractions only after DB approval. One database with module-owned tables/schemas is a proposal; EF Core DbContexts per module **or** a strictly modularized context can work if access boundaries are testable. See [`Database-Access-and-Migrations.md`](./Database-Access-and-Migrations.md).

- For single-DB aggregate changes, use transactions and concurrency controls.
- For external payment/media/messaging calls, use safe state transitions + outbox/inbox/idempotency, **not** distributed ACID assumptions.
- Scheduled background work may run in same host initially; any separate worker requires shared outbox ownership and deployment controls.

## 7. Coding and review guards

- Controllers thin; no business rules in UI or provider webhook HTTP handler.
- Domain invariant tests for subject selection, demo optionality, seat capacity, ledger, question version and teacher assignment.
- Architecture tests enforce forbidden cross-module persistence access.
- No production migration/route/provider changes until formal approvals are documented.

**Cross-reference:** [`Module-Contracts.md`](./Module-Contracts.md), [`Security-Architecture.md`](./Security-Architecture.md), [`Reliability-Observability-and-Testing.md`](./Reliability-Observability-and-Testing.md).
