import re

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

example = False
w, h = (11, 7) if example else (101, 103)
input_file = get_input(example)


# Start coding here
# ==========================================================================
def parse_input():
    robots = []
    for line in input_file.splitlines():
        d = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(
            {
                "px": int(d[1]),
                "py": int(d[2]),
                "vx": int(d[3]),
                "vy": int(d[4]),
                "line": line,
            }
        )

    grid = Grid(w, h, default=".", overlap=True)

    return grid, robots


def part_one():
    grid, robots = parse_input()

    for robot in robots:
        robot["px"] = (robot["px"] + (robot["vx"] * 100)) % w
        robot["py"] = (robot["py"] + (robot["vy"] * 100)) % h

    tl, tr, bl, br = 0, 0, 0, 0
    for robot in robots:
        wm = w // 2
        hm = h // 2
        x, y = robot["px"], robot["py"]
        if x < wm and y < hm:
            tl += 1
        elif x > wm and y < hm:
            tr += 1
        elif x < wm and y > hm:
            bl += 1
        elif x > wm and y > hm:
            br += 1

    return tl * tr * bl * br


def part_two():
    count = 0
    grid, robots = parse_input()

    found = False
    while not found:
        count += 1
        for robot in robots:
            robot["px"] = (robot["px"] + robot["vx"]) % w
            robot["py"] = (robot["py"] + robot["vy"]) % h

        # To speed up the process
        if count < 8100:
            continue

        def is_near(ra, rb):
            if ra == rb:
                return False
            dx = abs(ra["px"] - rb["px"])
            dy = abs(ra["py"] - rb["py"])
            return dx < 2 and dy < 2

        clustered = 0
        for robot in robots:
            if any(is_near(robot, r) for r in robots):
                clustered += 1

        threshold = clustered / len(robots)
        if threshold > 0.7:
            found = True

        # if count % 1000 == 0:
        #     print(count)

        # if count > 10000:
        #     found = True

        # g = grid.copy()
        # for r in robots:
        #     g[r["px"], r["py"]] = "#"
        #     with open(f"14/{count}.txt", "w") as f:
        #         f.write(str(g))
        #         f.close()

    for r in robots:
        grid[r["px"], r["py"]] = "#"
    print(grid)
    print(count)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
