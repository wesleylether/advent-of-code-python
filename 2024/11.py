from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return {v: 1 for v in input_file.split()}


def count_stones(iterations):
    index = 0
    values = parse_input()
    while index < iterations:
        index += 1

        new_values = {}

        def append_dict(key, value):
            if key in new_values.keys():
                new_values[key] += value
            else:
                new_values[key] = value

        for item, count in values.items():
            if item == "0":
                append_dict("1", count)
            elif len(item) % 2 == 0:
                mid = len(item) // 2
                l = int(item[:mid])
                r = int(item[mid:])
                append_dict(str(l), count)
                append_dict(str(r), count)
            else:
                append_dict(str(int(item) * 2024), count)

        values = new_values

    return sum(values.values())


def part_one():
    return count_stones(25)


def part_two():
    return count_stones(75)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
