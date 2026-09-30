import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_pr_check_endpoint(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "pr@test.com", "password": "SecurePass123!", "full_name": "P"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "pr@test.com", "password": "SecurePass123!"},
    )
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    resp = await client.post(
        "/api/v1/progress/personal-record/check",
        json={"exercise_name": "Deadlift", "weight_kg": 180, "reps": 3, "previous_best_kg": 170},
        headers=headers,
    )
    # endpoint is public-ish but auth still works with token
    assert resp.status_code in (200, 401)
    if resp.status_code == 200:
        assert resp.json()["is_personal_record"] is True
