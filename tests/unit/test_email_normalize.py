from app.domain.auth.email_normalize import normalize_email

def test_email():
    assert normalize_email("  Foo@Bar.COM ") == "foo@bar.com"
