"""Lightweight in-process domain event stubs (portfolio extension point)."""

from collections import defaultdict
from collections.abc import Callable, Awaitable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class DomainEvent:
    name: str
    payload: dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


EventHandler = Callable[[DomainEvent], Awaitable[None]]

_handlers: dict[str, list[EventHandler]] = defaultdict(list)


def subscribe(event_name: str, handler: EventHandler) -> None:
    _handlers[event_name].append(handler)


async def publish(event: DomainEvent) -> None:
    for handler in _handlers.get(event.name, []):
        await handler(event)
