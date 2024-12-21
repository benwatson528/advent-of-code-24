import os
from pathlib import Path

import pytest

from main.day21.keypad_conundrum import solve


@pytest.mark.skip("No solution found")
def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 1) == 126384


@pytest.mark.skip("No solution found")
def test_p1_real():
    assert solve(read_input("data/input.txt"), 2) == -1


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
