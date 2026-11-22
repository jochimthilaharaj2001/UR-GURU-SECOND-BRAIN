# MVP contract remediation — 292 source endpoint entries

The original 14 module files are preserved as **draft API inventory**; they are **not approved implementation-ready contracts**. Each endpoint is tracked in [MVP_CONTRACT_GAP_REGISTER.csv](MVP_CONTRACT_GAP_REGISTER.csv), with exact source path, method, BRD mapping and original tracker owner/status. A field marked TBD cannot be replaced by an invented required field.

## Definition of contract-ready (per API)
- Confirm request DTO and path/query/body fields: types, required/optional, defaults, validation, localization and example payload.
- Confirm response DTO and HTTP status codes; typed error codes; pagination/filtering if applicable.
- Define role + object ownership; authentication; PII restrictions; audit; concurrency/idempotency; rate limiting where needed.
- Map to approved entities and UI screen(s); attach UAT IDs, positive/negative examples and reviewer sign-off.
- Replace `_contractStatus` and `data: TBD` only after feature owner/engineering approval.

**Counts:** 292 MVP source entries. Post-MVP index states 177. The deferred 52 list is absent: no endpoints invented.
