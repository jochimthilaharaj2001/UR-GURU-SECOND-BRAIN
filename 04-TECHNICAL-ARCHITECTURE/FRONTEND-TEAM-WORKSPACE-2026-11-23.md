# Frontend Workspace and Team Ownership — Proposed 2026-11-23

**Decision proposal:** one Angular workspace, two Angular apps (`apps/web` for Student + Teacher, `apps/admin` for Admin), and shared libraries. This aligns with BRD v6.2.2's web channel separation. Angular is the team's selected implementation direction, not a BRD-mandated framework; confirm technical decision OD-20.

```text
UR-GURU-FRONTEND/
  apps/
    web/src/app/features/
      student/        # DEV 3 + DEV 4
      teacher/        # DEV 5
      auth/           # shared ownership to assign
    admin/src/app/features/  # DEV 6
  libs/
    shared-ui/
    shared-auth/
    api-client/
    models/
    integrations/     # livekit/payhere as approved
  angular.json
  package.json
```

Dependencies to evaluate/install with compatible pinned versions: Angular Router, HttpClient, Reactive Forms, Signals/RxJS (Angular workspace), LiveKit client, Angular CDK/Material, Transloco, KaTeX, Chart.js, Tailwind/PostCSS. Avoid requiring every optional package before the relevant MVP feature is confirmed. PayHere secrets, payment verification, LiveKit join tokens and server-side authorization remain backend responsibilities.

**Implementation boundaries:** public optional prerecorded demos are not live trial bookings; StudentSubject is distinct from paid Enrollment; XACT uses backend authoritative deadlines/scoring. Admin privileges are enforced server-side. Separate Admin build/deployment is supported; Student/Teacher remain a single web application unless a separately approved architecture decision changes that.
