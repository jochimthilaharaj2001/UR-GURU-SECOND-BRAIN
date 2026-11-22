# Media — MVP API Documentation

**API count:** 15
**Status:** Proposed request/response contracts; requires approval.

## MED-001 — Initialize private media upload

**POST** `/api/v1/media/uploads/init`

- **Feature area:** Private upload and playback
- **Purpose:** Create scoped signed upload token with file size and content type limits.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
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

## MED-002 — Finalize media upload

**POST** `/api/v1/media/uploads/{uploadId}/complete`

- **Feature area:** Private upload and playback
- **Purpose:** Verify completed object checksums metadata and queue processing.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "uploadId": "string (validate ID, ownership and existence)"
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

## MED-003 — Check upload processing

**GET** `/api/v1/media/uploads/{uploadId}/status`

- **Feature area:** Private upload and playback
- **Purpose:** Return owned transcode scan and moderation progress.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "uploadId": "string (validate ID, ownership and existence)"
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

## MED-005 — Get authorized playback token

**POST** `/api/v1/media/{mediaId}/playback-token`

- **Feature area:** Private upload and playback
- **Purpose:** Check entitlement medium review and issue short-lived playback URL.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "mediaId": "string (validate ID, ownership and existence)"
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

## MED-006 — Get accessible media metadata

**GET** `/api/v1/media/{mediaId}/metadata`

- **Feature area:** Private upload and playback
- **Purpose:** Return permitted playback format subtitle languages and duration.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "mediaId": "string (validate ID, ownership and existence)"
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

## MED-008 — Report media

**POST** `/api/v1/media/{mediaId}/report`

- **Feature area:** Private upload and playback
- **Purpose:** Submit question-video rights or safety concern.
- **Authorized role (tracker):** Student
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R1/R2 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "mediaId": "string (validate ID, ownership and existence)"
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

## MED-010 — Create video explanation submission

**POST** `/api/v1/teachers/me/xact/questions/{questionId}/videos`

- **Feature area:** Teacher question videos
- **Purpose:** Associate media with approved translation rights and selected spoken medium.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
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

## MED-011 — Get video status

**GET** `/api/v1/teachers/me/xact/videos/{videoId}`

- **Feature area:** Teacher question videos
- **Purpose:** Return owned video metadata review status and reviewer feedback.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-012 — Update video submission metadata

**PATCH** `/api/v1/teachers/me/xact/videos/{videoId}`

- **Feature area:** Teacher question videos
- **Purpose:** Edit draft description language rights and caption data.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-013 — Submit video for review

**POST** `/api/v1/teachers/me/xact/videos/{videoId}/submit`

- **Feature area:** Teacher question videos
- **Purpose:** Submit processed scanned media for independent content review.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-016 — Get video moderation queue

**GET** `/api/v1/admin/xact/videos/review-queue`

- **Feature area:** Media academic moderation
- **Purpose:** List eligible submissions and processing failures.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-04, BR-20
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

## MED-018 — Approve video

**POST** `/api/v1/admin/xact/videos/{videoId}/approve`

- **Feature area:** Media academic moderation
- **Purpose:** Approve correct reviewed video for publication.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-021 — Publish reviewed video

**POST** `/api/v1/admin/xact/videos/{videoId}/publish`

- **Feature area:** Media academic moderation
- **Purpose:** Expose approved processed video under entitlement policy.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-022 — Withdraw published video

**POST** `/api/v1/admin/xact/videos/{videoId}/withdraw`

- **Feature area:** Media academic moderation
- **Purpose:** Revoke playback while retaining review and reporting trail.
- **Authorized role (tracker):** Academic Reviewer
- **BRD mapping:** BR-04, BR-20
- **Release / phase:** R2 / R2 XACT
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "videoId": "string (validate ID, ownership and existence)"
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

## MED-025 — Receive media processing callback

**POST** `/api/v1/webhooks/media/processing`

- **Feature area:** Provider event integration
- **Purpose:** Authenticate provider callback and update media state idempotently.
- **Authorized role (tracker):** Provider webhook
- **BRD mapping:** BR-04, BR-20
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
