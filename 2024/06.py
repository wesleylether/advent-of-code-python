from enum import Enum

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.grid import Grid

timer = Timer()
input_file = get_input()
timer.start_timer()


# Start coding here
# ==========================================================================
class Direction(Enum):
    UP = 0
    RIGHT = 90
    DOWN = 180
    LEFT = 270


def get_direction(direction):
    match direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP

    return direction


def get_next(current, direction):
    match direction:
        case Direction.UP:
            return current[0], current[1] - 1
        case Direction.RIGHT:
            return current[0] + 1, current[1]
        case Direction.DOWN:
            return current[0], current[1] + 1
        case Direction.LEFT:
            return current[0] - 1, current[1]
    return current


grid = Grid.from_string(input_file)
direction = Direction.UP
current = grid.search("^")

while True:
    try:
        grid[current] = "X"

        while grid[get_next(current, direction)] == "#":
            direction = get_direction(direction)

        current = get_next(current, direction)
    except IndexError:
        break

answer_part_one(grid.count("X"))
timer.end_timer()
# print(grid)
print("\n")

# Part two
# ==========================================================================
p2 = 0
timer.start_timer()
grid = Grid.from_string(input_file)
start_position = grid.search("^")

for position in grid:
    current = start_position
    direction = Direction.UP
    seen = set()
    if position == ".":
        while True:
            try:
                if (current, direction) in seen:
                    p2 += 1
                    break
                seen.add((current, direction))
                while (
                    grid[get_next(current, direction)] == "#"
                    or get_next(current, direction) == grid.current
                ):
                    direction = get_direction(direction)

                current = get_next(current, direction)
            except IndexError:
                break

answer_part_two(p2)
timer.end_timer()
# print(grid)
