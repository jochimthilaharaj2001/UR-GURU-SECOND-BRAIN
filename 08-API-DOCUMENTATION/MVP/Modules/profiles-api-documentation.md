# Profiles — MVP API Documentation

**API count:** 21
**Status:** Proposed request/response contracts; requires approval.

## PRO-001 — Get student profile

**GET** `/api/v1/students/me`

- **Feature area:** Student profile
- **Purpose:** Return own grade stream medium and exam-year information.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R0/R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-002 — Update student profile

**PATCH** `/api/v1/students/me`

- **Feature area:** Student profile
- **Purpose:** Edit permitted student profile fields subject to curriculum validation.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R0/R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-003 — Get selected subjects

**GET** `/api/v1/students/me/subjects`

- **Feature area:** Student profile
- **Purpose:** Return student's chosen A/L subject combination.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R0/R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-004 — Set selected subjects

**PUT** `/api/v1/students/me/subjects`

- **Feature area:** Student profile
- **Purpose:** Validate allowed subject combination for stream and syllabus.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R0/R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-007 — Get own teacher profile

**GET** `/api/v1/teachers/me`

- **Feature area:** Teacher profile and availability
- **Purpose:** Read private and public teacher profile fields.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-008 — Update teacher profile

**PATCH** `/api/v1/teachers/me`

- **Feature area:** Teacher profile and availability
- **Purpose:** Update allowed teacher bio and public details.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-009 — List approved teaching subjects

**GET** `/api/v1/teachers/me/subjects`

- **Feature area:** Teacher profile and availability
- **Purpose:** Return authorized subjects and language mediums.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-010 — Request teacher subject

**POST** `/api/v1/teachers/me/subjects`

- **Feature area:** Teacher profile and availability
- **Purpose:** Submit subject and medium authorization evidence for review.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-012 — Get teacher verification progress

**GET** `/api/v1/teachers/me/verification`

- **Feature area:** Teacher profile and availability
- **Purpose:** Display own verification status reasons and missing evidence.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-013 — Submit teacher verification

**POST** `/api/v1/teachers/me/verification`

- **Feature area:** Teacher profile and availability
- **Purpose:** Submit identity and teaching qualification evidence for review.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-014 — Initialize verification document upload

**POST** `/api/v1/teachers/me/verification/documents/upload-init`

- **Feature area:** Teacher profile and availability
- **Purpose:** Create private upload authorization for sensitive evidence.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-015 — Complete verification document upload

**POST** `/api/v1/teachers/me/verification/documents/complete`

- **Feature area:** Teacher profile and availability
- **Purpose:** Attach validated uploaded evidence to verification application.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {},
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-017 — Search verified teachers

**GET** `/api/v1/teachers`

- **Feature area:** Teacher discovery
- **Purpose:** Search only active approved teachers by subject medium fees or availability.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-018 — Get public teacher profile

**GET** `/api/v1/teachers/{teacherId}`

- **Feature area:** Teacher discovery
- **Purpose:** Return approved public details only without sensitive evidence.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
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

## PRO-020 — Get teacher public classes

**GET** `/api/v1/teachers/{teacherId}/classes`

- **Feature area:** Teacher discovery
- **Purpose:** List published classes belonging to the verified teacher.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
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

## PRO-022 — List verification queue

**GET** `/api/v1/admin/teachers/verifications`

- **Feature area:** Teacher verification administration
- **Purpose:** Filter pending and previously reviewed teacher applications.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
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

## PRO-023 — View verification evidence

**GET** `/api/v1/admin/teachers/{teacherId}/verification`

- **Feature area:** Teacher verification administration
- **Purpose:** Read protected documents for authorized reviewers.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
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

## PRO-024 — Approve teacher

**POST** `/api/v1/admin/teachers/{teacherId}/verification/approve`

- **Feature area:** Teacher verification administration
- **Purpose:** Record decision author time and reason; enable approved publications.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
  },
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-025 — Request additional evidence

**POST** `/api/v1/admin/teachers/{teacherId}/verification/request-info`

- **Feature area:** Teacher verification administration
- **Purpose:** Request specific verification corrections from teacher.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
  },
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-026 — Reject verification

**POST** `/api/v1/admin/teachers/{teacherId}/verification/reject`

- **Feature area:** Teacher verification administration
- **Purpose:** Reject application with auditable reason and notice.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
  },
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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

## PRO-027 — Suspend approved teacher

**POST** `/api/v1/admin/teachers/{teacherId}/suspend`

- **Feature area:** Teacher verification administration
- **Purpose:** Block new publications and initiate continuity handling.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-02, BR-03, BR-21, BR-22
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "teacherId": "string (validate ID, ownership and existence)"
  },
  "body": {
    "_contractStatus": "TBD: define endpoint-specific DTO and validation with feature owner"
  }
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
