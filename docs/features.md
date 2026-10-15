# Feature overview (v0.3+)

## Core
- Auth: register, login, refresh, logout, change password
- Users: me, profile update, public profile

## Training
- Exercises CRUD + search/filters + seed-defaults
- Workouts with sets, volume, date filters, CSV export
- Workout templates
- Progress summary & personal records
- Stats dashboard

## Tracking
- Goals (CRUD, soft delete)
- Body weight log
- Activity feed
- User preferences

## Ops
- Health / readiness
- Meta version & feature flags
- Docker, Alembic, CI, tests

- Journal, favorites, streaks, weekly summary

- Shared version module and error codes

- Template domain helpers and overview service
- Central limits, enums, and API messages

- Preference domain + goal progress helpers

- Goal progress endpoint and auto-complete on update
- Domain-wired streaks, summary, activity, preferences

- Goals list pagination; progress days clamp; meta VersionResponse

- Goal completion endpoint; body-weight delta; domain session volume

- Personal-record check, journal search, template duplicate, favorites count

- Workout metrics, goal reopen, body-weight latest, preferences reset

- Recovery status, exercise search, template rename, mood stats, active goals count

- Weekly goal progress, resource counts, favorite exists, meta build

- Deepened weekly goal labels, recovery recommendations, density bands, PR margins

- Consistency score, volume load bands, body-weight trend, goal remaining

- Average RPE, goal status labels, training-days, template/journal counts

- Frequency band, PR improvement %, favorites capacity, effective preferences

- Duration band, mood polarity, pagination meta, CSV export helpers (0.8.0)

- Rest suggestions, muscle group normalize, streak milestones, deadline days (0.8.1)

- Refresh token store, email verification, frontend SPA (0.9.0)

- Password strength meta endpoint, notifications feed, Goals/Alerts UI (0.9.1)

- Volume trend, body-weight week-delta, Streaks UI (0.9.2)

- WebSocket live session tracking (0.10.0)

- Account soft-delete, audit events, Journal/Weight/Exercises/Prefs UI (0.11.0)

- SMTP delivery, Redis live backend, dashboard chart (1.0.0)
