from uuid import uuid4

from app.core.security_policies import can_modify_exercise, is_owner


def test_is_owner():
    uid = uuid4()
    assert is_owner(uid, uid) is True
    assert is_owner(uuid4(), uid) is False
    assert is_owner(None, uid) is False


def test_can_modify_exercise():
    owner = uuid4()
    other = uuid4()
    assert can_modify_exercise(owner, owner) is True
    assert can_modify_exercise(owner, other) is False
    assert can_modify_exercise(None, owner) is False
    assert can_modify_exercise(None, owner, is_superuser=True) is True
