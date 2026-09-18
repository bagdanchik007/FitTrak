import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_dashboard_requires_auth(client: AsyncClient):
    resp = await client.get("/api/v1/stats/dashboard")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_dashboard_for_new_user(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "stats@test.com", "password": "SecurePass123!", "full_name": "S"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "stats@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    resp = await client.get(
        "/api/v1/stats/dashboard",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_workouts"] == 0
    assert "workouts_last_7_days" in data
