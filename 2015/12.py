import json
import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    count = 0
    for n in re.findall(r"-?\d+", data):
        count += int(n)

    return count


def part_two(data):
    def loop_json_items(data, count):
        if isinstance(data, dict):
            if "red" in data.values():
                return count

            for key, value in data.items():
                count = loop_json_items(value, count)
        elif isinstance(data, list):
            for item in data:
                count = loop_json_items(item, count)
        else:
            try:
                count += int(data)
            except ValueError:
                pass

        return count

    return loop_json_items(json.loads(data), 0)


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
