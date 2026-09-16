import pytest
from httpx import AsyncClient
from uuid import uuid4


@pytest.mark.asyncio
async def test_create_workout_with_invalid_exercise_id(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "winv@test.com", "password": "SecurePass123!", "full_name": "W"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "winv@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    resp = await client.post(
        "/api/v1/workouts",
        json={
            "title": "Bad",
            "performed_at": "2026-09-01",
            "sets": [{"exercise_id": str(uuid4()), "set_number": 1, "reps": 5, "weight_kg": 50}],
        },
        headers=headers,
    )
    # FK violation or 4xx depending on DB constraint handling
    assert resp.status_code >= 400
