import random
import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid
from modules.helpers import dd, ddd, pp

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    lines, molecule = input_file.split("\n\n")
    replacements = defaultdict(list)
    for r_key, r_replacement in [l.split(" => ") for l in lines.split("\n")]:
        replacements[r_key].append(r_replacement)
    molecule = molecule.strip()

    return molecule, replacements.items()


def part_one():
    molecule, replacements = parse_input()
    results = set()
    for key, values in replacements:
        for value in values:
            for i in range(len(molecule)):
                if molecule[i : i + len(key)] == key:
                    results.add(molecule[:i] + value + molecule[i + len(key) :])
    return len(results)


def part_two():
    count = 0
    molecule, replacements = parse_input()

    reverse_replacements = []
    for key, values in replacements:
        for value in values:
            reverse_replacements.append((value, key))

    random.shuffle(reverse_replacements)

    target = molecule

    while target != "e":
        replaced = False
        for key, value in reverse_replacements:
            if key in target:
                target = target.replace(key, value, 1)
                count += 1
                replaced = True
                break
        if not replaced:
            print("No replacement found, shuffle and try again")
            target = molecule
            count = 0
            random.shuffle(reverse_replacements)

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
