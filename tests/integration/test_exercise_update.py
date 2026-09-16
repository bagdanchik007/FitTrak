import pytest
from httpx import AsyncClient
from uuid import uuid4


@pytest.mark.asyncio
async def test_update_missing_exercise_returns_404(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "upd@test.com", "password": "SecurePass123!", "full_name": "U"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "upd@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    resp = await client.patch(
        f"/api/v1/exercises/{uuid4()}",
        json={"name": "Nope"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 404
