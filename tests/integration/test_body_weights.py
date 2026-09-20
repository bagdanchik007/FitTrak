import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_log_body_weight(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "bw@test.com", "password": "SecurePass123!", "full_name": "B"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "bw@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.post(
        "/api/v1/body-weights",
        json={"recorded_at": "2026-09-01", "weight_kg": 82.3},
        headers=headers,
    )
    assert resp.status_code == 201
    assert resp.json()["weight_kg"] == 82.3
