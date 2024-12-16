import json
import re

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file


def part_one():
    count = 0
    for n in re.findall(r"-?\d+", parse_input()):
        count += int(n)

    return count


def part_two():
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

    return loop_json_items(json.loads(parse_input()), 0)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
