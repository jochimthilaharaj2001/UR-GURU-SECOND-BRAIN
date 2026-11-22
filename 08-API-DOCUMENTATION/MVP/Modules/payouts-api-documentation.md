# Payouts — MVP API Documentation

**API count:** 19
**Status:** Proposed request/response contracts; requires approval.

## PAY-001 — Get earning summary

**GET** `/api/v1/teachers/me/earnings`

- **Feature area:** Teacher earnings
- **Purpose:** Show gross tuition commissions deductions and approved net earnings.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-06
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

## PAY-002 — Get earning ledger

**GET** `/api/v1/teachers/me/earnings/transactions`

- **Feature area:** Teacher earnings
- **Purpose:** List own earnings and reversals by enrollment order.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-06
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

## PAY-003 — List own payouts

**GET** `/api/v1/teachers/me/payouts`

- **Feature area:** Teacher earnings
- **Purpose:** Show payout batch history settlement dates and status.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-06
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

## PAY-005 — Get masked payout settings

**GET** `/api/v1/teachers/me/payout-settings`

- **Feature area:** Teacher earnings
- **Purpose:** Read own approved payee and settlement preference without bank secrets.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-06
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

## PAY-006 — Update payout settings request

**PUT** `/api/v1/teachers/me/payout-settings`

- **Feature area:** Teacher earnings
- **Purpose:** Submit changed bank details for independent approval.
- **Authorized role (tracker):** Teacher
- **BRD mapping:** BR-06
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

## PAY-007 — List teacher payees

**GET** `/api/v1/admin/payouts/payees`

- **Feature area:** Payee verification and earnings finance
- **Purpose:** Review payee KYC and verified settlement accounts.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-008 — Inspect payee

**GET** `/api/v1/admin/payouts/payees/{teacherId}`

- **Feature area:** Payee verification and earnings finance
- **Purpose:** Review protected bank verification without exposing to public APIs.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
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

## PAY-009 — Verify payee bank account

**POST** `/api/v1/admin/payouts/payees/{teacherId}/verify`

- **Feature area:** Payee verification and earnings finance
- **Purpose:** Confirm authorized KYC and bank details before settlement.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
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

## PAY-012 — List teacher earning lines

**GET** `/api/v1/admin/payouts/earnings`

- **Feature area:** Payee verification and earnings finance
- **Purpose:** Filter accrued confirmed refunded and payout-eligible earnings.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-014 — Preview eligible payout pool

**GET** `/api/v1/admin/payouts/eligible`

- **Feature area:** Payee verification and earnings finance
- **Purpose:** Calculate verified net earnings after refunds and reserves.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-015 — List payout batches

**GET** `/api/v1/admin/payouts/batches`

- **Feature area:** Payout batches and settlements
- **Purpose:** Filter draft approved processing paid and failed settlement batches.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-016 — Create payout batch

**POST** `/api/v1/admin/payouts/batches`

- **Feature area:** Payout batches and settlements
- **Purpose:** Freeze eligible earnings into reviewed draft settlement batch.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-017 — View payout batch

**GET** `/api/v1/admin/payouts/batches/{batchId}`

- **Feature area:** Payout batches and settlements
- **Purpose:** Inspect payees total allocations and held items.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-018 — Approve payout batch

**POST** `/api/v1/admin/payouts/batches/{batchId}/approve`

- **Feature area:** Payout batches and settlements
- **Purpose:** Authorize verified payout allocations with independent review.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-019 — Release payout batch

**POST** `/api/v1/admin/payouts/batches/{batchId}/release`

- **Feature area:** Payout batches and settlements
- **Purpose:** Submit approved settlement through contracted process.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-021 — List payout items

**GET** `/api/v1/admin/payouts/batches/{batchId}/items`

- **Feature area:** Payout batches and settlements
- **Purpose:** Show payee allocations and statuses for batch.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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

## PAY-022 — Confirm settlement item

**POST** `/api/v1/admin/payouts/items/{itemId}/confirm`

- **Feature area:** Payout batches and settlements
- **Purpose:** Reconcile bank reference and actual settled amount.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
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

## PAY-023 — Mark payout item failure

**POST** `/api/v1/admin/payouts/items/{itemId}/mark-failed`

- **Feature area:** Payout batches and settlements
- **Purpose:** Record failed transfer and return eligible earnings to controlled queue.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
- **Release / phase:** R1 / R1 Marketplace / Shared
- **Assignee / status:** Unassigned / To Do
- **Source scope:** CURRENT - CONTRACT REVIEW

**Request contract — DRAFT, fields not yet approved**
```json
{
  "pathParameters": {
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

## PAY-024 — Get settlement reconciliation

**GET** `/api/v1/admin/payouts/reconciliation`

- **Feature area:** Payout batches and settlements
- **Purpose:** Compare payout batches bank transfers and ledger state.
- **Authorized role (tracker):** Finance
- **BRD mapping:** BR-06
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
