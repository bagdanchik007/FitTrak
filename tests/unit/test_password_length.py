from app.domain.auth.password_length import meets_min_length

def test_len():
    assert meets_min_length("12345678")
    assert not meets_min_length("short")
