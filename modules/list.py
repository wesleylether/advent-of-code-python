def swap_items(lst: list, i: int, j: int) -> list:
    lst[i], lst[j] = lst[j], lst[i]
    return lst
