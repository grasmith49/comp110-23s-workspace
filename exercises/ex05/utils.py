"""EX05 - 'list' Utility Functions."""
__author__ = "730546449"


def only_evens(given: list[int]) -> list[int]:
    """Given a list of integers, return a list of the even integers within the given list."""
    evens: list[int] = list()
    odds: list[int] = list()
    for numbs in range(0, len(given)):
        if given[numbs] % 2 == 0:
            evens.append(given[numbs])
        else:
            odds.append(given[numbs])
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists of ints, return a new list that has all elements of the first list followed by all elements of second list."""
    new_list: list[int] = list()
    for numbs in range(0, len(list_1)):
        new_list.append(list_1[numbs])
    for numbs in range(0, len(list_2)):
        new_list.append(list_2[numbs])
    return new_list


def sub(given: list[int], start_idx: int, end_idx: int):
    """Given a list of ints, start index, and end index (non-inclusive) generates a list of the subset of the given list between given start and end indicies."""
    new_list: list[int] = list()
    if start_idx < 0:
        start_idx = 0
    if len(given) < end_idx:
        end_idx = len(given)
    for numbs in range(start_idx, end_idx):
        new_list.append(given[numbs])
    return new_list
