import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_and_list_exercises(client: AsyncClient):
    # Register + login
    await client.post(
        "/api/v1/auth/register",
        json={"email": "ex@test.com", "password": "SecurePass123!", "full_name": "Ex User"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "ex@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create exercise
    resp = await client.post(
        "/api/v1/exercises",
        json={"name": "Bench Press", "muscle_group": "chest", "equipment": "barbell"},
        headers=headers,
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Bench Press"
    assert "id" in data

    # List
    resp = await client.get("/api/v1/exercises", headers=headers)
    assert resp.status_code == 200
    assert len(resp.json()) >= 1
