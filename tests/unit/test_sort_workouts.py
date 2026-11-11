from app.domain.workout.list_sort import sort_workouts_desc

def test_sort():
    items = [{"performed_at": "2026-01-01"}, {"performed_at": "2026-02-01"}]
    out = sort_workouts_desc(items)
    assert out[0]["performed_at"] == "2026-02-01"
