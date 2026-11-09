from app.domain.text.slugify import slugify

def test_slug():
    assert slugify("Push Day!") == "push-day"
