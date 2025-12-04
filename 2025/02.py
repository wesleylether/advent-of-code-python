import re

from modules.advent_of_code import solve
from modules.list import List


# Start coding here
# ==========================================================================
def parse(data):
    d = List()
    for numbers in data.split(","):
        matches = re.match(r"(\d+)-(\d+)", numbers)
        d.append((int(matches.group(1)), int(matches.group(2))))
    return d


def part_one(data):
    false_ids = List()
    for left, right in data:
        for n in range(left, right + 1):
            if len(str(n)) % 2 == 1:
                continue

            mid = len(str(n)) // 2
            if str(n)[:mid] == str(n)[mid:]:
                false_ids.append(n)

    return false_ids.sum()


def part_two(data):
    false_ids = List()
    for left, right in data:
        for n in range(left, right + 1):
            s = str(n)
            if s in (s + s)[1:-1]:
                false_ids.append(n)

    return false_ids.sum()


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
