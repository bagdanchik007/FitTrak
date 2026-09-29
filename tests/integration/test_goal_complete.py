import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_complete_goal(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "gcomp@test.com", "password": "SecurePass123!", "full_name": "G"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "gcomp@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    created = await client.post(
        "/api/v1/goals",
        json={"title": "DL", "target_value": 180, "current_value": 160, "unit": "kg"},
        headers=headers,
    )
    goal_id = created.json()["id"]
    resp = await client.post(f"/api/v1/goals/{goal_id}/complete", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["is_completed"] is True
