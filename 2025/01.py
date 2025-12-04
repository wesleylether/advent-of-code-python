import re

from modules.advent_of_code import solve
from modules.list import List


# Start coding here
# ==========================================================================
def parse(data):
    d = List()
    for line in data.splitlines():
        matches = re.match(r"([LR])(\d+)", line)
        d.append((matches.group(1), int(matches.group(2))))
    return d


def part_one(data):
    start = 50
    count = 0
    for d in data:
        direction, steps = d
        match direction:
            case "L":
                start -= steps
            case "R":
                start += steps

        start %= 100
        if start == 0:
            count += 1

    return count


def part_two(data):
    start = 50
    count = 0
    for d in data:
        direction, steps = d
        match direction:
            case "L":
                count += (start - 1) // 100 - (start - steps - 1) // 100
                start -= steps
            case "R":
                count += (start + steps) // 100
                start += steps

        start %= 100

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
