from app.domain.progress.services import format_pr_label, is_new_personal_record


def test_is_new_personal_record():
    assert is_new_personal_record(None, 100) is True
    assert is_new_personal_record(100, 101) is True
    assert is_new_personal_record(100, 99) is False


def test_format_pr_label():
    assert "Bench" in format_pr_label("Bench", 80, 3)
