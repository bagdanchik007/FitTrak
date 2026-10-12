from app.domain.notification.services import notification_priority, sort_notifications

def test_notification_priority():
    assert notification_priority("security") < notification_priority("tip")

def test_sort_notifications():
    items = [{"kind": "tip", "created_at": "b"}, {"kind": "goal", "created_at": "a"}]
    ordered = sort_notifications(items)
    assert ordered[0]["kind"] == "goal"
