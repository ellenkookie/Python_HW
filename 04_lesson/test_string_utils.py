import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ---------- 1. capitalize() ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),
    ("HELLO", "Hello"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("123", "123"),
    ("!@#", "!@#"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ---------- 2. trim() ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("\tpython", "\tpython"),  # табуляция НЕ удаляется (только пробелы)
    ("no_spaces", "no_spaces"),
    ("   123", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("abc   ", "abc   "),  # пробелы в конце НЕ удаляются
    ("   a", "a"),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ---------- 3. contains() ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("Hello world", "o", True),
    ("12345", "3", True),
    ("test", "test", True),
    (" ", " ", True),  # пробел как символ
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("Hello", "x", False),
    ("", "a", False),      # пустая строка не содержит символ
    ("abc", "", True),     # пустая подстрока есть ВСЕГДА
    ("", "", True),        # пустое в пустом = True
    ("SkyPro", " ", False),
    ("   ", "a", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# ---------- 4. delete_symbol() ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello world", "o", "Hell wrld"),
    ("12345", "3", "1245"),
    ("aaaaa", "a", ""),
    ("test", "t", "es"),
    ("   ", " ", ""),  # удалить все пробелы
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),     # символ не найден
    ("", "a", ""),                 # пустая строка
    ("", "", ""),                 # пустая строка, пустой символ
    ("hello", "", "hello"),       # удаление пустоты = ничего не меняется
    ("abc", "abc", ""),          # удалить всю строку
    ("!!!", "!", ""),           # удалить все спецсимволы
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected