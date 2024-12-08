import os
from collections import defaultdict
from pathlib import Path

from main.day08.resonant_collinearity import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 14


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 344


def test_p2_simple():
    assert solve(*read_input("data/test_input.txt"), is_expanded=True) == 34


def test_p2_real():
    assert solve(*read_input("data/input.txt"), is_expanded=True) == 1182


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        antennas = defaultdict(list)
        for y, row in enumerate(f):
            for x, a in enumerate(row.strip()):
                if a != ".":
                    antennas[a].append((x, y))
    return antennas, y
