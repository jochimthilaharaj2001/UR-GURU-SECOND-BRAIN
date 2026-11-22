# 09 — BUSINESS RULES

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Purpose
Business rule knowledge for UR GURU **V6.2.2 review baseline** — NOT a formally signed-off policy register. Use to prepare coding/test specifications, identify gaps, and request decisions. These rules should **not** be unconditionally treated as approved implementation requirements.

## Critical product alignment
- Responsive Student/Teacher web; separate Admin web portal.
- Initial launch curriculum **Biological Science / Physical Science (Maths)** only, Grades 12 and 13. Other streams future/uncommitted.
- **XACT** replaces historical **Exam Munnodi**.
- BR-04 = optional **free prerecorded demo**; watching or skipping has no booking/payment requirement. **No live trial-booking journey.**
- `StudentSubject` selection **≠** `Enrollment` or paid `Entitlement`.
- **Modular Monolith** is a proposed architecture; database and vendor decisions remain open under OD-20.

## File index
| Document | Content |
|---|---|
| [Business-Rules-Register.md](Business-Rules-Register.md) | Complete rule catalogue with BRD references and review states |
| [Business-Rules-Catalog.csv](Business-Rules-Catalog.csv) | Searchable table, proposed owners and pending policy gates |
| [Business-Rule-UAT-Mapping.csv](Business-Rule-UAT-Mapping.csv) | Rule-to-BRD requirement/AC candidate links; implementation tests pending |
| [Student-and-Teacher-Rules.md](Student-and-Teacher-Rules.md) | Registration, stream/subjects, verification and discovery |
| [Class-Demo-and-Enrollment-Rules.md](Class-Demo-and-Enrollment-Rules.md) | Optional demo and paid class enrollment (not trial booking) |
| [Payments-Refunds-Payouts.md](Payments-Refunds-Payouts.md) | GMV, payment verification, refunds, earnings, ledger |
| [XACT-Assessment-and-Paper-Rules.md](XACT-Assessment-and-Paper-Rules.md) | Versioned exam bank, mocks, attempts, teacher paper rules |
| [Privacy-Consent-and-Content-Rules.md](Privacy-Consent-and-Content-Rules.md) | Safeguarding, guardian consent, content rights and localization |
| [Admin-Notifications-and-Audit-Rules.md](Admin-Notifications-and-Audit-Rules.md) | Notifications, audit and operational exception rules |
| [Business-Decision-Gates.md](Business-Decision-Gates.md) | BRD OD-01 through OD-20 unresolved approvals |
| [Legacy-V2-Rule-Reconciliation.md](Legacy-V2-Rule-Reconciliation.md) | Historic 77 rules and current review disposition |
| [UR_GURU_Business_Rules_V2_0.docx](UR_GURU_Business_Rules_V2_0.docx) | **Unmodified historical source**, not current policy baseline |

## Source of truth
1. The current BRD review candidate is `../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf` (expected at that relative path after you copy the updated Section 02).
2. Earlier `UR_GURU_Business_Rules_V2_0.docx` is **historical evidence**; where it conflicts with v6.2.2, flag conflict and wait for sign-off, do not silently implement older logic.
3. For technical specifics, database design and APIs need separate review. The Section 08 API documentation remains **PENDING**; this pack **does not** complete it.
4. References `BR-01`–`BR-24` = BRD functional requirements; `AC-01`–`AC-33` = BRD acceptance checks; `UG-RULE-###` = this review register; `OD-01`–`OD-20` = pending decisions.

## Engineering handoff
- Read this README → affected domain document → rule IDs → original BRD section → decision gates.
- Include the rule ID and BRD section in new API, UI and test tickets.
- Do not treat **Review baseline** as approval; no numeric provider/SLA/commission/refund/retake parameters are finalized.


## 104-API MVP alignment
BRD v6.2.2 business rules remain authoritative even when the MVP API subset is smaller. Explicitly record which business rules are implemented, deferred or blocked by missing APIs; particularly consent, demo optionality, paid access, gateway callbacks, question approvals and auditability.
