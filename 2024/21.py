from functools import lru_cache
from itertools import permutations

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    return data.splitlines()


numpad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    ".": (0, 3),
    "0": (1, 3),
    "A": (2, 3),
}
keypad = {
    ".": (0, 0),
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


@lru_cache(None)
def sequence(sequence_str: str, depth=0, max_depth=2):
    def visits(x, y, moves, hole):
        for m in moves:
            if (x, y) == hole:
                return True
            match m:
                case "^":
                    y -= 1
                case "v":
                    y += 1
                case "<":
                    x -= 1
                case ">":
                    x += 1
        return (x, y) == hole

    def move_options(x, y, tx, ty, hole):
        dx, dy = tx - x, ty - y
        moves = ["v" if dy > 0 else "^"] * abs(dy) + ["<" if dx < 0 else ">"] * abs(dx)
        filtered_permutations = [m for m in set(permutations(moves)) if not visits(x, y, m, hole)]
        mapped_permutations = ["".join(m) + "A" for m in filtered_permutations]
        return mapped_permutations if mapped_permutations else list["A"]

    out = 0

    def get_from_depth(value):
        return numpad.get(value) if depth == 0 else keypad.get(value)

    x, y = get_from_depth("A")
    for i in sequence_str:
        tx, ty = get_from_depth(i)
        options = move_options(x, y, tx, ty, get_from_depth("."))
        if depth == max_depth:
            out += len(options[0])
        else:
            out += min(sequence(o, depth + 1, max_depth) for o in options)
        x, y = tx, ty
    return out


def part_one(data):
    return sum(sequence(i) * int(i[:-1]) for i in data)


def part_two(data):
    return sum(sequence(i, max_depth=25) * int(i[:-1]) for i in data)


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
