from collections import defaultdict, deque

from modules.advent_of_code import solve
from modules.enums import Direction
from modules.grid import Grid, GridOrientation


# Start coding here
# ==========================================================================
def parse(data):
    return Grid.from_string(data)


def part_one(data):
    count = 0
    seen = set()
    grid = data
    for garden_plot, position in grid:
        if position in seen:
            continue

        area = set()
        perimeter = 0
        queue = deque([position])
        while queue:
            pp = queue.popleft()
            if pp in area:
                continue

            neighbors = grid.neighbors(pp, GridOrientation.Horizontal | GridOrientation.Vertical)
            perimeter += 4 - len(neighbors)

            for nv, np in neighbors:
                if np not in area and nv == garden_plot:
                    queue.append(np)
                elif nv != garden_plot:
                    perimeter += 1

            area.add(pp)

        seen.update(area)
        count += len(area) * perimeter
    return count


def part_two(data):
    count = 0
    grid = data
    seen = set()
    for garden_plot, position in grid:
        if position in seen:
            continue

        area = set()
        borders = defaultdict(lambda: defaultdict(list))
        queue = deque([position])
        while queue:
            pp = queue.popleft()
            if pp in area:
                continue

            neighbors = grid.neighbors(pp, GridOrientation.Horizontal | GridOrientation.Vertical)

            for nv, np in neighbors:
                if np not in area and nv == garden_plot:
                    queue.append(np)

            directions = {
                Direction.Up: (0, -1),
                Direction.Down: (0, 1),
                Direction.Left: (-1, 0),
                Direction.Right: (1, 0),
            }

            for direction, d_pos in directions.items():
                xx = pp[0] + d_pos[0]
                yy = pp[1] + d_pos[1]

                def add_border():
                    match direction:
                        case Direction.Up | Direction.Down:
                            borders[direction][pp[1]].append(pp[0])
                        case Direction.Left | Direction.Right:
                            borders[direction][pp[0]].append(pp[1])

                try:
                    if grid[(xx, yy)] != garden_plot:
                        add_border()
                except IndexError:
                    add_border()

            area.add(pp)

        seen.update(area)

        sides = 0
        for border in borders.values():
            for line in border.values():
                sides += 1
                line.sort()
                for i, l in enumerate(line):
                    if i < len(line) - 1:
                        if l < (line[i + 1] - 1):
                            sides += 1

        count += len(area) * sides

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
