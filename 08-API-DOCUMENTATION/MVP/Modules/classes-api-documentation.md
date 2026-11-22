# Classes — MVP API Documentation

**API count:** 34
**Status:** Proposed request/response contracts; requires approval.

## CLA-001 — Search published classes

**GET** `/api/v1/classes`

- **Feature area:** Public courses and batches
- **Purpose:** Filter approved published classes by subject medium fee and timetable.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-002 — View published class

**GET** `/api/v1/classes/{classId}`

- **Feature area:** Public courses and batches
- **Purpose:** Return class fee teacher syllabus and published schedule.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-003 — List bookable class batches

**GET** `/api/v1/classes/{classId}/batches`

- **Feature area:** Public courses and batches
- **Purpose:** Return bookable batches with remaining capacity.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-004 — Get public batch detail

**GET** `/api/v1/batches/{batchId}`

- **Feature area:** Public courses and batches
- **Purpose:** Return schedule capacity fee and eligibility summary.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-005 — Check batch seat availability

**GET** `/api/v1/batches/{batchId}/seats`

- **Feature area:** Public courses and batches
- **Purpose:** Return current capacity availability without reserving a seat.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-006 — Get batch timetable

**GET** `/api/v1/batches/{batchId}/schedule`

- **Feature area:** Public courses and batches
- **Purpose:** View current active weekly schedule and upcoming sessions.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-007 — List my classes

**GET** `/api/v1/teachers/me/classes`

- **Feature area:** Teacher class authoring
- **Purpose:** List owned draft published archived and suspended offerings.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-008 — Create class

**POST** `/api/v1/teachers/me/classes`

- **Feature area:** Teacher class authoring
- **Purpose:** Create subject medium fee syllabus and class metadata draft.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
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

## CLA-009 — Get owned class

**GET** `/api/v1/teachers/me/classes/{classId}`

- **Feature area:** Teacher class authoring
- **Purpose:** Read own class including non-public fields.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-010 — Update owned class

**PATCH** `/api/v1/teachers/me/classes/{classId}`

- **Feature area:** Teacher class authoring
- **Purpose:** Edit allowed class details; changes to paid enrollment follow policy.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-011 — Publish class

**POST** `/api/v1/teachers/me/classes/{classId}/publish`

- **Feature area:** Teacher class authoring
- **Purpose:** Validate approved teacher syllabus fees and schedule before publication.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-014 — Create batch

**POST** `/api/v1/teachers/me/classes/{classId}/batches`

- **Feature area:** Teacher class authoring
- **Purpose:** Create capacity-limited batch for an owned class.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-015 — Edit batch

**PATCH** `/api/v1/teachers/me/batches/{batchId}`

- **Feature area:** Teacher class authoring
- **Purpose:** Update capacity term or batch details with reservation safeguards.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-016 — Add recurring schedule

**POST** `/api/v1/teachers/me/batches/{batchId}/schedule`

- **Feature area:** Teacher class authoring
- **Purpose:** Create recurring timetable with timezone information.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-019 — List enrolled students

**GET** `/api/v1/teachers/me/batches/{batchId}/students`

- **Feature area:** Teacher class authoring
- **Purpose:** Return only authorized batch enrollments.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-020 — List public class demo videos

**GET** `/api/v1/classes/{classId}/demos`

- **Feature area:** Optional free DemoVideo
- **Purpose:** List only approved published active free prerecorded demos for a class.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

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

## CLA-021 — Submit teacher class demo video

**POST** `/api/v1/teachers/me/classes/{classId}/demos`

- **Feature area:** Optional free DemoVideo
- **Purpose:** Submit teacher-owned class demo using validated media and rights attestation.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

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

## CLA-023 — Get public demo playback

**GET** `/api/v1/demos/{demoId}/playback`

- **Feature area:** Optional free DemoVideo
- **Purpose:** Return approved free demo playback without enrollment booking or payment gate.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "demoId": "string (validate ID, ownership and existence)"
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

## CLA-024 — Submit demo for review

**POST** `/api/v1/teachers/me/demos/{demoId}/submit`

