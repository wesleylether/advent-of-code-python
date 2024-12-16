import hashlib

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file


def calculate_hash(value):
    count = 0
    while True:
        hash_value = hashlib.md5(f"{input_file}{count}".encode()).hexdigest()
        if hash_value.startswith(value):
            break
        count += 1

    return count


def part_one():
    return calculate_hash("00000")


def part_two():
    return calculate_hash("000000")


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
