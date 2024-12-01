import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.grid import Grid

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
g1 = Grid(1000, 1000, 0)
g2 = Grid(1000, 1000, 0)
for line in input_file.split("\n"):
    action = re.findall(r"toggle|turn on|turn off", line)[0]
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "toggle":
                g1[x, y] = 1 if g1[x, y] == 0 else 0
                g2[x, y] += 2
            elif action == "turn on":
                g1[x, y] = 1
                g2[x, y] += 1
            elif action == "turn off":
                g1[x, y] = 0
                g2[x, y] = max(0, g2[x, y] - 1)

# Print the answers here
# ==========================================================================
answer_part_one(g1.count_value(1))
answer_part_two(g2.sum_values())

# End of Code
# ==========================================================================
timer.end_timer()
