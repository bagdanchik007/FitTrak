from app.domain.summary.services import SessionStats, average_volume_per_workout, merge_session_stats


def test_merge_session_stats():
    merged = merge_session_stats(
        [SessionStats(sets=3, volume_kg=100, duration_minutes=30), SessionStats(sets=2, volume_kg=50.5, duration_minutes=20)]
    )
    assert merged.sets == 5
    assert merged.volume_kg == 150.5
    assert merged.duration_minutes == 50


def test_average_volume():
    assert average_volume_per_workout(300, 3) == 100.0
    assert average_volume_per_workout(10, 0) == 0.0
