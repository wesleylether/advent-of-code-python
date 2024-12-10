from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.grid import Grid

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
grid = Grid.from_string(input_file)
antenna_types = set()
for antenna, _ in grid:
    if antenna != ".":
        antenna_types.add(antenna)

p1 = set()
p2 = set()
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
                    if a_pos not in p1 and grid[a_pos] != antenna:
                        p1.add(a_pos)
                except IndexError:
                    pass

            b_pos = (bx + dx, by + dy)
            if 0 <= b_pos[0] <= grid.width and 0 <= a_pos[1] <= grid.height:
                try:
                    if b_pos not in p1 and grid[b_pos] != antenna:
                        p1.add(b_pos)
                except IndexError:
                    pass

            for a in [(ax, ay), (bx, by)]:
                x_pos = (a[0] + dx, a[1] + dy)
                while 0 <= x_pos[0] < grid.width and 0 <= x_pos[1] < grid.height:
                    if x_pos not in p2 and grid[x_pos] == ".":
                        p2.add(x_pos)

                    x_pos = (x_pos[0] + dx, x_pos[1] + dy)

# Print the answers here
# ==========================================================================
antenna_count = 0
for antenna in antenna_types:
    antenna_count += grid.count(antenna)

answer_part_one(len(p1))
answer_part_two(len(p2) + antenna_count)

# End of Code
# ==========================================================================
timer.end_timer()
