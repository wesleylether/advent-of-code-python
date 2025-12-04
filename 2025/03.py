from modules.advent_of_code import solve
from modules.list import List

ParsedData = List[List[int]]


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    return List([List([int(x) for x in d]) for d in data.splitlines()])


def part_one(data: ParsedData):
    return data.map(
        lambda b: b.combinations(2).star_map(lambda x, y: x * 10 + y).max()
    ).sum()


def part_two(data):
    batteries = List()

    target_length = 12
    for battery in data:
        to_drop = len(battery) - target_length
        stack = List()

        for n in battery:
            while to_drop > 0 and stack and stack[-1] < n:
                stack.pop()
                to_drop -= 1
            stack.append(n)

        result = stack[:target_length]

        batteries.append(int("".join(str(x) for x in result)))

    return batteries.sum()


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
