import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_journal_create_list(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "journal@test.com", "password": "SecurePass123!", "full_name": "J"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "journal@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.post(
        "/api/v1/journal",
        json={"title": "Great session", "body": "Felt strong", "mood": "happy"},
        headers=headers,
    )
    assert resp.status_code == 201
    listed = await client.get("/api/v1/journal", headers=headers)
    assert listed.status_code == 200
    assert len(listed.json()) >= 1
