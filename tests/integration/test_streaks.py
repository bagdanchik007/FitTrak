import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_streak_endpoint_empty_user(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "streak@test.com", "password": "SecurePass123!", "full_name": "S"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "streak@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.get("/api/v1/streaks/me", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["current_streak_days"] == 0
    assert data["total_workout_days"] == 0
