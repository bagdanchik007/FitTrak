from app.domain.system.services import build_health_payload

def test_health_ok():
    p = build_health_payload()
    assert p["status"] == "ok"
    assert p["version"]

def test_health_degraded():
    p = build_health_payload(database_ok=False)
    assert p["status"] == "degraded"
    assert p["database"] == "down"
