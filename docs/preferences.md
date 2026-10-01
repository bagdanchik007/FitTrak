# User preferences

`GET/PUT /api/v1/preferences/me`

Fields:

- `weight_unit` – kg | lbs
- `language` – short locale code
- `weekly_goal_workouts` – 1..14
- `email_reminders` – bool

Domain helpers normalize units and clamp weekly goals.

On write, units are normalized and weekly goals clamped.

Reset: POST /api/v1/preferences/me/reset restores kg/en/3/false defaults.
