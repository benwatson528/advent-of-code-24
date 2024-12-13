import sympy as sym
from sympy import Integer


def solve(claws, max_turns=None) -> int:
    return sum(find_minimum_presses(claw, max_turns) for claw in claws)


def find_minimum_presses(claw, max_turns):
    a, b = sym.symbols('a,b')
    x_eq = sym.Eq(a * claw[0] + b * claw[2], claw[4])
    y_eq = sym.Eq(a * claw[1] + b * claw[3], claw[5])
    result = sym.solve([x_eq, y_eq], (a, b))
    if max_turns and (result[a] > max_turns or result[b] > max_turns):
        return 0
    elif not isinstance(result[a], Integer) or not isinstance(result[b], Integer):
        return 0
    else:
        return result[a] * 3 + result[b]
