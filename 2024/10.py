from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.grid import Grid, GridOrientation, GridValueType

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
grid = Grid.from_string(input_file, GridValueType.Int)
visited = set()


def check_neighbours(level, position):
    global p2

    for neighbour in grid.get_neighbors(
        position,
        GridOrientation.Horizontal | GridOrientation.Vertical,
    ):
        if level == 8 and neighbour[0] == 9:
            visited.add(neighbour[1])
            p2 += 1
            continue

        if level + 1 == neighbour[0]:
            check_neighbours(neighbour[0], neighbour[1])


for item, position in grid:
    if len(visited) > 0:
        p1 += len(visited)
        visited = set()

    if item == 0:
        check_neighbours(item, position)

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
