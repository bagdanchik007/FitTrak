import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_progress_summary_requires_auth(client: AsyncClient):
    resp = await client.get("/api/v1/progress/summary")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_progress_summary_empty_user(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "prog@test.com", "password": "SecurePass123!", "full_name": "Prog"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "prog@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    resp = await client.get("/api/v1/progress/summary", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_workouts"] == 0
    assert data["total_sets"] == 0
    assert "personal_records" in data
    assert "volume_last_30_days" in data
