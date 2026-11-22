# LearningResources — MVP API Documentation

**API count:** 13
**Status:** Proposed request/response contracts; requires approval.

## LEA-001 — List accessible resources

**GET** `/api/v1/resources/me`

- **Feature area:** Student resources
- **Purpose:** List approved material across current authorized enrollments.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
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

## LEA-002 — List class resource library

**GET** `/api/v1/classes/{classId}/resources`

- **Feature area:** Student resources
- **Purpose:** List current published resources for enrolled class members.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "classId": "string (validate ID, ownership and existence)"
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

## LEA-003 — Get resource detail

**GET** `/api/v1/resources/{resourceId}`

- **Feature area:** Student resources
- **Purpose:** Return authorized resource metadata and current version.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-005 — Generate resource access URL

**POST** `/api/v1/resources/{resourceId}/access`

- **Feature area:** Student resources
- **Purpose:** Issue short-lived signed URL after per-request entitlement check.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-007 — List owned resources

**GET** `/api/v1/teachers/me/resources`

- **Feature area:** Teacher resource authoring
- **Purpose:** List resources for teacher-owned active and archived classes.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
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

## LEA-008 — Create resource metadata

**POST** `/api/v1/teachers/me/classes/{classId}/resources`

- **Feature area:** Teacher resource authoring
- **Purpose:** Create draft class-linked material with medium and visibility.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "classId": "string (validate ID, ownership and existence)"
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

## LEA-011 — Initialize file upload

**POST** `/api/v1/teachers/me/resources/{resourceId}/uploads/init`

- **Feature area:** Teacher resource authoring
- **Purpose:** Create private signed upload request with expected type and size.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-012 — Finalize upload version

**POST** `/api/v1/teachers/me/resources/{resourceId}/uploads/complete`

- **Feature area:** Teacher resource authoring
- **Purpose:** Validate uploaded file and queue malware scan before publication.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-013 — Publish approved resource

**POST** `/api/v1/teachers/me/resources/{resourceId}/publish`

- **Feature area:** Teacher resource authoring
- **Purpose:** Expose scanned valid material to enrolled students.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-014 — Archive resource

**POST** `/api/v1/teachers/me/resources/{resourceId}/archive`

- **Feature area:** Teacher resource authoring
- **Purpose:** Withdraw from future distribution without deleting audit history.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-016 — List resources for moderation

**GET** `/api/v1/admin/resources`

- **Feature area:** Resource moderation
- **Purpose:** Filter queued quarantined rejected and published materials.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
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

## LEA-018 — Quarantine unsafe material

**POST** `/api/v1/admin/resources/{resourceId}/quarantine`

- **Feature area:** Resource moderation
- **Purpose:** Immediately revoke new access to unsafe file.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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

## LEA-019 — Withdraw resource

**POST** `/api/v1/admin/resources/{resourceId}/withdraw`

- **Feature area:** Resource moderation
- **Purpose:** Withdraw item after verified policy or copyright concern.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-07, BR-08, BR-09, BR-17
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "resourceId": "string (validate ID, ownership and existence)"
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
