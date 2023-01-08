# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, color: str, car_model: str, count_door: int):
        """
            Метод - констркутор. Инициализирует объект значениями.
            Принимает на вход цвет, модель и количество дверей автомобиля.
            >>> BMW = Car("Черный", 'BMW X5', 4)
        """
        self.color = color
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str.')
        self.car_model = car_model
        if not isinstance(car_model, str):
            raise TypeError('Модель автомобиля должна быть типа str.')
        self.count_door = count_door
        if count_door <= 0:
            raise TypeError('У автомобиля не может быть ни одной двери.')

    def print_info(self):
         """Метод печатает информацию об автомобиле."""
         print(f'Автомобиль - {self.car_model}, цвет - {self.color}, количество дверей -  {self.count_door} ')

    def fuel(self, way, speed):
        """Метод рассчитывает затраты топлива на определенный путь."""
        if way < 0:
            raise ValueError('Скорость не может быть отрицательным числом!')
        if 230 < speed or speed < 0:
            raise ValueError('Скорость не может быть отрицательным числом или больше 230 км/ч!')
        ...

class Ship:
    def __init__(self, ship_name: str, passengers: int):
        """
            Метод - констркутор. Инициализирует объект значениями.
            Принимает на вход название, количество пассажиров.
                   >>> Maria = Ship('Maria', 30)
                   >>> Maria.check_passengers(80)
                   False
                """
        if not isinstance(ship_name, str):
            raise TypeError("Название корабля должно быть типа str.")
        self.ship_name = ship_name
        if passengers < 27:
            raise ValueError("Количество пассажиров на борту должно быть больше 27")
        self.passengers = passengers

    def print_info(self):
        """Метод печатает информацию о корабле."""
        print(f'Корабль - {self.ship_name}. Количество пассажиров - {self.passengers} человек')

    def check_passengers(self, passengers_to_arrive):
        """Метод проверяет, хватит ли количества человек для отправки.
           Принимает на вход требуемое количество человек для отправления.
        """
        return self.passengers >= passengers_to_arrive

class Armchair:
    def __init__(self, weight: [int, float], length: [int, float]):
        """
            Метод - констркутор. Инициализирует объект значениями.
            Принимает на вход ширину, длину кресла.
            >>> armchair_1 = Armchair(50, 70)
        """
        if not isinstance(weight, (int, float)):
            raise TypeError('Ширина кресла может быть только целым или дробным числом.')
        if not isinstance(length, (int, float)):
            raise TypeError('Длина кресла может быть только целым или дробным числом.')
        if weight < 0:
            raise ValueError('Ширина не может быть отрицательным числом!')
        if length < 0:
            raise ValueError('Длина не может быть отрицательным числом!')
        self.weight = weight
        self.length = length

    def print_info(self):
        """Метод печатает информацию о кресле."""
        print(f'Размер кресла - {self.weight}X{self.length}')

    def check_room(self, room_weight, room_length):
        """Метод анализирует, поместится ли кресло в комнате.
           Принимает на вход ширину и длину комнаты.
        """
        if not isinstance(room_weight, (int, float)):
            raise TypeError('Ширина комнаты может быть только целым или дробным числом!')
        if not isinstance(room_length, (int, float)):
            raise TypeError('Длина комнаты может быть только целым или дробным числом!')
        ...


if __name__ == "__main__":  # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    BMW = Car("Черный", 'BMW X5', 4)
    ship_1 = Ship('Elsa', 54)
    doctest.testmod()
    pass
