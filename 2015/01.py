import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import get_input

start_time = time.time_ns()

input_file = get_input()
part_1 = 0
part_2 = 0
for index, char in enumerate(input_file):
    part_1 += 1 if char == '(' else -1

    if part_1 == -1 and part_2 == 0:
        part_2 = index + 1

print(part_1)
print(part_2)

end_time = time.time_ns()
duration = end_time - start_time
print(f"Time: {duration / 1_000_000.0}ms")