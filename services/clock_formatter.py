from datetime import datetime


class ClockFormatter:
    def format(self, value: datetime, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        return value.strftime(fmt)
