from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    grid = Grid.from_string(input_file)
    antenna_types = set()
    for antenna, _ in grid:
        if antenna != ".":
            antenna_types.add(antenna)

    return grid, antenna_types


def part_one():
    count = set()
    grid, antenna_types = parse_input()

    for antenna in antenna_types:
        antennas = list(grid.search_all(antenna))
        for i in range(len(antennas)):
            ax, ay = antennas[i]
            for bx, by in antennas[i + 1 :] + antennas[:i]:
                dx = ax - bx
                dy = ay - by

                a_pos = (ax + dx, ay + dy)
                if 0 <= a_pos[0] <= grid.width and 0 <= a_pos[1] <= grid.height:
                    try:
                        if a_pos not in count and grid[a_pos] != antenna:
                            count.add(a_pos)
                    except IndexError:
                        pass

                b_pos = (bx + dx, by + dy)
                if 0 <= b_pos[0] <= grid.width and 0 <= a_pos[1] <= grid.height:
                    try:
                        if b_pos not in count and grid[b_pos] != antenna:
                            count.add(b_pos)
                    except IndexError:
                        pass

    return len(count)


def part_two():
    count = set()
    grid, antenna_types = parse_input()

    for antenna in antenna_types:
        antennas = list(grid.search_all(antenna))
        for i in range(len(antennas)):
            ax, ay = antennas[i]
            for bx, by in antennas[i + 1 :] + antennas[:i]:
                dx = ax - bx
                dy = ay - by

                for a in [(ax, ay), (bx, by)]:
                    x_pos = (a[0] + dx, a[1] + dy)
                    while 0 <= x_pos[0] < grid.width and 0 <= x_pos[1] < grid.height:
                        if x_pos not in count and grid[x_pos] == ".":
                            count.add(x_pos)

                        x_pos = (x_pos[0] + dx, x_pos[1] + dy)

    antenna_count = 0
    for antenna in antenna_types:
        antenna_count += grid.count_value(antenna)

    return len(count) + antenna_count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
