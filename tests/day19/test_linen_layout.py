import os
from pathlib import Path

import pytest

from main.day19.linen_layout import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 6


@pytest.mark.skip("Takes 6s to run")
def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 317


def test_p2_simple():
    assert solve_p2(*read_input("data/test_input.txt")) == 16


@pytest.mark.skip("Takes 6s to run")
def test_p2_real():
    assert solve_p2(*read_input("data/input.txt")) == 883443544805484


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = f.read().splitlines()
        return raw[0].split(", "), raw[2:]
