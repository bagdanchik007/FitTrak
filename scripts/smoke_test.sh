#!/usr/bin/env sh
# Minimal smoke test against running API
set -e
BASE="${BASE_URL:-http://localhost:8000}"

echo "Health..."
curl -sf "$BASE/api/v1/health" > /dev/null

echo "Register..."
EMAIL="smoke_$(date +%s)@example.com"
curl -sf -X POST "$BASE/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$EMAIL\",\"password\":\"SecurePass123!\",\"full_name\":\"Smoke\"}" > /dev/null

echo "Login..."
TOKEN=$(curl -sf -X POST "$BASE/api/v1/auth/login" \
  -d "username=$EMAIL&password=SecurePass123!" | sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p')

echo "Me..."
curl -sf "$BASE/api/v1/users/me" -H "Authorization: Bearer $TOKEN" > /dev/null

echo "OK"
