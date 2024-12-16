import re

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    data = []
    for line in input_file.split():
        numbers = re.match(r"(\d+)x(\d+)x(\d+)", line.strip())
        data.append((int(numbers.group(1)), int(numbers.group(2)), int(numbers.group(3))))
    return data


def part_one():
    count = 0
    for l, w, h in parse_input():
        lw = l * w
        lh = l * h
        wh = w * h

        count += 2 * (lw + lh + wh) + min(lw, lh, wh)

    return count


def part_two():
    count = 0
    for l, w, h in parse_input():
        sides = [l, w, h]
        sides.sort()
        count += 2 * (sides[0] + sides[1]) + l * w * h
    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
