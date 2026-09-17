# Contributing

## Setup

```bash
cp .env.example .env
docker compose up --build
```

## Code style

- Ruff for lint + format
- Type hints on public functions
- Keep domain free of FastAPI/SQLAlchemy imports

## Tests

```bash
make test
# or
pytest -v
```

## Commit messages

Prefer Conventional Commits:

- `feat(scope): ...`
- `fix(scope): ...`
- `docs: ...`
- `test: ...`
- `chore: ...`
