# Derived metrics

- `GET /api/v1/workouts/{id}/metrics` — volume, completed sets, density
- Domain: `sets_per_minute` in `app.domain.workout.services`
- Application: `session_metrics` in `workout_metrics_service`

Metrics also return estimated_peak_1rm_kg and density_band.
