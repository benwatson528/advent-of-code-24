import os
from pathlib import Path

from main.day19.linen_layout import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 6


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 317


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = f.read().splitlines()
        return raw[0].split(", "), raw[2:]
