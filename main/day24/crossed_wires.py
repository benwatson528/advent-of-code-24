from collections import OrderedDict

BITWISE_OPS = {"AND": "&", "OR": "|", "XOR": "^"}


def solve(inputs, equations) -> int:
    while equations:
        for equation in equations:
            if equation[0] in inputs and equation[2] in inputs:
                inputs[equation[4]] = eval(f"{inputs[equation[0]]} {BITWISE_OPS[equation[1]]} {inputs[equation[2]]}")
                equations.remove(equation)
    return int("".join([str(v) for i, v in OrderedDict(reversed(sorted(inputs.items()))).items() if i.startswith("z")]),
               2)
