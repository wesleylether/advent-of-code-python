import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd
from random import choice

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input, dd

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
for line in input_file.split("\n"):
    speed, fly_time, rest_time = map(int, re.findall(r"\d+", line))
    total_time = 2503
    cycle_time = fly_time + rest_time
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time
    distance = speed * fly_time * full_cycles
    distance += speed * min(fly_time, remaining_time)
    p1 = max(p1, distance)

answer_part_one(p1)
timer.end_timer()

timer.start_timer()
reindeer = {}
for line in input_file.split("\n"):
    name = re.match(r"^(\w+)", line).group(1)
    speed, fly_time, rest_time = map(int, re.findall(r"\d+", line))
    reindeer[name] = {
        "speed": speed,
        "fly_time": fly_time,
        "rest_time": rest_time,
        "distance": 0,
        "points": 0,
        "fly": True,
        "time": fly_time,
    }
total_time = 2503
while total_time:
    total_time -= 1
    for name, data in reindeer.items():
        if data["fly"]:
            data["distance"] += data["speed"]
        data["time"] -= 1
        if data["time"] == 0:
            data["fly"] = not data["fly"]
            data["time"] = data["fly_time"] if data["fly"] else data["rest_time"]

    max_distance = max(reindeer.values(), key=lambda x: x["distance"])["distance"]
    for name, data in reindeer.items():
        if data["distance"] == max_distance:
            data["points"] += 1

p2 = max(reindeer.values(), key=lambda x: x["points"])["points"]
answer_part_two(p2)
timer.end_timer()
