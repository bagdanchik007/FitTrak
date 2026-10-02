import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_recovery_endpoint(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "rec@test.com", "password": "SecurePass123!", "full_name": "R"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "rec@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.get("/api/v1/streaks/me/recovery", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["status"] == "never"
