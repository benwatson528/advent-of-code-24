import os
from collections import defaultdict
from pathlib import Path

from main.day12.garden_groups import solve


def test_p1_simple_small():
    assert solve(read_input("data/test_input.txt")) == 140


def test_p1_simple_inside():
    assert solve(read_input("data/test_input_inside.txt")) == 772


def test_p1_simple_large():
    assert solve(read_input("data/test_input_large.txt")) == 1930


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        garden = defaultdict(list)
        for y, row in enumerate(f):
            for x, p in enumerate(row.strip()):
                garden[p].append((x, y))
    return garden
