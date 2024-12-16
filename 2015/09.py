import re
from itertools import permutations

from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    directions = {}
    for direction in input_file.splitlines():
        match = re.match(r"(\w+) to (\w+) = (\d+)", direction)
        if match:
            start, end, distance = match.groups()
            if start not in directions:
                directions[start] = {}

            if end not in directions:
                directions[end] = {}

            directions[start][end] = int(distance)
            directions[end][start] = int(distance)

    return directions, list(directions.keys())


def calculate_route_distance(route, directions):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += directions[route[i]][route[i + 1]]
    return total_distance


def part_one():
    directions, cities = parse_input()

    shortest_distance = float("inf")
    for route in permutations(cities):
        current_distance = calculate_route_distance(route, directions)
        if current_distance < shortest_distance:
            shortest_distance = current_distance

    return shortest_distance


def part_two():
    directions, cities = parse_input()

    longest_distance = float("-inf")
    for route in permutations(cities):
        current_distance = calculate_route_distance(route, directions)
        if current_distance > longest_distance:
            longest_distance = current_distance

    return longest_distance


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
