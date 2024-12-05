import re
from itertools import permutations

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
directions = {}
for direction in input_file.split("\n"):
    match = re.match(r"(\w+) to (\w+) = (\d+)", direction)
    if match:
        start, end, distance = match.groups()
        if start not in directions:
            directions[start] = {}

        if end not in directions:
            directions[end] = {}

        directions[start][end] = int(distance)
        directions[end][start] = int(distance)

cities = list(directions.keys())


def calculate_route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += directions[route[i]][route[i + 1]]
    return total_distance


shortest_distance = float("inf")
longest_distance = float("-inf")
for route in permutations(cities):
    current_distance = calculate_route_distance(route)
    if current_distance < shortest_distance:
        shortest_distance = current_distance
    if current_distance > longest_distance:
        longest_distance = current_distance

# Print the answers here
# ==========================================================================
answer_part_one(shortest_distance)
answer_part_two(longest_distance)

# End of Code
# ==========================================================================
timer.end_timer()
