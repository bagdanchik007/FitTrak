# Deployment notes

## Docker

```bash
docker compose up --build -d
```

## Environment

Copy `.env.example` → `.env` and set at least:

- `SECRET_KEY` (≥ 32 chars)
- `DATABASE_URL` (asyncpg URL)

## Migrations

```bash
docker compose exec api alembic upgrade head
```

## Health checks

- Liveness: `GET /api/v1/health`
- Readiness: `GET /api/v1/health/ready`

## Production checklist

- [ ] Strong `SECRET_KEY`
- [ ] `APP_ENV=production` / `DEBUG=false`
- [ ] Restrict `CORS_ORIGINS`
- [ ] TLS termination (reverse proxy)
- [ ] Managed PostgreSQL
- [ ] Log aggregation


## Migrations after pull
Run `alembic upgrade head` so revisions 002 and 003 apply.

After pull: alembic upgrade head && make verify

Migration 004 adds index `ix_workouts_user_performed_at`.

No new migration in 0.6.2; restart API after deploy.

0.6.3 requires no new migration.

0.6.4 requires no new migration.

0.8.0 requires no new migration.
