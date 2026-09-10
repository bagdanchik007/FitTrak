# Architecture Overview

FitTrack follows **Clean Architecture** principles.

## Layers

```
┌─────────────────────────────────────────┐
│              API (FastAPI)              │  ← HTTP, validation, auth
├─────────────────────────────────────────┤
│         Application (Services)          │  ← Use cases / orchestration
├─────────────────────────────────────────┤
│              Domain                     │  ← Entities + Repository interfaces
├─────────────────────────────────────────┤
│           Infrastructure                │  ← SQLAlchemy, concrete repos
└─────────────────────────────────────────┘
```

### Domain
Pure business logic. No framework dependencies.
- Entities (dataclasses)
- Repository interfaces (ABC)

### Application
Use-case services that orchestrate domain logic.
- `AuthService`, `ExerciseService`, `WorkoutService`, `ProgressService`

### Infrastructure
Technical details:
- SQLAlchemy models & session
- Concrete repository implementations

### API
Thin controllers that:
1. Receive HTTP requests
2. Call application services
3. Return Pydantic responses

## Key Design Decisions

- **Async everywhere** – FastAPI + async SQLAlchemy + asyncpg
- **Soft deletes** – `deleted_at` instead of hard deletes
- **UUID primary keys** – better for distributed systems
- **JWT** – Access + Refresh tokens
- **Dependency Injection** – FastAPI `Depends` + repository pattern
