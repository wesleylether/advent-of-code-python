from typing import Optional, Tuple

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.list import swap_items

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    ordering = {}
    ordering_numbers, queues = input_file.split("\n\n")
    for order in [order.split("|") for order in ordering_numbers.splitlines()]:
        if order[0] not in ordering:
            ordering[order[0]] = []

        ordering[order[0]].append(int(order[1]))
    return ordering, queues


def check_order(print_order, ordering) -> Optional[Tuple[int, int]]:
    for i, a in enumerate(print_order):
        for j, b in enumerate(print_order[i + 1 :]):
            if str(b) in ordering and a in ordering[str(b)]:
                return i, i + j + 1

    return None


def part_one():
    count = 0
    ordering, queues = parse_input()

    queues = queues.splitlines()
    for queue in queues:
        print_order = [int(x) for x in queue.split(",")]

        result = check_order(print_order, ordering)
        if result is None:
            count += print_order[len(print_order) // 2]
            continue

    return count


def part_two():
    count = 0
    ordering, queues = parse_input()

    queues = queues.splitlines()
    for queue in queues:
        print_order = [int(x) for x in queue.split(",")]

        result = check_order(print_order, ordering)
        if result is None:
            continue

        while result is not None:
            print_order = swap_items(print_order, result[0], result[1])
            result = check_order(print_order, ordering)

        count += print_order[len(print_order) // 2]

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
