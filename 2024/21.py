from functools import lru_cache
from itertools import permutations

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file.splitlines()


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
def sequence(sequence: str, depth=0, max_depth=2):
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
    for i in sequence:
        tx, ty = get_from_depth(i)
        options = move_options(x, y, tx, ty, get_from_depth("."))
        if depth == max_depth:
            out += len(options[0])
        else:
            out += min(sequence(o, depth + 1, max_depth) for o in options)
        x, y = tx, ty
    return out


def part_one():
    return sum(sequence(i) * int(i[:-1]) for i in parse_input())


def part_two():
    return sum(sequence(i, max_depth=25) * int(i[:-1]) for i in parse_input())


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
