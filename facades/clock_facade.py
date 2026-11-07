"""
Здесь необходимо реализовать Facade.

Фасад должен скрывать работу как минимум с:
- цифровым адаптером;
- ClockFormatter;
- ClockHistory.
"""
from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from services import ClockFormatter, ClockHistory


# TODO: реализуйте ClockFacade.

class ClockFacade:
    def __init__(self, clock:DigitalClockAdapter, formatter:ClockFormatter, history:ClockHistory):
        self.clock = clock
        self.formatter = formatter
        self.history = history

    def set_time(self, date: datetime) -> None:
        """установка текущих даты и времени"""
        self.clock.set_date_time(date)
        self.history.add(date)

    def get_time(self) -> datetime:
        """Получение текущих даты и времени"""
        return self.clock.get_date_time()

    def get_time_format(self) -> str:
        """Получение форматированного представления"""
        return self.formatter.format(self.get_time())

    def get_time_history(self) -> tuple[datetime, ...]:
        """Получение истории изменений"""
        return self.history.all()




