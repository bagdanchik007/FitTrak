from app.infrastructure.live.redis_backend import get_redis_backend

def test_get_redis_backend_none_without_url(monkeypatch):
    class S:
        redis_url = None
    monkeypatch.setattr("app.core.config.get_settings", lambda: S())
    # factory imports get_settings from config inside function
    monkeypatch.setattr(
        "app.infrastructure.live.redis_backend.get_settings",
        lambda: S(),
    )
    assert get_redis_backend() is None
