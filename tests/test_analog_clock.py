from clocks import AnalogClock
from consts import DayNightDivision


def test_analog_clock_stores_values() -> None:
    clock = AnalogClock()
    clock.set_date_time(
        year=2026,
        month=9,
        day=24,
        hour_angle=90.0,
        minute_angle=180.0,
        second_angle=270.0,
        day_night_division=DayNightDivision.PM,
    )

    assert clock.get_year() == 2026
    assert clock.get_month() == 9
    assert clock.get_day() == 24
    assert clock.get_hour_angle() == 90.0
    assert clock.get_minute_angle() == 180.0
    assert clock.get_second_angle() == 270.0
    assert clock.get_day_night_division() is DayNightDivision.PM
