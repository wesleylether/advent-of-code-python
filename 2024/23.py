from collections import defaultdict

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    connected = defaultdict(list)
    for line in input_file.splitlines():
        computer1, computer2 = line.split("-")
        connected[computer1].append(computer2)
        connected[computer2].append(computer1)

    return connected


def part_one():
    count = 0
    data = parse_input()

    inter_connected = set()
    for computer, others in data.items():
        for other in others:
            for last in set(others) & set(data[other]):
                inter_connected.add(frozenset([computer, other, last]))

    for connected in inter_connected:
        if any([computer.startswith("t") for computer in connected]):
            count += 1
    return count


def part_two():
    data = parse_input()

    biggest_group = set()
    for computer, others in data.items():
        for other in others:
            rest_of_group = set(others) & set(data[other])
            group = frozenset([computer, other]) | rest_of_group
            for comp in rest_of_group:
                if comp in group:
                    group &= {comp} | set(data[comp])
            biggest_group.add(group)

    return ",".join(sorted(max(biggest_group, key=len)))


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
