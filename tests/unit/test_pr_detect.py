from app.domain.pr.detect import best_of, is_pr

def test_first_is_pr():
    assert is_pr(weight_kg=100, previous_best=None)

def test_higher_is_pr():
    assert is_pr(weight_kg=110, previous_best=100)

def test_best():
    assert best_of([80, 100, 90]) == 100
