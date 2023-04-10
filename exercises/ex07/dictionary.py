"""EX07 - Dictionary Functions."""
__author__ = "730456449"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of inp_dict."""
    new_dict: dict[str, str] = {}
    if inp_dict == {}:
        return "None"
    for x in inp_dict:
        new_dict[inp_dict[x]] = x
    for y in new_dict:
        z: int = 0
        for x in inp_dict:
            if y == inp_dict[x]:
                z += 1
        if z > 1:
            raise KeyError("Inversion could not take place because there would be multiple of a key in the new dictionary.")
    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """With a dictionary of individuals' names and their perefered colors, will return the most popular color."""
    color_count: dict[str, int] = {}
    if inp_dict == {}:
        return "None"
    for x in inp_dict:
        if inp_dict[x] in color_count:
            color_count[inp_dict[x]] += 1
        else:
            color_count[inp_dict[x]] = 1
    top_color: str = ""
    for x in color_count:
        if top_color == "":
            top_color = x
        if color_count[x] > color_count[top_color]:
            top_color = x
    return top_color
            

def count(inp_list: list[str]) -> dict[str, int]:
    """Counts the number of times that a value appeared in inp_dict."""
    ret_dict: dict[str, int] = {}
    if inp_list == ():
        return "None"
    for i in inp_list:
        if i in ret_dict:
            ret_dict[i] += 1
        else:
            ret_dict[i] = 1
    return ret_dict 