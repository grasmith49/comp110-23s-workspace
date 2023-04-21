from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with collumn headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(data: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Generates a column-based table with only the first rows of data for each column."""
    ret_dict: dict[str, list[str]] = {}
    for col in data:
        first_N: list[str] = []
        if N >= len(data[col]):
            ret_dict = data
            return ret_dict
        for x in range(N):
            first_N.append(data[col][x])
        ret_dict[col] = first_N
    return ret_dict 


def select(data: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Generates a column-based table with only a specific subset of the original columns."""
    ret_dict: dict[str, list[str]] = {}
    for col in column_names:
        ret_dict[col] = data[col]
    return ret_dict


def concat(data1: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Generates a column-based table from two column-based tables."""
    ret_dict: dict[str, list[str]] = {}
    for col in data1:
        ret_dict[col] = data1[col]
    for col in data2:
        if col in ret_dict:
            ret_dict[col] += data2[col]
        else:
            ret_dict[col] = data2[col]
    return ret_dict


def count(freq: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value is associated with the frequency of that value in the input list."""
    ret_dict: dict[str, int] = {}
    for item in freq:
        if item in ret_dict:
            ret_dict[item] += 1
        else:
            ret_dict[item] = 1
    return ret_dict