import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_favorites_flow(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "fav@test.com", "password": "SecurePass123!", "full_name": "F"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "fav@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    ex = await client.post(
        "/api/v1/exercises",
        json={"name": "Row", "muscle_group": "back"},
        headers=headers,
    )
    assert ex.status_code == 201
    exercise_id = ex.json()["id"]
    fav = await client.post(
        "/api/v1/favorites",
        json={"exercise_id": exercise_id},
        headers=headers,
    )
    assert fav.status_code == 201
    listed = await client.get("/api/v1/favorites", headers=headers)
    assert listed.status_code == 200
    assert len(listed.json()) >= 1
