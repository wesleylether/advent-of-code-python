import re
from itertools import permutations

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    directions = {}
    for direction in data.splitlines():
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


def part_one(data):
    directions, cities = data

    shortest_distance = float("inf")
    for route in permutations(cities):
        current_distance = calculate_route_distance(route, directions)
        if current_distance < shortest_distance:
            shortest_distance = current_distance

    return shortest_distance


def part_two(data):
    directions, cities = data

    longest_distance = float("-inf")
    for route in permutations(cities):
        current_distance = calculate_route_distance(route, directions)
        if current_distance > longest_distance:
            longest_distance = current_distance

    return longest_distance


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
