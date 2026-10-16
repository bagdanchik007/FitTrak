# AI Coach

## Endpoints

- `POST /api/v1/ai/suggest-workout` — body: `{ recent_focuses?, experience?, focus? }`
- `POST /api/v1/ai/coach` — body: `{ message }`

## Engines

- **rules** (default): domain heuristics, no external calls
- **openai**: when `OPENAI_API_KEY` is set

Not medical advice.
