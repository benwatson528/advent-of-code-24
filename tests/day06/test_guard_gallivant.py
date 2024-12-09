import os
from pathlib import Path

import pytest

from main.day06.guard_gallivant import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 41


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 4826


def test_p2_simple():
    assert solve_p2(*read_input("data/test_input.txt")) == 6


@pytest.mark.skip(reason="Runs in 6s")
def test_p2_real():
    assert solve_p2(*read_input("data/input.txt")) == 1721


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        obstructions = set()
        arr = f.read().splitlines()
        for y, row in enumerate(arr):
            for x, col in enumerate(row):
                if col == "#":
                    obstructions.add((x, y))
                elif col == "^":
                    start = (x, y)
        return obstructions, start
