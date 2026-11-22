> **2026-11-22 architecture alignment:** API transport/DTO contracts must remain database-independent. Backend implementation now targets MySQL 8.4 LTS as a planning selection; existing TBD request/response contracts and approval gates are **not** resolved by this change. [Architecture reference](../04-TECHNICAL-ARCHITECTURE/TECHNICAL-ARCHITECTURE-BASELINE-2026-11-22.md).

> **22 Nov 2026 correction notice:** Refer to root README and BRD v6.2.2 for active scope. Earlier counts, approvals and legacy references below are historical until reconciled.

# UR GURU — 08-API-DOCUMENTATION

**Controlled reference:** UR_GURU_Full_Corrected_BRD_v6.2.2.pdf (19 Nov 2026).  
**API inventory:** UR_GURU_MVP_API_LIST_BRD_v6.2.2.xlsx.  
**Status:** Working draft; not a signed-off implementation contract.

## Folder structure

- `MVP/` — 292 MVP endpoint entries in 14 module files; endpoint metadata comes from the supplied workbook. DTO contracts are **not approved** and remain placeholders.
- `POST-MVP/` — 177 current-scope endpoints not selected for MVP, indexed from the workbook. Not an implementation commitment.
- `DEFERRED-CONDITIONAL/` — boundary and review process for 52 deferred/conditional APIs cited in project planning; their endpoint-level list is **not in the supplied MVP workbook**, so no endpoints are fabricated.
- `TEMPLATES/` — standard API specification, request/response, and QA template.
- `GOVERNANCE/` — conventions, ownership, change control, traceability and decision gates.

## Usage

1. Start with `MVP/MVP_API_INDEX.md`, then open the relevant `MVP/Modules/*-api-documentation.md`.
2. Before coding, resolve each `TBD` in request and response DTOs, validate roles, and sign off its contract.
3. Map endpoints to BRD requirement IDs, authorized roles, ERD v1.2 entities and actual UI screens.
4. Keep POST-MVP and deferred work separate from the MVP release.
5. Record every contract change in `GOVERNANCE/CHANGELOG.md`.

## Hard scope boundaries

XACT is the current assessment name. Demo video is a **free, optional prerecorded preview**, not a trial booking; watching it must never gate enrollment. `StudentSubject` selection is not a paid `Enrollment`. Do not implement superseded trial-booking flows. Initial focus: Grades 12–13, Bio/Maths streams. Teacher-reviewed AI notes/transcription are later/conditional, not automatic MVP commitments.
