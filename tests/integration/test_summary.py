import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_weekly_summary_empty(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "sum@test.com", "password": "SecurePass123!", "full_name": "S"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "sum@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.get("/api/v1/summary/weekly", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["workouts"] == 0
    assert data["total_volume_kg"] == 0
