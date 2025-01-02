import re
from enum import Enum
from functools import reduce
from operator import mul

from modules.advent_of_code import solve
from modules.helpers import generate_number_distributions


# Start coding here
# ==========================================================================
def parse(data):
    ingredients = {}

    for i, line in enumerate(data.splitlines()):
        properties = re.findall(r"-?\d+", line)
        ingredients[i] = list(map(int, properties))
    return ingredients


class Properties(Enum):
    capacity = 0
    durability = 1
    flavor = 2
    texture = 3
    calories = 4


def part_one(data):
    count = 0
    ingredients = data
    for combination in generate_number_distributions(100, len(ingredients)):
        values = {}
        for index, combination_value in enumerate(combination):
            for i, prop in enumerate(ingredients[index]):
                if index not in values:
                    values[index] = {}
                values[index][i] = prop * combination_value

        total = reduce(
            mul, [max(sum([ingredient[i] for ingredient in values.values()]), 0) for i in range(4)]
        )
        count = max(count, total)

        # if sum([ingredient[Properties.calories.value] for ingredient in values.values()]) == 500:
        #     total = reduce(
        #         mul, [max(sum([ingredient[i] for ingredient in values.values()]), 0) for i in range(4)]
        #     )
        #     p2 = max(p2, total)

    return count


def part_two(data):
    count = 0
    ingredients = data
    for combination in generate_number_distributions(100, len(ingredients)):
        values = {}
        for index, combination_value in enumerate(combination):
            for i, prop in enumerate(ingredients[index]):
                if index not in values:
                    values[index] = {}
                values[index][i] = prop * combination_value

        if sum([ingredient[Properties.calories.value] for ingredient in values.values()]) == 500:
            total = reduce(
                mul,
                [max(sum([ingredient[i] for ingredient in values.values()]), 0) for i in range(4)],
            )
            count = max(count, total)

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
