import os
from pathlib import Path

import pytest

from main.day20.race_condition import solve


def test_p1_simple():
    assert sum(x >= 10 for x in solve(*read_input("data/test_input.txt"), 2)) == 10


def test_p1_real():
    assert sum(x >= 100 for x in solve(*read_input("data/input.txt"), 2)) == 1332


def test_p2_simple():
    assert sum(x >= 70 for x in solve(*read_input("data/test_input.txt"), 20)) == 41


@pytest.mark.skip(reason="Runs in 5s")
def test_p2_real():
    assert sum(x >= 100 for x in solve(*read_input("data/input.txt"), 20)) == 987695


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = f.read().splitlines()
        path = []
        for y, row in enumerate(raw):
            for x, c in enumerate(row):
                if c in ".SE":
                    path.append((x, y))
                if c == 'S':
                    start = (x, y)

    return path, start
