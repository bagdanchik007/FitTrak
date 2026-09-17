from app.core.cache import InMemoryCache


def test_cache_set_get_delete():
    c = InMemoryCache()
    c.set("k", {"a": 1}, ttl_seconds=60)
    assert c.get("k") == {"a": 1}
    c.delete("k")
    assert c.get("k") is None


def test_cache_miss():
    c = InMemoryCache()
    assert c.get("missing") is None
