from app.domain.account.soft_delete_copy import soft_delete_confirm_label, soft_delete_warning

def test_copy():
    assert "deactivate" in soft_delete_warning().lower() or "account" in soft_delete_warning().lower()
    assert soft_delete_confirm_label()
