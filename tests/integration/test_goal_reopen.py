import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_goal_reopen(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "reopen@test.com", "password": "SecurePass123!", "full_name": "R"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "reopen@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    created = await client.post(
        "/api/v1/goals",
        json={"title": "OHP", "target_value": 60, "current_value": 60, "unit": "kg"},
        headers=headers,
    )
    gid = created.json()["id"]
    await client.post(f"/api/v1/goals/{gid}/complete", headers=headers)
    resp = await client.post(f"/api/v1/goals/{gid}/reopen", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["is_completed"] is False
