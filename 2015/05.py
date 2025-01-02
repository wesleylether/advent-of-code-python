import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    count = 0
    for string in data.split():
        vowels = re.findall(r"[aeiou]", string)
        if len(vowels) < 3:
            continue
        if not re.search(r"(.)\1", string):
            continue
        if re.search(r"ab|cd|pq|xy", string):
            continue
        count += 1

    return count


def part_two(data):
    count = 0
    for string in data.split():
        if re.search(r"(..).*\1", string) and re.search(r"(.).\1", string):
            count += 1

    return count


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
