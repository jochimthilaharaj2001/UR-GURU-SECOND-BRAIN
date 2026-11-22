# UR GURU — Post-MVP Current API Index

**Source:** `Post MVP Current` worksheet; 177 endpoints. These are **not** in the selected MVP set. Fields are copied from the workbook; this index does not approve implementation.

| API ID | Module | API name | Method | Endpoint | Role | BRD |
|---|---|---|---|---|---|---|
| IDE-006 | Identity | Log out all devices | POST | /api/v1/auth/logout-all | Authenticated | BR-01, BR-22 |
| IDE-007 | Identity | List active sessions | GET | /api/v1/auth/sessions | Authenticated | BR-01, BR-22 |
| IDE-008 | Identity | Revoke session | DELETE | /api/v1/auth/sessions/{sessionId} | Authenticated | BR-01, BR-22 |
| IDE-011 | Identity | Send phone verification code | POST | /api/v1/auth/phone/verification/send | Public | BR-01, BR-22 |
| IDE-012 | Identity | Confirm phone | POST | /api/v1/auth/phone/verification/confirm | Public | BR-01, BR-22 |
| IDE-021 | Identity | Disable MFA | DELETE | /api/v1/auth/mfa | Authenticated | BR-01, BR-22 |
| IDE-022 | Identity | Rotate MFA recovery codes | POST | /api/v1/auth/mfa/recovery-codes/rotate | Authenticated | BR-01, BR-22 |
| IDE-026 | Identity | List role definitions | GET | /api/v1/admin/roles | Admin | BR-01, BR-22 |
| IDE-029 | Identity | Review user sessions | GET | /api/v1/admin/users/{userId}/sessions | Admin | BR-01, BR-22 |
| IDE-030 | Identity | Revoke all user sessions | POST | /api/v1/admin/users/{userId}/sessions/revoke | Admin | BR-01, BR-22 |
| PRO-005 | Profiles | Get learning preferences | GET | /api/v1/students/me/learning-preferences | Student | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-006 | Profiles | Save learning preferences | PUT | /api/v1/students/me/learning-preferences | Student | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-011 | Profiles | Remove requested teaching subject | DELETE | /api/v1/teachers/me/subjects/{teacherSubjectId} | Teacher | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-016 | Profiles | Resubmit teacher verification | POST | /api/v1/teachers/me/verification/resubmit | Teacher | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-019 | Profiles | Get public teaching subjects | GET | /api/v1/teachers/{teacherId}/subjects | Public | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-021 | Profiles | Get teacher availability | GET | /api/v1/teachers/{teacherId}/availability | Public | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-028 | Profiles | Reinstate teacher | POST | /api/v1/admin/teachers/{teacherId}/reinstate | Admin | BR-01, BR-02, BR-03, BR-21, BR-22 |
| PRO-029 | Profiles | Read verification history | GET | /api/v1/admin/teachers/{teacherId}/verification/history | Admin | BR-01, BR-02, BR-03, BR-21, BR-22 |
| CAT-002 | Catalog | Get stream detail | GET | /api/v1/catalog/streams/{streamId} | Public | BR-01, BR-23 |
| CAT-005 | Catalog | Get subject detail | GET | /api/v1/catalog/subjects/{subjectId} | Public | BR-01, BR-23 |
| CAT-009 | Catalog | Get topic | GET | /api/v1/catalog/topics/{topicId} | Public | BR-01, BR-23 |
| CAT-010 | Catalog | List subtopics | GET | /api/v1/catalog/topics/{topicId}/children | Public | BR-01, BR-23 |
| CAT-013 | Catalog | List all streams | GET | /api/v1/admin/catalog/streams | Admin | BR-01, BR-23 |
| CAT-014 | Catalog | Create stream | POST | /api/v1/admin/catalog/streams | Admin | BR-01, BR-23 |
| CAT-015 | Catalog | Update stream | PATCH | /api/v1/admin/catalog/streams/{streamId} | Admin | BR-01, BR-23 |
| CAT-018 | Catalog | Update stream-subject mappings | PUT | /api/v1/admin/catalog/streams/{streamId}/subjects | Admin | BR-01, BR-23 |
| CAT-020 | Catalog | Update syllabus | PATCH | /api/v1/admin/catalog/syllabi/{syllabusId} | Admin | BR-01, BR-23 |
| CAT-022 | Catalog | Update topic | PATCH | /api/v1/admin/catalog/topics/{topicId} | Admin | BR-01, BR-23 |
| CAT-024 | Catalog | Update catalogue translation | PATCH | /api/v1/admin/catalog/translations/{translationId} | Admin | BR-01, BR-23 |
| CAT-025 | Catalog | Get curriculum coverage dashboard | GET | /api/v1/admin/catalog/coverage | Admin | BR-01, BR-23 |
| CLA-012 | Classes | Unpublish class | POST | /api/v1/teachers/me/classes/{classId}/unpublish | Teacher | BR-03, BR-04, BR-05 |
| CLA-013 | Classes | Archive class | POST | /api/v1/teachers/me/classes/{classId}/archive | Teacher | BR-03, BR-04, BR-05 |
| CLA-017 | Classes | Modify recurring schedule | PATCH | /api/v1/teachers/me/batches/{batchId}/schedule/{scheduleId} | Teacher | BR-03, BR-04, BR-05 |
| CLA-018 | Classes | Remove schedule slot | DELETE | /api/v1/teachers/me/batches/{batchId}/schedule/{scheduleId} | Teacher | BR-03, BR-04, BR-05 |
| CLA-022 | Classes | List teacher demo submissions | GET | /api/v1/teachers/me/demos | Teacher | BR-04 |
| CLA-031 | Classes | Release checkout seat | DELETE | /api/v1/seat-holds/{holdId} | Student | BR-03, BR-04, BR-05 |
| CLA-035 | Classes | Suspend enrollment access | POST | /api/v1/admin/enrollments/{enrollmentId}/suspend | Admin | BR-03, BR-04, BR-05 |
| CLA-036 | Classes | Restore enrollment | POST | /api/v1/admin/enrollments/{enrollmentId}/restore | Admin | BR-03, BR-04, BR-05 |
| CLA-040 | Classes | Admin attendance review | GET | /api/v1/admin/sessions/{sessionId}/attendance | Admin | BR-03, BR-04, BR-05 |
| CLA-041 | Classes | Admin attendance correction | POST | /api/v1/admin/attendance/{attendanceId}/correct | Admin | BR-03, BR-04, BR-05 |
| CLA-045 | Classes | Admin enrollment list | GET | /api/v1/admin/enrollments | Admin | BR-03, BR-04, BR-05 |
| CLA-046 | Classes | Review seat holds | GET | /api/v1/admin/seat-holds | Admin | BR-03, BR-04, BR-05 |
| CLA-047 | Classes | Force release seat hold | POST | /api/v1/admin/seat-holds/{holdId}/release | Admin | BR-03, BR-04, BR-05 |
| LIV-002 | LiveSessions | List my past sessions | GET | /api/v1/sessions/me/history | Student | BR-05 |
| LIV-005 | LiveSessions | Record voluntary leave | POST | /api/v1/sessions/{sessionId}/leave | Student | BR-05 |
| LIV-009 | LiveSessions | Update session metadata | PATCH | /api/v1/teachers/me/sessions/{sessionId} | Teacher | BR-05 |
| LIV-015 | LiveSessions | List participants | GET | /api/v1/teachers/me/sessions/{sessionId}/participants | Teacher | BR-05 |
| LIV-017 | LiveSessions | Admin session operations | GET | /api/v1/admin/sessions | Admin | BR-05 |
| LIV-018 | LiveSessions | Get provider event history | GET | /api/v1/admin/sessions/{sessionId}/events | Admin | BR-05 |
| LEA-004 | LearningResources | Get accessible resource versions | GET | /api/v1/resources/{resourceId}/versions | Student | BR-07, BR-08, BR-09, BR-17 |
| LEA-006 | LearningResources | Report resource concern | POST | /api/v1/resources/{resourceId}/report | Student | BR-07, BR-08, BR-09, BR-17 |
| LEA-009 | LearningResources | Get resource details | GET | /api/v1/teachers/me/resources/{resourceId} | Teacher | BR-07, BR-08, BR-09, BR-17 |
| LEA-010 | LearningResources | Update resource metadata | PATCH | /api/v1/teachers/me/resources/{resourceId} | Teacher | BR-07, BR-08, BR-09, BR-17 |
| LEA-015 | LearningResources | Restore previous resource version | POST | /api/v1/teachers/me/resources/{resourceId}/versions/{versionId}/restore | Teacher | BR-07, BR-08, BR-09, BR-17 |
| LEA-017 | LearningResources | Inspect resource history | GET | /api/v1/admin/resources/{resourceId} | Admin | BR-07, BR-08, BR-09, BR-17 |
| LEA-020 | LearningResources | Restore resource | POST | /api/v1/admin/resources/{resourceId}/restore | Admin | BR-07, BR-08, BR-09, BR-17 |
| LEA-021 | LearningResources | View access audit | GET | /api/v1/admin/resources/{resourceId}/access-log | Admin | BR-07, BR-08, BR-09, BR-17 |
| QUE-012 | QuestionBank | Withdraw source rights | POST | /api/v1/admin/xact/paper-sources/{sourceId}/withdraw | Admin | BR-18, BR-23 |
| QUE-013 | QuestionBank | Start question import | POST | /api/v1/admin/xact/imports | Academic Reviewer / Admin | BR-18, BR-23 |
| QUE-014 | QuestionBank | List import jobs | GET | /api/v1/admin/xact/imports | Academic Reviewer / Admin | BR-18, BR-23 |
| QUE-015 | QuestionBank | Get import validation report | GET | /api/v1/admin/xact/imports/{importId} | Academic Reviewer / Admin | BR-18, BR-23 |
| QUE-016 | QuestionBank | Commit validated import | POST | /api/v1/admin/xact/imports/{importId}/commit | Academic Reviewer / Admin | BR-18, BR-23 |
| QUE-017 | QuestionBank | Cancel import job | POST | /api/v1/admin/xact/imports/{importId}/cancel | Academic Reviewer / Admin | BR-18, BR-23 |
| QUE-022 | QuestionBank | Add canonical option | POST | /api/v1/admin/xact/questions/{questionId}/options | Academic Reviewer | BR-18, BR-23 |
| QUE-023 | QuestionBank | Update canonical option | PATCH | /api/v1/admin/xact/questions/{questionId}/options/{optionId} | Academic Reviewer | BR-18, BR-23 |
| QUE-025 | QuestionBank | List question translations | GET | /api/v1/admin/xact/questions/{questionId}/translations | Academic Reviewer | BR-18, BR-23 |
| QUE-026 | QuestionBank | Get translation version | GET | /api/v1/admin/xact/translations/{translationId} | Academic Reviewer | BR-18, BR-23 |
| QUE-030 | QuestionBank | Request translation changes | POST | /api/v1/admin/xact/translations/{translationId}/request-changes | Academic Reviewer | BR-18, BR-23 |
| QUE-031 | QuestionBank | Reject translation | POST | /api/v1/admin/xact/translations/{translationId}/reject | Academic Reviewer | BR-18, BR-23 |
| QUE-032 | QuestionBank | Withdraw translation | POST | /api/v1/admin/xact/translations/{translationId}/withdraw | Academic Reviewer | BR-18, BR-23 |
| QUE-036 | QuestionBank | Revoke invalid answer key | POST | /api/v1/admin/xact/answer-keys/{keyVersionId}/revoke | Academic Reviewer | BR-18, BR-23 |
| QUE-037 | QuestionBank | List explanation versions | GET | /api/v1/admin/xact/translations/{translationId}/explanations | Academic Reviewer | BR-18, BR-23 |
| QUE-039 | QuestionBank | Update explanation draft | PATCH | /api/v1/admin/xact/explanations/{explanationId} | Academic Reviewer | BR-18, BR-23 |
| QUE-041 | QuestionBank | Withdraw explanation | POST | /api/v1/admin/xact/explanations/{explanationId}/withdraw | Academic Reviewer | BR-18, BR-23 |
| QUE-042 | QuestionBank | List pending corrections | GET | /api/v1/admin/xact/corrections | Academic Reviewer | BR-18, BR-23 |
| QUE-045 | QuestionBank | Get question coverage matrix | GET | /api/v1/admin/xact/coverage | Academic Reviewer | BR-18, BR-23 |
| ASS-002 | Assessment | Get mock preset | GET | /api/v1/xact/mock-presets/{presetId} | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-003 | Assessment | Preview mock configuration | POST | /api/v1/xact/mocks/preview | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-005 | Assessment | List my mocks | GET | /api/v1/xact/mocks/me | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-006 | Assessment | Get own mock detail | GET | /api/v1/xact/mocks/{mockId} | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-013 | Assessment | Clear saved answer | DELETE | /api/v1/xact/attempts/{attemptId}/answers/{itemId} | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-020 | Assessment | Get attempt history | GET | /api/v1/xact/attempts/{attemptId}/timeline | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-021 | Assessment | List my XACT results | GET | /api/v1/xact/results/me | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-023 | Assessment | Get subject performance | GET | /api/v1/xact/analytics/me/subjects | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-025 | Assessment | Get difficulty breakdown | GET | /api/v1/xact/analytics/me/difficulty | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-026 | Assessment | Get progress history | GET | /api/v1/xact/analytics/me/history | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-027 | Assessment | Get rules-based practice suggestions | GET | /api/v1/xact/analytics/me/recommendations | Student | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-033 | Assessment | Update paper item | PATCH | /api/v1/teachers/me/xact/papers/{paperId}/items/{itemId} | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-035 | Assessment | Reorder paper questions | PUT | /api/v1/teachers/me/xact/papers/{paperId}/items/order | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-038 | Assessment | List paper versions | GET | /api/v1/teachers/me/xact/papers/{paperId}/versions | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-039 | Assessment | Duplicate paper to draft | POST | /api/v1/teachers/me/xact/papers/{paperId}/duplicate | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-040 | Assessment | Archive teacher paper | POST | /api/v1/teachers/me/xact/papers/{paperId}/archive | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-044 | Assessment | Update unstarted assignment | PATCH | /api/v1/teachers/me/xact/assignments/{assignmentId} | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-045 | Assessment | Add assignment recipients | POST | /api/v1/teachers/me/xact/assignments/{assignmentId}/recipients | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-046 | Assessment | Remove recipient | DELETE | /api/v1/teachers/me/xact/assignments/{assignmentId}/recipients/{recipientId} | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-047 | Assessment | Close teacher assignment | POST | /api/v1/teachers/me/xact/assignments/{assignmentId}/close | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-048 | Assessment | Extend assignment deadline | POST | /api/v1/teachers/me/xact/assignments/{assignmentId}/extend | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-051 | Assessment | Review student submission | GET | /api/v1/teachers/me/xact/assignments/{assignmentId}/students/{studentId}/result | Teacher | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-062 | Assessment | List regrade cases | GET | /api/v1/admin/xact/regrades | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-063 | Assessment | Create regrade batch | POST | /api/v1/admin/xact/regrades | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-064 | Assessment | Approve regrade batch | POST | /api/v1/admin/xact/regrades/{batchId}/approve | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-065 | Assessment | Get regrade outcomes | GET | /api/v1/admin/xact/regrades/{batchId}/results | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-066 | Assessment | Review assignments | GET | /api/v1/admin/xact/assignments | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| ASS-067 | Assessment | Suspend assignment | POST | /api/v1/admin/xact/assignments/{assignmentId}/suspend | Admin / Academic Reviewer | BR-11, BR-18, BR-19, BR-10, BR-12 |
| MED-004 | Media | Cancel pending upload | POST | /api/v1/media/uploads/{uploadId}/cancel | Teacher | BR-04, BR-20 |
| MED-007 | Media | List media subtitle tracks | GET | /api/v1/media/{mediaId}/subtitles | Student | BR-04, BR-20 |
| MED-009 | Media | List my explanation videos | GET | /api/v1/teachers/me/xact/videos | Teacher | BR-04, BR-20 |
| MED-014 | Media | Withdraw own video | POST | /api/v1/teachers/me/xact/videos/{videoId}/withdraw | Teacher | BR-04, BR-20 |
| MED-015 | Media | Submit revised video media | POST | /api/v1/teachers/me/xact/videos/{videoId}/replace | Teacher | BR-04, BR-20 |
| MED-017 | Media | Inspect video review | GET | /api/v1/admin/xact/videos/{videoId} | Academic Reviewer | BR-04, BR-20 |
| MED-019 | Media | Request video corrections | POST | /api/v1/admin/xact/videos/{videoId}/request-changes | Academic Reviewer | BR-04, BR-20 |
| MED-020 | Media | Reject video | POST | /api/v1/admin/xact/videos/{videoId}/reject | Academic Reviewer | BR-04, BR-20 |
| MED-023 | Media | List media processing exceptions | GET | /api/v1/admin/media/processing-failures | Academic Reviewer | BR-04, BR-20 |
| MED-024 | Media | Retry media processing | POST | /api/v1/admin/media/{mediaId}/retry-processing | Academic Reviewer | BR-04, BR-20 |
| COM-007 | Commerce | Cancel unpaid order | POST | /api/v1/commerce/orders/{orderId}/cancel | Student | BR-06 |
| COM-015 | Commerce | Retire offer | POST | /api/v1/admin/commerce/offers/{offerId}/retire | Admin / Finance | BR-06 |
| COM-018 | Commerce | Search payment attempts | GET | /api/v1/admin/commerce/payment-attempts | Admin / Finance | BR-06 |
| COM-019 | Commerce | Inspect payment attempt | GET | /api/v1/admin/commerce/payment-attempts/{attemptId} | Admin / Finance | BR-06 |
| COM-023 | Commerce | List gateway webhook events | GET | /api/v1/admin/commerce/webhooks | Finance | BR-06 |
| COM-024 | Commerce | Inspect payment webhook | GET | /api/v1/admin/commerce/webhooks/{eventId} | Finance | BR-06 |
| COM-025 | Commerce | Reprocess safe webhook | POST | /api/v1/admin/commerce/webhooks/{eventId}/reprocess | Finance | BR-06 |
| COM-026 | Commerce | Re-query provider payment | POST | /api/v1/admin/commerce/payments/{attemptId}/verify | Finance | BR-06 |
| COM-028 | Commerce | Start reconciliation run | POST | /api/v1/admin/commerce/reconciliation/run | Finance | BR-06 |
| COM-029 | Commerce | Get reconciliation result | GET | /api/v1/admin/commerce/reconciliation/{runId} | Finance | BR-06 |
| COM-033 | Commerce | List my refunds | GET | /api/v1/refunds/me | Student | BR-06 |
| COM-034 | Commerce | Get refund detail | GET | /api/v1/refunds/{refundId} | Student | BR-06 |
| COM-040 | Commerce | Retry failed refund | POST | /api/v1/admin/refunds/{refundId}/retry | Finance | BR-06 |
| COM-042 | Commerce | Get ledger posting detail | GET | /api/v1/admin/ledger/transactions/{transactionId} | Finance | BR-06 |
| COM-043 | Commerce | Request correcting ledger transaction | POST | /api/v1/admin/ledger/adjustments | Finance | BR-06 |
| COM-044 | Commerce | Search payment disputes | GET | /api/v1/admin/commerce/disputes | Finance | BR-06 |
| COM-045 | Commerce | Resolve dispute | POST | /api/v1/admin/commerce/disputes/{disputeId}/resolve | Finance | BR-06 |
| PAY-004 | Payouts | Get payout detail | GET | /api/v1/teachers/me/payouts/{payoutId} | Teacher | BR-06 |
| PAY-010 | Payouts | Hold teacher settlements | POST | /api/v1/admin/payouts/payees/{teacherId}/hold | Finance | BR-06 |
| PAY-011 | Payouts | Release settlement hold | POST | /api/v1/admin/payouts/payees/{teacherId}/release | Finance | BR-06 |
| PAY-013 | Payouts | Create earning adjustment | POST | /api/v1/admin/payouts/earnings/{earningId}/adjust | Finance | BR-06 |
| PAY-020 | Payouts | Cancel draft batch | POST | /api/v1/admin/payouts/batches/{batchId}/cancel | Finance | BR-06 |
| PAY-025 | Payouts | Run settlement reconciliation | POST | /api/v1/admin/payouts/reconciliation/run | Finance | BR-06 |
| NOT-002 | Notifications | Get unread notification count | GET | /api/v1/notifications/me/unread-count | Authenticated | BR-13 |
| NOT-003 | Notifications | Get notification detail | GET | /api/v1/notifications/{notificationId} | Authenticated | BR-13 |
| NOT-005 | Notifications | Mark all notifications read | POST | /api/v1/notifications/me/read-all | Authenticated | BR-13 |
| NOT-006 | Notifications | Dismiss notification | DELETE | /api/v1/notifications/{notificationId} | Authenticated | BR-13 |
| NOT-009 | Notifications | List message templates | GET | /api/v1/admin/notifications/templates | Admin | BR-13 |
| NOT-010 | Notifications | Create notification template | POST | /api/v1/admin/notifications/templates | Admin | BR-13 |
| NOT-011 | Notifications | Update notification template | PATCH | /api/v1/admin/notifications/templates/{templateId} | Admin | BR-13 |
| NOT-012 | Notifications | Publish notification template | POST | /api/v1/admin/notifications/templates/{templateId}/publish | Admin | BR-13 |
| NOT-014 | Notifications | Get delivery attempt | GET | /api/v1/admin/notifications/deliveries/{deliveryId} | Admin | BR-13 |
| NOT-016 | Notifications | Send test notification | POST | /api/v1/admin/notifications/test | Admin | BR-13 |
| NOT-017 | Notifications | Register browser push subscription | POST | /api/v1/notifications/push-subscriptions | Authenticated | BR-13 |
| NOT-018 | Notifications | Remove push subscription | DELETE | /api/v1/notifications/push-subscriptions/{subscriptionId} | Authenticated | BR-13 |
| NOT-019 | Notifications | List push subscriptions | GET | /api/v1/notifications/push-subscriptions/me | Authenticated | BR-13 |
| SAF-015 | Safeguarding | Initiate safety evidence upload | POST | /api/v1/safety-reports/{reportId}/evidence/upload-init | Authenticated | BR-21, BR-22, BR-24, BR-15 |
| SAF-016 | Safeguarding | Attach safety evidence | POST | /api/v1/safety-reports/{reportId}/evidence/complete | Authenticated | BR-21, BR-22, BR-24, BR-15 |
| SAF-023 | Safeguarding | Assign safeguarding reviewer | POST | /api/v1/admin/safety-reports/{reportId}/assign | Safeguarding Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-026 | Safeguarding | Record safety case event | POST | /api/v1/admin/safety-reports/{reportId}/events | Safeguarding Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-028 | Safeguarding | Review consent records | GET | /api/v1/admin/consents | Safeguarding Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-029 | Safeguarding | Inspect consent evidence | GET | /api/v1/admin/consents/{consentId} | Safeguarding Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-030 | Safeguarding | Review guardian verification exceptions | GET | /api/v1/admin/guardians/verification-queue | Safeguarding Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-032 | Safeguarding | Assign support case | POST | /api/v1/admin/support/tickets/{ticketId}/assign | Support Admin | BR-21, BR-22, BR-24, BR-15 |
| SAF-036 | Safeguarding | List my privacy requests | GET | /api/v1/privacy/requests/me | Authenticated | BR-21, BR-22, BR-24, BR-15 |
| SAF-038 | Safeguarding | Inspect privacy request | GET | /api/v1/admin/privacy/requests/{requestId} | Privacy Admin | BR-21, BR-22, BR-24, BR-15 |
| AUD-003 | AuditReporting | Get user change history | GET | /api/v1/admin/audit/users/{userId} | Admin | BR-14, BR-24 |
| AUD-007 | AuditReporting | Assign exception owner | POST | /api/v1/admin/operations/exceptions/{exceptionId}/assign | Admin | BR-14, BR-24 |
| AUD-008 | AuditReporting | Resolve operational exception | POST | /api/v1/admin/operations/exceptions/{exceptionId}/resolve | Admin | BR-14, BR-24 |
| AUD-009 | AuditReporting | List report definitions | GET | /api/v1/admin/operations/reports | Admin | BR-14, BR-24 |
| AUD-010 | AuditReporting | Generate operational report | POST | /api/v1/admin/operations/reports | Admin | BR-14, BR-24 |
| AUD-011 | AuditReporting | Check report generation | GET | /api/v1/admin/operations/reports/{reportId} | Admin | BR-14, BR-24 |
| AUD-012 | AuditReporting | Download generated report | POST | /api/v1/admin/operations/reports/{reportId}/download | Admin | BR-14, BR-24 |
| AUD-016 | AuditReporting | List background job states | GET | /api/v1/admin/system/jobs | Admin | BR-14, BR-24 |
| AUD-017 | AuditReporting | Get job execution | GET | /api/v1/admin/system/jobs/{jobId} | Admin | BR-14, BR-24 |
| AUD-018 | AuditReporting | Retry safe background job | POST | /api/v1/admin/system/jobs/{jobId}/retry | Admin | BR-14, BR-24 |
| AUD-019 | AuditReporting | List outbox messages | GET | /api/v1/admin/system/outbox | Admin | BR-14, BR-24 |
| AUD-020 | AuditReporting | Retry outbox dispatch | POST | /api/v1/admin/system/outbox/{messageId}/retry | Admin | BR-14, BR-24 |
| AUD-021 | AuditReporting | List incidents | GET | /api/v1/admin/system/incidents | Admin | BR-14, BR-24 |
| AUD-022 | AuditReporting | Create incident record | POST | /api/v1/admin/system/incidents | Admin | BR-14, BR-24 |
| AUD-023 | AuditReporting | Update incident | PATCH | /api/v1/admin/system/incidents/{incidentId} | Admin | BR-14, BR-24 |
| AUD-027 | AuditReporting | Get content review report | GET | /api/v1/admin/reports/content-quality | Academic Reviewer | BR-14, BR-24 |
| AUD-031 | AuditReporting | Get assignments performance report | GET | /api/v1/admin/reports/xact/teacher-assignments | Admin / Academic Reviewer | BR-14, BR-24 |
