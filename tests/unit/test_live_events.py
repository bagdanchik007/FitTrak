from app.domain.live.services import is_session_active, normalize_live_event

def test_normalize_live_event():
    assert normalize_live_event("SET_LOGGED") == "set_logged"
    assert normalize_live_event("nope") == "ping"

def test_is_session_active():
    assert is_session_active("set_logged") is True
    assert is_session_active("ended") is False
