import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from enum import Enum
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd
from operator import mul

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input, dd, ddd

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
data = input_file.splitlines()


class Properties(Enum):
    capacity = 0
    durability = 1
    flavor = 2
    texture = 3
    calories = 4


ingredients = {}
for i, line in enumerate(data):
    properties = re.findall(r"-?\d+", line)
    ingredients[i] = list(map(int, properties))


def generate_combinations(total, divisions):
    possible_numbers = range(1, total)  # Mogelijke getallen van 1 tot totaal-1
    combinations = []

    def find_combinations(current, rest):
        if len(current) == divisions:
            if sum(current) == total:
                combinations.append(tuple(current))
            return
        for num in rest:
            find_combinations(current + [num], rest)

    find_combinations([], list(possible_numbers))

    return sorted(combinations, key=lambda x: (sum(x), tuple(x)))


for combination in generate_combinations(100, len(ingredients)):
    values = {}
    for index, combination_value in enumerate(combination):
        for i, prop in enumerate(ingredients[index]):
            if index not in values:
                values[index] = {}
            values[index][i] = prop * combination_value

    total = reduce(
        mul, [max(sum([ingredient[i] for ingredient in values.values()]), 0) for i in range(4)]
    )
    p1 = max(p1, total)

    if sum([ingredient[Properties.calories.value] for ingredient in values.values()]) == 500:
        total = reduce(
            mul, [max(sum([ingredient[i] for ingredient in values.values()]), 0) for i in range(4)]
        )
        p2 = max(p2, total)

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
