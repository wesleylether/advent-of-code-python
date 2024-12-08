import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from itertools import permutations
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

people = set()
happiness = defaultdict(dict)

for line in input_file.split("\n"):
    data = re.findall(
        r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).", line
    )[0]
    person1, sign, value, person2 = data
    value = int(value) if sign == "gain" else -int(value)

    people.add(person1)
    people.add(person2)

    happiness[person1][person2] = value


def calculate_happiness(people, happiness):
    max_happiness = 0
    for arrangement in permutations(people):
        current_happiness = 0
        for i in range(len(arrangement)):
            current_happiness += happiness[arrangement[i]][arrangement[(i + 1) % len(arrangement)]]
            current_happiness += happiness[arrangement[(i + 1) % len(arrangement)]][arrangement[i]]
        max_happiness = max(max_happiness, current_happiness)
    return max_happiness


p1 = calculate_happiness(people, happiness)

for person in people:
    happiness["me"][person] = 0
    happiness[person]["me"] = 0
people.add("me")

p2 = calculate_happiness(people, happiness)


# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
