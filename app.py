from clocks import AnalogClock


def main() -> None:
    clock = AnalogClock()
    print("Исходный объект AnalogClock создан.")
    print(f"Дата по умолчанию: {clock.get_year():04d}-{clock.get_month():02d}-{clock.get_day():02d}")
    print("После выполнения задания клиентский код должен работать через ClockFacade.")


if __name__ == "__main__":
    main()
