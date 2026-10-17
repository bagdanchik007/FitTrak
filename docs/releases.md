# Release history

Linear product versions (no jumps in the public story):

| Version | Focus |
|---------|--------|
| **1.0.0** | Portfolio baseline — API complete, SPA, Docker, MIT |
| **1.1.0** | Responsive UI — mobile drawer, desktop nav, safe areas |
| **1.1.1** | PWA — manifest, service worker, install icons |
| **1.2.0** | AI Coach — rule engine + optional OpenAI, `/coach` page |
| **1.3.0** | App shell — desktop sidebar + mobile bottom tabs |

## 1.0.0 — Baseline
Auth, workouts, goals, streaks, live WebSocket, soft-delete, Redis/SMTP options.

## 1.1.0 — Responsive shell
Hamburger menu, slide-over nav, touch targets, `viewport-fit=cover`.

## 1.1.1 — Installable PWA
`manifest.webmanifest`, `sw.js`, theme-color, offline app shell (API not cached).

## 1.2.0 — AI Coach
`POST /ai/suggest-workout`, `POST /ai/coach`, SPA Coach screen, `OPENAI_API_KEY` optional.

## 1.3.0 — App shell
Desktop sidebar and mobile bottom navigation; same functions on both.
