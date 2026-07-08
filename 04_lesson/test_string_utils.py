import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),          # Пространства в начале
    ("   sky pro", "sky pro"),        # Пространства в начале и середине
    ("   skypro   ", "skypro   "),   # Пространства в начале и конце
    ("123", "123"),                  # Без пробелов
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты: удаление начальных пробелов"""
    result = string_utils.trim(input_str)
    assert result == expected, f"{result} ≠ {expected}"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                     # Пустая строка
    ("   ", ""),                 # Только пробелы
    (None, None),               # Некорректный ввод
    ("sky pro", "sky pro"),     # Пробелы в середине не меняются
])
def test_trim_negative(input_str, expected):
    """Негативные тесты: особые случаи"""
    try:
        result = string_utils.trim(input_str)
        assert result == expected, f"{result} ≠ {expected}"
    except AttributeError:
        assert expected is None, "Метод не должен обрабатывать None"


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),           # Первый символ
    ("SkyPro", "o", True),           # Последний символ
    ("SkyPro", "y", True),           # Средний символ
    ("SkyPro", "Sk", True),          # Часть строки
])
def test_contains_positive(input_str, symbol, expected):
    """Символ есть в строке"""
    result = string_utils.contains(input_str, symbol)
    assert result == expected, f"{input_str} не содержит {symbol}"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "z", False),             # Отсутствие символа
    ("SkyPro", "sk", False),            # Регистр важен
    ("", "A", False),                   # Пустая строка
    (None, "A", None),                  # Некорректный ввод
])
def test_contains_negative(input_str, symbol, expected):
    """Символ отсутствует или недопустимый ввод"""
    try:
        result = string_utils.contains(input_str, symbol)
        assert result == expected, f"{input_str} ошибочно содержит {symbol}"
    except AttributeError:
        assert expected is None, "Метод не должен обрабатывать None"


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),                # Одинарный символ
    ("SkyPro", "Pro", "Sky"),                # Слово целиком
    ("SkyPro", "yPr", "So"),                 # Несколько символов подряд
    ("SkyPro", ".", "SkyPro"),               # Символа нет
])
def test_delete_symbol_positive(input_str, symbol, expected):
    """Корректное удаление фрагментов"""
    result = string_utils.delete_symbol(input_str, symbol)
    assert result == expected, f"{input_str} после удаления {symbol} ≠ {expected}"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "A", ""),                         # Пустая строка
    (None, "A", None),                    # Некорректный ввод
    ("SkyPro", "", "SkyPro"),              # Пустой символ для удаления
])
def test_delete_symbol_negative(input_str, symbol, expected):
    """Особые случаи и недопустимый ввод"""
    try:
        result = string_utils.delete_symbol(input_str, symbol)
        assert result == expected, f"{input_str} после удаления {symbol} ≠ {expected}"
    except AttributeError:
        assert expected is None, "Метод не должен обрабатывать None"

