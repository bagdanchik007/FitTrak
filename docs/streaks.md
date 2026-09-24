# Workout streaks

`GET /api/v1/streaks/me` returns:

- `current_streak_days` – consecutive days ending today or yesterday
- `longest_streak_days` – best run in history
- `last_workout_date`
- `total_workout_days` – distinct days with at least one workout

Logic lives in `app/domain/streak/services.py` (pure, unit-tested).
