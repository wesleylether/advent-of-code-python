import re

from modules.advent_of_code import solve
from modules.list import List

ParsedData = List[str]


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    return List(data.splitlines())


def part_one(data: ParsedData):
    numbers = List()
    for l in data:
        numbers.append(re.findall(r"\S+", l))

    numbers = numbers.map(lambda x: List(x).map(lambda y: int(y) if y.isdigit() else y))
    total = List()
    for equation in numbers.transpose():
        operator = equation.pop()
        match operator:
            case "+":
                total.append(equation.sum())
            case "*":
                total.append(equation.product())

    return total.sum()


def part_two(data: ParsedData):
    calculations = List()
    numbers = List()

    max_width = max(len(line) for line in data)
    padded_data = [line.ljust(max_width) for line in data]

    cols = list(zip(*padded_data))

    for col in reversed(cols):
        n = ""
        for f in col:
            if f in ("+", "*"):
                if n.strip():
                    numbers.append(int(n.strip()))

                match f:
                    case "+":
                        calculations.append(numbers.sum())
                    case "*":
                        calculations.append(numbers.product())

                numbers = List()
                n = ""
            else:
                n += f

        if n.strip():
            numbers.append(int(n.strip()))

    return calculations.sum()


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
