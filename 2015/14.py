import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data, total_time):
    count = 0
    for line in data.splitlines():
        speed, fly_time, rest_time = map(int, re.findall(r"\d+", line))
        cycle_time = fly_time + rest_time
        full_cycles = total_time // cycle_time
        remaining_time = total_time % cycle_time
        distance = speed * fly_time * full_cycles
        distance += speed * min(fly_time, remaining_time)
        count = max(count, distance)

    return count


def part_two(data, total_time):
    reindeer = {}
    for line in data.splitlines():
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
solve(part_one, None, 2503)
solve(part_two, None, 2503)
