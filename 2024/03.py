import re

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def part_one():
    count = 0
    for m in re.findall(r"mul\((\d+){,3},(\d+){,3}\)", input_file):
        count += int(m[0]) * int(m[1])

    return count


def part_two():
    count = 0
    skip_next = False
    for token in re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", input_file):
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
solve_one(part_one)
solve_two(part_two)
