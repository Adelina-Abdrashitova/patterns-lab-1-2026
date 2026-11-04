from abc import ABC, abstractmethod

from consts import DayNightDivision


class BaseAnalogClock(ABC):
    @abstractmethod
    def set_date_time(
        self,
        year: int,
        month: int,
        day: int,
        hour_angle: float,
        minute_angle: float,
        second_angle: float,
        day_night_division: DayNightDivision,
    ) -> None:
        """
        Устанавливает текущие дату и время.
        """
        raise NotImplementedError

    @abstractmethod
    def get_hour_angle(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_minute_angle(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_second_angle(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_year(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_month(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_day(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_day_night_division(self) -> DayNightDivision:
        raise NotImplementedError
