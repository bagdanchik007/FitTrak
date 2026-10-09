from app.domain.user.services import display_name

def test_display_name():
    assert display_name("Ada Lovelace", "ada@x.com") == "Ada Lovelace"
    assert display_name(None, "ada@x.com") == "ada"
