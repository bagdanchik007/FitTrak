### 1.8.0
- Activity page, weigh-in form, goal form, recovery card

### 1.7.0
- Notes preview, activity labels, SPA document titles

### 1.6.0
- Templates UI, pagination meta, recovery hints

### 1.5.0
- Domain polish: titles, bands, milestones, coach sanitize

### 1.4.0
- SPA workout logging + history-aware AI suggestions

### 1.3.0
- Desktop sidebar + mobile bottom nav (one app, two shells)

### 1.2.0
- PWA + AI coach (rules / optional OpenAI)

# Roadmap

## Status: **Complete (v1.0.0)**

All planned portfolio features are implemented.

## Core

- [x] Auth (register, login, refresh, change password, logout)
- [x] Exercises & workouts CRUD + soft delete
- [x] Progress summary & personal records
- [x] Stats dashboard
- [x] Docker, Alembic, CI, tests

## Platform

- [x] Refresh token rotation stored in DB
- [x] Email verification + SMTP/dev delivery
- [x] Export workouts as CSV
- [x] WebSocket live session tracking
- [x] Optional Redis snapshot backend for live sessions
- [x] Frontend (React + TypeScript + Vite + Tailwind)
- [x] Journal, favorites, streaks, weekly summary
- [x] Notifications, password strength, Goals UI
- [x] Volume trend, week-delta, Streaks UI
- [x] Account soft-delete + audit events
- [x] SPA screens: Journal, Body weight, Exercises, Preferences, Live
- [x] Dashboard volume chart (responsive SVG)

## Releases

### 1.0.0 — Production-ready portfolio release
- SMTP email delivery, Redis live backend, dashboard chart, roadmap complete

### 0.11.0
- Soft-delete, audit, more SPA screens

### 0.10.0
- WebSocket live session

### 0.9.x
- Refresh tokens, email verification tokens, frontend baseline
