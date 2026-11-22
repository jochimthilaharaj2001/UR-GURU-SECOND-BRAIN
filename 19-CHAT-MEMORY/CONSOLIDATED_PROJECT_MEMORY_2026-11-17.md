# UR GURU — Consolidated Project Memory

**Prepared 17 November 2026** | **Project handoff memory, not an approved replacement BRD**

## 1. Product identity and mission

UR GURU is an education marketplace for Sri Lankan **G.C.E. Advanced Level (A/L) Grade 12 and Grade 13 students**. It connects learners with administrator-verified tutors/teachers for live tuition and adds **Exam Munnodi**, a structured MCQ/mock-exam service for past-paper practice. `[VERIFIED:BRD]`

Student curriculum scope: A/L streams **Science, Commerce, Arts, Technology**. O/L and Grades 10/11 are explicitly excluded. `[VERIFIED:BRD]` Current direction is a **responsive web application**, with Student/Teacher web UI and a separate Admin web UI backed by the same API/database. `[HISTORY]`

## 2. What must exist in the student learning journey

Student signup/login; grade 12/13, A/L stream/subject/medium profile; verified teacher search/discovery; profile comparison; free trial eligibility and booking; class discovery and schedule; enrollment/booking, server-verified payment, authorized live-class join; resources; class notifications, attendance and cancellation/rescheduling/refund status; Exam Munnodi mocks; results/progress; paper assignments received from teachers; question written/video explanation access where permitted. `[VERIFIED:BRD]` for core flows; attendance and extra operational detail `[HISTORY]`.

Students **select subjects** and **attend classes**; do not connect Admin as enroller/attendee. `[HISTORY]`

## 3. Teacher experience

Teacher registration/application, qualification and identity submission, verification by Admin, approved subject/medium expertise, profile/public listing; class creation and management, scheduling and capacity, trial handling, live teaching, enrolled student view, resources upload; earnings, commission, payout statements; Exam Munnodi question selection from **approved predefined bank**, paper draft/preview/publish/assign to multiple students, view authorized results; explanation-video creation/upload with academic review and approval. `[VERIFIED:BRD]` + operational elaboration `[HISTORY]`.

Conversation decisions say **teacher creates/teaches subject offerings**, while **student selects subjects**. The BRD also requires a controlled syllabus/subject catalog; implementation must distinguish an admin-maintained `Subject` master record from teacher-submitted offerings until sign-off. `[HISTORY]`/`[OPEN]`

## 4. Admin and guardian

Admin verifies educators, reviews/question-bank content and video explanations, controls platform catalog/syllabus, moderates users and reports, configures exam rules, reviews disputes/refunds/payout records and logs privileged actions. `[VERIFIED:BRD]`

Parent/guardian is **not** a separate full portal in the current scope; latest history restricts parent details to **name and phone** (and legally necessary consent/assisted-payment touchpoints). `[HISTORY]` Full guardian dashboard is a future feature in PDF. `[VERIFIED:BRD]`

## 5. Exam Munnodi core mechanics

- Input question bank targets **five years** of A/L past-paper MCQs; year/subject/rights must be inventoried, no automatic assumption of full coverage.
- Question metadata: stable identifier, stream, subject, syllabus version, topic/subtopic, source year/paper, options, approved answer key, difficulty, marks, review status, rights status and versions.
- Student selects subject, **selected topics or all topics**, difficulty (`Easy/Medium/Hard` or admin-configured mix), receives an eligible mock and answers under optional configured exam timer/attempt rules.
- Backend generates and persists eligible questions; no duplicates in an attempt; browser cannot provide scores or correct answers before approved review state.
- Final submit: server-side marking; correct/incorrect/unanswered and topic-wise results; show written explanation and, if approved/available, teacher-recorded explanation video.
- Teachers create papers by choosing from approved predefined questions, save drafts and issue the same paper to several authorized students; each assignment/attempt/result is independent. Reused papers do not overwrite history.
- Reviewer approval, content licensing, correction/regrade/audit and immutable attempt snapshots are essential.

`[VERIFIED:BRD]` Full details: `17-EXAM-MUNNODI/EXAM_MUNNODI_FULL_SPEC.md`.

## 6. Architecture snapshot

**Current product direction:** responsive web only. **Backend:** C# ASP.NET Core Web API selected/preferred in discussions. **Web UI:** Angular/TypeScript appears in old BRD and architecture diagram; latest UI prototype artifacts are HTML. The final frontend framework should be confirmed against the actual repo. **Relational database:** SQL Server proposed in BRD and shown in architecture image. Cloud storage: Azure Blob or AWS S3 candidates; live class: LiveKit/Agora candidates; gateway: Sri Lankan-compatible gateway TBD (PayHere recommended *only* on diagram); notifications: email/SMS service TBD; deploy Docker + CI/CD proposed. `[HISTORY]` `[VERIFIED:BRD]` `[VERIFIED:IMAGE]` `[OPEN]`

