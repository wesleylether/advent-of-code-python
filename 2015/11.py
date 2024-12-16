import re

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file


def check_password(password):
    if not re.search(
        r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)",
        password,
    ):
        return False

    if re.search(r"[iol]", password):
        return False

    if len(re.findall(r"(.)\1", password)) < 2:
        return False

    return True


def increment_password(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return "".join(password)


def part_one():
    password = parse_input()
    while not check_password(password):
        password = increment_password(password)

    return password


def part_two():
    password = increment_password(part_one())
    while not check_password(password):
        password = increment_password(password)

    return password


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
