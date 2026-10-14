from app.domain.audit.services import build_audit_event

def test_build_audit_event():
    e = build_audit_event(action="create", resource="workout", resource_id="1")
    assert e["action"] == "create"
    assert "at" in e
