import os
from pathlib import Path

from main.day03.mull_it_over import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 161


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 187825547


def test_p2_simple():
    assert solve(read_input("data/test_input_conditional.txt"), handle_ranges=True) == 48


def test_p2_real():
    assert solve(read_input("data/input.txt"), handle_ranges=True) == 85508223


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read()
