import os
from pathlib import Path

from main.day15.warehouse_woes import solve


def test_p1_small_simple():
    assert solve(*read_input("data/test_input_small.txt")) == 2028


def test_p1_large_simple():
    assert solve(*read_input("data/test_input_large.txt")) == 10092


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 1577255


def test_p2_wide_simple():
    assert solve(*read_input("data/test_input_wide.txt", is_wide=True), is_wide=True) == 618


def test_p2_large_simple():
    assert solve(*read_input("data/test_input_large.txt", is_wide=True), is_wide=True) == 9021


def test_p2_real():
    assert solve(*read_input("data/input.txt", is_wide=True), is_wide=True) == 1597035


def read_input(file_name, is_wide=False):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        s = lines.index("")
        raw_grid, raw_movements = lines[:s], lines[s + 1:]
        movements = "".join(raw_movements)
        print()
        walls = set()
        boxes = set()
        for y, row in enumerate(raw_grid):
            for x, col in enumerate(raw_grid[y]):
                if is_wide:
                    if col == "@":
                        robot = x * 2, y
                    elif col == "#":
                        walls.update(((x * 2, y), (x * 2 + 1, y)))
                    elif col == "O":
                        boxes.add((x * 2, y))
                else:
                    if col == "@":
                        robot = x, y
                    elif col == "#":
                        walls.add((x, y))
                    elif col == "O":
                        boxes.add((x, y))
        return walls, boxes, robot, movements
