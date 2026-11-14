
from app.domain.nutrition.mets import met_for

def test_met():
    assert met_for("running") > met_for("walking")
