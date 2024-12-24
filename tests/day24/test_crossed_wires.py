import os
from pathlib import Path

from main.day24.crossed_wires import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 4


def test_p1_simple_large():
    assert solve(*read_input("data/test_input_large.txt")) == 2024


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 48508229772400


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        inputs = {}
        equations = []
        for l in f.read().splitlines():
            if ":" in l:
                inputs[l.split(": ")[0]] = int(l.split(": ")[1])
            elif "->" in l:
                equations.append(l.split())
        return inputs, equations
