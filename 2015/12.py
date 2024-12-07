import json
import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input, pp, dd

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

for n in re.findall(r"-?\d+", input_file):
    p1 += int(n)


def loop_json_items(data):
    global p2
    if isinstance(data, dict):
        if "red" in data.values():
            return

        for key, value in data.items():
            loop_json_items(value)
    elif isinstance(data, list):
        for item in data:
            loop_json_items(item)
    else:
        try:
            p2 += int(data)
        except ValueError:
            pass


loop_json_items(json.loads(input_file))

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
