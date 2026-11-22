# QuestionBank — MVP API Documentation

**API count:** 26
**Status:** Proposed request/response contracts; requires approval.

## QUE-001 — Browse approved past papers

**GET** `/api/v1/xact/papers`

- **Feature area:** Student approved question discovery
- **Purpose:** Filter available paper sources by year subject and medium.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
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

## QUE-002 — Get past-paper summary

**GET** `/api/v1/xact/papers/{paperSourceId}`

- **Feature area:** Student approved question discovery
- **Purpose:** Show source year subject question availability and permitted access.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "paperSourceId": "string (validate ID, ownership and existence)"
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

## QUE-003 — Check available questions

**GET** `/api/v1/xact/questions/availability`

- **Feature area:** Student approved question discovery
- **Purpose:** Count approved bank questions for subject medium topics and difficulty.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
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

## QUE-004 — Browse eligible questions

**GET** `/api/v1/xact/questions`

- **Feature area:** Student approved question discovery
- **Purpose:** Return approved question list for permitted practice filters without exposing answer keys.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
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

## QUE-005 — Get approved question

**GET** `/api/v1/xact/questions/{questionId}`

- **Feature area:** Student approved question discovery
- **Purpose:** Return language-specific approved question text media and options subject to reveal policy.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-006 — Get written explanation

**GET** `/api/v1/xact/questions/{questionId}/explanation`

- **Feature area:** Student approved question discovery
- **Purpose:** Return approved written explanation only after authorization and reveal rules.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-007 — Get explanation videos

**GET** `/api/v1/xact/questions/{questionId}/videos`

- **Feature area:** Student approved question discovery
- **Purpose:** List approved accessible video explanations for chosen medium.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-008 — List source inventory

**GET** `/api/v1/admin/xact/paper-sources`

- **Feature area:** Content import and source rights
- **Purpose:** Review five-year paper inventory and rights state.
- **Authorized role (tracker):** Academic Reviewer / Admin
- **BRD mapping:** BR-18, BR-23
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

## QUE-009 — Register past-paper source

**POST** `/api/v1/admin/xact/paper-sources`

- **Feature area:** Content import and source rights
- **Purpose:** Create year paper medium citation and rights evidence record.
- **Authorized role (tracker):** Academic Reviewer / Admin
- **BRD mapping:** BR-18, BR-23
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

## QUE-010 — Update source record

**PATCH** `/api/v1/admin/xact/paper-sources/{sourceId}`

- **Feature area:** Content import and source rights
- **Purpose:** Update metadata rights and attribution details with audit.
- **Authorized role (tracker):** Academic Reviewer / Admin
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "sourceId": "string (validate ID, ownership and existence)"
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

## QUE-011 — Approve source rights

**POST** `/api/v1/admin/xact/paper-sources/{sourceId}/rights-review`

- **Feature area:** Content import and source rights
- **Purpose:** Record evidence-backed reproduction and adaptation decision.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "sourceId": "string (validate ID, ownership and existence)"
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

## QUE-018 — Search question concepts

**GET** `/api/v1/admin/xact/questions`

- **Feature area:** Canonical questions and versions
- **Purpose:** Find draft approved withdrawn and duplicate concepts.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
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

## QUE-019 — Create question concept

**POST** `/api/v1/admin/xact/questions`

- **Feature area:** Canonical questions and versions
- **Purpose:** Create canonical syllabus topic provenance and difficulty record.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
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

## QUE-020 — Get question concept

**GET** `/api/v1/admin/xact/questions/{questionId}`

- **Feature area:** Canonical questions and versions
- **Purpose:** Read all versions options rights and review activity.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-021 — Update draft concept

**PATCH** `/api/v1/admin/xact/questions/{questionId}`

- **Feature area:** Canonical questions and versions
- **Purpose:** Edit unpublished canonical metadata while preserving published history.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-024 — Add question translation

**POST** `/api/v1/admin/xact/questions/{questionId}/translations`

- **Feature area:** Canonical questions and versions
- **Purpose:** Create Tamil Sinhala or English translation draft.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-027 — Revise draft translation

**PATCH** `/api/v1/admin/xact/translations/{translationId}`

- **Feature area:** Canonical questions and versions
- **Purpose:** Create or update permitted draft version and media references.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-028 — Submit translation for review

**POST** `/api/v1/admin/xact/translations/{translationId}/submit`

- **Feature area:** Canonical questions and versions
- **Purpose:** Lock candidate version and request independent language review.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-029 — Approve translated question

**POST** `/api/v1/admin/xact/translations/{translationId}/approve`

- **Feature area:** Canonical questions and versions
- **Purpose:** Confirm options answer mapping accuracy and reviewer independence.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-033 — List answer-key versions

**GET** `/api/v1/admin/xact/translations/{translationId}/answer-keys`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Review canonical option correctness for translated option order.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-034 — Create answer-key version

**POST** `/api/v1/admin/xact/translations/{translationId}/answer-keys`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Propose a newly versioned correct option mapping.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-035 — Approve answer-key version

**POST** `/api/v1/admin/xact/answer-keys/{keyVersionId}/approve`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Approve checked key without exposing it to active attempts.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "keyVersionId": "string (validate ID, ownership and existence)"
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

## QUE-038 — Create written explanation

**POST** `/api/v1/admin/xact/translations/{translationId}/explanations`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Create explanation draft with media and citation support.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "translationId": "string (validate ID, ownership and existence)"
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

## QUE-040 — Approve written explanation

**POST** `/api/v1/admin/xact/explanations/{explanationId}/approve`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Publish reviewed correct explanation to entitled users.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "explanationId": "string (validate ID, ownership and existence)"
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

## QUE-043 — Request question correction

**POST** `/api/v1/admin/xact/questions/{questionId}/corrections`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Record incorrect key translation or rights withdrawal evidence.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "questionId": "string (validate ID, ownership and existence)"
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

## QUE-044 — Approve correction release

**POST** `/api/v1/admin/xact/corrections/{correctionId}/approve`

- **Feature area:** Answer keys explanations corrections
- **Purpose:** Publish approved new version and schedule affected-attempt review.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-18, BR-23
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "correctionId": "string (validate ID, ownership and existence)"
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
