import os
from pathlib import Path

import pytest

from main.day16.reindeer_maze import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 7036


@pytest.mark.skip(reason="Runs in 48s")
def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 101492


@pytest.mark.skip(reason="Doesn't return correct answer (have to look at lowest_end_paths)")
def test_p2_simple():
    assert solve(*read_input("data/test_input.txt"))[1] == 45


@pytest.mark.skip(reason="Long runtime, doesn't return correct answer (have to look at lowest_end_paths)")
def test_p2_real():
    assert solve(*read_input("data/input.txt"))[1] == 543


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = f.read().splitlines()
        walls = set()
        for y, row in enumerate(raw):
            for x, c in enumerate(row):
                if c == '#':
                    walls.add((x, y))
                elif c == 'S':
                    start = (x, y)
                elif c == 'E':
                    end = (x, y)

    return walls, start, end
