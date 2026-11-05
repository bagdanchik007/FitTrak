from app.domain.validation.positive import is_positive_number

def test_pos():
    assert is_positive_number(1)
    assert not is_positive_number(0)
