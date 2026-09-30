# Project conventions

- Conventional Commits: `feat|fix|docs|test|chore|refactor(scope): message`
- Domain code has no FastAPI/SQLAlchemy imports
- API routers stay thin; business rules in services/domain
- Soft deletes via `deleted_at` where applicable
- Auth required for user-owned resources

- Prefer app.core.messages for user-facing API error strings

- Stateless evaluation endpoints (e.g. PR check) still live under authenticated routers when they touch user context elsewhere.
