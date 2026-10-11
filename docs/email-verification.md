# Email verification

- `POST /api/v1/auth/request-verification` (auth required)
- `POST /api/v1/auth/verify-email?token=...`

Token is returned in API responses for local testing; production should only email the link.
