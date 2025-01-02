import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    d = []
    for line in data.splitlines():
        numbers = re.match(r"(\d+)x(\d+)x(\d+)", line.strip())
        d.append((int(numbers.group(1)), int(numbers.group(2)), int(numbers.group(3))))
    return d


def part_one(data):
    count = 0
    for l, w, h in data:
        lw = l * w
        lh = l * h
        wh = w * h

        count += 2 * (lw + lh + wh) + min(lw, lh, wh)

    return count


def part_two(data):
    count = 0
    for l, w, h in data:
        sides = [l, w, h]
        sides.sort()
        count += 2 * (sides[0] + sides[1]) + l * w * h
    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
