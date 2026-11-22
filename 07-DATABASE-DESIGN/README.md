> **2026-11-22 MySQL alignment:** MySQL 8.4 LTS is the user-selected *engineering candidate*, replacing older SQL Server/PostgreSQL assumptions. All table inventories, DBML, ERD diagrams, column definitions and constraints here remain **logical proposals**; they have **not** been certified as MySQL 8.4 physical DDL. Run compatibility, collation, FK/index, transactional concurrency and EF Core migration reviews before sign-off. [Technical alignment](../04-TECHNICAL-ARCHITECTURE/TECHNICAL-ARCHITECTURE-BASELINE-2026-11-22.md).

> **22 Nov 2026 correction notice:** Refer to root README and BRD v6.2.2 for active scope. Earlier counts, approvals and legacy references below are historical until reconciled.

# 07 — DATABASE DESIGN | UR GURU v6.2.2

> **Status: PROPOSED LOGICAL DATABASE DESIGN — NOT AN APPROVED PHYSICAL ERD OR MIGRATION**  
> **Source:** `../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf` (19 November 2026), pp. 3–12; architecture section 04.  
> **Approval gate:** BRD **OD-20** (database vendor / ERD v1.2 / schema approval), plus OD-02/03/04/05/07/09/10/15/19.

**Current release context:** Responsive Student/Teacher Web + separate Admin Web; Bio/Maths initial streams; optional free **prerecorded demo**, no scheduled trial booking; XACT is current assessment brand. Existing UI prototypes are **PENDING**, not the authority for database fields.

## Start here

| File | Purpose |
|---|---|
| [00-Design-Baseline-and-Sources.md](./00-Design-Baseline-and-Sources.md) | Document authority, review status, scope and legacy warnings |
| [01-Logical-Entity-Catalog.md](./01-Logical-Entity-Catalog.md) | 64 **proposed candidates**, grouped by bounded context |
| [02-Table-Definitions.md](./02-Table-Definitions.md) | Provisional identifiers, key fields and module ownership |
| [03-Data-Dictionary.md](./03-Data-Dictionary.md) | Type conventions / important field definitions |
| [04-Relationships-and-Cardinalities.md](./04-Relationships-and-Cardinalities.md) | PK/FK links, required vs optional edges |
| [05-Constraints-and-Indexes.md](./05-Constraints-and-Indexes.md) | Integrity, uniqueness, indexing, concurrency and transactions |
| [06-Module-Ownership-and-Security.md](./06-Module-Ownership-and-Security.md) | Modular-monolith persistence boundaries and privacy |
| [07-XACT-Versioning-and-Attempts.md](./07-XACT-Versioning-and-Attempts.md) | Immutable question, translation, answer key and attempts |
| [08-Demo-Subjects-and-Enrollment.md](./08-Demo-Subjects-and-Enrollment.md) | Demo optionality and independent subject selection |
| [09-Commerce-and-Ledger.md](./09-Commerce-and-Ledger.md) | Money trail, entitlements, refunds and payout accounting |
| [10-EF-Core-Migration-Plan.md](./10-EF-Core-Migration-Plan.md) | Safe migration approach, conditional on OD-20 |
| [11-Legacy-45-Table-Gap-Analysis.md](./11-Legacy-45-Table-Gap-Analysis.md) | Why old PostgreSQL SQL/DBML cannot be used as the approved v6.2.2 schema |
| [12-Approval-Gates-and-Open-Decisions.md](./12-Approval-Gates-and-Open-Decisions.md) | Outstanding schema choices |
| [Table-Inventory.csv](./Table-Inventory.csv) | Proposed entity registry for review |
| [Column-Dictionary.csv](./Column-Dictionary.csv) | Provisional columns and generic data types |
| [Relationships.csv](./Relationships.csv) | Reviewable candidate foreign keys |
| [Proposed-Logical-Schema.dbml](./Proposed-Logical-Schema.dbml) | **Editable proposal**, not approved SQL DDL |
| [Database-Module-Overview.png](./Database-Module-Overview.png) | High-level database module map |
| [Core-Relationships.png](./Core-Relationships.png) | Readable selected core relationships; not exhaustive |

## Existing files that should REMAIN as historic references

- `UR_GURU_A_L_ONLY_V2.dbml` and `UR_GURU_A_L_ONLY_V2_PostgreSQL.sql` — **LEGACY / NOT FOR EXECUTION AS CURRENT SCHEMA**.
- Existing ERD JPG/SVG assets — older version; retain with `LEGACY` label pending validated ERD v1.2.
- `TABLE-SPEC-TEMPLATE.md` — useful blank standard for future table-by-table approvals.

**No executable migration / production DDL is supplied** because the database vendor and physical schema are unapproved (OD-20). Do not create `DbContext` migrations from the old 45-table schema.
