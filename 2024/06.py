from modules.advent_of_code import solve_one, solve_two, get_input
from modules.enums import Direction
from modules.grid import Grid, GridOrientation

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    grid = Grid.from_string(input_file)
    return grid, grid.search("^")


def get_direction(direction):
    match direction:
        case Direction.Up:
            return Direction.Right
        case Direction.Right:
            return Direction.Down
        case Direction.Down:
            return Direction.Left
        case Direction.Left:
            return Direction.Up

    return direction


def get_next(current, direction):
    match direction:
        case Direction.Up:
            return current[0], current[1] - 1
        case Direction.Right:
            return current[0] + 1, current[1]
        case Direction.Down:
            return current[0], current[1] + 1
        case Direction.Left:
            return current[0] - 1, current[1]
    return current


visited = set()


def part_one():
    grid, current = parse_input()
    direction = Direction.Up

    while True:
        try:
            grid[current] = "X"
            visited.add(current)

            while grid[get_next(current, direction)] == "#":
                direction = get_direction(direction)

            current = get_next(current, direction)
        except IndexError:
            break

    return grid.count_value("X")


def part_two():
    count = 0
    grid, start_position = parse_input()
    done = set()
    for v in visited:
        for item, position in grid.get_neighbors(
            v,
            GridOrientation.Horizontal | GridOrientation.Vertical,
        ):
            if position in done:
                continue
            done.add(position)

            current = start_position
            direction = Direction.Up
            seen = set()
            if item == ".":
                while True:
                    try:
                        if (current, direction) in seen:
                            count += 1
                            break
                        seen.add((current, direction))
                        while (
                            grid[get_next(current, direction)] == "#"
                            or get_next(current, direction) == position
                        ):
                            direction = get_direction(direction)

                        current = get_next(current, direction)
                    except IndexError:
                        break

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
