# UR GURU — Team Chat Memory & Development Handbook
**Folder:** `19-CHAT-MEMORY/`  
**Purpose:** Each developer's daily work log, decisions, blockers, and AI context — stored separately per member.  
**Last Updated:** 17 November 2026

---

## 1. Team Structure (6 Members)

| Folder | Role | Owns |
|---|---|---|
| [`DEV_1/`](DEV_1/) | **Jochim** (Project Lead / Full Stack Architect) | Architecture decisions, sprint planning, cross-team decisions, stakeholder updates |
| [`DEV_2/`](DEV_2/) | Backend Developer | C# ASP.NET Core API, Auth, Business Logic, Gateway integration |
| [`DEV_3/`](DEV_3/) | Frontend Developer | Responsive Web UI — Student & Teacher portal, Admin portal |
| [`DEV_4/`](DEV_4/) | Database Developer | SQL Server schema, EF Core migrations, queries, ERD maintenance |
| [`DEV_5/`](DEV_5/) | Exam Munnodi Developer | Question bank ingestion, mock engine, teacher paper builder, scoring |
| [`DEV_6/`](DEV_6/) | QA / Test Engineer | Test cases, automated tests, bug reports, UAT sign-off |
| [`SHARED-DECISIONS/`](SHARED-DECISIONS/) | All Members | Cross-team decisions, ADRs, blockers needing group discussion |

---

## 2. How Each Developer Uses Their Folder

Each developer maintains files in their folder using this naming convention:

```
DEV_X/
├── CONTEXT.md              ← "My AI context starter" — always read this first in a new chat
├── WORK-LOG-YYYY-MM-DD.md  ← Daily work log (create one per day)
├── DECISIONS.md            ← My own technical decisions with rationale
├── BLOCKERS.md             ← Current blockers (update daily)
└── HANDOFF-YYYY-MM-DD.md   ← End-of-sprint handoff notes to team
```

---

## 3. How to Add Changes to Chat Memory — Step-by-Step

### Every time you work on the project with AI (Antigravity/ChatGPT/Claude):

**Step 1 — Start your session:**
```
"Read D:\Unicom\UR_GURU_finalProject\UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_X\CONTEXT.md 
 and the shared BRD: 02-BRD-AND-REQUIREMENTS\UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md"
```

**Step 2 — Do your work** (coding, design, review etc.)

**Step 3 — End of session, update your log:**
```
"Update my work log at DEV_X\WORK-LOG-2026-11-17.md with:
 - What I completed today
 - What decisions I made (with reasoning)
 - What blockers I have
 - What I need from other team members"
```

**Step 4 — If your change affects others:**
```
"Add an entry to SHARED-DECISIONS\CROSS-TEAM-LOG.md about [your decision/change]"
```

---

## 4. Golden Rules for All 6 Members

> [!IMPORTANT]
> 1. **Never change the BRD or ERD files directly** — only the Project Lead (DEV_1) can update `02-BRD-AND-REQUIREMENTS/` after team discussion.
> 2. **Write your work log in English** — so AI can read and help any team member.
> 3. **If you are blocked**, add it to `BLOCKERS.md` AND `SHARED-DECISIONS/CROSS-TEAM-LOG.md` immediately.
> 4. **Before starting a feature**, check if another member has already noted a decision about it in `SHARED-DECISIONS/`.
> 5. **Link your work to BR IDs** — every code change should reference a Business Rule (e.g., `BR-03`, `BR-05`).

---

## 5. Shared Project Context Files (Read-Only for Developers)

| File | What it contains |
|---|---|
| [`../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) | Full BRD V6.1 — all requirements, AC, OD |
| [`../07-DATABASE-DESIGN/README.md`](../07-DATABASE-DESIGN/README.md) | 26-Entity ERD with 7 critical bug fixes |
| [`../07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql`](../07-DATABASE-DESIGN/UR_GURU_A_L_ONLY_V2_PostgreSQL.sql) | Relational SQL schema (45 tables) |
| [`../08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx`](../08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx) | 161 active API endpoints |
| [`../09-BUSINESS-RULES/UR_GURU_Business_Rules_V2_0.docx`](../09-BUSINESS-RULES/UR_GURU_Business_Rules_V2_0.docx) | BR-001 to BR-077 |
| [`../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md`](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md) | ADR-01..14, OD-01..16 |
| [`CONSOLIDATED_PROJECT_MEMORY_2026-11-17.md`](CONSOLIDATED_PROJECT_MEMORY_2026-11-17.md) | Full project history & key decisions |

