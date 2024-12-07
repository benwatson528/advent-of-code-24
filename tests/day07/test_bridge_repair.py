import os
import re
from pathlib import Path

from main.day07.bridge_repair import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 3749


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 12839601725877


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), is_concat=True) == 11387


def test_p2_real():
    assert solve(read_input("data/input.txt"), is_concat=True) == 149956401519484


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [[int(x) for x in re.findall(r"\d+", line)] for line in f]
