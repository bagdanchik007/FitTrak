# Roadmap

## Done

- Auth (register, login, refresh, change password, logout)
- Exercises & workouts CRUD + soft delete
- Progress summary & personal records
- Stats dashboard
- Docker, Alembic, CI, tests

## Platform (completed)

- [x] Refresh token rotation stored in DB
- [x] Email verification (token issue + verify endpoints)
- [x] Export workouts as CSV (download header)
- [x] WebSocket live session tracking
- [x] Frontend scaffold (React + TypeScript + Vite + Tailwind)
- [x] Journal & favorites, streaks & weekly summary
- [x] Notifications, password strength, Goals UI
- [x] Volume trend, week-delta, Streaks UI
- [x] Account soft-delete + audit event shaping
- [x] Frontend Journal / Body weight / Exercises / Preferences

## Future (optional)

- [ ] Redis-backed live session for multi-instance deploys
- [ ] Real email delivery for verification tokens
- [ ] Mobile-responsive charting on dashboard

## Releases

### 0.11.0
- Soft-delete account, audit helper, more SPA screens

### 0.10.0
- WebSocket live session + frontend Live page

### 0.9.x
- Refresh tokens, email verification, frontend SPA baseline
