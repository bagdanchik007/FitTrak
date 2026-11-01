from app.domain.plan.split import next_split_day

def test_rotation():
    assert next_split_day("push") == "pull"
