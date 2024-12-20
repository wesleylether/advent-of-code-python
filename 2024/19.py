from functools import lru_cache

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    patterns_input, lines = input_file.split("\n\n")
    patterns = patterns_input.split(", ")
    patterns = sorted(patterns, key=lambda x: (-len(x), x))
    return patterns, lines.splitlines()


@lru_cache(None)
def check_pattern(patterns: tuple[str, ...], line: str) -> int:
    if not line:
        return 1

    count = 0
    for pattern in patterns:
        if line.startswith(pattern):
            count += check_pattern(patterns, line[len(pattern) :])

    return count


def part_one():
    patterns, lines = parse_input()

    count = 0
    for line in lines:
        if check_pattern(tuple(patterns), line) > 0:
            count += 1

    return count


def part_two():
    patterns, lines = parse_input()

    count = 0
    for line in lines:
        count += check_pattern(tuple(patterns), line)

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
