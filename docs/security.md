# Security notes

## Authentication

- JWT access + refresh tokens
- Passwords hashed with bcrypt (passlib)
- `type` claim distinguishes access vs refresh

## Authorization

- Workout resources scoped by `user_id`
- Custom exercises: only owner may delete
- System exercises (`created_by=null`): restricted

## Rate limiting

- Login and change-password endpoints are rate-limited in-memory
- For production, use Redis-backed limiting and edge WAF

## Secrets

- Never commit `.env`
- Generate secrets with `python -m scripts.generate_secret`

## Journal privacy
Journal entries are always scoped to the authenticated user_id.
