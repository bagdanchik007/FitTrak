# Live session (WebSocket)

## Endpoint

`WS /api/v1/ws/live-session?token=<access_jwt>`

## Client events (JSON)

- `{ "event": "set_logged", "exercise_name": "Bench Press" }`
- `{ "event": "exercise_changed", "exercise_name": "Squat" }`
- `{ "event": "ended" }`
- `{ "event": "ping" }`

## HTTP

`GET /api/v1/live-session/status` — snapshot of active session for the authenticated user.

## Notes

In-memory hub is process-local (demo / single instance). Horizontal scale would use Redis pub/sub.
