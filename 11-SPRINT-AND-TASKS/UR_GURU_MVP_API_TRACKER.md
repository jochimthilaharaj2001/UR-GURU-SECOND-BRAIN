# UR GURU - MVP 104 API Implementation Tracker

**Overall Progress:** 18/104 APIs Completed (17.3%)
**Last Updated:** 2026-11-24
**Primary Backend Dev:** DEV_2 (Identity & Curriculum Modules Owner)

---

### Module Summary
| Module | Total APIs | Completed | Status |
|---|---|---|---|
| Identity | 13 | 13 | ✅ Done (100%) |
| Curriculum | 5 | 5 | ✅ Done (100%) |
| Discovery | 3 | 0 | ⚪ Pending (0%) |
| Classes | 12 | 0 | ⚪ Pending (0%) |
| Demo Videos | 4 | 0 | ⚪ Pending (0%) |
| Live Classes | 7 | 0 | ⚪ Pending (0%) |
| Payments | 13 | 0 | ⚪ Pending (0%) |
| Resources | 4 | 0 | ⚪ Pending (0%) |
| XACT Source | 4 | 0 | ⚪ Pending (0%) |
| XACT Exams | 8 | 0 | ⚪ Pending (0%) |
| XACT Teacher | 6 | 0 | ⚪ Pending (0%) |
| Notifications | 3 | 0 | ⚪ Pending (0%) |
| Admin | 12 | 0 | ⚪ Pending (0%) |
| Support Safety | 4 | 0 | ⚪ Pending (0%) |
| Community | 6 | 0 | ⚪ Pending (0%) |

---

### Detailed API Checklist

