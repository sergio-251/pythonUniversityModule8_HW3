# Создание исключений
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self):
        self.message = 'Неверная длина номера'


class Car:
    def __init__(self, model, vin_number, numbers):
        if self.__is_valid_vin(vin_number) and self.___is_valid_numbers(numbers):
            self.model = model
            self.__vin = vin_number
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int): raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number not in range(1000000, 10000000): raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def ___is_valid_numbers(self, numbers):
        if not isinstance(numbers, str) or len(numbers) != 6: raise IncorrectVinNumber('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
