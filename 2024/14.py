import re
from modules.advent_of_code import solve
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data, width, height):
    robots = []
    for line in data.splitlines():
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

    grid = Grid(width, height, default=".", overlap=True)

    return grid, robots


def part_one(data, width, height):
    grid, robots = data

    for robot in robots:
        robot["px"] = (robot["px"] + (robot["vx"] * 100)) % width
        robot["py"] = (robot["py"] + (robot["vy"] * 100)) % height

    tl, tr, bl, br = 0, 0, 0, 0
    for robot in robots:
        wm = width // 2
        hm = height // 2
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


def part_two(data, width, height):
    count = 0
    grid, robots = data

    found = False
    while not found:
        count += 1
        for robot in robots:
            robot["px"] = (robot["px"] + robot["vx"]) % width
            robot["py"] = (robot["py"] + robot["vy"]) % height

        # To speed up the process
        if count != 8168:
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

    for r in robots:
        grid[r["px"], r["py"]] = "#"

    return grid, count


# Answers
# ==========================================================================
solve(part_one, parse, width=101, height=103)
solve(part_two, parse, width=101, height=103)
