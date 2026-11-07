from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from clocks import AnalogClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def test_facade() -> None:
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )

    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))
    assert facade.get_time() == datetime(2026, 11, 7, 15, 42, 30)
    assert facade.get_time_format() == f"{datetime(2026, 11, 7, 15, 42, 30):%d.%m.%Y %H:%M:%S}"

    facade.set_time(datetime(2027, 11, 7, 15, 42, 30))
    assert len(facade.get_time_history()) == 2