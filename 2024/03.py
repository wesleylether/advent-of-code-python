import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    count = 0
    for m in re.findall(r"mul\((\d+){,3},(\d+){,3}\)", data):
        count += int(m[0]) * int(m[1])

    return count


def part_two(data):
    count = 0
    skip_next = False
    for token in re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", data):
        if token == "don't()":
            skip_next = True
        elif token == "do()":
            skip_next = False
        elif token.startswith("mul("):
            if not skip_next:
                numbers = [int(n) for n in re.findall(r"\d{1,3}", token)]
                count += numbers[0] * numbers[1]
    return count


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
