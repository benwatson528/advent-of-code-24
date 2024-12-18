import os
from pathlib import Path

from main.day18.ram_run import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), 6, 12) == 22


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 70, 1024) == 384


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt"), 6, 12) == 22


def test_p2_real():
    assert solve_p2(read_input("data/input.txt"), 70, 1024) == 384


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [(int(l.split(",")[0]), int(l.split(",")[1])) for l in f.read().splitlines()]
