from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data, _):
    instructions = []
    # Handle both string and list input
    if isinstance(data, str):
        lines = data.strip().split("\n")
    else:
        lines = data

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        op = parts[0]

        if op in ["hlf", "tpl", "inc"]:
            # Single register operations
            instructions.append((op, parts[1]))
        elif op == "jmp":
            # Jump with offset
            instructions.append((op, int(parts[1])))
        elif op in ["jie", "jio"]:
            # Conditional jumps with register and offset
            reg = parts[1].rstrip(",")
            offset = int(parts[2])
            instructions.append((op, reg, offset))

    return instructions


def execute_program(instructions, a_init=0, b_init=0):
    registers = {"a": a_init, "b": b_init}
    pc = 0  # program counter

    while 0 <= pc < len(instructions):
        instr = instructions[pc]
        op = instr[0]

        if op == "hlf":
            registers[instr[1]] //= 2
        elif op == "tpl":
            registers[instr[1]] *= 3
        elif op == "inc":
            registers[instr[1]] += 1
        elif op == "jmp":
            pc += instr[1]
            continue
        elif op == "jie":
            if registers[instr[1]] % 2 == 0:
                pc += instr[2]
                continue
        elif op == "jio":
            if registers[instr[1]] == 1:
                pc += instr[2]
                continue

        pc += 1

    return registers


def part_one(data, register):
    registers = execute_program(data)
    return registers[register]


def part_two(data, register):
    registers = execute_program(data, a_init=1)
    return registers[register]


# Answers
# ==========================================================================
solve(part_one, parse, "b")
solve(part_two, parse, "b")
