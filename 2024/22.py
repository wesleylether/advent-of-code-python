from collections import defaultdict
from functools import lru_cache

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    return list(map(int, data.splitlines()))


@lru_cache(None)
def evolve(secret: int) -> int:
    secret ^= secret * 64
    secret %= 16777216
    secret ^= secret // 32
    secret %= 16777216
    secret ^= secret * 2048
    secret %= 16777216
    return secret


def part_one(data):
    for _ in range(2000):
        data = [evolve(x) for x in data]

    return sum(data)


def part_two(data):
    values = defaultdict(int)

    for value in data:
        evolved_data = [value]
        for _ in range(1999):
            evolved_data.append(evolve(evolved_data[-1]))

        diffs = [
            evolved_data[i + 1] % 10 - evolved_data[i] % 10 for i in range(len(evolved_data) - 1)
        ]

        seen = set()

        for v, (a, b, c, d) in zip(evolved_data[4:], zip(diffs, diffs[1:], diffs[2:], diffs[3:])):
            if (a, b, c, d) not in seen:
                values[a, b, c, d] += v % 10
                seen.add((a, b, c, d))

            new_val = evolve(v)
            _, _, _, _ = b, c, d, -(v % 10 - new_val % 10)

    return max(values.values())


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
