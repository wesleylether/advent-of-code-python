from functools import lru_cache

from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    data = {}
    for command in input_file.splitlines():
        signals, wire = command.split("->")
        data[wire.strip()] = signals.strip().split(" ")

    return data


def calculate(name, instructions, results: dict):
    try:
        return int(name)
    except ValueError:
        pass

    result = None
    if name not in results:
        signals = instructions[name]
        if len(signals) == 1:
            result = calculate(signals[0], instructions, results)
        else:
            operation = signals[-2]
            if operation == "AND":
                result = calculate(signals[0], instructions, results) & calculate(
                    signals[2], instructions, results
                )
            elif operation == "OR":
                result = calculate(signals[0], instructions, results) | calculate(
                    signals[2], instructions, results
                )
            elif operation == "NOT":
                result = ~calculate(signals[1], instructions, results) & 0xFFFF
            elif operation == "RSHIFT":
                result = calculate(signals[0], instructions, results) >> calculate(
                    signals[2], instructions, results
                )
            elif operation == "LSHIFT":
                result = calculate(signals[0], instructions, results) << calculate(
                    signals[2], instructions, results
                )
        results[name] = result
    return results[name]


@lru_cache(None)
def part_one():
    return calculate("a", parse_input(), {})


def part_two():
    return calculate("a", parse_input(), {"b": part_one()})


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
