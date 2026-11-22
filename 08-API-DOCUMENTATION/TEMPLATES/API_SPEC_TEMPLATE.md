# API: <API-ID> — <API NAME>

**Status:** Draft / In review / Approved  
**Source tracker row:** <sheet, API ID>  
**BRD mapping:** <BR-XX; acceptance AC-XX>  
**Module / owner:** <module, developer, reviewer>  
**Consumers:** Student / Teacher / Admin / Service  
**Screen mapping:** <actual prototype screen ID / TBD>

## Endpoint
`<METHOD> /api/v1/<path>`

**Purpose:** <business outcome>  
**Authentication:** <scheme>  
**Authorization:** <role AND ownership/membership rules>  
**Idempotency / concurrency:** <requirements or N/A>

## Request

Path parameters: <names, types, constraints>  
Query parameters: <names, types, constraints>  
Headers: <auth, content type, idempotency key as applicable>

```json
{"exampleField": "TBD — proposed only"}
```

## Response

**Success status:** <200/201/204 as approved>

```json
{"data": "TBD — proposed only", "correlationId": "TBD"}
```

**Error cases:** validation, unauthorized, forbidden, not found, conflict, business rule, throttling; list actual per-endpoint status and codes.

## Data and integrations
Entities, transaction boundary, external providers, event/outbox, audit and PII rules: <TBD>

## Tests and acceptance
- Happy path and validation failures
- Authentication, ownership, role isolation
- Retry/idempotency and concurrent requests where relevant
- BRD AC mapping and UI loading/empty/error/success states

**Approvals:** Product <TBD>; Backend <TBD>; Security <TBD>; QA <TBD>; date <TBD>.
