"""Example function for unit tests."""

def old_sum(xs: list[float]) -> float:
    """return sum of all elements in sx."""
    sum_total: float = 0.0
    idx: int = 0
    while idx <= len(xs) - 1:
        sum_total += xs[idx]
        idx += 1
    return sum_total

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs."""
    sum_total: float = 0.0
    for numbs in range(0, len(xs)):
        sum_total += xs[numbs]
    return(sum_total)