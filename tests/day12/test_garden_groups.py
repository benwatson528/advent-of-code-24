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
    assert solve(read_input("data/input.txt")) == 1352976


def test_p2_simple_small():
    assert solve(read_input("data/test_input.txt"), count_straight=True) == 80


def test_p2_simple_inside():
    assert solve(read_input("data/test_input_inside.txt"), count_straight=True) == 436


def test_p2_simple_e_shaped():
    assert solve(read_input("data/test_input_e_shaped.txt"), count_straight=True) == 236


def test_p2_simple_two_region():
    assert solve(read_input("data/test_input_two_region.txt"), count_straight=True) == 368


def test_p2_simple_large():
    assert solve(read_input("data/test_input_large.txt"), count_straight=True) == 1206


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        garden = defaultdict(list)
        for y, row in enumerate(f):
            for x, p in enumerate(row.strip()):
                garden[p].append((x, y))
    return garden
