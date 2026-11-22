# Modular monolith data ownership and access

**Status:** Proposed; corresponds to Section 03 & 04 modular-monolith approach. One backend deployable with business-owned data modules. One relational database is a valid candidate, not a confirmed vendor.

| Module | Owns entities for writing | Allowed external callers |
|---|---|---|
| Identity | Account, profile, verification, guardian contact/consent | Auth/role policy and documented commands |
| Catalogue | Stream/subject/syllabus/topic, StudentSubject, TeacherSubject | Read/query contracts; enrollment may validate eligibility |
| Marketplace | ClassOffering, demo, batch, schedule, session, enrollment, attendance | Approved class/enrollment contracts |
| Media | MediaAsset, reviews, resources and revisions | Signed delivery requests, content moderation contracts |
| Commerce | Order/payment/ledger/earnings/entitlements/payout | Payment verification/entitlement checks; do not directly edit ledger |
| XACT Content | Paper source/rights, concept, translation, key, explanations | Approved eligible-question queries |
| XACT Assessments | Mock generation/attempt/autosave/grading/result | Student-authorized actions and teacher-assignment contract |
| XACT Assignments | Teacher papers, versions, recipients | Authorized teacher and learner workflows |
| Operations | Notification/outbox, audit, safety, support | Audited workflow events |

**Principles**

- No cross-module writes through another module's `DbContext`. Use in-process contracts, domain events and outbox for external effects.
- Cross-module identity references must be validated with server-side access policy. Do not leak student attempt or safety report data through analytics joins.
- A `GuardianContact` is not a user account or dashboard. Guardian consent evidence should have purpose and version, protected from unrelated staff.
- `MediaAsset.StorageKeyRef` should never be returned to browser; access uses policy-checked short-lived delivery link.
- Subject and translation medium cannot bypass academic review by selecting a different client-side language.
- Finance/admin actions require least privilege, reason, timestamp, audit actor and settlement reconciliation.
- Subject catalog and reference table data can be shared via read-only queries and published events, never arbitrary table updates.
- Define row ownership (student own, assigned teacher, admin reviewer) in application policy and integration tests.
