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
