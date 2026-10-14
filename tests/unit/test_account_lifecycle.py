from app.domain.user.account import anonymized_email, can_soft_delete

def test_can_soft_delete():
    assert can_soft_delete(is_active=True, is_superuser=False) is True
    assert can_soft_delete(is_active=True, is_superuser=True) is False

def test_anonymized_email():
    assert anonymized_email("abc-123").startswith("deleted-")
