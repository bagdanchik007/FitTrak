# Workouts

## Volume
Total volume is `sum(weight_kg * reps)` over sets, computed in
`app.domain.workout.services.calculate_session_volume` and exposed as
`total_volume_kg` on read models.

## Constraints
- At most `MAX_SETS_PER_WORKOUT` sets per create request
- `set_number` must be unique within a workout payload
- List endpoints are scoped to the authenticated user

## Export
`GET /api/v1/workouts/export/csv` returns a CSV of the caller's sessions.
