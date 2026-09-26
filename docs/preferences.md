# User preferences

`GET/PUT /api/v1/preferences/me`

Fields:

- `weight_unit` – kg | lbs
- `language` – short locale code
- `weekly_goal_workouts` – 1..14
- `email_reminders` – bool

Domain helpers normalize units and clamp weekly goals.
