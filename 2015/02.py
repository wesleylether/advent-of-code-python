import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
PART_1 = 0
PART_2 = 0
for line in input_file.split():
    numbers = re.match(r"(\d+)x(\d+)x(\d+)", line.strip())
    l, w, h = int(numbers.group(1)), int(numbers.group(2)), int(numbers.group(3))

    lw = l * w
    lh = l * h
    wh = w * h

    PART_1 += 2 * (lw + lh + wh) + min(lw, lh, wh)

    sides = [l, w, h]
    sides.sort()
    PART_2 += 2 * (sides[0] + sides[1]) + l * w * h


# Print the answers here
# ==========================================================================
answer_part_one(PART_1)
answer_part_two(PART_2)

# End of Code
# ==========================================================================
timer.end_timer()
