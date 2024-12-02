import os
from pathlib import Path

from main.day02.rednosed_reports import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 2


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 549


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), dampen=True) == 4


def test_p2_real():
    assert solve(read_input("data/input.txt"), dampen=True) == 589


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [[int(x) for x in line.split(" ")] for line in f]
