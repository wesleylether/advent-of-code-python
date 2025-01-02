from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    x, y = 0, 0
    houses1 = set()
    houses1.add((x, y))
    for i, d in enumerate(data):
        match d:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1

        houses1.add((x, y))

    return len(houses1)


def part_two(data):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    houses2 = set()
    houses2.add((0, 0))

    for i, d in enumerate(data):
        if i % 2 == 0:
            match d:
                case "^":
                    y1 += 1
                case "v":
                    y1 -= 1
                case ">":
                    x1 += 1
                case "<":
                    x1 -= 1

            houses2.add((x1, y1))
        else:
            match d:
                case "^":
                    y2 += 1
                case "v":
                    y2 -= 1
                case ">":
                    x2 += 1
                case "<":
                    x2 -= 1

            houses2.add((x2, y2))

    return len(houses2)


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
