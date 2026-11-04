from datetime import datetime

from services import ClockFormatter, ClockHistory


def test_formatter() -> None:
    value = datetime(2026, 9, 24, 12, 34, 56)
    assert ClockFormatter().format(value) == "24.09.2026 12:34:56"


def test_history_returns_tuple() -> None:
    history = ClockHistory()
    value = datetime(2026, 9, 24, 12, 34, 56)
    history.add(value)

    assert history.all() == (value,)
