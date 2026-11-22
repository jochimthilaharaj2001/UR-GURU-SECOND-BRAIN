# Assessment — MVP API Documentation

**API count:** 39
**Status:** Proposed request/response contracts; requires approval.

## ASS-001 — List mock exam presets

**GET** `/api/v1/xact/mock-presets`

- **Feature area:** Mock configuration and presets
- **Purpose:** Return approved counts durations marks and eligibility by subject.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-004 — Create custom mock

**POST** `/api/v1/xact/mocks`

- **Feature area:** Mock configuration and presets
- **Purpose:** Select approved immutable questions without duplicate canonical concepts.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-007 — Create past-paper practice

**POST** `/api/v1/xact/papers/{paperSourceId}/practice`

- **Feature area:** Mock configuration and presets
- **Purpose:** Create source-paper practice with eligible approved translations.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperSourceId": "string (validate ID, ownership and existence)"
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

## ASS-008 — Start mock attempt

**POST** `/api/v1/xact/mocks/{mockId}/attempts`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Validate entitlement retake policy and create server-timebox attempt.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "mockId": "string (validate ID, ownership and existence)"
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

## ASS-009 — Get attempt state

**GET** `/api/v1/xact/attempts/{attemptId}`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Return owned attempt start deadline question snapshots and progress.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-010 — Fetch exam questions

**GET** `/api/v1/xact/attempts/{attemptId}/questions`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Return immutable question and shuffled option snapshots without correct keys.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-011 — Autosave answer

**PUT** `/api/v1/xact/attempts/{attemptId}/answers/{itemId}`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Persist choice or unanswered state idempotently for one attempt item.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)",
    "itemId": "string (validate ID, ownership and existence)"
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

## ASS-012 — Batch autosave answers

**POST** `/api/v1/xact/attempts/{attemptId}/answers/batch`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Persist safe batch updates and return per-item acknowledgments.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-014 — Submit exam attempt

**POST** `/api/v1/xact/attempts/{attemptId}/submit`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Close exam once and grade server-side with idempotency key.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-015 — Resume interrupted attempt

**POST** `/api/v1/xact/attempts/{attemptId}/resume`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Enforce original deadline and resume-policy status.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-016 — List my attempts

**GET** `/api/v1/xact/attempts/me`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Filter owned submitted in-progress and expired attempts.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-017 — Get attempt result

**GET** `/api/v1/xact/attempts/{attemptId}/result`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Return scoring counts total and release-eligible result details.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-018 — Review submitted answers

**GET** `/api/v1/xact/attempts/{attemptId}/answers/review`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Reveal allowed answers explanations only after configured release window.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-019 — Get topic performance

**GET** `/api/v1/xact/attempts/{attemptId}/topics`

- **Feature area:** Exam attempt and scoring
- **Purpose:** Show topic accuracy with minimum sample-size qualifications.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-022 — Get performance overview

**GET** `/api/v1/xact/analytics/me/overview`

- **Feature area:** Student progress and analytics
- **Purpose:** Return overall attempt trends and explanation usage.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-024 — Get topic strengths and weaknesses

**GET** `/api/v1/xact/analytics/me/topics`

- **Feature area:** Student progress and analytics
- **Purpose:** Report confidence-qualified topic accuracy and practice volume.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-028 — List my teacher papers

**GET** `/api/v1/teachers/me/xact/papers`

- **Feature area:** Teacher paper authoring
- **Purpose:** List teacher-owned draft published and archived papers.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-029 — Create teacher paper

**POST** `/api/v1/teachers/me/xact/papers`

- **Feature area:** Teacher paper authoring
- **Purpose:** Create draft referencing authorized subject and approved question bank.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-030 — Get teacher paper

**GET** `/api/v1/teachers/me/xact/papers/{paperId}`

- **Feature area:** Teacher paper authoring
- **Purpose:** View own paper metadata version and item count.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-031 — Update teacher paper draft

**PATCH** `/api/v1/teachers/me/xact/papers/{paperId}`

- **Feature area:** Teacher paper authoring
- **Purpose:** Edit allowed paper name description timing and subject rules.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-032 — Add paper question

**POST** `/api/v1/teachers/me/xact/papers/{paperId}/items`

- **Feature area:** Teacher paper authoring
- **Purpose:** Add approved question translation to draft without duplicates.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-034 — Remove paper question

