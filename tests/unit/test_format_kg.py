from app.domain.body_weight.format_kg import format_kg

def test_fmt():
    assert format_kg(80.25) == "80.3 kg"
