import os
from pathlib import Path

import pytest

from main.day24.crossed_wires import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 4


def test_p1_simple_large():
    assert solve_p1(*read_input("data/test_input_large.txt")) == 2024


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 48508229772400


@pytest.mark.skip(reason="Manual graph visualisation and investigation")
def test_p2_real():
    assert solve_p2(*read_input("data/input_modified.txt")) == "cqr,ncd,nfj,qnw,vkg,z15,z20,z37"


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
