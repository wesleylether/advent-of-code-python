import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
password = get_input()
timer.start_timer()


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


while not check_password(password):
    password = increment_password(password)


# Print the answers here
# ==========================================================================
answer_part_one(password)

password = increment_password(password)
while not check_password(password):
    password = increment_password(password)

answer_part_two(password)

# End of Code
# ==========================================================================
timer.end_timer()
