from modules.advent_of_code import solve
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data):
    wherehouse, instructions = data.split("\n\n")
    moves = [j for i in instructions.splitlines() for j in i]
    grid = Grid.from_string(wherehouse)
    return grid, moves


def get_direction(move):
    return {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }[move]


def part_one(data):
    grid, moves = data
    cx, cy = grid.search("@")

    for move in moves:
        dx, dy = get_direction(move)
        nx, ny = cx + dx, cy + dy

        match grid[nx, ny]:
            case "#":
                continue
            case "O":
                zx, zy = nx + dx, ny + dy
                while grid[zx, zy] == "O":
                    zx, zy = zx + dx, zy + dy
                if grid[zx, zy] == "#":
                    continue
                grid[zx, zy] = "O"

        grid[nx, ny] = "@"
        grid[cx, cy] = "."
        cx, cy = nx, ny

    return grid, sum(list(map(lambda pos: 100 * pos[1] + pos[0], grid.search_all("O"))))


def resize_grid(grid):
    new_grid = Grid(grid.width * 2, grid.height, ".")
    for g, pos in grid:
        p = pos[0] * 2, pos[1]
        match g:
            case "#":
                new_grid[p] = "#"
                new_grid[p[0] + 1, p[1]] = "#"
            case "@":
                new_grid[p] = "@"
            case "O":
                new_grid[p] = "["
                new_grid[p[0] + 1, p[1]] = "]"
    return new_grid


def part_two(data):
    grid, moves = data
    grid = resize_grid(grid)
    cx, cy = grid.search("@")

    for move_index, move in enumerate(moves):
        dx, dy = get_direction(move)
        nx, ny = cx + dx, cy + dy

        def can_push(bx, by):
            match grid[bx, by]:
                case "[":
                    match grid[bx + 2 * dx, by + dy]:
                        case "#":
                            return False
                        case "[" | "]":
                            if not can_push(bx + 2 * dx, by + dy):
                                return False
                    match grid[bx + dx + 1, by + dy]:
                        case "#":
                            return False
                        case "[" | "]":
                            if not can_push(bx + dx + 1, by + dy):
                                return False
                    return True
                case "]":
                    match grid[bx + 2 * dx, by + dy]:
                        case "#":
                            return False
                        case "[" | "]":
                            if not can_push(bx + 2 * dx, by + dy):
                                return False
                    match grid[bx + dx - 1, by + dy]:
                        case "#":
                            return False
                        case "[" | "]":
                            if not can_push(bx + dx - 1, by + dy):
                                return False
                    return True

        def push(bx, by):
            if not can_push(bx, by):
                raise ValueError(f"Invalid push: {bx}, {by} -> {dx}, {dy}")
            match grid[bx, by]:
                case "[":
                    grid[bx, by] = "."
                    grid[bx + 1, by] = "."
                    match grid[bx + 2 * dx, by + dy]:
                        case "[" | "]":
                            push(bx + 2 * dx, by + dy)
                    match grid[bx + dx + 1, by + dy]:
                        case "[" | "]":
                            push(bx + dx + 1, by + dy)
                    grid[bx + dx, by + dy] = "["
                    grid[bx + dx + 1, by + dy] = "]"
                case "]":
                    grid[bx, by] = "."
                    grid[bx - 1, by] = "."
                    match grid[bx + 2 * dx, by + dy]:
                        case "[" | "]":
                            push(bx + 2 * dx, by + dy)
                    match grid[bx + dx - 1, by + dy]:
                        case "[" | "]":
                            push(bx + dx - 1, by + dy)
                    grid[bx + dx - 1, by + dy] = "["
                    grid[bx + dx, by + dy] = "]"

        if grid[nx, ny] == "#":
            continue

        match move:
            case "<":
                if grid[nx, ny] in ["[", "]"]:
                    zx, zy = nx + dx, ny + dy
                    while grid[zx, zy] in ["[", "]"]:
                        zx += dx
                        zy += dy
                    if grid[zx, zy] == "#":
                        continue
                    for i, x in enumerate(range(zx, nx)):
                        grid[x, zy] = "[" if i % 2 == 0 else "]"
            case ">":
                if grid[nx, ny] in ["[", "]"]:
                    zx, zy = nx + dx, ny + dy
                    while grid[zx, zy] in ["[", "]"]:
                        zx += dx
                        zy += dy
                    if grid[zx, zy] == "#":
                        continue
                    for i, x in enumerate(range(zx, nx, -1)):
                        grid[x, zy] = "]" if i % 2 == 0 else "["
            case "^" | "v":
                match grid[nx, ny]:
                    case "[":
                        zx, zy = nx, ny
                        valid = True
                        if grid[zx + dx, zy + dy] == "#" or grid[(zx + dx) + 1, zy + dy] == "#":
                            valid = False
                        while grid[zx, zy] in ["[", "]"]:
                            valid = can_push(zx, zy)
                            if not valid:
                                break
                            zx += 2 * dx
                            zy += dy
                        if not valid:
                            continue
                        push(nx, ny)
                    case "]":
                        zx, zy = nx, ny
                        valid = True
                        if grid[zx + dx, zy + dy] == "#" or grid[(zx + dx) - 1, zy + dy] == "#":
                            valid = False
                        if not valid:
                            continue
                        while grid[zx, zy] in ["[", "]"]:
                            valid = can_push(zx, zy)
                            if not valid:
                                break
                            zx += 2 * dx
                            zy += dy
                        if not valid:
                            continue
                        push(nx, ny)

        grid[nx, ny] = "@"
        grid[cx, cy] = "."
        cx, cy = nx, ny

    return grid, sum(list(map(lambda pos: 100 * pos[1] + pos[0], grid.search_all("["))))


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
