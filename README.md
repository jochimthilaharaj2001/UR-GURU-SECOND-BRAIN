# UR GURU — Development Second Brain

**Knowledge-base revision:** 2.1-corrected | **Updated:** 22 November 2026 | **Status:** CORRECTED / REVIEW REQUIRED (not a signed production baseline)

## Authority and scope
**Primary requirements source:** [UR GURU BRD v6.2.2](02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf), controlled review copy dated 19 November 2026; stakeholder sign-off pending. No supporting file supersedes it. [Correction audit](SECOND-BRAIN-CORRECTION-AUDIT-2026-11-22.md) identifies remaining approval gates.

UR GURU is a responsive web platform for Sri Lankan G.C.E. A/L Grades 12–13. **Initial curricular scope: Biological Science (Bio) and Physical Science (Maths) only.** Student/Teacher responsive web and separate Admin web portal share a proposed ASP.NET Core modular-monolith backend. XACT is the current assessment brand (Exam Munnodi is historical). Native apps, Commerce/Arts/Technology, O/L and Grades 10/11 are excluded from initial release.

## Functional release lanes
- **R0 Foundation:** identity, approved catalogue, student-subject selection, access control, consent/safeguarding, audit, notifications, migrations.
- **R1 Marketplace:** teacher verification/discovery, *optional free prerecorded approved demo video*, classes/batches, enrollment, authorized live sessions, resources, payment/refund/earnings/payout controls.
- **R2 XACT:** five-year approved bank, practice/mocks, scoring, assignments, moderated explanation videos.
- **Later/conditional:** transcription, teacher-reviewed AI notes, AI assistance, ExamPilot, DataSmart, institutions. Separate approval required.

**No scheduled live trial booking:** demos are optional, free, prerecorded and never gate checkout or reserve a seat. StudentSubject is distinct from paid Enrollment.

## Inventory and document use
19 existing numbered sections retained. API inventory: **292 MVP + 177 Post-MVP = 469 individually listed**. A further **52 deferred/conditional** is an unverified planning count without approved endpoint-level source; do not treat 521 as a validated implementation contract. MVP DTO examples currently contain TBD; see [contract gap register](08-API-DOCUMENTATION/GOVERNANCE/MVP_CONTRACT_GAP_REGISTER.csv). Database inventory is a design candidate, **not** an approved schema or runnable migrations. Read [source precedence](18-SOURCES/SOURCE_REGISTRY.md) and [decision log](13-DECISION-LOG/Business-Decision-Register.csv) before implementing.

## Folder navigation
01 Project Overview · 02 BRD & Requirements · 03 System Architecture · 04 Technical Architecture · 05 User Journeys · 06 UI/UX · 07 Database · 08 API Documentation · 09 Business Rules · 10 Development Guidelines · 11 Sprint & Tasks · 12 Testing · 13 Decision Log · 14 Deployment · 15 Issues & Changelog · 16 Finance · 17 XACT (legacy folder name retained) · 18 Sources · 19 Chat Memory.

## Rules for contributors
1. Never infer approval from an old diagram, prototype, historical specification, or discussion.
2. Implement only endpoint contracts reviewed for DTO fields, status codes, ownership, validation and test coverage.
3. Record architecture/provider choices as *team-selected / verification pending* until signed decision evidence exists.
4. Use the populated backlog/UAT registers as **proposed work**, not completed tasks or passing tests.
5. Record changes, decisions, PRs and evidence links; preserve historical documents with explicit archived labels.
