# Identity — MVP API Documentation

**API count:** 20
**Status:** Proposed request/response contracts; requires approval.

## IDE-001 — Register student account

**POST** `/api/v1/auth/register/student`

- **Feature area:** Authentication
- **Purpose:** Create student credentials and pending verification account.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-002 — Register teacher account

**POST** `/api/v1/auth/register/teacher`

- **Feature area:** Authentication
- **Purpose:** Create teacher credentials and begin verification onboarding.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-003 — Sign in

**POST** `/api/v1/auth/login`

- **Feature area:** Authentication
- **Purpose:** Authenticate credentials and issue authorized session credentials.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-004 — Refresh session

**POST** `/api/v1/auth/token/refresh`

- **Feature area:** Authentication
- **Purpose:** Rotate refresh token and renew access token securely.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-005 — Log out session

**POST** `/api/v1/auth/logout`

- **Feature area:** Authentication
- **Purpose:** Invalidate current refresh/session credentials.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-009 — Send email verification code

**POST** `/api/v1/auth/email/verification/send`

- **Feature area:** Authentication
- **Purpose:** Issue expiring email verification code with rate limit.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-010 — Confirm email

**POST** `/api/v1/auth/email/verification/confirm`

- **Feature area:** Authentication
- **Purpose:** Verify ownership of email using expiring code.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-013 — Request password reset

**POST** `/api/v1/auth/password/forgot`

- **Feature area:** Authentication
- **Purpose:** Start secure account recovery without disclosing account existence.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-014 — Reset password

**POST** `/api/v1/auth/password/reset`

- **Feature area:** Authentication
- **Purpose:** Validate reset token and set new password with session invalidation.
- **Authorized role (tracker):** Public
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-015 — Change password

**POST** `/api/v1/auth/password/change`

- **Feature area:** Authentication
- **Purpose:** Validate current password before rotating password and sessions.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-016 — Get current account

**GET** `/api/v1/auth/me`

- **Feature area:** Authentication
- **Purpose:** Return current user roles and account-security status.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-017 — Start MFA enrollment

**POST** `/api/v1/auth/mfa/setup`

- **Feature area:** MFA & account protection
- **Purpose:** Issue MFA setup challenge for a signed-in account.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-018 — Confirm MFA enrollment

**POST** `/api/v1/auth/mfa/confirm`

- **Feature area:** MFA & account protection
- **Purpose:** Verify MFA enrollment and activate second factor.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-019 — Issue MFA challenge

**POST** `/api/v1/auth/mfa/challenge`

- **Feature area:** MFA & account protection
- **Purpose:** Generate challenge for step-up protected operations.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-020 — Verify MFA challenge

**POST** `/api/v1/auth/mfa/verify`

- **Feature area:** MFA & account protection
- **Purpose:** Validate proof and issue step-up authorization.
- **Authorized role (tracker):** Authenticated
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-023 — Search user accounts

**GET** `/api/v1/admin/users`

- **Feature area:** Privileged identity administration
- **Purpose:** Filter accounts by status role and verified contact.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
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

## IDE-024 — View user account

**GET** `/api/v1/admin/users/{userId}`

- **Feature area:** Privileged identity administration
- **Purpose:** Read controlled account information excluding secrets.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "userId": "string (validate ID, ownership and existence)"
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

## IDE-025 — Change user status

**PATCH** `/api/v1/admin/users/{userId}/status`

- **Feature area:** Privileged identity administration
- **Purpose:** Lock suspend or restore account with audit reason.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "userId": "string (validate ID, ownership and existence)"
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

## IDE-027 — Grant role

**POST** `/api/v1/admin/users/{userId}/roles`

- **Feature area:** Privileged identity administration
- **Purpose:** Grant an allowed role with privileged change audit.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "userId": "string (validate ID, ownership and existence)"
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

## IDE-028 — Revoke role

**DELETE** `/api/v1/admin/users/{userId}/roles/{roleCode}`

- **Feature area:** Privileged identity administration
- **Purpose:** Revoke role and invalidate affected authorizations.
- **Authorized role (tracker):** Admin
- **BRD mapping:** BR-01, BR-22
- **Release / phase:** R0 / R0 Foundation
- **Assignee / status:** Dinoshan / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
    "userId": "string (validate ID, ownership and existence)",
    "roleCode": "string (validate ID, ownership and existence)"
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
