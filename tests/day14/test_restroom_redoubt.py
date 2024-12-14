import os
import re
from pathlib import Path

from main.day14.restroom_redoubt import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 100, (11, 7)) == 12


def test_p1_real():
    assert solve(read_input("data/input.txt"), 100, (101, 103)) == 218619120


def test_p2_real():
    assert solve(read_input("data/input.txt"), 8000, (101, 103)) == 7055



def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [[int(x) for x in re.findall(r"-?\d+", l)] for l in f]
