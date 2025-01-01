from itertools import product

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    return data.splitlines()


def evaluate_expression(expression):
    tokens = expression.split()
    result = float(tokens[0])

    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = float(tokens[i + 1])

        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number
        elif operator == "||":
            result = float(f"{str(int(result))}{str(int(next_number))}")

        i += 2

    return result


def calculate_possibilities(numbers, operators=None):
    if operators is None:
        operators = ["+", "*"]

    combinations = product(operators, repeat=len(numbers) - 1)

    results = []

    for combo in combinations:
        expression = str(numbers[0])
        for i, operator in enumerate(combo):
            expression += f" {operator} {numbers[i + 1]}"

        try:
            result = evaluate_expression(expression)
            results.append((expression, result))
        except ZeroDivisionError:
            results.append((expression, "divide by zero not possible"))

    return results


def part_one(data):
    count = 0
    for row in data:
        result, numbers_string = row.split(": ")
        result = int(result)
        numbers = list(map(int, numbers_string.split()))

        r1 = calculate_possibilities(numbers)
        if result in [r for _, r in r1]:
            count += result

    return count


def part_two(data):
    count = 0
    for row in data:
        result, numbers_string = row.split(": ")
        result = int(result)
        numbers = list(map(int, numbers_string.split()))

        r2 = calculate_possibilities(numbers, ["||", "+", "*"])
        if result in [r for _, r in r2]:
            count += result

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
