import heapq
import re
from collections import namedtuple

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

example = False
W, H = (7, 7) if example else (71, 71)
END = (W - 1, H - 1)
B = 12 if example else 1024
input_file = get_input(example)

Direction = namedtuple("Direction", ["value"])
Direction.Up = Direction((0, -1))
Direction.Down = Direction((0, 1))
Direction.Left = Direction((-1, 0))
Direction.Right = Direction((1, 0))


def heuristic(pos, end_pos):
    return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])


# Start coding here
# ==========================================================================
def parse_input():
    data = [tuple(map(int, re.findall(r"\d+", line))) for line in input_file.splitlines()]

    return data


def create_grid_with_data(data):
    grid = Grid(W, H, ".")
    for p in data:
        grid[p] = "#"

    return grid


def calculate_path_cost(grid):
    priority_queue = []
    g_costs = {(0, 0): 0}
    heapq.heappush(priority_queue, (0, 0, (0, 0), None, set()))

    while priority_queue:
        _, g_cost, pos, direction, visited = heapq.heappop(priority_queue)
        x, y = pos

        if pos == END:
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
                    h_cost = heuristic(next_pos, END)
                    f_cost = next_g_cost + h_cost

                    if next_pos not in g_costs or next_g_cost < g_costs[next_pos]:
                        g_costs[next_pos] = next_g_cost
                        heapq.heappush(
                            priority_queue,
                            (f_cost, next_g_cost, next_pos, next_direction, visited.copy()),
                        )
            except IndexError:
                pass


def part_one():
    data = parse_input()
    grid = create_grid_with_data(data[:B])

    return calculate_path_cost(grid)


def part_two():
    data = parse_input()
    grid = create_grid_with_data(data[:B])

    for d in data[B:]:
        grid[d] = "#"

        if calculate_path_cost(grid) is None:
            return d

    raise RuntimeError("No solution found")


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
