import re

from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file.split()


def part_one():
    count = 0
    for string in parse_input():
        vowels = re.findall(r"[aeiou]", string)
        if len(vowels) < 3:
            continue
        if not re.search(r"(.)\1", string):
            continue
        if re.search(r"ab|cd|pq|xy", string):
            continue
        count += 1

    return count


def part_two():
    count = 0
    for string in parse_input():
        if re.search(r"(..).*\1", string) and re.search(r"(.).\1", string):
            count += 1

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