- **Feature area:** Optional free DemoVideo
- **Purpose:** Submit processed demo for independent rights and content review.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "demoId": "string (validate ID, ownership and existence)"
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

## CLA-025 — List demo moderation queue

**GET** `/api/v1/admin/demos/review-queue`

- **Feature area:** Optional free DemoVideo
- **Purpose:** List demo videos awaiting authorized independent review.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

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

## CLA-026 — Review demo submission

**POST** `/api/v1/admin/demos/{demoId}/review`

- **Feature area:** Optional free DemoVideo
- **Purpose:** Approve reject or request changes with actor reason and audit trail.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "demoId": "string (validate ID, ownership and existence)"
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

## CLA-027 — Publish or withdraw reviewed demo

**POST** `/api/v1/admin/demos/{demoId}/publication`

- **Feature area:** Optional free DemoVideo
- **Purpose:** Publish approved processed demo or withdraw it with audit.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-04
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - DEMO REPLACEMENT

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "demoId": "string (validate ID, ownership and existence)"
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

## CLA-028 — List my enrollments

**GET** `/api/v1/enrollments/me`

- **Feature area:** Enrollment and seats
- **Purpose:** List paid active expired and trial-derived authorized enrollments.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-029 — Get enrollment

**GET** `/api/v1/enrollments/{enrollmentId}`

- **Feature area:** Enrollment and seats
- **Purpose:** Return owned enrollment and entitlement state.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "enrollmentId": "string (validate ID, ownership and existence)"
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

## CLA-030 — Reserve checkout seat

**POST** `/api/v1/batches/{batchId}/seat-holds`

- **Feature area:** Enrollment and seats
- **Purpose:** Create expiring seat hold before paid checkout with concurrency control.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "batchId": "string (validate ID, ownership and existence)"
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

## CLA-032 — Get seat reservation

**GET** `/api/v1/seat-holds/{holdId}`

- **Feature area:** Enrollment and seats
- **Purpose:** Inspect owned hold expiration and status.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "holdId": "string (validate ID, ownership and existence)"
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

## CLA-033 — List teacher enrollments

**GET** `/api/v1/teachers/me/enrollments`

- **Feature area:** Enrollment and seats
- **Purpose:** Read enrolled students only for authorized teacher batches.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-034 — Get teacher enrollment detail

**GET** `/api/v1/teachers/me/enrollments/{enrollmentId}`

- **Feature area:** Enrollment and seats
- **Purpose:** Return class-level enrollment records to authorized teacher.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "enrollmentId": "string (validate ID, ownership and existence)"
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

## CLA-037 — View session attendance

**GET** `/api/v1/teachers/me/sessions/{sessionId}/attendance`

- **Feature area:** Attendance
- **Purpose:** List authorized join leave and attendance statuses.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "sessionId": "string (validate ID, ownership and existence)"
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

## CLA-038 — Correct attendance

**PUT** `/api/v1/teachers/me/sessions/{sessionId}/attendance/{studentId}`

- **Feature area:** Attendance
- **Purpose:** Correct specific student attendance with attributable reason.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-03, BR-04, BR-05
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "sessionId": "string (validate ID, ownership and existence)",
    "studentId": "string (validate ID, ownership and existence)"
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

## CLA-039 — View own attendance

**GET** `/api/v1/students/me/attendance`

- **Feature area:** Attendance
- **Purpose:** Return enrolled student's own attendance records.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-042 — Admin class list

**GET** `/api/v1/admin/classes`

- **Feature area:** Marketplace operations
- **Purpose:** Find all class lifecycle states and approval exceptions.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-043 — Suspend class

**POST** `/api/v1/admin/classes/{classId}/suspend`

- **Feature area:** Marketplace operations
- **Purpose:** Prevent new purchases and apply enrolled-student continuity policy.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-03, BR-04, BR-05
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

## CLA-044 — Restore class

**POST** `/api/v1/admin/classes/{classId}/restore`

- **Feature area:** Marketplace operations
- **Purpose:** Restore class if teacher and policy conditions pass.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-03, BR-04, BR-05
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
