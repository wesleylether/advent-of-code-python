import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from itertools import permutations
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input, dd
from modules.grid import Grid

timer = Timer()
input_file = get_input(True)
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
grid = Grid.with_string(input_file)
antenna_types = set()
for antenna in grid:
    if antenna != ".":
        antenna_types.add(antenna)

p1 = set()
p2 = set()
for antenna in antenna_types:
    antennas = list(grid.search_all(antenna))
    for i in range(len(antennas)):
        f = antennas[i]
        to_check = antennas[i + 1 :] + antennas[:i]
        for check in to_check:
            x = f[0] - check[0]
            y = f[1] - check[1]

            try:
                if grid[f[0] + x, f[1] + y] != "#":
                    p1.add((f[0] + x, f[1] + y))

                if grid[check[0] + x, check[1] + y] != "#":
                    p1.add((check[0] + x, check[1] + y))
            except IndexError:
                pass

            for a in [f, check]:
                xx = a[0] + x
                yy = a[1] + y
                while 0 <= xx < grid.width and 0 <= yy < grid.height:
                    if grid[xx, yy] == "#":
                        break
                    p2.add((xx, yy))
                    xx += x
                    yy += y


# Print the answers here
# ==========================================================================
answer_part_one(len(p1))
answer_part_two(len(p2))

# End of Code
# ==========================================================================
timer.end_timer()
