import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_goal_progress_endpoint(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "gprog@test.com", "password": "SecurePass123!", "full_name": "G"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "gprog@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    created = await client.post(
        "/api/v1/goals",
        json={"title": "Squat", "target_value": 100, "current_value": 40, "unit": "kg"},
        headers=headers,
    )
    assert created.status_code == 201
    goal_id = created.json()["id"]
    resp = await client.get(f"/api/v1/goals/{goal_id}/progress", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["percent_complete"] == 40.0
    assert data["is_completed"] is False
