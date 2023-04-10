"""Uniit Tests for EX05 - 'list' Utility Functions."""
__author__ = "730546449"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_given_empty() -> None:
    """Testing to see what only evens function should do with a given empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_only_odds() -> None:
    """Testing to make sure that only evens function doesn't return odd values of the given list."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_only_evens_only_evens() -> None:
    """Testing to make sure that only evens function returns even values of the given list."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_sub_start_idx() -> None:
    """Testing to make sure that start index is initialized to 0 if inputed as a negative."""
    test_list: list[int] = [1, 2, 3]
    assert sub(test_list, -2, 2) == [1, 2]


def test_sub_with_negatives() -> None:
    """Testing to see if sub function will work with negative values in the given list."""
    test_list: list[int] = [-2, -3, -4, -5]
    assert sub(test_list, 1, 3) == [-3, -4]


def test_sub_empty() -> None:
    """Testing to see if sub function will work with empty."""
    test_list: list[int] = []
    assert sub(test_list, 1, 3) == []


def test_concat_1_empty_list() -> None:
    """Testing to see if concat function will concatonate with an empty list."""
    test_list1: list[int] = []
    test_list2: list[int] = [1, 2]
    assert concat(test_list1, test_list2) == [1, 2]


def test_concat_same_lens() -> None:
    """Testing to see if concat function will concatonate two lists of the same length."""
    test_list1: list[int] = [1, 2]
    test_list2: list[int] = [3, 4]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4]


def test_concat_2_empty_lists() -> None:
    """Testing to see if concat function will concatonate two lists that are empty."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []