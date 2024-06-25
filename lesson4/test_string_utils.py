import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize('str1, result', [('skypro', 'Skypro'), ('1abc', '1abc'), ('привет', 'Привет'), ("", ""), (" ", " ") ])
def testCapitalize(str1, result):
    res = string_utils.capitilize(str1)
    assert res == result

def testTrim():
    string_utils = StringUtils()
    res = string_utils.trim("   skypro")
    assert res == "skypro"

@pytest.mark.parametrize('string, delimeter, result', 
    [("a,b,c,d", ",", ["a", "b", "c", "d"]), 
     ("1:2:3", ":", ["1", "2", "3"]),
     ("ф й ц т", " ", ["ф", "й", "ц", "т"]),
     ("", None, []),
     (" ", ",", [" "]),
     ("1,2,3,4", None, ["1", "2", "3", "4"])])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = string_utils.to_list(string)
    else:
        res = string_utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',
    [("кот", "т", True), ("987456", "4", True), ("Иван-чай", "-", True), ("dog", "d", True), ("красивый подарок", " ", True),
    ("яблоко", "а", False), ("12345", "6", False), ("Cat", "U", False), ("", "ф", False), (" ", "", False)])
def test_contains(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result',
    [("Картофель", "тофель", "Кар"), ("Potato", "Po", "tato"), ("гоголь-моголь", "-", "гогольмоголь"), ("хорошая погода", " ", "хорошаяпогода"),
    ("Клубника", "вм", "Клубника"), ("1256", "48", "1256"), ("abc", "", "abc")])
def test_delete_symbol(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result',
    [("Cat", "C", True), ("1,2,3,4", "1", True),
     ("Cat", "G", False), ("1,2,3,4", "5", False), ("abc", "", False)])
def test_starts_with(string, symbol, result):
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result',
    [("Cat", "t", True), ("1,2,3,4", "4", True),
     ("Cat", "i", False), ("1,2,3,4", "5", False), ("abc", "", False)])
def test_end_with(string, symbol, result):
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result',
    [("", True), (" ", True),
    ("Cat", False), ("1,2,3,4", False), ("-", False)])
def test_is_empty(string, result):
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result',[([1,2,3,4], ",", "1,2,3,4"), 
        (["Кото", "Пес"], ",", "Кото,Пес"),
        (["Темно", "Черный"], "-", "Темно-Черный"), ([], ",", "")])
def test_list_to_string(lst, joiner, result):
    res = string_utils.list_to_string(lst, joiner)
    assert res == result

