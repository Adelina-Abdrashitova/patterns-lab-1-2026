from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from clocks import AnalogClock


def test_1_adapter_regular_time() -> None:
    """Обычное время суток"""
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2026, 11, 7, 15, 42, 30))
    assert clock.get_date_time() == datetime(2026, 11, 7, 15, 42, 30)


def test_2_adapter_midnight_and_end_of_day() -> None:
    """Полночь и последняя секунда суток"""
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2026, 11, 7, 0, 0, 0))
    assert clock.get_date_time() == datetime(2026, 11, 7, 0, 0, 0)

    clock.set_date_time(datetime(2026, 11, 7, 23, 59, 59))
    assert clock.get_date_time() == datetime(2026, 11, 7, 23, 59, 59)


def test_3_adapter_noon_boundary() -> None:
    """Переход AM - PM: 11:59:59, 12:00:00, 13:00:00"""
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2026, 11, 7, 11, 59, 59))
    assert clock.get_date_time() == datetime(2026, 11, 7, 11, 59, 59)

    clock.set_date_time(datetime(2026, 11, 7, 12, 0, 0))
    assert clock.get_date_time() == datetime(2026, 11, 7, 12, 0, 0)

    clock.set_date_time(datetime(2026, 11, 7, 13, 0, 0))
    assert clock.get_date_time() == datetime(2026, 11, 7, 13, 0, 0)


def test_4_adapter_minute_second_boundary() -> None:
    """Последняя минута и секунда часа"""
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2026, 11, 7, 0, 59, 59))
    assert clock.get_date_time() == datetime(2026, 11, 7, 0, 59, 59)


def test_5_adapter_leap_day() -> None:
    """29 февраля високосного года"""
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2024, 2, 29, 23, 59, 59))
    assert clock.get_date_time() == datetime(2024, 2, 29, 23, 59, 59)