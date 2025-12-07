from collections import deque
from functools import lru_cache

from modules.advent_of_code import solve
from modules.grid import Grid

ParsedData = Grid


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    return Grid.from_string(data)


def part_one(data: ParsedData):
    grid = data
    queue = deque()
    queue.append(grid.search("S"))
    count = 0

    while queue:
        location = queue.popleft()
        try:
            new_location = (location[0], location[1] + 1)
            grid_item = grid[new_location]
            match grid_item:
                case ".":
                    grid[new_location] = "|"
                    queue.append(new_location)
                case "^":
                    count += 1
                    queue.append((new_location[0] - 1, new_location[1]))
                    queue.append((new_location[0] + 1, new_location[1]))
        except IndexError:
            continue

    return count


def part_two(data):
    grid = data
    start = grid.search("S")

    @lru_cache(maxsize=None)
    def count_from(position: tuple[int, int]) -> int:
        x, y = position
        ny = y + 1

        if ny >= grid.height:
            return 1

        new_loc = (x, ny)
        cell = grid[new_loc]

        if cell == "^":
            total = 0
            lx = x - 1
            total += count_from((lx, ny))

            rx = x + 1
            total += count_from((rx, ny))

            return total
        else:
            return count_from(new_loc)

    return count_from(start)


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
