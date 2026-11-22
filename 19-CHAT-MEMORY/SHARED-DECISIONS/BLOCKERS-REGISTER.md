# UR GURU — Team Blockers Register

**Folder:** `19-CHAT-MEMORY/SHARED-DECISIONS/`  
**Purpose:** Surface any blocker that prevents a developer from proceeding with their tasks.

---

## Active Blockers

| Blocker ID | Reported Date | Reporter | Blocking Area | Waiting On | Severity | Status |
|---|---|---|---|---|---|---|
| BLK-001 | 2026-11-17 | DEV_2 | Payment Gateway Integration | Finance decision on Sri Lankan gateway provider (`OD-05`) | High | `Active` (Using Mock Gateway in interim) |
| BLK-002 | 2026-11-17 | DEV_5 | Past-paper MCQ Ingestion | Academic Lead content rights & 5-year paper inventory (`OD-07`, `OD-08`) | High | `Active` (Using sample seed set) |
| BLK-003 | 2026-11-17 | DEV_2 | Live Video Provider | LiveKit Cloud vs Agora procurement decision (`OD-06`) | Medium | `Active` (Abstracted behind `ILiveClassService`) |

---

## Blocker Entry Format
```markdown
### [BLK-XXX] <Blocker Title>
- **Date:** YYYY-MM-DD
- **Reported By:** DEV_X
- **Description:** <What is blocked?>
- **Need Help From:** DEV_Y / Product / Finance / Legal
- **Temporary Workaround:** <How work continues until unblocked>
```

