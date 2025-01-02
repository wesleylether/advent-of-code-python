import hashlib

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def calculate_hash(data, value):
    count = 0
    while True:
        hash_value = hashlib.md5(f"{data}{count}".encode()).hexdigest()
        if hash_value.startswith(value):
            break
        count += 1

    return count


def part_one(data):
    return calculate_hash(data, "00000")


def part_two(data):
    return calculate_hash(data, "000000")


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
