import os
from pathlib import Path

from main.day05.print_queue import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 143


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 5248


def test_p2_simple():
    assert solve_p2(*read_input("data/test_input.txt")) == 123


def test_p2_real():
    assert solve_p2(*read_input("data/input.txt")) == 4507


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        raw_rules, raw_pages = lines[:lines.index("")], lines[lines.index("") + 1:]
        rules = [tuple(int(y) for y in x.split("|")) for x in raw_rules]
        pages = [[int(y) for y in x.split(",")] for x in raw_pages]
        return rules, pages
