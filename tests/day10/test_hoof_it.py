import os
from pathlib import Path

from main.day10.hoof_it import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 36


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 512


def test_p2_simple():
    assert solve_p2(*read_input("data/test_input.txt")) == 81


def test_p2_real():
    assert solve_p2(*read_input("data/input.txt")) == 1045


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        grid = {}
        trailheads = set()
        for y, row in enumerate(f):
            for x, t in enumerate(row.strip()):
                if t.isdigit():
                    grid[(x, y)] = int(t)
                if t == "0":
                    trailheads.add((x, y))
    return grid, trailheads
