from datetime import datetime


class ClockHistory:
    def __init__(self) -> None:
        self._items: list[datetime] = []

    def add(self, value: datetime) -> None:
        self._items.append(value)

    def all(self) -> tuple[datetime, ...]:
        return tuple(self._items)
