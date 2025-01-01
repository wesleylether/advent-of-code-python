import re

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    parsed_data = []
    for group in data.split("\n\n"):
        lines = group.splitlines()
        parsed_data.append(
            {
                "A": tuple(int(n) for n in re.findall(r"(\d+)", lines[0])),
                "B": tuple(int(n) for n in re.findall(r"(\d+)", lines[1])),
                "P": tuple(int(n) for n in re.findall(r"(\d+)", lines[2])),
            }
        )
    return parsed_data


def part_one(data):
    count = 0

    for d in data:
        for a in range(1, 101):
            for b in range(1, 101):
                if (
                    d["P"][0] == a * d["A"][0] + b * d["B"][0]
                    and d["P"][1] == a * d["A"][1] + b * d["B"][1]
                ):
                    count += a * 3 + b

    return count


def part_two(data):
    count = 0

    for d in data:
        a1, a2 = d["A"]
        b1, b2 = d["B"]
        p1, p2 = d["P"]

        p1 += 10000000000000
        p2 += 10000000000000

        new_b1 = b1 * a2 - b2 * a1
        new_c1 = p1 * a2 - p2 * a1

        e = new_c1 / new_b1
        d = (p1 - b1 * e) / a1

        if d % 1 == 0 and e % 1 == 0:
            count += int(d * 3 + e)

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
