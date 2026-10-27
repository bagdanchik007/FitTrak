from app.domain.ai.services import infer_focus_from_title, infer_focuses_from_titles

def test_infer_push():
    assert infer_focus_from_title("Push Day") == "push"

def test_infer_list():
    assert "legs" in infer_focuses_from_titles(["Leg Day", "Random"])
