"""EX07- Dictionary Functions Unit Tests."""
__author__ = "730546449"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest


def test_invert_empty() -> None:
    """Testing to see what invert should do with a given empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == "None"


def test_invert_capital() -> None:
    """Testing to make sure that invert with values and keys that are capitalized."""
    test_dict: dict[str, str] = {"Apple": "Jack"}
    assert invert(test_dict) == {"Jack": "Apple"}


def test_invert_key_value_same() -> None:
    """Testing to make sure that invert will invert even if individual keys and values of the inp_dict are the same."""
    test_dict: dict[str, str] = {"a": "a"}
    assert invert(test_dict) == {"a": "a"}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Testing to see what favorite_color should do with a given empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == "None"


def test_favorite_color_capital_keys() -> None:
    """Testing to make sure that favorite_color with keys capitalized from inp_dict."""
    test_dict: dict[str, str] = {"Jack": "blue", "Maya": "blue", "Grace": "green"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_capital_values() -> None:
    """Testing to make sure that favorite_color with values capitalized from inp_dict."""
    test_dict: dict[str, str] = {"jack": "Blue", "maya": "Blue", "grace": "Green"}
    assert favorite_color(test_dict) == "Blue"


def test_count_empty() -> None:
    """Testing to see what count should do with a given empty list."""
    test_list: list[str] = ()
    assert count(test_list) == "None"


def test_count_all_same() -> None:
    """Testing to see what count should do if the given list values are all the same."""
    test_list: list[str] = ("blue", "blue", "blue")
    assert count(test_list) == {"blue": 3}


def test_count_all_different() -> None:
    """Testing to see what count should do if the given list values are all different."""
    test_list: list[str] = ("blue", "yellow", "red")
    assert count(test_list) == {"blue": 1, "yellow": 1, "red": 1}