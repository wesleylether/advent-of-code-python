import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from functools import lru_cache
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input, dd

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

containers = sorted(map(int, input_file.splitlines()))


@lru_cache(maxsize=None)
def count_combinations(target, index):
    if target == 0:
        return 1
    if target < 0 or index == len(containers):
        return 0
    return count_combinations(target - containers[index], index + 1) + count_combinations(
        target, index + 1
    )


@lru_cache(maxsize=None)
def count_minimum_combinations(target, index, used):
    if target == 0:
        return used
    if target < 0 or index == len(containers):
        return float("inf")
    return min(
        count_minimum_combinations(target - containers[index], index + 1, used + 1),
        count_minimum_combinations(target, index + 1, used),
    )


@lru_cache(maxsize=None)
def count_exact_combinations(target, index, used, min_used):
    if target == 0:
        return 1 if used == min_used else 0
    if target < 0 or index == len(containers):
        return 0
    return count_exact_combinations(
        target - containers[index], index + 1, used + 1, min_used
    ) + count_exact_combinations(target, index + 1, used, min_used)


# Print the answers here
# ==========================================================================
answer_part_one(count_combinations(150, 0))

min_containers = count_minimum_combinations(150, 0, 0)
answer_part_two(count_exact_combinations(150, 0, 0, min_containers))

# End of Code
# ==========================================================================
timer.end_timer()
