# Endpoints quick reference

## Auth
- POST /api/v1/auth/register
- POST /api/v1/auth/login
- POST /api/v1/auth/refresh
- POST /api/v1/auth/logout

## Training
- /api/v1/exercises
- /api/v1/workouts
- /api/v1/templates
- /api/v1/favorites

## Tracking
- /api/v1/goals
- /api/v1/body-weights
- /api/v1/journal
- /api/v1/progress/summary
- /api/v1/streaks/me
- /api/v1/summary/weekly
- /api/v1/stats/dashboard
- /api/v1/activity/feed


## Docs
- docs/streaks.md
- docs/weekly-summary.md
- docs/error-codes.md

- docs/templates.md

- POST /api/v1/progress/personal-record/check
- GET /api/v1/journal/search
- POST /api/v1/templates/{id}/duplicate
- GET /api/v1/favorites/count

- GET /api/v1/workouts/{id}/metrics
- POST /api/v1/goals/{id}/reopen
- GET /api/v1/body-weights/latest
- POST /api/v1/preferences/me/reset
- GET /api/v1/users/me/activity-summary

- GET /api/v1/streaks/me/recovery
- GET /api/v1/exercises/search
- PATCH /api/v1/templates/{id}/rename
- GET /api/v1/journal/mood-stats
- GET /api/v1/goals/active-count

- GET /api/v1/summary/weekly-goal
- GET /api/v1/workouts/count
- GET /api/v1/body-weights/count
- GET /api/v1/favorites/exists/{exercise_id}
- GET /api/v1/meta/build

- GET /api/v1/goals/with-progress