#### Module: Identity

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [x] ✅ Done | **MVP-01-001** | `POST` | `/api/v1/auth/register/student` | Register student (Student registration [AUTH01]) | Public | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-002** | `POST` | `/api/v1/auth/register/teacher` | Register teacher (Teacher registration [AUTH02]) | Public | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-003** | `POST` | `/api/v1/auth/login` | Login (Authentication sessions [AUTH03]) | Public | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-004** | `POST` | `/api/v1/auth/logout` | Logout (Authentication sessions [AUTH03]) | Authenticated | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-005** | `POST` | `/api/v1/auth/refresh` | Refresh access token (Authentication sessions [AUTH03]) | Authenticated | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-006** | `POST` | `/api/v1/auth/forgot-password` | Request password reset (Password recovery [AUTH04]) | Public | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-007** | `POST` | `/api/v1/auth/reset-password` | Reset password (Password recovery [AUTH04]) | Public | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-008** | `POST` | `/api/v1/auth/verify-contact` | Verify contact (Contact verification [AUTH05]) | Authenticated | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-009** | `POST` | `/api/v1/auth/resend-verification` | Resend verification (Contact verification [AUTH05]) | Authenticated | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-010** | `GET` | `/api/v1/users/me` | Get my identity (Current user + RBAC [AUTH06]) | Authenticated | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-011** | `PATCH` | `/api/v1/students/me/profile` | Update my student profile (Student profiles [AUTH07]) | Student | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-012** | `PATCH` | `/api/v1/teachers/me/profile` | Update my teacher profile (Teacher profiles [AUTH08]) | Teacher | DEV_2 | Verified (113 Tests) |
| [x] ✅ Done | **MVP-01-013** | `POST` | `/api/v1/teachers/me/identity-documents` | Submit teacher identity evidence (Teacher-only NIC [AUTH11]) | Teacher | DEV_2 | Verified (113 Tests) |
#### Module: Curriculum

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [x] ✅ Done | **MVP-02-001** | `GET` | `/api/v1/curriculum/streams` | List streams (Streams and subject eligibility [CUR01,CUR02,CUR03,CUR07]) | Authenticated | DEV_2 | Verified (123 Tests) |
| [x] ✅ Done | **MVP-02-002** | `GET` | `/api/v1/curriculum/subjects` | List eligible subjects (Streams and subject eligibility [CUR02,CUR03,CUR04,CUR07]) | Authenticated | DEV_2 | Verified (123 Tests) |
| [x] ✅ Done | **MVP-02-003** | `GET` | `/api/v1/curriculum/syllabuses` | List syllabus versions (Syllabus and topics [CUR06]) | Authenticated | DEV_2 | Verified (123 Tests) |
| [x] ✅ Done | **MVP-02-004** | `GET` | `/api/v1/curriculum/topics` | List syllabus topics (Syllabus and topics [CUR06]) | Authenticated | DEV_2 | Verified (123 Tests) |
| [x] ✅ Done | **MVP-02-005** | `PUT` | `/api/v1/students/me/academic-profile` | Save student academic profile (Academic profile selection [CUR01,CUR04,CUR05,CUR07]) | Student | DEV_2 | Verified (123 Tests) |
#### Module: Discovery

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-03-001** | `GET` | `/api/v1/teachers` | Find approved teachers (Teacher browse / filters [TCH04,TCH05,TCH06,TCH07]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-03-002** | `GET` | `/api/v1/teachers/{teacherId}` | View approved teacher (Public teacher profile [TCH03,TCH07]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-03-003** | `GET` | `/api/v1/teachers/{teacherId}/classes` | View teacher published classes (Teacher class visibility [TCH07]) | Public | Unassigned | Needs verification |
#### Module: Classes

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-04-001** | `POST` | `/api/v1/teacher/classes` | Create class offering (Class offerings [CLS01]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-002** | `GET` | `/api/v1/teacher/classes` | List my class offerings (Class offerings [CLS01]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-003** | `PATCH` | `/api/v1/teacher/classes/{classId}` | Edit my class offering (Class offerings [CLS01]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-004** | `POST` | `/api/v1/teacher/classes/{classId}/batches` | Create batch (Batches and schedules [CLS02,CLS04]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-005** | `PATCH` | `/api/v1/teacher/batches/{batchId}` | Update batch / cancel (Batches and schedules [CLS02,CLS09]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-006** | `GET` | `/api/v1/classes` | Browse published classes (Class discovery [CLS03]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-007** | `GET` | `/api/v1/classes/{classId}` | Get class details (Class discovery [CLS03]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-008** | `GET` | `/api/v1/classes/{classId}/batches` | List class batches and availability (Batch selection + seats [CLS04,CLS05]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-009** | `GET` | `/api/v1/batches/{batchId}` | Get batch and calculated fee (Batch selection + seats [CLS04,CLS05]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-010** | `GET` | `/api/v1/students/me/enrollments` | List my enrollments (Enrollment access [CLS06,CLS07,CLS10]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-011** | `GET` | `/api/v1/teacher/batches/{batchId}/students` | List students in my batch (Batch roster [CLS08]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-04-012** | `POST` | `/api/v1/teacher/batches/{batchId}/reschedule` | Reschedule batch (Cancel or reschedule class [CLS09]) | Teacher | Unassigned | Needs verification |
#### Module: Demo Videos

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-05-001** | `POST` | `/api/v1/teacher/classes/{classId}/demos` | Create demo upload (Demo upload [DEM01,DEM02]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-05-002** | `POST` | `/api/v1/teacher/demos/{demoId}/complete-upload` | Complete demo upload (Demo upload [DEM01,DEM02]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-05-003** | `GET` | `/api/v1/classes/{classId}/demos` | List approved demos (Approved demo discovery [DEM04,DEM06]) | Public | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-05-004** | `GET` | `/api/v1/demos/{demoId}/playback` | Get free demo playback (Free demo playback [DEM05]) | Public | Unassigned | Needs verification |
#### Module: Live Classes

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-06-001** | `POST` | `/api/v1/teacher/batches/{batchId}/sessions` | Schedule live class (Session scheduling [LIVE01]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-002** | `GET` | `/api/v1/batches/{batchId}/sessions` | List batch sessions (Session scheduling [LIVE01]) | Entitled Student / Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-003** | `PATCH` | `/api/v1/teacher/sessions/{sessionId}` | Update / reschedule session (Session changes [LIVE07]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-004** | `POST` | `/api/v1/teacher/sessions/{sessionId}/cancel` | Cancel session (Session changes [LIVE07]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-005** | `POST` | `/api/v1/sessions/{sessionId}/join` | Issue secure live join credentials (Secure live access [LIVE02,LIVE03,LIVE04,LIVE05]) | Teacher / Entitled Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-006** | `POST` | `/api/v1/live/provider/events` | Receive authenticated provider events (Attendance [LIVE06]) | Provider Webhook | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-06-007** | `GET` | `/api/v1/teacher/sessions/{sessionId}/attendance` | Get teacher attendance (Attendance [LIVE06]) | Teacher | Unassigned | Needs verification |
#### Module: Payments

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-07-001** | `POST` | `/api/v1/checkout/orders` | Create checkout order (Checkout + seat reserve [PAY01,PAY02]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-002** | `GET` | `/api/v1/checkout/orders/{orderId}` | Get order checkout details (Checkout + fee display [PAY01,PAY02]) | Order Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-003** | `POST` | `/api/v1/payments/{orderId}/initiate` | Initiate gateway payment (Payment gateway [PAY03]) | Order Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-004** | `POST` | `/api/v1/payments/gateway/webhook` | Receive verified gateway webhook (Verified payment [PAY04,PAY05]) | Provider Webhook | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-005** | `GET` | `/api/v1/payments/{paymentId}/status` | Get payment status (Payment status [PAY04]) | Owner / Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-006** | `GET` | `/api/v1/students/me/payments` | My payment history (Payment history [PAY06]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-007** | `GET` | `/api/v1/payments/{paymentId}/receipt` | View payment receipt (Payment history [PAY06]) | Owner / Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-008** | `POST` | `/api/v1/refunds` | Request manual refund (Manual refunds [PAY07]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-009** | `GET` | `/api/v1/students/me/refunds` | My refund requests (Manual refunds [PAY07]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-010** | `GET` | `/api/v1/teacher/me/earnings` | My earnings summary (Teacher earnings [PAY08]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-011** | `GET` | `/api/v1/teacher/me/payouts` | My payout history (Manual payouts [PAY09]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-012** | `GET` | `/api/v1/admin/finance/summary` | Admin finance summary (Financial oversight [PAY10,ADM08]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-07-013** | `GET` | `/api/v1/admin/finance/ledger` | View financial ledger (Ledger / reconciliation [PAY10]) | Admin | Unassigned | Needs verification |
#### Module: Resources

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-08-001** | `POST` | `/api/v1/teacher/classes/{classId}/materials` | Upload learning material (File upload and validation [RES01,RES06]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-08-002** | `GET` | `/api/v1/classes/{classId}/materials` | List class materials (Protected list [RES02,RES03]) | Entitled Student / Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-08-003** | `GET` | `/api/v1/materials/{materialId}/download` | Download protected file (Secure delivery [RES02,RES03,RES06]) | Entitled Student / Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-08-004** | `PATCH` | `/api/v1/teacher/materials/{materialId}/status` | Withdraw/archive material (Material withdrawal [RES05]) | Teacher | Unassigned | Needs verification |
#### Module: XACT Source

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-09-001** | `GET` | `/api/v1/xact/catalog/papers` | List external past papers (Exam Munnodi catalogue [XQB01,XQB02]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-09-002** | `GET` | `/api/v1/xact/catalog/topics` | List source topics (Exam Munnodi topics [XQB02]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-09-003** | `GET` | `/api/v1/xact/catalog/questions` | Get eligible question previews (Question + answer adapter [XQB05,XQB06,XQB07]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-09-004** | `GET` | `/api/v1/xact/catalog/status` | Check source connectivity (External source health [XQB01,XQB10]) | Admin | Unassigned | Needs verification |
#### Module: XACT Exams

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-10-001** | `POST` | `/api/v1/xact/exams` | Create exam from eligible questions (Create past paper / mock [XPR01,XPR02,XPR03,XPR04,XPR05,XPR06]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-002** | `GET` | `/api/v1/xact/exams/{examId}` | Get exam questions (Exam questions [XPR02,XPR06]) | Exam Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-003** | `POST` | `/api/v1/xact/exams/{examId}/attempts` | Start or resume attempt (Attempt start / resume [XPR07,XPR09]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-004** | `GET` | `/api/v1/xact/attempts/{attemptId}` | Get active attempt (Attempt start / resume [XPR07,XPR09]) | Attempt Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-005** | `PUT` | `/api/v1/xact/attempts/{attemptId}/answers/{questionId}` | Save one answer (Answer autosave [XPR08]) | Attempt Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-006** | `POST` | `/api/v1/xact/attempts/{attemptId}/submit` | Submit and score attempt (Submit + score [XPR10,XPR11]) | Attempt Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-007** | `GET` | `/api/v1/xact/attempts/{attemptId}/result` | Get score and explanations (Review results [XPR12,XPR13]) | Attempt Owner | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-10-008** | `GET` | `/api/v1/xact/me/attempts` | List previous attempts (Attempt history [XPR14]) | Student | Unassigned | Needs verification |
#### Module: XACT Teacher

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-11-001** | `POST` | `/api/v1/xact/teacher/papers` | Create teacher MCQ paper (Paper authoring from external IDs [XTA02]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-11-002** | `GET` | `/api/v1/xact/teacher/papers` | List my teacher papers (Teacher papers [XTA02]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-11-003** | `GET` | `/api/v1/xact/teacher/papers/{paperId}` | View teacher paper (Teacher papers [XTA02]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-11-004** | `POST` | `/api/v1/xact/teacher/papers/{paperId}/assign` | Assign paper (Assign to multiple students [XTA05]) | Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-11-005** | `GET` | `/api/v1/xact/me/assignments` | List assigned papers (Student assignments [XTA07,XTA08]) | Student | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-11-006** | `GET` | `/api/v1/xact/teacher/assignments/{assignmentId}/results` | Get students assignment results (Assignment results [XTA09]) | Teacher | Unassigned | Needs verification |
#### Module: Notifications

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-12-001** | `GET` | `/api/v1/notifications` | List my notifications (In-app notification feed [NOT01,NOT02,NOT03,NOT04,NOT07]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-12-002** | `GET` | `/api/v1/notifications/unread-count` | Get unread count (Unread notification count [NOT07]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-12-003** | `PATCH` | `/api/v1/notifications/{notificationId}/read` | Mark notification read (Notification read status [NOT07]) | Owner | Unassigned | Needs verification |
#### Module: Admin

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-13-001** | `GET` | `/api/v1/admin/teachers/pending` | List pending teacher verifications (Teacher review [TCH02,ADM02]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-002** | `GET` | `/api/v1/admin/teachers/{teacherId}/verification` | Get teacher verification evidence (Teacher review [TCH02,ADM02]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-003** | `POST` | `/api/v1/admin/teachers/{teacherId}/decision` | Approve or reject teacher (Teacher review [TCH02,ADM02]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-004** | `PATCH` | `/api/v1/admin/teachers/{teacherId}/publication` | Set teacher publication status (Publication control [TCH07,ADM04]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-005** | `PATCH` | `/api/v1/admin/classes/{classId}/publication` | Set class publication status (Publication control [TCH07,ADM04]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-006** | `GET` | `/api/v1/admin/demos/pending` | List pending demos (Demo moderation [DEM03,ADM05]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-007** | `POST` | `/api/v1/admin/demos/{demoId}/decision` | Approve or reject demo (Demo moderation [DEM03,ADM05]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-008** | `PATCH` | `/api/v1/admin/batches/{batchId}/capacity` | Adjust batch capacity (Admin batch capacity [CLS04]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-009** | `POST` | `/api/v1/admin/refunds/{refundId}/decision` | Approve/reject refund (Refund approval (manual) [PAY07,ADM08]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-010** | `POST` | `/api/v1/admin/refunds/{refundId}/record-completion` | Record completed refund (Refund processing (manual) [PAY07,ADM08]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-011** | `POST` | `/api/v1/admin/payouts` | Record manual teacher payout (Payout processing (manual) [PAY09,ADM08]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-13-012** | `PATCH` | `/api/v1/admin/users/{userId}/status` | Change user account status (User suspension [AUTH09,ADM09]) | Admin | Unassigned | Needs verification |
#### Module: Support Safety

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-14-001** | `POST` | `/api/v1/support/cases` | Submit support or safeguarding case (Help / complaint / safety [SAFE01,SAFE02,SAFE03]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-14-002** | `GET` | `/api/v1/support/me/cases` | List my submitted cases (User case tracking [SAFE01,SAFE02]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-14-003** | `GET` | `/api/v1/admin/support/cases` | List admin support cases (Admin case queue [SAFE04]) | Admin | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-14-004** | `PATCH` | `/api/v1/admin/support/cases/{caseId}` | Update admin case (Case review / escalation [SAFE04,SAFE07]) | Admin | Unassigned | Needs verification |
#### Module: Community

| Status | API ID | Method | Endpoint | API Name / Feature | Access / Role | Assignee | Verification / PR |
|---|---|---|---|---|---|---|---|
| [ ] ⏳ Pending | **MVP-15-001** | `GET` | `/api/v1/community/posts` | List subject discussion posts (Subject forum browse [CHAT01]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-15-002** | `POST` | `/api/v1/community/posts` | Create post / question (Create discussion [CHAT03]) | Student / Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-15-003** | `GET` | `/api/v1/community/posts/{postId}/comments` | List comments (Replies / comments [CHAT04,CHAT05]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-15-004** | `POST` | `/api/v1/community/posts/{postId}/comments` | Add comment / teacher answer (Replies / comments [CHAT04,CHAT05]) | Student / Teacher | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-15-005** | `POST` | `/api/v1/community/reports` | Report content (Content reporting [CHAT06]) | Authenticated | Unassigned | Needs verification |
| [ ] ⏳ Pending | **MVP-15-006** | `PATCH` | `/api/v1/admin/community/content/{contentId}/status` | Hide or remove forum content (Admin moderation [CHAT06]) | Admin | Unassigned | Needs verification |
