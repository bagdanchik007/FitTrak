from app.domain.notification.unread import unread_count

def test_unread():
    assert unread_count([True, False, True]) == 2
