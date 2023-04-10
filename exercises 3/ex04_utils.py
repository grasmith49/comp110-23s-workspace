"""EX04 - 'list' Utility Functions."""
__author__ = "730546449"


def all(check_list: list[int], check_int: int) -> bool:
    """Check to see if check_int matches all indicies of check_list."""
    if len(check_list) == 0:
        return False
    list_idx: int = 0
    checking: bool = True
    while list_idx < len(check_list) - 1 and checking is True:
        if check_list[list_idx] == check_int:
            checking = True
        else:
            return False
        list_idx += 1
    return True


def max(check_list: list[int]) -> int:
    """Given a list of integers, check to find the largest number in the list."""
    if len(check_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0 
    max_int: int = 0
    if check_list[idx] > check_list[idx + 1]:
        max_int = check_list[idx]
    else:
        max_int = check_list[idx + 1]
    idx += 1
    while idx < len(check_list) - 1:
        if max_int < check_list[idx + 1]:
            max_int = check_list[idx + 1]
        idx += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check to see if two given list of iintegers are equal to eachother."""
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx <= len(list1) - 1 and idx <= len(list2) - 1:
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True
