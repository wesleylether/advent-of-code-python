import heapq
from collections import namedtuple

from modules.advent_of_code import solve
from modules.grid import Grid, GridOrientation
from modules.helpers import dd


# Start coding hier
# ==========================================================================
def parse(data, *_):
    grid = Grid.from_string(data)
    start_position = grid.search("S")
    end_position = grid.search("E")

    return grid, start_position, end_position


Direction = namedtuple("Direction", ["value"])
Direction.Up = Direction((0, -2))
Direction.Down = Direction((0, 2))
Direction.Left = Direction((-2, 0))
Direction.Right = Direction((2, 0))


def path_score(grid, start, end):
    prio_queue = []
    path = {start: 0}
    heapq.heappush(prio_queue, (0, start))
    while prio_queue:
        current_score, current_position = heapq.heappop(prio_queue)
        if current_position == end:
            return list(path.values())[-1], path

        for neighbor, neighbor_position in grid.neighbors(
            current_position, GridOrientation.Horizontal | GridOrientation.Vertical
        ):
            if neighbor != "#":
                new_score = current_score + 1
                if neighbor_position not in path:
                    path[neighbor_position] = new_score
                    heapq.heappush(prio_queue, (new_score, neighbor_position))
                elif new_score < path[neighbor_position]:
                    print(grid)
                    dd(new_score, neighbor_position, path)

    raise RuntimeError("No path found")


def part_one(data, pico_seconds):
    grid, s, e = data
    max_pico_points, default_path = path_score(grid, s, e)
    cheats = {}

    for path, score in default_path.items():
        for d in [Direction.Up, Direction.Down, Direction.Left, Direction.Right]:
            dx, dy = path[0] + d.value[0], path[1] + d.value[1]
            try:
                cheat = grid[dx, dy]
                if cheat != "#" and score + 2 < default_path[dx, dy]:
                    if default_path[dx, dy] - (score + 2) in cheats:
                        cheats[default_path[dx, dy] - (score + 2)] += 1
                    else:
                        cheats[default_path[dx, dy] - (score + 2)] = 1
                    continue
            except IndexError:
                continue
    sorted_cheats = sorted(cheats.items(), reverse=True)
    filtered_cheats = dict(filter(lambda x: x[0] >= pico_seconds, sorted_cheats))

    return sum(filtered_cheats.values())


def part_two(data, pico_seconds):
    grid, s, e = data
    max_pico_points, default_path = path_score(grid, s, e)
    cheats = 0
    visited_list = list(default_path.keys())
    costs_list = [default_path[i] for i in visited_list]

    for i in range(len(visited_list)):
        x1, y1 = visited_list[i]
        for j in range(i + 1, len(visited_list)):
            x2, y2 = visited_list[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= 20:
                cost1, cost2 = costs_list[i], costs_list[j]
                if cost2 - cost1 - distance >= pico_seconds:
                    cheats += 1

    return cheats


# Answers
# ==========================================================================
solve(part_one, parse, 100)
solve(part_two, parse, 100)
