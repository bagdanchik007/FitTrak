from types import SimpleNamespace
from app.domain.workout.services import average_rpe

def test_average_rpe():
    sets = [SimpleNamespace(rpe=8), SimpleNamespace(rpe=9), SimpleNamespace(rpe=None)]
    assert average_rpe(sets) == 8.5
