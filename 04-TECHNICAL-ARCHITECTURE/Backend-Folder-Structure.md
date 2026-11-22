# Proposed Backend Folder Structure — C# ASP.NET Core Modular Monolith

**Status:** **Illustrative source architecture; OD-20 approval pending.** Paths are recommendations, not existing code. Module and project split can be adjusted after repository review.

## Suggested repository layout

```text
UR-GURU/                               # proposed application repository (not Second Brain)
├── src/
│   ├── UrGuru.Api/                    # single ASP.NET Core entry point/deployable
│   │   ├── Program.cs
│   │   ├── Composition/
│   │   │   └── ModuleRegistration.cs
│   │   ├── Middleware/
│   │   ├── Auth/
│   │   └── Endpoints/               # maps per-module HTTP endpoint contracts
│   ├── BuildingBlocks/
│   │   ├── Domain/
│   │   ├── Application/
│   │   ├── Infrastructure/
│   │   └── Contracts/               # only cross-cutting primitives
│   ├── Modules/
│   │   ├── Identity/
│   │   ├── AcademicCatalogue/
│   │   ├── Teachers/
│   │   ├── DemoMedia/
│   │   ├── Classes/
│   │   ├── Commerce/
│   │   ├── LearningResources/
│   │   ├── XactQuestions/
│   │   ├── XactExams/
│   │   ├── XactAssignments/
│   │   └── Operations/
│   └── UrGuru.Workers/              # OPTIONAL same-system deployment component;
│                                     # not required initially and not a microservice
├── tests/
│   ├── Unit/
│   ├── Integration/
│   ├── Architecture/
│   ├── Contract/
│   └── EndToEnd/
├── deploy/                            # only after environment decision
├── docs/                              # links to approved Second Brain sources
├── .github/workflows/                 # or other approved CI provider
├── Directory.Build.props              # proposed code-analysis policy
├── .editorconfig
└── UrGuru.sln
```

## Inside one feature module (example: `DemoMedia`)

```text
Modules/DemoMedia/
├── Domain/
│   ├── DemoVideo.cs                   # approved lifecycle invariants
│   ├── Events/
│   └── ValueObjects/
├── Application/
│   ├── Commands/
│   │   ├── SubmitDemo/
│   │   ├── ReviewDemo/
│   │   └── PublishDemo/
│   ├── Queries/
│   │   └── GetPublishedDemos/
│   ├── Policies/
│   └── Ports/                         # interfaces for storage/moderation
├── Infrastructure/
│   ├── Persistence/
│   │   ├── Mappings/
│   │   └── Migrations/                # provider-specific after OD-20
│   ├── Media/
│   └── Notifications/
├── Contracts/
│   ├── Requests/
│   ├── Responses/
│   └── Events/
└── ModuleRegistration.cs
```

## Structural rules

1. `UrGuru.Api` composes modules; it must not contain business decisions such as refund percentage or grading logic.
2. `Modules/X/*` exposes its **Contracts/Application** interface; a different module cannot reference `X/Infrastructure/Persistence` or directly run SQL on X-owned tables.
3. `BuildingBlocks` contains **generic** primitives, not a monolithic `CommonServices` collection of all features.
4. Module IDs/use cases should link to a BRD ID, a test, and the API contract when it exists.
5. Provider SDK implementations belong in infrastructure adapters behind interfaces; secret values belong in an approved secret manager, **not** source files.
6. Distinguish R0/R1/R2 implementation/release flags but avoid shipping half-implemented privileged operations by flipping a UI flag alone.
7. Event handlers are idempotent, auditable and deployed with the same application version where necessary.
8. The optional worker project can be introduced if media/notifications workload requires process isolation; it still shares the same monolith's domain contracts and deployment governance.

## Database/feature boundaries to retain

- Identity + Catalogue: `StudentSubject` is a selection association (BR-01), **not** an enrollment.
- DemoMedia: `DemoVideo` is optional, free, independently reviewed, class-linked, and **not** a `TrialBooking`.
- Commerce: one authoritative entitlement path after server-verified payment, with auditable ledger adjustments.
- XACT: `QuestionConcept`/`QuestionTranslation`/`AnswerKeyVersion` and attempt snapshots support historical scoring.
- Teacher papers: versioned `TeacherPaperVersion` and `AssignmentRecipient` relationships.

## Avoid premature complexity

No default microservices, Kafka, Kubernetes, one database per module, distributed sagas, or separate CI for every module are implied. Choose these only for a demonstrated scaling/reliability need and record a technical decision.

**References:** BRD v6.2.2 Appendix A/C; [`Backend-Architecture.md`](./Backend-Architecture.md); [`Database-Access-and-Migrations.md`](./Database-Access-and-Migrations.md).
