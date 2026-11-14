
from app.domain.steps.estimate import distance_km_from_steps, steps_from_distance_km

def test_steps():
    s = steps_from_distance_km(distance_km=1.0, height_cm=170)
    assert s > 0
    assert distance_km_from_steps(steps=s, height_cm=170) > 0
