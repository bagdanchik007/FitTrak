# Settings security

- Change password uses `POST /api/v1/auth/change-password` (rate limited).
- Soft-delete uses `POST /api/v1/users/me/soft-delete` and clears local tokens.
