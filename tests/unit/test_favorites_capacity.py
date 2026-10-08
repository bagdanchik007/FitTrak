from app.domain.favorite.services import favorites_capacity_hint

def test_favorites_capacity_hint():
    assert favorites_capacity_hint(10) == "ok"
    assert favorites_capacity_hint(45) == "near_capacity"
    assert favorites_capacity_hint(50) == "at_capacity"
