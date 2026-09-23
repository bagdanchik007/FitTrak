from app.core.feature_flags import FEATURES, is_enabled


def test_known_flags():
    assert is_enabled("journal") is True
    assert is_enabled("not_a_real_flag") is False
    assert "streaks" in FEATURES
