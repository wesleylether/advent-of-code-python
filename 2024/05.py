from typing import Optional, Tuple

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.list import swap_items

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

ordering = {}
ordering_numbers, queues = input_file.split("\n\n")
for order in [order.split("|") for order in ordering_numbers.split("\n")]:
    if order[0] not in ordering:
        ordering[order[0]] = []

    ordering[order[0]].append(int(order[1]))


def check_order(print_order) -> Optional[Tuple[int, int]]:
    for i, a in enumerate(print_order):
        for j, b in enumerate(print_order[i + 1 :]):
            if str(b) in ordering and a in ordering[str(b)]:
                return i, i + j + 1

    return None


queues = queues.split("\n")
for queue in queues:
    print_order = [int(x) for x in queue.split(",")]

    result = check_order(print_order)
    if result is None:
        p1 += print_order[len(print_order) // 2]
        continue

    while result is not None:
        print_order = swap_items(print_order, result[0], result[1])
        result = check_order(print_order)

    p2 += print_order[len(print_order) // 2]


# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
