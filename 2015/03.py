from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return enumerate(input_file)


def part_one():
    x, y = 0, 0
    houses1 = set()
    houses1.add((x, y))
    for i, d in parse_input():
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


def part_two():
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    houses2 = set()
    houses2.add((0, 0))

    for i, d in parse_input():
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
solve_one(part_one)
solve_two(part_two)
