from collections import defaultdict

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    connected = defaultdict(list)
    for line in data.splitlines():
        computer1, computer2 = line.split("-")
        connected[computer1].append(computer2)
        connected[computer2].append(computer1)

    return connected


def part_one(data):
    count = 0

    inter_connected = set()
    for computer, others in data.items():
        for other in others:
            for last in set(others) & set(data[other]):
                inter_connected.add(frozenset([computer, other, last]))

    for connected in inter_connected:
        if any([computer.startswith("t") for computer in connected]):
            count += 1
    return count


def part_two(data):
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
solve(part_one, parse)
solve(part_two, parse)
