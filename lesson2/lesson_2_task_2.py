def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    return year % 4 == 0


# Пример использования функции
year_to_check = 2024  # Вы можете изменить это значение для проверки
result = is_year_leap(year_to_check)
print(f"год {year_to_check}: {result}")
