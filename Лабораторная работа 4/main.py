if __name__ == "__main__":
    import datetime


    class Vehicle:
        """Базовый класс транспортного средства."""

        def __init__(self, make: str, model: str, year: int, weight: float) -> None:
            """
            Конструктор класса Vehicle. Инициализирует объект первоначальными свойствами
            :param make: Марка
            :param model: Модель
            :param year: Год выпуска
            :param weight: Вес
            """
            self.make = make
            self.model = model
            self.year = year
            self.weight = weight

        def __str__(self) -> str:
            """
            Магический метод для строкового представления объекта
            Возвращает читаемую строку с информацией об объекте
            """
            return f'{self.make} {self.model} ({self.year}) весом {self.weight} кг.'

        def __repr__(self) -> str:
            """
            Магический метод для определения поведения функции repr()
            Метод возвращает строку, показывающую, как может быть инициализирован экземпляр
            """
            return f'Vehicle({self.make!r}, {self.model!r}, {self.year}, {self.weight})'

        def how_old(self) -> int:
            """Метод возвращает возраст транспортного средства."""
            return datetime.date.today().year - self.year

        def print_info(self) -> None:
            """Метод возвращает информацию о транспортном средстве."""
            print(f'Транспортное средство - {self.make} {self.model}\nГод выпуска: {self.year}\nВес ТС: {self.weight}')


    class Car(Vehicle):
        """
        Класс для создания объектов легкового автомобиля
        Является наследником класса Vehicle
        """

        def __init__(self, make: str, model: str, year: int, weight: float, fuel_consumption: float,
                     gas_tank: float) -> None:
            """
            Конструктор класса Car. Инициализирует объект первоначальными свойствами
            :param make: Марка
            :param model: Модель
            :param year: Год выпуска
            :param weight: Вес
            :param fuel_consumption: Расход топлива
            :param gas_tank: Бензобак
            """
            super().__init__(make, model, year, weight)
            self.fuel_consumption = fuel_consumption
            self.gas_tank = gas_tank

        def __str__(self) -> str:
            return f'{self.make} {self.model} ({self.year})\nРасход топлива: {self.fuel_consumption}л/100км'

        def __repr__(self) -> str:
            return f'Car({self.make!r}, {self.model!r}, {self.year}, {self.weight}, {self.fuel_consumption}, {self.gas_tank})'

        def how_much_we_can_drive(self) -> float:
            """
            Метод рассчитывает, какое расстояние может преодолеть
            автомобиль с полным баком при среднем расходе топлива
            """
            return self.gas_tank / self.fuel_consumption * 100

        def print_info(self) -> None:
            """
            Метод возвращает информацию о легковом автомобиле
            Перегрузили метод, так как есть дополнительная информация
            """
            print(
                f'Легковой автомобиль - {self.make} {self.model}\n',
                f'Год выпуска: {self.year}\n',
                f'Вес автомобиля: {self.weight} кг.\n',
                f'Расход топлива: {self.fuel_consumption}л/100км\n',
                f'Бензобак вместительностью: {self.gas_tank} л.',
                sep='')


    class Truck(Vehicle):
        """
        Класс для создания объектов грузового автомобиля
        Является наследником класса Vehicle
        """

        def __init__(self, make: str, model: str, year: int, weight: float, load_capacity: float) -> None:
            """

            Конструктор класса Truck. Инициализирует объект первоначальными свойствами
            :param make: Марка
            :param model: Модель
            :param year: Год выпуска
            :param weight: Вес
            :param load_capacity: Грузоподъемность
            """
            super().__init__(make, model, year, weight)
            self.load_capacity = load_capacity

        def __str__(self) -> str:
            return f'{self.make} {self.model} ({self.year})\nГрузоподъемность: {self.load_capacity} кг'

        def __repr__(self) -> str:
            return f'Truck({self.make!r}, {self.model!r}, {self.year}, {self.weight}, {self.load_capacity})'

        def able_to_lift(self, weight: float) -> bool:
            """Метод определяет, сможет ли грузовой автомобиль перевезти данный вес."""
            return self.load_capacity >= weight

        def print_info(self) -> None:
            """
            Метод возвращает информацию о грузовом автомобиле
            Перегрузили метод, так как есть дополнительная информация
            """
            print(
                f'Грузовой автомобиль - {self.make} {self.model}\n',
                f'Год выпуска: {self.year}\n',
                f'Вес автомобиля: {self.weight} кг.\n',
                f'Грузоподъемность: {self.load_capacity} кг.',
                sep='')
