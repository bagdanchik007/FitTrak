from app.domain.auth.password_hints import password_hints

def test_hints():
    h = password_hints("short")
    assert "prefer_12_plus_chars" in h
