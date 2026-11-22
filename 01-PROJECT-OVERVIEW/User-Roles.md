# UR GURU — User Roles, Capabilities and Access Boundaries

| Field | Value |
|---|---|
| Document ID | `OV-04` |
| Version / prepared | Draft 1.0 / 19 November 2026 |
| Approval | **DRAFT — ROLE/PERMISSION MATRIX REQUIRES TECHNICAL & SAFEGUARDING REVIEW** |
| Main source | [BRD V6.1 §3, §8–9, §14](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) |

## 1. Roles in the current responsive-web product

| Actor | Product description | Entry / status |
|---|---|---|
| **Student** | Grade 12/13 A/L learner using tuition and, in Phase 2, Exam Munnodi | Registered identity with applicable consent and academic profile |
| **Teacher** | Educator who offers approved A/L teaching and assessments | Applicant until admin verification; `Pending`, `More Information Required`, `Approved`, `Rejected`, `Suspended` |
| **Administrator** | Authorized operator who manages verification, catalogue, finance exceptions, safety and audit | Privileged internal role with restricted administrative rights |
| **Academic/Content Reviewer** | Permission set for academic answer/translation/video review | May be assigned to qualified admin/reviewer personnel; **separate account role not yet finalized** |
| **Parent/Guardian contact** | Contact/consent or assisted-payment touchpoint if legally required | **Not** a full interactive guardian account/dashboard in Phase 1 |

The system should model users, business roles and granular authorization separately; exact `Role`/`Permission` tables are **not** prescribed by this overview.

## 2. Student permissions

**May (subject to entitlement/policy):**

- Register, authenticate, manage own profile (grade 12/13, stream, subjects, medium).
- Search and view public **approved** teacher listings, classes, fees, available trials and schedules.
- Request an eligible trial, enroll/pay for permitted class offerings and view own booking/payment state.
- Join only the class sessions for which the backend authorizes access, view own attendance and allowed class resources.
- Receive relevant notifications and submit safety/support reports.
- In Phase 2, configure subject/medium/topic/difficulty mock exams, answer, submit and view only own approved results/explanations/history.
- Access papers explicitly assigned to them during allowed windows and permitted attempt counts.

**Must not:**

- Access another student's profile, answers, exam attempts or results.
- Access private class materials without enrollment/entitlement.
- View a teacher's private verification evidence or bank details.
- Bypass timing, eligibility, approved question/medium restrictions, or client-side scoring restrictions.

## 3. Teacher permissions

**Before approval:** submit application, evidence and corrections; track own verification status. **Do not allow paid public class publication or approved question-bank modification.**

**After verified/active approval (and for authorized A/L subjects):**

- Create/edit class offerings, batches, capacity, timetables and session plans within allowed policy.
- Manage trial requests and view authorized enrolled students; begin/reschedule/cancel permitted live sessions.
- Record/view authorized attendance and publish permitted class-linked materials.
- View own commission/earnings and payout statements (financial details subject to finance role boundaries).
- In Phase 2, search approved read-only question translations, create drafts, preview/publish papers, assign to multiple eligible students, and view only their allowed submissions/results.
- Upload question-linked explanation videos for review; view reviewer feedback and content status.

**Must not:** self-approve teacher verification, change source question-bank answers, approve own explanation videos, see other teachers' private student results, create unsolicited assignments to unrelated students or expose private contact information.

**Suspension/revocation:** block new publishing and new assignment starts; ongoing classes/assignments need an **approved continuity policy** rather than a hard-coded assumption.

## 4. Administrator permissions

Role-appropriate operators may:

- Verify/suspend teacher identities and credentials; audit changes and reasons.
- Maintain master stream/subject/syllabus/topic catalogue and public eligibility settings.
- Manage content moderation and academic review workflows; determine restricted access via assigned permissions.
- Oversee trial/class operational exceptions, refunds/payout approvals and dispute workflows subject to segregation of duties.
- Process safety concerns, privacy requests and complaints within permitted case-access controls.
- Review operational, finance and audit reports (minimum necessary data only).

**Must not:** skip audit records, expose private results without legal/operational authorization, silently overwrite prior exam versions, or unilaterally bypass formal finance/safeguarding approval policies.

## 5. Academic/content reviewer permissions

An authorized reviewer (possibly within Admin) may check question keys, medium-specific translation/options, written explanations and submitted teacher videos for academic quality, rights and safeguarding. Reviewers can approve/reject/request changes **only for assigned content and roles**. Content approval must be independent of a teacher's submission; reviewer identity, timestamp and decision history must be retained.

## 6. Parent/guardian boundary

**Current scope:** student profile may store the parent/guardian **name and phone number**, and legally necessary consent/assisted-payment evidence. The exact consent model is subject to `OD-15` legal review.

**Not provided at Phase 1:** guardian login, guardian dashboard, unrestricted student attempts/results, independent class-enrollment actor, or universal access to private teaching activity. Full dashboard is `BR-16` Future.

Do **not** convert legacy `GuardianProfile` or guardian APIs into launch features without a formally approved change.

## 7. Suggested access-control matrix for implementation design

`✓` indicates an action **within the applicable business rules**; `—` means not authorized by default. This is a **proposed enforcement summary**, not a complete security policy.

| Action | Student | Approved teacher | Admin / designated reviewer | Guardian contact |
|---|---|---|---|---|
| Manage own profile | ✓ | ✓ | Privileged support only | — |
| View public approved teacher/classes | ✓ | ✓ | ✓ | Public-only, if applicable |
| Publish paid class | — | ✓ (own, authorized) | Admin oversight | — |
| Approve teacher identity | — | — | Designated admin only | — |
| Book/enroll/attend as student | ✓ (own) | — | Admin exception only | — |
| View student attempt/results | Own only | Assigned/authorized only | Case-scoped privileged access | — |
| Build/assign paper | — | ✓ (authorized students) | Designated admin controls | — |
| Edit source question/answer | — | — | Academic authoring role only | — |
| Approve explanation video | — | — | Designated reviewer only | — |
| Verify payment event | — | — | Backend/gateway workflow; finance review | — |
| Approve refund/payout exception | — | — | Authorized finance/admin only | — |
| See audit/security events | — | — | Restricted admin/audit function | — |
| Submit safety report | ✓ | As allowed | ✓/case handling | Contact route only if approved |

**Critical engineering note:** A browser's visible button is not permission. All authorization must be enforced server-side on the specific target student, class, session, assignment, content and transaction.

## 8. Authentication / authorization lifecycle

1. Account created and authenticated through the approved login/recovery flow.
2. Student profile and consent requirements validated (if applicable) before restricted actions.
3. Teacher's verification and subject authorization checked on every publishing/assignment action.
4. Backend checks *role + record ownership/relationship + entitlement + active status + relevant dates*.
5. Sensitive changes (verification, payments, content review, consent, safety) produce traceable audit records.
6. Cross-student/cross-teacher forbidden access is included in negative tests (`AC-19`).

## 9. Approvals still required

- `OD-01`: educator qualification and screening requirements.
- `OD-15`: guardian consent, minor-data retention/PDPA and safeguarding review.
- Operational separation of academic-review, financial and general-admin permissions.
- Role-driven API permissions and final DB authorization model.
- Teacher suspension continuity for existing enrolled students and issued assessments.

## References

[BRD §3, §8, §9](../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md) · [Project Scope](Project-Scope.md) · [Modules and Features](Modules-and-Features.md) · [Decision Register](../13-DECISION-LOG/DECISIONS_AND_OPEN_ITEMS.md)
