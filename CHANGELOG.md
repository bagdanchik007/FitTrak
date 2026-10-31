## [1.9.0] - 2026-11-14

### Added
- Set volume helper and meta endpoint
- Rest timer suggestions by RPE
- Weekly volume delta percent
- CSV escape helper, goal deadline status
- EmptyState component and more document titles

## [1.8.0] - 2026-11-13

### Added
- Activity feed labels plus SPA activity page
- Weigh-in and goal create forms
- Password hints on registration
- Recovery hint card on the dashboard

### Fixed
- Goals page again loads `/goals/with-progress`

## [1.7.0] - 2026-11-12

### Added
- Notes preview, activity labels, password hints, notification priority
- Document titles on Goals/Coach/Streaks, shared date helper

## [1.6.0] - 2026-11-11

### Added
- Exercise name normalize, pagination meta, recovery hints
- Journal mood score, theme normalize
- Templates SPA page

## [1.5.0] - 2026-11-10

### Added
- Workout title normalize, duration bands, goal labels
- Streak milestones, BW trend helpers, coach sanitize
- SPA format helpers and document title hook

## [1.4.0] - 2026-11-09

### Added
- Create workout form in the SPA
- AI workout suggestions use recent workout title history

## [1.3.1] - 2026-11-08

### Added
- Download / install GUI buttons on home page (PWA prompt + GitHub releases link)

## [1.3.0] - 2026-11-08

### Added
- Dual app shell: desktop sidebar + mobile bottom navigation
- Shared features and API for laptop and phone

## [1.2.0] - 2026-11-07

### Added
- AI coach API (`/ai/suggest-workout`, `/ai/coach`)
- Rule engine by default; optional OpenAI via `OPENAI_API_KEY`
- SPA Coach page (`/coach`)

## [1.1.1] - 2026-11-06

### Added
- PWA manifest, service worker, installable icons
- Theme color and Apple web-app meta tags

## [1.1.0] - 2026-11-06

### Added
- Responsive layout: mobile drawer + desktop nav
- Safe-area insets and touch-friendly CSS

## [1.0.0] - 2026-11-05

### Added
- Public portfolio baseline (API + SPA + Docker)
- SMTP/dev email, optional Redis live backend
- Dashboard volume chart, MIT license

## [0.11.0] - 2026-11-04

### Added
- Account soft-delete endpoint
- Audit event helper and meta example
- Frontend Journal, Body weight, Exercises, Preferences pages

## [0.10.0] - 2026-11-03

### Added
- WebSocket live workout session tracking
- Live session HTTP status endpoint
- Live session domain event normalization
- Frontend Live session page

## [0.9.2] - 2026-11-02

### Added
- Volume trend endpoint (7d vs prior 7d)
- Body-weight week-delta endpoint
- Workout notes truncation helper
- Theme normalization helper
- Common timezones meta list
- Frontend Streaks page

## [0.9.1] - 2026-11-01

### Added
- Password strength scoring endpoint
- In-app notifications derived from workouts and goals
- Frontend Goals and Notifications pages

## [0.9.0] - 2026-10-31

### Added
- Refresh token model, rotation service and migration
- Email verification request/verify endpoints
- CSV export Content-Disposition attachment header
- Frontend: React + TypeScript + Vite + Tailwind (login, register, dashboard, workouts)

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
