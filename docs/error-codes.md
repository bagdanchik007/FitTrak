# Error codes

Stable string codes for clients (see `app/core/errors.py`):

- `not_found`
- `conflict`
- `unauthorized`
- `forbidden`
- `validation_error`
- `rate_limited`
- `internal_error`

Responses still use `{"detail": "..."}`; codes can be added gradually.
