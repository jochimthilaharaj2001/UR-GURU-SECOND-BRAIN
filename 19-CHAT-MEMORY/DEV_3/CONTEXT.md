# DEV_3: Frontend Specialist (Responsive Web) — Context & Starter

**Developer ID:** `DEV_3`  
**Role:** Frontend Developer (Responsive Web Application)  
**Primary Focus:** Student & Teacher responsive web portal, separate Admin portal, forms validation, error handling UX, and theme fidelity.

---

## 1. My Core Responsibilities
- **Responsive Web UI:** Implement the approved responsive web interface (Student, Teacher, Admin) based on prototypes:
  - `MergedScreens2.html`
  - `UR_GURU_Admin_Web_Only_Updated.html`
- **Zero Validation Bypass (BUG-001 Prevention):** Form submit buttons must ALWAYS validate required fields, highlight inline errors, focus on the first invalid field, and NEVER navigate on empty/invalid inputs.
- **Student Journeys:** Build the 30 student journeys (`SJ-01` to `SJ-30`) covering onboarding, teacher discovery, trial booking, paid enrollment, waiting room, live classroom UI, and results.
- **Design Tokens:** Strict adherence to Indigo/Violet theme (`brand.primary` `#4F46E5`, `brand.secondary` `#7C3AED`, responsive widths 390px mobile to 1440px desktop).
- **Exam Munnodi UI:** Question viewer with LaTeX/math rendering, option selection, timer, autosave indicators, and topic result breakdown.
- **Video Player:** Responsive HLS/DASH video playback supporting low-bandwidth 240p/360p options with written explanation fallback.

---

## 2. Key References I Must Read
1. [`06-UI-UX-DESIGN/MergedScreens2.html`](../../06-UI-UX-DESIGN/MergedScreens2.html)
2. [`06-UI-UX-DESIGN/UR_GURU_Admin_Web_Only_Updated.html`](../../06-UI-UX-DESIGN/UR_GURU_Admin_Web_Only_Updated.html)
3. [`05-USER-JOURNEYS/README.md`](../../05-USER-JOURNEYS/README.md)
4. [`15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md`](../../15-ISSUES-AND-CHANGELOG/ISSUES_AND_CHANGELOG.md) (BUG-001 analysis)
5. [`02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)

---

## 3. AI Starter Prompt (Copy-paste this when starting a new session)
```markdown
I am DEV_3 (Frontend Developer) working on the UR GURU Responsive Web Application.
Workspace: D:\Unicom\UR_GURU_finalProject
Please read my context file:
UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_3\CONTEXT.md
And our UI prototype:
UR-GURU-SECOND-BRAIN\06-UI-UX-DESIGN\MergedScreens2.html

Today I am building/refactoring [SCREEN ID / JOURNEY / COMPONENT].
Maintain the official Indigo/Violet theme, robust form validation with inline errors, accessible labels, responsive layout, and never navigate on invalid inputs.
```

---

## 4. My Daily Work Log
Record daily activities in `WORK-LOG-YYYY-MM-DD.md`.
Log any UI state adjustments or API expectation changes in `../SHARED-DECISIONS/CROSS-TEAM-LOG.md`.
