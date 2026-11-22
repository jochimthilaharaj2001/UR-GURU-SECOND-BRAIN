# UR GURU — MVP API Master Index

Source: uploaded 104-endpoint MVP tracker. BRD baseline: v6.2.2. Individual endpoint metadata is copied from tracker; DTOs remain pending approval.

| ID | Module | API | Method | Route | Document |
|---|---|---|---|---|---|
| MVP-01-001 | Identity | Register student | POST | `/api/v1/auth/register/student` | [MVP-01-001](01-IDENTITY/MVP-01-001.md) |
| MVP-01-002 | Identity | Register teacher | POST | `/api/v1/auth/register/teacher` | [MVP-01-002](01-IDENTITY/MVP-01-002.md) |
| MVP-01-003 | Identity | Login | POST | `/api/v1/auth/login` | [MVP-01-003](01-IDENTITY/MVP-01-003.md) |
| MVP-01-004 | Identity | Logout | POST | `/api/v1/auth/logout` | [MVP-01-004](01-IDENTITY/MVP-01-004.md) |
| MVP-01-005 | Identity | Refresh access token | POST | `/api/v1/auth/refresh` | [MVP-01-005](01-IDENTITY/MVP-01-005.md) |
| MVP-01-006 | Identity | Request password reset | POST | `/api/v1/auth/forgot-password` | [MVP-01-006](01-IDENTITY/MVP-01-006.md) |
| MVP-01-007 | Identity | Reset password | POST | `/api/v1/auth/reset-password` | [MVP-01-007](01-IDENTITY/MVP-01-007.md) |
| MVP-01-008 | Identity | Verify contact | POST | `/api/v1/auth/verify-contact` | [MVP-01-008](01-IDENTITY/MVP-01-008.md) |
| MVP-01-009 | Identity | Resend verification | POST | `/api/v1/auth/resend-verification` | [MVP-01-009](01-IDENTITY/MVP-01-009.md) |
| MVP-01-010 | Identity | Get my identity | GET | `/api/v1/users/me` | [MVP-01-010](01-IDENTITY/MVP-01-010.md) |
| MVP-01-011 | Identity | Update my student profile | PATCH | `/api/v1/students/me/profile` | [MVP-01-011](01-IDENTITY/MVP-01-011.md) |
| MVP-01-012 | Identity | Update my teacher profile | PATCH | `/api/v1/teachers/me/profile` | [MVP-01-012](01-IDENTITY/MVP-01-012.md) |
| MVP-01-013 | Identity | Submit teacher identity evidence | POST | `/api/v1/teachers/me/identity-documents` | [MVP-01-013](01-IDENTITY/MVP-01-013.md) |
| MVP-02-001 | Curriculum | List streams | GET | `/api/v1/curriculum/streams` | [MVP-02-001](02-CURRICULUM/MVP-02-001.md) |
| MVP-02-002 | Curriculum | List eligible subjects | GET | `/api/v1/curriculum/subjects` | [MVP-02-002](02-CURRICULUM/MVP-02-002.md) |
| MVP-02-003 | Curriculum | List syllabus versions | GET | `/api/v1/curriculum/syllabuses` | [MVP-02-003](02-CURRICULUM/MVP-02-003.md) |
| MVP-02-004 | Curriculum | List syllabus topics | GET | `/api/v1/curriculum/topics` | [MVP-02-004](02-CURRICULUM/MVP-02-004.md) |
| MVP-02-005 | Curriculum | Save student academic profile | PUT | `/api/v1/students/me/academic-profile` | [MVP-02-005](02-CURRICULUM/MVP-02-005.md) |
| MVP-03-001 | Discovery | Find approved teachers | GET | `/api/v1/teachers` | [MVP-03-001](03-DISCOVERY/MVP-03-001.md) |
| MVP-03-002 | Discovery | View approved teacher | GET | `/api/v1/teachers/{teacherId}` | [MVP-03-002](03-DISCOVERY/MVP-03-002.md) |
| MVP-03-003 | Discovery | View teacher published classes | GET | `/api/v1/teachers/{teacherId}/classes` | [MVP-03-003](03-DISCOVERY/MVP-03-003.md) |
| MVP-04-001 | Classes | Create class offering | POST | `/api/v1/teacher/classes` | [MVP-04-001](04-CLASSES/MVP-04-001.md) |
| MVP-04-002 | Classes | List my class offerings | GET | `/api/v1/teacher/classes` | [MVP-04-002](04-CLASSES/MVP-04-002.md) |
| MVP-04-003 | Classes | Edit my class offering | PATCH | `/api/v1/teacher/classes/{classId}` | [MVP-04-003](04-CLASSES/MVP-04-003.md) |
| MVP-04-004 | Classes | Create batch | POST | `/api/v1/teacher/classes/{classId}/batches` | [MVP-04-004](04-CLASSES/MVP-04-004.md) |
| MVP-04-005 | Classes | Update batch / cancel | PATCH | `/api/v1/teacher/batches/{batchId}` | [MVP-04-005](04-CLASSES/MVP-04-005.md) |
| MVP-04-006 | Classes | Browse published classes | GET | `/api/v1/classes` | [MVP-04-006](04-CLASSES/MVP-04-006.md) |
| MVP-04-007 | Classes | Get class details | GET | `/api/v1/classes/{classId}` | [MVP-04-007](04-CLASSES/MVP-04-007.md) |
| MVP-04-008 | Classes | List class batches and availability | GET | `/api/v1/classes/{classId}/batches` | [MVP-04-008](04-CLASSES/MVP-04-008.md) |
| MVP-04-009 | Classes | Get batch and calculated fee | GET | `/api/v1/batches/{batchId}` | [MVP-04-009](04-CLASSES/MVP-04-009.md) |
| MVP-04-010 | Classes | List my enrollments | GET | `/api/v1/students/me/enrollments` | [MVP-04-010](04-CLASSES/MVP-04-010.md) |
| MVP-04-011 | Classes | List students in my batch | GET | `/api/v1/teacher/batches/{batchId}/students` | [MVP-04-011](04-CLASSES/MVP-04-011.md) |
| MVP-04-012 | Classes | Reschedule batch | POST | `/api/v1/teacher/batches/{batchId}/reschedule` | [MVP-04-012](04-CLASSES/MVP-04-012.md) |
| MVP-05-001 | Demo Videos | Create demo upload | POST | `/api/v1/teacher/classes/{classId}/demos` | [MVP-05-001](05-DEMO-VIDEOS/MVP-05-001.md) |
| MVP-05-002 | Demo Videos | Complete demo upload | POST | `/api/v1/teacher/demos/{demoId}/complete-upload` | [MVP-05-002](05-DEMO-VIDEOS/MVP-05-002.md) |
| MVP-05-003 | Demo Videos | List approved demos | GET | `/api/v1/classes/{classId}/demos` | [MVP-05-003](05-DEMO-VIDEOS/MVP-05-003.md) |
| MVP-05-004 | Demo Videos | Get free demo playback | GET | `/api/v1/demos/{demoId}/playback` | [MVP-05-004](05-DEMO-VIDEOS/MVP-05-004.md) |
| MVP-06-001 | Live Classes | Schedule live class | POST | `/api/v1/teacher/batches/{batchId}/sessions` | [MVP-06-001](06-LIVE-CLASSES/MVP-06-001.md) |
| MVP-06-002 | Live Classes | List batch sessions | GET | `/api/v1/batches/{batchId}/sessions` | [MVP-06-002](06-LIVE-CLASSES/MVP-06-002.md) |
| MVP-06-003 | Live Classes | Update / reschedule session | PATCH | `/api/v1/teacher/sessions/{sessionId}` | [MVP-06-003](06-LIVE-CLASSES/MVP-06-003.md) |
| MVP-06-004 | Live Classes | Cancel session | POST | `/api/v1/teacher/sessions/{sessionId}/cancel` | [MVP-06-004](06-LIVE-CLASSES/MVP-06-004.md) |
| MVP-06-005 | Live Classes | Issue secure live join credentials | POST | `/api/v1/sessions/{sessionId}/join` | [MVP-06-005](06-LIVE-CLASSES/MVP-06-005.md) |
| MVP-06-006 | Live Classes | Receive authenticated provider events | POST | `/api/v1/live/provider/events` | [MVP-06-006](06-LIVE-CLASSES/MVP-06-006.md) |
| MVP-06-007 | Live Classes | Get teacher attendance | GET | `/api/v1/teacher/sessions/{sessionId}/attendance` | [MVP-06-007](06-LIVE-CLASSES/MVP-06-007.md) |
| MVP-07-001 | Payments | Create checkout order | POST | `/api/v1/checkout/orders` | [MVP-07-001](07-PAYMENTS/MVP-07-001.md) |
| MVP-07-002 | Payments | Get order checkout details | GET | `/api/v1/checkout/orders/{orderId}` | [MVP-07-002](07-PAYMENTS/MVP-07-002.md) |
| MVP-07-003 | Payments | Initiate gateway payment | POST | `/api/v1/payments/{orderId}/initiate` | [MVP-07-003](07-PAYMENTS/MVP-07-003.md) |
| MVP-07-004 | Payments | Receive verified gateway webhook | POST | `/api/v1/payments/gateway/webhook` | [MVP-07-004](07-PAYMENTS/MVP-07-004.md) |
| MVP-07-005 | Payments | Get payment status | GET | `/api/v1/payments/{paymentId}/status` | [MVP-07-005](07-PAYMENTS/MVP-07-005.md) |
| MVP-07-006 | Payments | My payment history | GET | `/api/v1/students/me/payments` | [MVP-07-006](07-PAYMENTS/MVP-07-006.md) |
| MVP-07-007 | Payments | View payment receipt | GET | `/api/v1/payments/{paymentId}/receipt` | [MVP-07-007](07-PAYMENTS/MVP-07-007.md) |
| MVP-07-008 | Payments | Request manual refund | POST | `/api/v1/refunds` | [MVP-07-008](07-PAYMENTS/MVP-07-008.md) |
| MVP-07-009 | Payments | My refund requests | GET | `/api/v1/students/me/refunds` | [MVP-07-009](07-PAYMENTS/MVP-07-009.md) |
| MVP-07-010 | Payments | My earnings summary | GET | `/api/v1/teacher/me/earnings` | [MVP-07-010](07-PAYMENTS/MVP-07-010.md) |
| MVP-07-011 | Payments | My payout history | GET | `/api/v1/teacher/me/payouts` | [MVP-07-011](07-PAYMENTS/MVP-07-011.md) |
| MVP-07-012 | Payments | Admin finance summary | GET | `/api/v1/admin/finance/summary` | [MVP-07-012](07-PAYMENTS/MVP-07-012.md) |
| MVP-07-013 | Payments | View financial ledger | GET | `/api/v1/admin/finance/ledger` | [MVP-07-013](07-PAYMENTS/MVP-07-013.md) |
| MVP-08-001 | Resources | Upload learning material | POST | `/api/v1/teacher/classes/{classId}/materials` | [MVP-08-001](08-RESOURCES/MVP-08-001.md) |
| MVP-08-002 | Resources | List class materials | GET | `/api/v1/classes/{classId}/materials` | [MVP-08-002](08-RESOURCES/MVP-08-002.md) |
| MVP-08-003 | Resources | Download protected file | GET | `/api/v1/materials/{materialId}/download` | [MVP-08-003](08-RESOURCES/MVP-08-003.md) |
| MVP-08-004 | Resources | Withdraw/archive material | PATCH | `/api/v1/teacher/materials/{materialId}/status` | [MVP-08-004](08-RESOURCES/MVP-08-004.md) |
| MVP-09-001 | XACT Source | List external past papers | GET | `/api/v1/xact/catalog/papers` | [MVP-09-001](09-XACT-SOURCE/MVP-09-001.md) |
| MVP-09-002 | XACT Source | List source topics | GET | `/api/v1/xact/catalog/topics` | [MVP-09-002](09-XACT-SOURCE/MVP-09-002.md) |
| MVP-09-003 | XACT Source | Get eligible question previews | GET | `/api/v1/xact/catalog/questions` | [MVP-09-003](09-XACT-SOURCE/MVP-09-003.md) |
| MVP-09-004 | XACT Source | Check source connectivity | GET | `/api/v1/xact/catalog/status` | [MVP-09-004](09-XACT-SOURCE/MVP-09-004.md) |
| MVP-10-001 | XACT Exams | Create exam from eligible questions | POST | `/api/v1/xact/exams` | [MVP-10-001](10-XACT-EXAMS/MVP-10-001.md) |
| MVP-10-002 | XACT Exams | Get exam questions | GET | `/api/v1/xact/exams/{examId}` | [MVP-10-002](10-XACT-EXAMS/MVP-10-002.md) |
| MVP-10-003 | XACT Exams | Start or resume attempt | POST | `/api/v1/xact/exams/{examId}/attempts` | [MVP-10-003](10-XACT-EXAMS/MVP-10-003.md) |
| MVP-10-004 | XACT Exams | Get active attempt | GET | `/api/v1/xact/attempts/{attemptId}` | [MVP-10-004](10-XACT-EXAMS/MVP-10-004.md) |
| MVP-10-005 | XACT Exams | Save one answer | PUT | `/api/v1/xact/attempts/{attemptId}/answers/{questionId}` | [MVP-10-005](10-XACT-EXAMS/MVP-10-005.md) |
| MVP-10-006 | XACT Exams | Submit and score attempt | POST | `/api/v1/xact/attempts/{attemptId}/submit` | [MVP-10-006](10-XACT-EXAMS/MVP-10-006.md) |
| MVP-10-007 | XACT Exams | Get score and explanations | GET | `/api/v1/xact/attempts/{attemptId}/result` | [MVP-10-007](10-XACT-EXAMS/MVP-10-007.md) |
| MVP-10-008 | XACT Exams | List previous attempts | GET | `/api/v1/xact/me/attempts` | [MVP-10-008](10-XACT-EXAMS/MVP-10-008.md) |
| MVP-11-001 | XACT Teacher | Create teacher MCQ paper | POST | `/api/v1/xact/teacher/papers` | [MVP-11-001](11-XACT-TEACHER/MVP-11-001.md) |
| MVP-11-002 | XACT Teacher | List my teacher papers | GET | `/api/v1/xact/teacher/papers` | [MVP-11-002](11-XACT-TEACHER/MVP-11-002.md) |
| MVP-11-003 | XACT Teacher | View teacher paper | GET | `/api/v1/xact/teacher/papers/{paperId}` | [MVP-11-003](11-XACT-TEACHER/MVP-11-003.md) |
| MVP-11-004 | XACT Teacher | Assign paper | POST | `/api/v1/xact/teacher/papers/{paperId}/assign` | [MVP-11-004](11-XACT-TEACHER/MVP-11-004.md) |
| MVP-11-005 | XACT Teacher | List assigned papers | GET | `/api/v1/xact/me/assignments` | [MVP-11-005](11-XACT-TEACHER/MVP-11-005.md) |
| MVP-11-006 | XACT Teacher | Get students assignment results | GET | `/api/v1/xact/teacher/assignments/{assignmentId}/results` | [MVP-11-006](11-XACT-TEACHER/MVP-11-006.md) |
| MVP-12-001 | Notifications | List my notifications | GET | `/api/v1/notifications` | [MVP-12-001](12-NOTIFICATIONS/MVP-12-001.md) |
| MVP-12-002 | Notifications | Get unread count | GET | `/api/v1/notifications/unread-count` | [MVP-12-002](12-NOTIFICATIONS/MVP-12-002.md) |
| MVP-12-003 | Notifications | Mark notification read | PATCH | `/api/v1/notifications/{notificationId}/read` | [MVP-12-003](12-NOTIFICATIONS/MVP-12-003.md) |
| MVP-13-001 | Admin | List pending teacher verifications | GET | `/api/v1/admin/teachers/pending` | [MVP-13-001](13-ADMIN/MVP-13-001.md) |
| MVP-13-002 | Admin | Get teacher verification evidence | GET | `/api/v1/admin/teachers/{teacherId}/verification` | [MVP-13-002](13-ADMIN/MVP-13-002.md) |
| MVP-13-003 | Admin | Approve or reject teacher | POST | `/api/v1/admin/teachers/{teacherId}/decision` | [MVP-13-003](13-ADMIN/MVP-13-003.md) |
| MVP-13-004 | Admin | Set teacher publication status | PATCH | `/api/v1/admin/teachers/{teacherId}/publication` | [MVP-13-004](13-ADMIN/MVP-13-004.md) |
| MVP-13-005 | Admin | Set class publication status | PATCH | `/api/v1/admin/classes/{classId}/publication` | [MVP-13-005](13-ADMIN/MVP-13-005.md) |
| MVP-13-006 | Admin | List pending demos | GET | `/api/v1/admin/demos/pending` | [MVP-13-006](13-ADMIN/MVP-13-006.md) |
| MVP-13-007 | Admin | Approve or reject demo | POST | `/api/v1/admin/demos/{demoId}/decision` | [MVP-13-007](13-ADMIN/MVP-13-007.md) |
| MVP-13-008 | Admin | Adjust batch capacity | PATCH | `/api/v1/admin/batches/{batchId}/capacity` | [MVP-13-008](13-ADMIN/MVP-13-008.md) |
| MVP-13-009 | Admin | Approve/reject refund | POST | `/api/v1/admin/refunds/{refundId}/decision` | [MVP-13-009](13-ADMIN/MVP-13-009.md) |
| MVP-13-010 | Admin | Record completed refund | POST | `/api/v1/admin/refunds/{refundId}/record-completion` | [MVP-13-010](13-ADMIN/MVP-13-010.md) |
| MVP-13-011 | Admin | Record manual teacher payout | POST | `/api/v1/admin/payouts` | [MVP-13-011](13-ADMIN/MVP-13-011.md) |
| MVP-13-012 | Admin | Change user account status | PATCH | `/api/v1/admin/users/{userId}/status` | [MVP-13-012](13-ADMIN/MVP-13-012.md) |
| MVP-14-001 | Support Safety | Submit support or safeguarding case | POST | `/api/v1/support/cases` | [MVP-14-001](14-SUPPORT-SAFETY/MVP-14-001.md) |
| MVP-14-002 | Support Safety | List my submitted cases | GET | `/api/v1/support/me/cases` | [MVP-14-002](14-SUPPORT-SAFETY/MVP-14-002.md) |
| MVP-14-003 | Support Safety | List admin support cases | GET | `/api/v1/admin/support/cases` | [MVP-14-003](14-SUPPORT-SAFETY/MVP-14-003.md) |
| MVP-14-004 | Support Safety | Update admin case | PATCH | `/api/v1/admin/support/cases/{caseId}` | [MVP-14-004](14-SUPPORT-SAFETY/MVP-14-004.md) |
| MVP-15-001 | Community | List subject discussion posts | GET | `/api/v1/community/posts` | [MVP-15-001](15-COMMUNITY/MVP-15-001.md) |
| MVP-15-002 | Community | Create post / question | POST | `/api/v1/community/posts` | [MVP-15-002](15-COMMUNITY/MVP-15-002.md) |
| MVP-15-003 | Community | List comments | GET | `/api/v1/community/posts/{postId}/comments` | [MVP-15-003](15-COMMUNITY/MVP-15-003.md) |
| MVP-15-004 | Community | Add comment / teacher answer | POST | `/api/v1/community/posts/{postId}/comments` | [MVP-15-004](15-COMMUNITY/MVP-15-004.md) |
| MVP-15-005 | Community | Report content | POST | `/api/v1/community/reports` | [MVP-15-005](15-COMMUNITY/MVP-15-005.md) |
| MVP-15-006 | Community | Hide or remove forum content | PATCH | `/api/v1/admin/community/content/{contentId}/status` | [MVP-15-006](15-COMMUNITY/MVP-15-006.md) |
