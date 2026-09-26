from app.core.status_texts import DB_CONNECTED, STATUS_OK


def test_status_texts():
    assert STATUS_OK == "ok"
    assert DB_CONNECTED == "connected"
