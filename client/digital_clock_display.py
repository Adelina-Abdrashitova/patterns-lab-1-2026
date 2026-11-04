from interfaces import BaseDigitalClock


class DigitalClockDisplay:
    """Пример клиента, ожидающего цифровой интерфейс."""

    def __init__(self, clock: BaseDigitalClock) -> None:
        self._clock = clock

    def render(self) -> str:
        return self._clock.get_date_time().strftime("%Y-%m-%d %H:%M:%S")
