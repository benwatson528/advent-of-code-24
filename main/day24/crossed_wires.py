from collections import OrderedDict

import graphviz

BITWISE_OPS = {"AND": "&", "OR": "|", "XOR": "^"}


def solve_p1(inputs, equations) -> int:
    while equations:
        for equation in equations:
            if equation[0] in inputs and equation[2] in inputs:
                inputs[equation[4]] = eval(f"{inputs[equation[0]]} {BITWISE_OPS[equation[1]]} {inputs[equation[2]]}")
                equations.remove(equation)
    return int("".join([str(v) for i, v in OrderedDict(reversed(sorted(inputs.items()))).items() if i.startswith("z")]),
               2)


def solve_p2(inputs, equations) -> str:
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
    return ""
