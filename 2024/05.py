from typing import Optional, Tuple

from modules.advent_of_code import solve
from modules.list import List


# Start coding here
# ==========================================================================
def parse(data):
    ordering = {}
    ordering_numbers, queues = data.split("\n\n")
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


def part_one(data):
    count = 0
    ordering, queues = data

    queues = queues.splitlines()
    for queue in queues:
        print_order = [int(x) for x in queue.split(",")]

        result = check_order(print_order, ordering)
        if result is None:
            count += print_order[len(print_order) // 2]
            continue

    return count


def part_two(data):
    count = 0
    ordering, queues = data

    queues = queues.splitlines()
    for queue in queues:
        print_order = List([int(x) for x in queue.split(",")])

        result = check_order(print_order, ordering)
        if result is None:
            continue

        while result is not None:
            print_order.swap_items(result[0], result[1])
            result = check_order(print_order, ordering)

        count += print_order[len(print_order) // 2]

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
