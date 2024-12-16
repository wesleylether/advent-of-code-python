import heapq
from collections import namedtuple
from functools import lru_cache

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    grid = Grid.from_string(input_file)
    start_pos = grid.search("S")
    end_pos = grid.search("E")
    return grid, start_pos, end_pos


Direction = namedtuple("Direction", ["value"])
Direction.Up = Direction((0, -1))
Direction.Down = Direction((0, 1))
Direction.Left = Direction((-1, 0))
Direction.Right = Direction((1, 0))


def heuristic(pos, end_pos):
    return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])


@lru_cache(None)
def part_one():
    grid, pos, end_pos = parse_input()

    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, pos, Direction.Right))

    while priority_queue:
        priority, cost, pos, direction = heapq.heappop(priority_queue)
        x, y = pos

        if pos == end_pos:
            return cost

        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))

        for next_direction in [Direction.Up, Direction.Left, Direction.Right, Direction.Down]:
            if (direction, next_direction) in {
                (Direction.Up, Direction.Down),
                (Direction.Down, Direction.Up),
                (Direction.Left, Direction.Right),
                (Direction.Right, Direction.Left),
            }:
                continue

            step_cost = 1 if next_direction == direction else 1001
            next_cost = cost + step_cost
            next_pos = x + next_direction.value[0], y + next_direction.value[1]

            if grid[next_pos] != "#" and next_pos not in visited:
                estimated_total_cost = next_cost + heuristic(next_pos, end_pos)
                heapq.heappush(
                    priority_queue,
                    (estimated_total_cost, next_cost, next_pos, next_direction),
                )

    raise RuntimeError("No path found")


def part_two():
    best_score = part_one()

    grid, pos, end_pos = parse_input()

    visited = {}
    spots = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, pos, Direction.Right, [pos]))

    while priority_queue:
        cost, pos, direction, path = heapq.heappop(priority_queue)

        if cost > best_score:
            continue

        if pos == end_pos:
            for p in path:
                spots.add(p)
            continue

        if visited.get((pos, direction), cost) != cost:
            continue
        visited[(pos, direction)] = cost
        x, y = pos

        for next_direction in [Direction.Up, Direction.Left, Direction.Right, Direction.Down]:
            if (direction, next_direction) in {
                (Direction.Up, Direction.Down),
                (Direction.Down, Direction.Up),
                (Direction.Left, Direction.Right),
                (Direction.Right, Direction.Left),
            }:
                continue

            step_cost = 1 if next_direction == direction else 1001
            next_cost = cost + step_cost
            next_pos = x + next_direction.value[0], y + next_direction.value[1]

            if grid[next_pos] != "#":
                heapq.heappush(
                    priority_queue,
                    (next_cost, next_pos, next_direction, [*path, next_pos]),
                )

    return len(spots)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
