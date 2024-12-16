import os
from pathlib import Path

from main.day16.reindeer_maze import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt"))[0] == 7036


def test_p1_real():
    assert solve(*read_input("data/input.txt"))[0] == 101492


def test_p2_simple():
    assert len(solve(*read_input("data/test_input.txt"))[1]) == 45


def test_p2_real():
    assert len(solve(*read_input("data/input.txt"))[1]) == -1  # 595 too high


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