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
x, y = 0, 0
x1, y1 = 0, 0
x2, y2 = 0, 0
houses1 = {(x, y): 1}
houses2 = {(0, 0): 2}

for index, direction in enumerate(input_file):
    match direction:
        case "^":
            y += 1
        case "v":
            y -= 1
        case ">":
            x += 1
        case "<":
            x -= 1

    if index % 2 == 0:
        match direction:
            case "^":
                y1 += 1
            case "v":
                y1 -= 1
            case ">":
                x1 += 1
            case "<":
                x1 -= 1

        if (x1, y1) in houses2:
            houses2[(x1, y1)] += 1
        else:
            houses2[(x1, y1)] = 1
    else:
        match direction:
            case "^":
                y2 += 1
            case "v":
                y2 -= 1
            case ">":
                x2 += 1
            case "<":
                x2 -= 1

        if (x2, y2) in houses2:
            houses2[(x2, y2)] += 1
        else:
            houses2[(x2, y2)] = 1

    if (x, y) in houses1:
        houses1[(x, y)] += 1
    else:
        houses1[(x, y)] = 1


# Print the answers here
# ==========================================================================
answer_part_one(len(houses1))
answer_part_two(len(houses2))

# End of Code
# ==========================================================================
timer.end_timer()
