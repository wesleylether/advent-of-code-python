import hashlib
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
p1 = 1

while True:
    hash_value = hashlib.md5(f"{input_file}{p1}".encode()).hexdigest()
    if hash_value.startswith("00000"):
        break
    p1 += 1
answer_part_one(p1)
timer.end_timer()

p2 = 0
timer.start_timer()
while True:
    hash_value = hashlib.md5(f"{input_file}{p2}".encode()).hexdigest()
    if hash_value.startswith("000000"):
        break
    p2 += 1
answer_part_two(p2)
timer.end_timer()
