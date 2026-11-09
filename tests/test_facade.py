from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from clocks import AnalogClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def test_1_facade_set_and_get_time() -> None:
    """Установка и получение времени"""
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )

    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))
    assert facade.get_time() == datetime(2026, 11, 7, 15, 42, 30)


def test_2_facade_formatted_time() -> None:
    """Форматированное представление"""
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )

    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))
    assert facade.get_time_format() == f"{datetime(2026, 11, 7, 15, 42, 30):%d.%m.%Y %H:%M:%S}"


def test_3_facade_history() -> None:
    """История изменений"""
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )

    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))
    facade.set_time(datetime(2027, 11, 7, 15, 42, 30))
    assert len(facade.get_time_history()) == 2


def test_4_facade_empty_history() -> None:
    """Пустая история"""
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )

    assert facade.get_time_history() == ()