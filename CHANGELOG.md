## [0.4.0] - 2026-10-12

### Added
- Journal entries API
- Exercise favorites
- Workout streaks
- Weekly summary
- Migration 003

# Changelog

## [0.2.0] - 2026-09-23

### Added
- Token refresh and change-password endpoints
- Logout endpoint (client-side token discard)
- Token expiry fields in login response
- Profile update and public user profile
- Password strength validation (digit + letter)
- Exercise search, muscle_group and equipment filters
- Workout title search and total volume on read
- Soft-delete for exercises and workouts
- Progress summary and personal-records endpoints
- Rate limiting on login
- Global exception handlers
- Paginated exercise list with total count
- Health and readiness probes

### Changed
- Auth responses include access_expires_in / refresh_expires_in


## [0.2.1] - 2026-10-05
### Added
- Exercise sort/order, seed-defaults, date filters on workouts
- Owner-only delete and reference checks for exercises
- Additional integration and unit tests

## [0.3.0] - 2026-10-10

### Added
- MIT LICENSE
- Workout CSV export (`GET /workouts/export/csv`)
- Stats dashboard & meta features endpoints
- Domain services, security policies, metrics, cache
- UserService wired in users router
- `.dockerignore`, `py.typed`
- Expanded unit/integration tests and docs
