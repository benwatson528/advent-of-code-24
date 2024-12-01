import os
from pathlib import Path

from main.day01.historian_hysteria import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 11


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 3569916


def test_p2_simple():
    assert solve_p2(*read_input("data/test_input.txt")) == 31


def test_p2_real():
    assert solve_p2(*read_input("data/input.txt")) == 26407426


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        left = []
        right = []
        for line in f:
            l, r = line.strip().split()
            left.append(int(l))
            right.append(int(r))
        return left, right
