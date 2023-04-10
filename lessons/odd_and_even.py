"""Practice writing functions for Quiz 02."""

def odd_and_even(list_1: list[int]) -> list[int]:
    """Returns list with elements of input list that are odd and have an even index."""
    i: int = 0
    list_2: list[int] = []
    while i < len(list_1):
        if i % 2 == 0:
            if list_1[i] % 2 != 0:
                list_2.append(list_1[i])
                i += 1
        i += 1
    return list_2