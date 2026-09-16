import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_exercise_search_case_insensitive(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "search@test.com", "password": "SecurePass123!", "full_name": "S"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "search@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    await client.post(
        "/api/v1/exercises",
        json={"name": "Bench Press", "muscle_group": "chest"},
        headers=headers,
    )
    resp = await client.get("/api/v1/exercises?search=bench", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    items = data.get("items", data) if isinstance(data, dict) else data
    assert any("Bench" in (i.get("name") or "") for i in items)
