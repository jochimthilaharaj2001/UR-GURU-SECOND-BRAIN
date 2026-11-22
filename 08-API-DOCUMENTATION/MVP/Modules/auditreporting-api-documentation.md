# AuditReporting — MVP API Documentation

**API count:** 14
**Status:** Proposed request/response contracts; requires approval.

## AUD-001 — Search audit events

**GET** `/api/v1/admin/audit/events`

- **Feature area:** Audit and operational dashboards
- **Purpose:** Filter protected privileged changes by actor action subject and time.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-002 — Inspect audit event

**GET** `/api/v1/admin/audit/events/{eventId}`

- **Feature area:** Audit and operational dashboards
- **Purpose:** Read immutable original and correlating operation identifiers.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "eventId": "string (validate ID, ownership and existence)"
  },
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-004 — Get operations dashboard

**GET** `/api/v1/admin/operations/overview`

- **Feature area:** Audit and operational dashboards
- **Purpose:** Summarize teacher trial class payment and safety exceptions.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-005 — List operational exceptions

**GET** `/api/v1/admin/operations/exceptions`

- **Feature area:** Audit and operational dashboards
- **Purpose:** Find stuck callbacks attendance issues or failed jobs.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-006 — Inspect operational exception

**GET** `/api/v1/admin/operations/exceptions/{exceptionId}`

- **Feature area:** Audit and operational dashboards
- **Purpose:** Read correlated system status and retry history.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "exceptionId": "string (validate ID, ownership and existence)"
  },
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-013 — Liveness endpoint

**GET** `/api/v1/health/live`

- **Feature area:** Service health and internal metrics
- **Purpose:** Return process-alive status for orchestrator probes.
- **Authorized role (tracker):** Infrastructure
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-014 — Readiness endpoint

**GET** `/api/v1/health/ready`

- **Feature area:** Service health and internal metrics
- **Purpose:** Check readiness of required persistence and critical dependencies.
- **Authorized role (tracker):** Infrastructure
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-015 — Get system integration health

**GET** `/api/v1/admin/system/health`

- **Feature area:** Service health and internal metrics
- **Purpose:** Read sanitized service and provider health for administrators.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-024 — Get marketplace KPI report

**GET** `/api/v1/admin/reports/marketplace`

- **Feature area:** Academic and finance operational reports
- **Purpose:** Show teacher class trial enrollment and conversion metrics.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-025 — Get financial reconciliation report

**GET** `/api/v1/admin/reports/payments`

- **Feature area:** Academic and finance operational reports
- **Purpose:** Summarize verified GMV refunds revenue and provider exceptions.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-026 — Get payout control report

**GET** `/api/v1/admin/reports/payouts`

- **Feature area:** Academic and finance operational reports
- **Purpose:** Summarize outstanding verified and blocked teacher settlements.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-028 — Get XACT usage report

**GET** `/api/v1/admin/reports/xact/usage`

- **Feature area:** XACT operations metrics
- **Purpose:** Report practice completion and usage by subject medium and period.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-029 — Get XACT coverage report

**GET** `/api/v1/admin/reports/xact/content-coverage`

- **Feature area:** XACT operations metrics
- **Purpose:** Show question pool and review coverage by syllabus topic medium.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---

## AUD-030 — Get exam integrity exceptions

**GET** `/api/v1/admin/reports/xact/attempt-errors`

- **Feature area:** XACT operations metrics
- **Purpose:** Find autosave expiry scoring and double-submit anomalies.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-14, BR-24
- **Release / phase:** R0-R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "queryParameters": "TBD: pagination, sorting and filters where relevant"
}
```

**Success response — DRAFT, fields not yet approved**
```json
{
  "data": "TBD: endpoint-specific response DTO",
  "correlationId": "string"
}
```

**Errors & validations to define:** request validation; authentication/authorization; not-found; domain conflict; retry and idempotency where applicable.

**Acceptance checklist:** role and ownership test; positive/negative validation; BRD-linked UAT; UI loading/empty/error/success; audit and security review.

**Open decisions:** exact DTO fields/types, required/optional rules, response status, error catalog, DB mapping, API example, approval owner.

---