Architecture modules: Auth & Access, Students/Teachers, Academic Catalog, Course/Class/Trial, Enrollment/Attendance, Live Sessions, Payments/Refund/Payout, Exam Munnodi, Paper Assignments, Notifications, Reports/Analytics, Admin/Audit.

## 7. Payment and revenue memory

Confirmed concept: student pays to attend class; teacher receives contracted share and UR GURU receives *approved* commission. **Student full class fee = GMV, not platform revenue**. Commission proposed **15%** in older examples but unapproved. `[VERIFIED:BRD]`

Other ideas from BRD: Exam Munnodi freemium premium access, one-time mock packs, teacher-video access, optional teacher Pro tools, future institute licensing, carefully approved sponsorship and ethical advertising. Teacher-created video fees are normally **expense or sharing arrangement**, not direct revenue. Terms, gateway, refund logic, exact prices, subscription packaging remain `[OPEN]`. The BYJU'S document is **only background revenue-model research**, and its prices/examples must not become UR GURU pricing.

## 8. Project documentation and ERD history

The team repeatedly requested a single, readable overall ERD **including attributes, PK/FK, relationships and cardinalities**, not disconnected student-only diagrams or messy crossing arrows. Important user corrections: students select subjects; teachers create subject/class offerings; teachers conduct classes; students enroll in/attend classes; parent is not a full user account; Admin is not a student; `Course` vs `Class` naming should be reconciled rather than duplicated. A previous ERD-design concern file was mentioned but is **not** included here. `[HISTORY]`

User's preferred knowledge tree has 15 folders: Project Overview, BRD Requirements, System Architecture, Technical Architecture, User Journeys, UI/UX, Database Design, APIs, Business Rules, Development Guidelines, Sprint/Tasks, Testing, Decision Log, Deployment, Issues/Changelog. This pack uses those and extra Finance, Exam Munnodi, Sources, Chat Memory folders. `[HISTORY]`

## 9. UI and FAQ memory

Student and Teacher prototype discussed as a shared responsive web application; Admin is a distinct web portal, backed by the same backend. Previous files include `MergedScreens2.html`, `UR_GURU_Student_Teacher_prototype.html`, `UR_GURU_Admin_Portal_Prototype.html`, Exam Munnodi HTML/screens and Teacher/Student FAQs, but these actual binaries were **not available for inspection in this session**. Do not assert screen-by-screen compliance until imported and compared. `[HISTORY]`

FAQ updated to A/L-only scope and web application, not mobile app. Student and teacher Google Forms were planned to understand class-technology problems (Zoom, Teams etc.); questionnaire contents are historical discussions, not final approved research results. `[HISTORY]`

## 10. Timelines and team

History states **3–5 developers**, currently primarily **UI designs ready**, with a November 30 development-completion question. No signed release date was available in the inspected BRD; its OD-16 explicitly requires staffing/budget/date approval. Treat **30 November 2026 as an aspiration, not a proven deliverable deadline**. A working slice is more realistic than promising all marketplace, payment, Exam Munnodi and content moderation flows by that date. `[HISTORY]` `[VERIFIED:BRD]`

## 11. Status: agreed vs unresolved

**Stronger alignment:** A/L-only Grade 12/13; four streams; core Student/Teacher/Admin roles; responsive web-only latest direction; one backend; C# ASP.NET Core direction; verified educators; class/payment marketplace; Exam Munnodi fundamentals; parent name/phone limited; server-side controls.

**Unresolved or contradictory:** actual signed-off BRD V6, Flutter/mobile legacy references, final Angular framework, `Course`/`Class` naming, teacher-created subject versus approved catalog, exact ERD/API artefact, SQL Server and cloud/provider procurement, PayHere, teacher commission, refunds/payout schedule, question licensing, exam defaults, A/L subject catalog/medium list, subscription pricing, project launch date, content production agreement, AI-phase scope.

## 12. How an engineer should apply this memory

1. Use the source registry and the tags to distinguish actual facts from generated suggestions.
2. Always map a change to BR IDs (PDF), a history decision (if relevant), and a test case.
3. Do not turn older draft artefacts or benchmark business models into production requirements.
4. For feature disagreements, record an ADR/decision request and implement a flexible interface only where safe.
5. Before claiming full project completion, require feature-by-feature acceptance and evidence from deployed, tested UI/backend, not just screens.

See `13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md` and `15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md`.
