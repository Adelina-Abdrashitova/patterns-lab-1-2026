from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from clocks import AnalogClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def main() -> None:
    facade = ClockFacade(
        clock=DigitalClockAdapter(AnalogClock()),
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )
    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))

    print("Исходный объект ClockFacade создан.")
    print(f"Дата по умолчанию: {facade.get_time():%Y-%m-%d}")
    print(f"Дата форматированного представления: {facade.get_time_format()}")
    print(f"История изменений: {facade.get_time_history()}")


if __name__ == "__main__":
    main()
