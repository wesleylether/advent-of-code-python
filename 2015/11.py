import re

from modules.advent_of_code import solve

# Start coding here
# ==========================================================================


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


results_part_one = None


def part_one(data):
    global results_part_one
    password = data
    while not check_password(password):
        password = increment_password(password)

    results_part_one = password
    return password


def part_two(_):
    password = increment_password(results_part_one)
    while not check_password(password):
        password = increment_password(password)

    return password


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
