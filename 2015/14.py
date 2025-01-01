import re

from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file.splitlines()


def part_one():
    count = 0
    for line in parse_input():
        speed, fly_time, rest_time = map(int, re.findall(r"\d+", line))
        total_time = 2503
        cycle_time = fly_time + rest_time
        full_cycles = total_time // cycle_time
        remaining_time = total_time % cycle_time
        distance = speed * fly_time * full_cycles
        distance += speed * min(fly_time, remaining_time)
        count = max(count, distance)

    return count


def part_two():
    reindeer = {}
    for line in parse_input():
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

    return max(reindeer.values(), key=lambda x: x["points"])["points"]


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
