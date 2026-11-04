from abc import ABC, abstractmethod
from datetime import datetime


class BaseDigitalClock(ABC):
    @abstractmethod
    def set_date_time(self, date: datetime) -> None:
        """Устанавливает дату и время."""
        raise NotImplementedError

    @abstractmethod
    def get_date_time(self) -> datetime:
        """Возвращает дату и время как datetime."""
        raise NotImplementedError
