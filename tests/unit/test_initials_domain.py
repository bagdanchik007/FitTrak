from app.domain.text.initials import initials

def test_init():
    assert initials("Ada Lovelace") == "AL"
