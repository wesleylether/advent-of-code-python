import heapq
import re
from collections import namedtuple

from modules.advent_of_code import solve
from modules.grid import Grid

Direction = namedtuple("Direction", ["value"])
Direction.Up = Direction((0, -1))
Direction.Down = Direction((0, 1))
Direction.Left = Direction((-1, 0))
Direction.Right = Direction((1, 0))


def heuristic(pos, end_pos):
    return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])


# Start coding here
# ==========================================================================
def parse(data, **_):
    return [tuple(map(int, re.findall(r"\d+", line))) for line in data.splitlines()]


def create_grid_with_data(data, size):
    w, h = size
    grid = Grid(w, h, ".")
    for p in data:
        grid[p] = "#"

    return grid


def calculate_path_cost(grid, end):
    priority_queue = []
    g_costs = {(0, 0): 0}
    heapq.heappush(priority_queue, (0, 0, (0, 0), None, set()))

    while priority_queue:
        _, g_cost, pos, direction, visited = heapq.heappop(priority_queue)
        x, y = pos

        if pos == end:
            return g_cost

        if pos in visited:
            continue
        visited.add(pos)

        for next_direction in [Direction.Up, Direction.Left, Direction.Right, Direction.Down]:
            if (direction, next_direction) in {
                (Direction.Up, Direction.Down),
                (Direction.Down, Direction.Up),
                (Direction.Left, Direction.Right),
                (Direction.Right, Direction.Left),
            }:
                continue

            next_pos = x + next_direction.value[0], y + next_direction.value[1]
            try:
                if grid[next_pos] != "#" and next_pos not in visited:
                    next_g_cost = g_cost + 1
                    h_cost = heuristic(next_pos, end)
                    f_cost = next_g_cost + h_cost

                    if next_pos not in g_costs or next_g_cost < g_costs[next_pos]:
                        g_costs[next_pos] = next_g_cost
                        heapq.heappush(
                            priority_queue,
                            (f_cost, next_g_cost, next_pos, next_direction, visited.copy()),
                        )
            except IndexError:
                pass


def part_one(data, width, height, byte_count):
    grid = create_grid_with_data(data[:byte_count], (width, height))

    return calculate_path_cost(grid, (width - 1, height - 1))


def part_two(data, width, height, byte_count):
    grid = create_grid_with_data(data[:byte_count], (width, height))

    for d in data[byte_count:]:
        grid[d] = "#"

        if calculate_path_cost(grid, (width - 1, height - 1)) is None:
            return ",".join(map(str, d))

    raise RuntimeError("No solution found")


# Answers
# ==========================================================================
solve(part_one, parse, width=71, height=71, byte_count=1024)
solve(part_two, parse, width=71, height=71, byte_count=1024)
