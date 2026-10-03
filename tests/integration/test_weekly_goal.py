import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_weekly_goal_endpoint(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "wg@test.com", "password": "SecurePass123!", "full_name": "W"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "wg@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.get("/api/v1/summary/weekly-goal", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "workouts_done" in data
    assert "weekly_goal" in data
