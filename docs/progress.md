# Progress

## Summary
`GET /api/v1/progress/summary?days=30` — aggregates for the authenticated user.

## Personal records
`GET /api/v1/progress/personal-records`

## PR evaluation
`POST /api/v1/progress/personal-record/check` evaluates whether a candidate lift
would beat a known previous best (stateless helper for clients).
