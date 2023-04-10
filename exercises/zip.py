"""Challenge Question 04 - Dict Function Writing."""
__author__ = "730546449"


def zip(str_list: list[str], int_list: list[int]) -> None:
    """With a list of strings and a list of integers, produces dictionary where keys are items of the first list and values are corresponding items at the same index of the second list."""
    returned_list: dict[str, int] = {}
    idx: int = 0
    if len(str_list) != len(int_list):
        return returned_list
    while idx < len(str_list):
        returned_list[str_list[idx]] = int_list[idx]
        idx += 1
    return returned_list