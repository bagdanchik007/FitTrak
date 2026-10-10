## [0.8.1] - 2026-10-30

### Added
- Rest interval suggestion endpoint for sets
- Muscle group normalization helpers
- Streak milestone labels
- Days until deadline on goals with-progress

## [0.8.0] - 2026-10-29

### Added
- Session duration band on workout metrics
- Goal on-track helper against schedule
- Journal mood polarity breakdown endpoint
- CSV export helpers
- Pagination clamp utilities and meta endpoint
- User display-name helper
- Empty dashboard defaults

## [0.7.2] - 2026-10-28

### Added
- Training frequency band on training-days endpoint
- PR improvement percentage versus previous best
- Favorites capacity hint on count endpoint
- Effective preferences snapshot endpoint
- Build channel metadata on meta/build
- Longest rest-gap domain helper

## [0.7.1] - 2026-10-27

### Added
- Average RPE on session metrics
- Goal status labels on with-progress list
- Template and journal counts
- Training-days summary endpoint
- Activity type labels helper

## [0.7.0] - 2026-10-26

### Added
- Session average working weight and volume load bands
- Consistency score endpoint under streaks
- Goal remaining_to_target on with-progress list
- Body-weight trend direction on delta
- Exercise name normalization and compound hints
- Template name normalization helpers
- User activity summary includes last-7-days count

## [0.6.5] - 2026-10-24

### Changed
- Weekly goal status includes window dates and status label
- Recovery snapshot includes actionable recommendation
- Workout metrics include peak estimated 1RM and density band
- PR check reports margin versus previous best
- Preferences language normalized to supported codes
- Goals list-with-progress enrichment endpoint

## [0.6.4] - 2026-10-23

### Added
- Weekly goal progress endpoint
- Workouts and body-weight counts
- Favorite existence check
- Meta build info
- Logout-all placeholder for multi-device sessions

## [0.6.3] - 2026-10-22

### Added
- Recovery status endpoint (rest days since last workout)
- Exercise name search
- Template rename action
- Journal mood statistics
- Active goals count

## [0.6.2] - 2026-10-21

### Added
- Workout session metrics endpoint
- Goal reopen action
- Latest body-weight lookup
- Preferences reset-to-defaults
- User activity summary
- Activity feed type filter

## [0.6.1] - 2026-10-20

### Added
- Stateless personal-record evaluation endpoint
- Journal title search
- Template duplicate action
- Favorites count endpoint

### Fixed
- Progress summary days clamp applied once

## [0.6.0] - 2026-10-19

### Added
- Goal completion endpoint
- Body-weight delta summary
- Composite index on workouts (user_id, performed_at)
- Workout set_number uniqueness validation

### Changed
- Session volume calculated in domain layer
- Workout and exercise repositories expose ownership/active lookups
- OpenAPI tag descriptions for major resource groups

## [0.5.1] - 2026-10-18

### Changed
- Goals list pagination and progress wiring refined
- Journal/exercises/workouts use shared page limits
- Meta version response uses VersionResponse schema
- Auth service uses shared message constants

## [0.5.0] - 2026-10-17

### Changed
- Goals API uses domain progress helpers and auto-complete
- Preferences normalize weight unit and weekly goal on write
- Streaks/summary/activity/journal wired through domain services
- Shared messages and status texts used in API errors

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



## [0.4.1] - 2026-10-14
### Added
- Domain helpers for summary and activity
- StreakService and shared version module
- Error code and HTTP header constants


## [0.4.2] - 2026-10-15
### Added
- Template domain layer, mapper, overview service
- Core limits, enums, and message constants
- Architecture and conventions docs


## [0.4.3] - 2026-10-16
### Added
- Preference domain layer and mappers
- Goal progress helpers and services
- Timezone, status text, path constants
