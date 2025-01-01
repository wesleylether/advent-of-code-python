import re
from collections import defaultdict
from itertools import permutations

from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    people = set()
    happiness = defaultdict(dict)

    for line in input_file.splitlines():
        data = re.findall(
            r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).", line
        )[0]
        person1, sign, value, person2 = data
        value = int(value) if sign == "gain" else -int(value)

        people.add(person1)
        people.add(person2)

        happiness[person1][person2] = value

    return people, happiness


def calculate_happiness(people, happiness):
    max_happiness = 0
    for arrangement in permutations(people):
        current_happiness = 0
        for i in range(len(arrangement)):
            current_happiness += happiness[arrangement[i]][arrangement[(i + 1) % len(arrangement)]]
            current_happiness += happiness[arrangement[(i + 1) % len(arrangement)]][arrangement[i]]
        max_happiness = max(max_happiness, current_happiness)
    return max_happiness


def part_one():
    people, happiness = parse_input()

    return calculate_happiness(people, happiness)


def part_two():
    people, happiness = parse_input()

    for person in people:
        happiness["me"][person] = 0
        happiness[person]["me"] = 0
    people.add("me")

    return calculate_happiness(people, happiness)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
