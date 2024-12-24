import os
from pathlib import Path

import pytest

from main.day21.keypad_conundrum import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 2) == 126384


def test_p1_real():
    assert solve(read_input("data/input.txt"), 2) == 136780


def test_p2_real():
    assert solve(read_input("data/input.txt"), 25) == 167538833832712


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
