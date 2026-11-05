from app.domain.live.status import live_status_label

def test_connected():
    assert live_status_label("connected") == "Connected"
