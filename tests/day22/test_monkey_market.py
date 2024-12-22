import os
from pathlib import Path

import pytest

from main.day22.monkey_market import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), 2000) == 37327623


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 2000) == 12759339434


def test_p2_simple():
    assert solve_p2(read_input("data/test_input_p2.txt"), 2000) == 23


@pytest.mark.skip("Runs in 32s")
def test_p2_real():
    assert solve_p2(read_input("data/input.txt"), 2000) == 1405


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [int(x) for x in f.read().splitlines()]
