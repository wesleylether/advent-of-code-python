import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    MFCSAM = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    pattern = re.compile(r"(\w+): (\d+)")
    parse_line = lambda line: [(n, int(v)) for n, v in re.findall(pattern, line)]
    data = list(map(parse_line, data.splitlines()))

    return data, MFCSAM


solve = lambda data, func: next(i for i, line in enumerate(data, 1) if all(func(*p) for p in line))


def part_one(data):
    data, scan_data = data

    return solve(data, lambda name, val: val == scan_data[name])


def part_two(data):
    data, scan_data = data

    return solve(
        data,
        lambda name, val: (
            val > scan_data[name]
            if name in ("cats", "trees")
            else (
                val < scan_data[name]
                if name in ("pomeranians", "goldfish")
                else val == scan_data[name]
            )
        ),
    )


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
