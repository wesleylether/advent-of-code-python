import re
import numpy as np

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    lines = data.splitlines()
    a, b, c = (int(re.search(r"\d+", line).group()) for line in lines[:3])
    program = list(map(int, re.findall(r"\d+", lines[4])))

    return a, b, c, program


def part_one(data):
    a, b, c, program = data
    instruction_pointer = 0

    def operand(n):
        match program[n]:
            case 0 | 1 | 2 | 3:
                return program[n]
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c

    output = []

    while instruction_pointer in range(len(program)):
        opcode = program[instruction_pointer]
        instruction_pointer += 2
        match opcode:
            case 0:
                a >>= operand(instruction_pointer - 1)
            case 1:
                b ^= program[instruction_pointer - 1]
            case 2:
                b = operand(instruction_pointer - 1) & 7
            case 3:
                if a:
                    instruction_pointer = program[instruction_pointer - 1]
            case 4:
                b ^= c
            case 5:
                output.append(operand(instruction_pointer - 1) & 7)
            case 6:
                b = a >> operand(instruction_pointer - 1)
            case 7:
                c = a >> operand(instruction_pointer - 1)

    return ",".join(map(str, output))


def part_two(data):
    a, b, c, program = data
    instructions = []
    found_jump = False
    for opcode, operand in np.array_split(program, len(program) // 2):
        operand2 = [0, 1, 2, 3, "a", "b", "c"][operand]
        assert not found_jump
        match opcode:
            case 0:
                instructions.append(f"a >>= {operand2}")
            case 1:
                instructions.append(f"b ^= {operand}")
            case 2:
                instructions.append(f"b = {operand2} & 7")
            case 3:
                assert operand == 0
                found_jump = True
            case 4:
                instructions.append("b ^= c")
            case 5:
                instructions.append(f"return {operand2} & 7")
            case 6:
                instructions.append(f"b = a >> {operand2}")
            case 7:
                instructions.append(f"c = a >> {operand2}")
    vals = globals() | locals()
    exec(
        "def out_val(a):\n    b=c=0\n" + "\n".join("    " + i for i in instructions),
        vals,
        vals,
    )
    possible_a = [0]
    for i in program[::-1]:
        possible_a = [
            new_a
            for a in range(8)
            for last_a in possible_a
            if vals["out_val"](new_a := a + (last_a << 3)) == i
        ]
    return min(possible_a)


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
