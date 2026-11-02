from app.domain.ui_copy.errors import error_message

def test_unauth():
    assert "sign" in error_message("unauthorized").lower()
