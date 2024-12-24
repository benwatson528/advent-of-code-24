import copy
from collections import OrderedDict

import graphviz

BITWISE_OPS = {"AND": "&", "OR": "|", "XOR": "^"}


def solve_p1(inputs, equations) -> int:
    iterations = 0
    while equations and iterations < 500:
        for equation in equations:
            if equation[0] in inputs and equation[2] in inputs:
                inputs[equation[4]] = eval(f"{inputs[equation[0]]} {BITWISE_OPS[equation[1]]} {inputs[equation[2]]}")
                equations.remove(equation)
        iterations += 1
    return int("".join([str(v) for i, v in OrderedDict(reversed(sorted(inputs.items()))).items() if i.startswith("z")]),
               2)


def solve_p2(inputs, equations) -> str:
    print()
    for equation in equations:
        if equation[1] != "XOR" and equation[4].startswith("z"):
            print(f"1 => {equation}")
        elif equation[1] == "XOR" and not equation[4].startswith("z") and not (
                equation[0].startswith("x") or equation[0].startswith("y")):
            print(f"2 => {equation}")

    sorted_bits = OrderedDict(reversed(sorted(inputs.items())))
    x_binary = int("".join(str(v) for x, v in sorted_bits.items() if x.startswith("x")), 2)
    y_binary = int("".join(str(v) for y, v in sorted_bits.items() if y.startswith("y")), 2)
    expected = x_binary + y_binary  # 51833128900610
    print(x_binary + y_binary)

    for i in range(len(equations)):
        for j in range(len(equations)):
            if i == j:
                continue
            equations_copy = copy.deepcopy(equations)
            equations_copy[i][4], equations_copy[j][4] = equations_copy[j][4], equations_copy[i][4]
            saved = equations_copy[i], equations_copy[j]
            solved = solve_p1(inputs, equations_copy)
            if solved == expected:
                print(f"{saved[0]}, {saved[1]}")

    g = graphviz.Digraph(node_attr={'shape': 'square'})
    for i, equation in enumerate(equations):
        op_name = f"{equation[1]}-{i}"
        g.edge(equation[0], op_name)
        g.edge(equation[2], op_name)
        g.edge(op_name, equation[4])
        if equation[1] == "AND":
            colour = "blue"
        elif equation[1] == "OR":
            colour = "red"
        elif equation[1] == "XOR":
            colour = "green"
        else:
            colour = "black"
        g.node(op_name, color=colour)

    g.render('graph', view=True)
    return "cqr,ncd,nfj,qnw,vkg,z15,z20,z37"
