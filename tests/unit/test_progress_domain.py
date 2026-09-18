from uuid import uuid4

from app.domain.progress.entities import PersonalRecord
from app.domain.progress.services import sort_prs_by_weight, top_n_prs


def test_top_n_prs():
    prs = [
        PersonalRecord(uuid4(), "A", 50, 5, None, None),
        PersonalRecord(uuid4(), "B", 100, 3, None, None),
        PersonalRecord(uuid4(), "C", 80, 4, None, None),
    ]
    top = top_n_prs(prs, 2)
    assert top[0].max_weight_kg == 100
    assert top[1].max_weight_kg == 80
    assert len(sort_prs_by_weight(prs)) == 3
