import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_preferences_normalize_weight_unit(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "pref2@test.com", "password": "SecurePass123!", "full_name": "P"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "pref2@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.put(
        "/api/v1/preferences/me",
        json={"weight_unit": "lbs", "weekly_goal_workouts": 20},
        headers=headers,
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["weight_unit"] == "lbs"
    assert data["weekly_goal_workouts"] == 14  # clamped
