from modules.advent_of_code import solve
from modules.list import List

ParsedData = List[str]


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    return List(data)


def part_one(data: ParsedData):
    return data.reduce(
        lambda carry, item: carry + 1 if item == "(" else carry - 1,
        0,
    )


def part_two(data: ParsedData):
    count = {"a": 0, "b": 0}
    for i, char in data.enumerate():
        count["a"] += 1 if char == "(" else -1

        if count["a"] == -1 and count["b"] == 0:
            count["b"] = i + 1

    return count["b"]


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
