# FitTrack API

Modern, production-ready fitness tracking backend built with **FastAPI**, **Clean Architecture**, **SQLAlchemy 2.0** and **PostgreSQL**.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- **Clean Architecture** – Domain, Application, Infrastructure and API layers clearly separated
- **Async everything** – FastAPI + SQLAlchemy 2.0 async + asyncpg
- **JWT Authentication** – Access + Refresh tokens
- **Exercises & Workouts** – Full CRUD with nested sets (reps, weight, RPE)
- **Soft deletes** – Data is never hard-deleted
- **Docker-ready** – Multi-stage build + docker-compose with healthchecks
- **Alembic migrations** – Proper database versioning
- **Beautiful OpenAPI docs** – Available at `/docs`
- **Structured & type-safe** – Pydantic v2 + mypy-ready

---

## Quick Start

### 1. Clone & setup environment

```bash
cp .env.example .env
# Edit .env and set a strong SECRET_KEY
```

### 2. Start with Docker (recommended)

```bash
docker compose up --build
```

The API will be available at: **http://localhost:8000**

- Interactive docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### 3. Run migrations (already done by docker-compose)

```bash
docker compose exec api alembic upgrade head
```

---

## Project Structure

```text
fittrack/
├── app/
│   ├── api/                  # HTTP layer (routers)
│   ├── application/          # Use cases / services
│   ├── core/                 # Config, security, dependencies
│   ├── domain/               # Business entities & repository interfaces
│   ├── infrastructure/       # Database, concrete repositories
│   └── schemas/              # Pydantic request/response models
├── migrations/               # Alembic
├── tests/
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

---

## API Overview

| Method | Endpoint                      | Description                  |
|--------|-------------------------------|------------------------------|
| POST   | `/api/v1/auth/register`       | Register new user            |
| POST   | `/api/v1/auth/login`          | Login (returns tokens)       |
| POST   | `/api/v1/auth/refresh`        | Refresh access token         |
| POST   | `/api/v1/auth/change-password`| Change password              |
| PATCH  | `/api/v1/users/me`            | Update profile               |
| PATCH  | `/api/v1/exercises/{id}`      | Update exercise              |
| PATCH  | `/api/v1/workouts/{id}`       | Update workout               |
| GET    | `/api/v1/users/me`            | Current user profile         |
| POST   | `/api/v1/exercises`           | Create exercise              |
| GET    | `/api/v1/exercises`           | List exercises               |
| POST   | `/api/v1/workouts`            | Create workout + sets        |
| GET    | `/api/v1/workouts`            | List my workouts             |
| DELETE | `/api/v1/workouts/{id}`       | Soft-delete a workout        |
| GET    | `/api/v1/progress/summary`    | Progress, PRs & volume       |
| DELETE | `/api/v1/exercises/{id}`      | Soft-delete an exercise      |

---

## Local Development (without Docker)

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create venv & install
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Start PostgreSQL (or use docker only for db)
docker compose up db -d

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

---

## Tech Stack

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy 2.0** (async)
- **PostgreSQL 16**
- **Alembic**
- **Pydantic v2**
- **python-jose** + **passlib** (JWT + bcrypt)
- **Docker** + **docker-compose**
- **Ruff** + **mypy** + **pytest**

---

## Roadmap / Possible Extensions

- [ ] Progress endpoints (Personal Records, volume charts)
- [ ] Cursor-based pagination
- [ ] Rate limiting
- [ ] Background tasks (e.g. weekly summary emails)
- [ ] Soft-delete endpoints + restore
- [ ] Frontend (Next.js / React)

---

## License

MIT

---

## Development Notes

- Use `docker compose logs -f api` to follow application logs
- After model changes run: `alembic revision --autogenerate -m "description"`
- Keep the domain layer free of framework dependencies

## Contributing

This is a portfolio project. Feel free to fork and extend it.


## Troubleshooting

| Problem | Fix |
|--------|-----|
| DB connection refused | Wait for healthcheck: `docker compose ps` |
| 401 on every request | Check SECRET_KEY is set and tokens not expired |
| CORS errors from frontend | Add origin to `CORS_ORIGINS` in `.env` |
| Migration errors | `docker compose exec api alembic upgrade head` |


## Example requests

```bash
# Register
curl -s -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"you@example.com","password":"SecurePass123!","full_name":"You"}'

# Login
curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -d "username=you@example.com&password=SecurePass123!"

# Progress (replace TOKEN)
curl -s http://localhost:8000/api/v1/progress/summary \
  -H "Authorization: Bearer TOKEN"
```


### Layer responsibilities
- **Domain**: entities & repository interfaces (no framework)
- **Application**: use-case services
- **Infrastructure**: SQLAlchemy models & repos
- **API**: FastAPI routers only
