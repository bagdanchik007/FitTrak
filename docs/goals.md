# Goals

CRUD under `/api/v1/goals`.

Progress helpers:

- `progress_ratio` on entity
- `percent_complete` / `is_overdue` in `app/domain/goal/progress.py`

Goals list supports skip/limit pagination.

Reopen: POST /api/v1/goals/{id}/reopen clears is_completed.

Active count: GET /api/v1/goals/active-count
