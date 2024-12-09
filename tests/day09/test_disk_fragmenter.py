import os
from pathlib import Path

import pytest

from main.day09.disk_fragmenter import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 1928


@pytest.mark.skip(reason="Runs in 30s")
def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 6340197768906


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 2858


@pytest.mark.skip(reason="Runs in 24s")
def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 6363913128533


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        disk_map = []
        file_id = 0
        for i, c in enumerate(f.read().strip()):
            if i % 2 == 0:
                for j in range(int(c)):
                    disk_map.append(str(file_id))
                file_id += 1
            else:
                for j in range(int(c)):
                    disk_map.append(".")
        return disk_map
