import pytest
from httpx import AsyncClient


async def _auth(client: AsyncClient, email: str) -> dict:
    await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": "SecurePass123!", "full_name": "G"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": "SecurePass123!"},
    )
    return {"Authorization": f"Bearer {login.json()['access_token']}"}


@pytest.mark.asyncio
async def test_create_and_list_goals(client: AsyncClient):
    headers = await _auth(client, "goals@test.com")
    resp = await client.post(
        "/api/v1/goals",
        json={"title": "Bench 100kg", "target_value": 100, "unit": "kg"},
        headers=headers,
    )
    assert resp.status_code == 201
    assert resp.json()["title"] == "Bench 100kg"

    listed = await client.get("/api/v1/goals", headers=headers)
    assert listed.status_code == 200
    assert len(listed.json()) >= 1
