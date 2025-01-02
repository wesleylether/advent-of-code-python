from functools import lru_cache

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    d = {}
    for command in data.splitlines():
        signals, wire = command.split("->")
        d[wire.strip()] = signals.strip().split(" ")

    return d


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


results_part_one = None


def part_one(data):
    global results_part_one
    results_part_one = calculate("a", data, {})
    return results_part_one


def part_two(data):
    return calculate("a", data, {"b": results_part_one})


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
