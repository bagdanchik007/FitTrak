"""Pure check mirroring goals update auto-complete rule."""


def should_auto_complete(target: float | None, current: float | None) -> bool:
    if target is None or current is None:
        return False
    return current >= target


def test_auto_complete_rule():
    assert should_auto_complete(100, 100) is True
    assert should_auto_complete(100, 99) is False
    assert should_auto_complete(None, 50) is False