**DELETE** `/api/v1/teachers/me/xact/papers/{paperId}/items/{itemId}`

- **Feature area:** Teacher paper authoring
- **Purpose:** Remove item from draft without mutating source bank.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)",
    "itemId": "string (validate ID, ownership and existence)"
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

## ASS-036 — Preview paper

**GET** `/api/v1/teachers/me/xact/papers/{paperId}/preview`

- **Feature area:** Teacher paper authoring
- **Purpose:** Render full approved source snapshot for teacher validation.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-037 — Publish paper version

**POST** `/api/v1/teachers/me/xact/papers/{paperId}/publish`

- **Feature area:** Teacher paper authoring
- **Purpose:** Lock immutable paper version after content eligibility checks.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-041 — List my paper assignments

**GET** `/api/v1/teachers/me/xact/assignments`

- **Feature area:** Assignments and students
- **Purpose:** List owned assignments including active overdue completed.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-042 — Assign paper to students

**POST** `/api/v1/teachers/me/xact/papers/{paperId}/assignments`

- **Feature area:** Assignments and students
- **Purpose:** Assign one published version to authorized students or enrolled class.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperId": "string (validate ID, ownership and existence)"
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

## ASS-043 — Get assignment detail

**GET** `/api/v1/teachers/me/xact/assignments/{assignmentId}`

- **Feature area:** Assignments and students
- **Purpose:** Read assigned window time rules and recipients.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "assignmentId": "string (validate ID, ownership and existence)"
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

## ASS-049 — Get assignment submissions

**GET** `/api/v1/teachers/me/xact/assignments/{assignmentId}/submissions`

- **Feature area:** Assignments and students
- **Purpose:** List authorized students' submission states only.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "assignmentId": "string (validate ID, ownership and existence)"
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

## ASS-050 — Get assignment report

**GET** `/api/v1/teachers/me/xact/assignments/{assignmentId}/analytics`

- **Feature area:** Assignments and students
- **Purpose:** View aggregates and question/topic performance of allowed class.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "assignmentId": "string (validate ID, ownership and existence)"
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

## ASS-052 — List my assigned papers

**GET** `/api/v1/xact/assignments/me`

- **Feature area:** Assignments and students
- **Purpose:** List assignments that explicitly include the current student.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-053 — Get assigned paper

**GET** `/api/v1/xact/assignments/{assignmentId}`

- **Feature area:** Assignments and students
- **Purpose:** Validate recipient due window and time rules.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "assignmentId": "string (validate ID, ownership and existence)"
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

## ASS-054 — Start assigned paper

**POST** `/api/v1/xact/assignments/{assignmentId}/attempts`

- **Feature area:** Assignments and students
- **Purpose:** Start own authorized timed attempt under attempt limit.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "assignmentId": "string (validate ID, ownership and existence)"
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

## ASS-055 — List all exam presets

**GET** `/api/v1/admin/xact/mock-presets`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Read active draft and retired exam presets.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-056 — Create exam preset

**POST** `/api/v1/admin/xact/mock-presets`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Create timer question count score and reveal settings.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-057 — Update exam preset

**PATCH** `/api/v1/admin/xact/mock-presets/{presetId}`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Revise future-use presets without altering existing attempts.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "presetId": "string (validate ID, ownership and existence)"
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

## ASS-058 — Publish exam preset

**POST** `/api/v1/admin/xact/mock-presets/{presetId}/publish`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Enable reviewed policy version for new exams.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "presetId": "string (validate ID, ownership and existence)"
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

## ASS-059 — Search exam attempts

**GET** `/api/v1/admin/xact/attempts`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Inspect status and audit issues with role restrictions.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
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

## ASS-060 — Get attempt audit detail

**GET** `/api/v1/admin/xact/attempts/{attemptId}`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Inspect submitted snapshot without unauthorized student disclosure.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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

## ASS-061 — Invalidate attempt

**POST** `/api/v1/admin/xact/attempts/{attemptId}/invalidate`

- **Feature area:** Assessment administration and regrading
- **Purpose:** Invalidate corrupted or fraudulent attempt with reason and event.
- **Authorized role (tracker):** Admin / Academic Reviewer
- **BRD mapping:** BR-11, BR-18, BR-19, BR-10, BR-12
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "attemptId": "string (validate ID, ownership and existence)"
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
