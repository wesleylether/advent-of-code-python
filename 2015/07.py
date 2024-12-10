from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
instructions = {}
results = {}

for command in input_file.splitlines():
    signals, wire = command.split("->")
    instructions[wire.strip()] = signals.strip().split(" ")


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    result = None
    if name not in results:
        signals = instructions[name]
        if len(signals) == 1:
            result = calculate(signals[0])
        else:
            operation = signals[-2]
            if operation == "AND":
                result = calculate(signals[0]) & calculate(signals[2])
            elif operation == "OR":
                result = calculate(signals[0]) | calculate(signals[2])
            elif operation == "NOT":
                result = ~calculate(signals[1]) & 0xFFFF
            elif operation == "RSHIFT":
                result = calculate(signals[0]) >> calculate(signals[2])
            elif operation == "LSHIFT":
                result = calculate(signals[0]) << calculate(signals[2])
        results[name] = result
    return results[name]


# Print the answers here
# ==========================================================================
p1 = calculate("a")
answer_part_one(p1)
results = {"b": p1}
answer_part_two(calculate("a"))

# End of Code
# ==========================================================================
timer.end_timer()
