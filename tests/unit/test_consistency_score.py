from app.application.services.consistency_service import consistency_report
from app.domain.streak.services import consistency_score


def test_consistency_score():
    assert consistency_score(14, 28) == 0.5
    assert consistency_score(30, 28) == 1.0


def test_consistency_report_band():
    assert consistency_report(20, 28)["band"] == "high"
    assert consistency_report(2, 28)["band"] == "low"
