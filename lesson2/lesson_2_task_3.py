import math


def square(side):
    """Вычисляет площадь квадрата,округляя результат вверх при необходимости"""
    area = side * side
    # Проверяем, является ли сторона целым числом.
    # isinstance(5.0, int) -> False, поэтому используем сравнение с int(side)
    if side != int(side):
        return math.ceil(area)
    return area


# Пример вызова функции
print(square(5))  # Выведет: 25
print(square(5.5))  # Выведет: 31 (округление вверх от 30.25)
