from uuid import uuid4

from app.application.services.favorite_service import favorite_key


def test_favorite_key_stable():
    u, e = uuid4(), uuid4()
    assert favorite_key(u, e) == f"{u}:{e}"
