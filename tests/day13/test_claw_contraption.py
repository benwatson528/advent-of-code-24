import os
import re
from pathlib import Path

from main.day13.claw_contraption import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 100) == 480


def test_p1_real():
    assert solve(read_input("data/input.txt"), 100) == 36838


def test_p2_real():
    assert solve(read_input("data/input.txt", is_expanded=True)) == 83029436920891


def read_input(file_name, is_expanded=False):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        claws = []
        claw = []
        for l in f:
            claw.extend(int(x) for x in re.findall(r"\d+", l))
            if len(claw) == 6:
                if is_expanded:
                    claw[4] += 10000000000000
                    claw[5] += 10000000000000
                claws.append(tuple(claw))
                claw = []
        return claws
