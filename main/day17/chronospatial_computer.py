def solve(register, program) -> str:
    i = 0
    output = []
    while i < len(program):
        i, op_output = operate(register, program, i)
        if op_output is not None:
            output.append(str(op_output))
    return ",".join(output)


def operate(register, program, i):
    instruction = program[i]
    operand = program[i + 1]
    output = None
    match instruction:
        case 0:  # adv
            register["A"] = int(register["A"] / (pow(2, combo_op(operand, register))))
        case 1:  # bxl
            register["B"] = register["B"] ^ operand
        case 2:  # bst
            register["B"] = combo_op(operand, register) % 8
        case 3:  # jnz
            if register["A"] != 0:
                i = operand - 2
        case 4:  # bxc
            register["B"] = register["B"] ^ register["C"]
        case 5:  # out
            register_ = combo_op(operand, register) % 8
            output = register_
        case 6:  # bdv
            register["B"] = int(register["A"] / (pow(2, combo_op(operand, register))))
        case 7:  # cdv
            register["C"] = int(register["A"] / (pow(2, combo_op(operand, register))))
        case _:
            raise f"Invalid operate argument {instruction}"
    return i + 2, output


def combo_op(operand, register):
    if operand in (0, 1, 2, 3):
        return operand
    elif operand == 4:
        return register["A"]
    elif operand == 5:
        return register["B"]
    elif operand == 6:
        return register["C"]
    else:
        raise f"Invalid combo operand argument {operand}"
