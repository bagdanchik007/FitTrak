# API Reference (short)

Base URL: `/api/v1`

## Authentication

| Method | Path | Description |
|--------|------|-------------|
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Get access + refresh tokens |

## Users

| Method | Path | Description |
|--------|------|-------------|
| GET | `/users/me` | Current user profile |

## Exercises

| Method | Path | Description |
|--------|------|-------------|
| POST | `/exercises` | Create exercise |
| GET | `/exercises` | List exercises |
| GET | `/exercises/{id}` | Get one exercise |

## Workouts

| Method | Path | Description |
|--------|------|-------------|
| POST | `/workouts` | Create workout + sets |
| GET | `/workouts` | List my workouts |
| GET | `/workouts/{id}` | Get one workout |

## Progress

| Method | Path | Description |
|--------|------|-------------|
| GET | `/progress/summary` | PRs, volume, totals |

## Health

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness |
| GET | `/health/ready` | Readiness (DB check) |

Interactive docs: `/docs`


## Authentication Header
```
Authorization: Bearer <access_token>
```

| DELETE | `/exercises/{id}` | Soft-delete exercise |
| DELETE | `/workouts/{id}` | Soft-delete workout |


## Refresh rotation
After using a refresh token, issue a new pair and invalidate the old refresh when storing tokens server-side.


### Exercise query params: search, muscle_group, equipment, skip, limit

Exercise list supports: search, muscle_group, equipment, sort_by, order, skip, limit.


## Auth flow
1. POST /auth/register 2. POST /auth/login 3. Use Bearer access token 4. POST /auth/refresh when expired
