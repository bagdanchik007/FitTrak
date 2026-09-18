"""Simple in-process counters for demo observability."""

from threading import Lock

_lock = Lock()
_counters: dict[str, int] = {}


def incr(name: str, amount: int = 1) -> None:
    with _lock:
        _counters[name] = _counters.get(name, 0) + amount


def get(name: str) -> int:
    with _lock:
        return _counters.get(name, 0)


def snapshot() -> dict[str, int]:
    with _lock:
        return dict(_counters)
