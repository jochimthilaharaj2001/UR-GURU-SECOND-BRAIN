# Internal Module Contracts — Proposal

**Status:** PROPOSED; no externally published API or persisted event schema is approved. 
**Goal:** One modular-monolith host, strongly separated R0/R1/R2 application boundaries.

## 1. Contract rules

- Internal module clients depend on exported **application interfaces**, never another module's persistence or vendor SDK.
- Contracts define caller identity/authorization, input, output, errors, idempotency, audit and state invariants.
- Version internal events when payloads may persist in outbox; consumers tolerate replay and reordering or reject unsupported versions explicitly.
- Avoid synchronous circular dependencies; extract shared primitives or use a durable event/read model instead.

## 2. Cross-module read/command contract candidates

| Producer / owner | Consumer | Purpose | Constraints |
|---|---|---|---|
| Identity | All | Current actor, roles, object-policy decision | Authenticated and least-privilege |
| Academic Catalogue | Teachers / XACT / Classes | Active curriculum/medium/syllabus eligibility | Bio/Maths launch, per-medium approval |
| Teachers | Demo / Classes / XACT Assignments | Teacher approval and subject authorization | Suspended teacher must not create new restricted actions |
| DemoMedia | Teacher Discovery | Public approved class demo reference | Free and optional, no checkout dependency |
| Classes | Commerce | Eligible batch/seat/enrollment status | Approved capacity/payment policy |
| Commerce | Classes/Resources/XACT monetization | Verified access entitlement | No browser redirect trust |
| XACT Questions | Exam Engine / Teacher Papers | Immutable eligible content-version snapshot | Rights/keys/medium approval; no duplicate canonical question |
| XACT Exam Engine | XACT Reporting / Teacher Papers | Student-scoped attempt/result | Server-side score and deadlines |
| Modules | Operations Outbox | Notification/audit/safety event | Non-sensitive payload, dedupable and retryable |

## 3. Domain events: illustrative names only

| Candidate event | Emitted when | Consumers |
|---|---|---|
| `TeacherApproved` | Authorized verified decision committed | Discovery, Notifications |
| `DemoPublished` / `DemoWithdrawn` | Independently reviewed preview status changes | Discovery cache, media delivery, Notifications |
| `StudentSubjectSelected` | Valid unique selected-subject row committed | Academic profile UI, analytics with consent |
| `PaymentVerified` | Server-confirmed gateway success and accepted processing | Entitlement/Enrollment flows per approved transaction design |
| `EnrollmentActivated` | Authorized class access state committed | Classes, Notifications |
| `XactAttemptSubmitted` | One final immutable server submission exists | Result service, notifications if configured |
| `TeacherPaperAssigned` | Individual recipients committed | Notifications, student assignment list |

Names, structures and ordering are **not approved public contracts**. No `TrialBooked` event for current BR-04.

## 4. Contract checklist for every internal use case

`ID | requirement | owner | callable method | request | response | auth | object policy | preconditions | postconditions | idempotency key | transaction boundary | failure states | audit | test IDs | change owner`.

## 5. Example: demo publication invariant

1. `PublishDemo` requires approved reviewer permission and all rights/media/approval preconditions.
2. Must reject self-review if role/ownership policy forbids it (BRD explicitly bars teacher self-approval).
3. Changes published state and adds audit/outbox notification.
4. Discovery reads **approved public projection only**.
5. Any preview failure must leave class discovery and enrollment path available.

**Source:** BRD v6.2.2 §§4–9 and Appendix A; [`../03-SYSTEM-ARCHITECTURE/Module-Interaction.md`](../03-SYSTEM-ARCHITECTURE/Module-Interaction.md).
