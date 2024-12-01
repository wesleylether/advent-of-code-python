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
for index, char in enumerate(input_file):
    PART_1 += 1 if char == "(" else -1

    if PART_1 == -1 and PART_2 == 0:
        PART_2 = index + 1

# Print the answers here
# ==========================================================================
answer_part_one(PART_1)
answer_part_two(PART_2)

# End of Code
# ==========================================================================
timer.end_timer()
