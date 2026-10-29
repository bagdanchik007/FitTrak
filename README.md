# FitTrack

**Version 1.0.0** — Portfolio-ready fitness tracking platform.

Backend: **FastAPI** · **Clean Architecture** · **SQLAlchemy 2.0** · **PostgreSQL** · **Docker**  
Frontend: **React** · **TypeScript** · **Vite** · **Tailwind CSS**

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- Clean Architecture (domain / application / infrastructure / API)
- Async FastAPI + SQLAlchemy 2.0 + Alembic
- JWT access + refresh tokens (rotation in DB)
- Email verification (SMTP or dev log)
- Exercises, workouts, goals, body weight, journal, favorites
- Streaks, weekly summary, volume trends, personal records
- WebSocket live session tracking (optional Redis snapshots)
- CSV export, soft deletes, feature flags
- React SPA with dashboard chart, live session UI, and more

---

## Quick start

### Prerequisites

- Python 3.12+ 
- Docker (for PostgreSQL) **or** local Postgres
- Node.js 20+ (for the frontend)

### 1. Environment

```bash
git clone https://github.com/YOUR_USERNAME/fittrack.git
cd fittrack
cp .env.example .env
```

Edit `.env`: set a strong `SECRET_KEY` (32+ chars). For local Postgres:

```env
DATABASE_URL=postgresql+asyncpg://fittrack:fittrack_secret@localhost:5432/fittrack
```

### 2. Database

```bash
docker compose up -d db
```

### 3. Backend

```bash
python -m venv .venv
# Windows Git Bash: source .venv/Scripts/activate
# Windows: py -m venv .venv && source .venv/Scripts/activate
pip install -e ".[dev]"
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API: http://localhost:8000  
- OpenAPI: http://localhost:8000/docs  
- Health: http://localhost:8000/api/v1/health  

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

- UI: http://localhost:5173  

### Full stack with Docker

```bash
docker compose up --build
```

---

## Project structure

```
app/
  api/v1/          # HTTP & WebSocket routers
  application/     # Services & DTOs
  domain/          # Pure domain logic
  infrastructure/  # DB models, repositories, Redis
  core/            # Config, security, feature flags
frontend/          # React + TypeScript + Tailwind SPA
migrations/        # Alembic
tests/             # Unit & integration
docs/              # Architecture & feature docs
```

---

## Documentation

- [Roadmap](docs/roadmap.md) — completed (v1.0.0)
- [Features](docs/features.md)
- [Architecture](docs/architecture-layers.md)
- [Live session](docs/live-session.md)
- [Deployment](docs/deployment.md)
- [Contributing](docs/contributing.md)

---

## License

MIT — see [LICENSE](LICENSE).


## Release ladder

See [docs/releases.md](docs/releases.md): **1.0.0** → **1.1.0** (responsive) → **1.1.1** (PWA) → **1.3.0** (AI coach).


**Version 1.6.0**
