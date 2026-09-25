# Project conventions

- Conventional Commits: `feat|fix|docs|test|chore|refactor(scope): message`
- Domain code has no FastAPI/SQLAlchemy imports
- API routers stay thin; business rules in services/domain
- Soft deletes via `deleted_at` where applicable
- Auth required for user-owned resources
