import os
from pathlib import Path

from main.day05.print_queue import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 143


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 5248


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        raw_ordering, raw_pages = lines[:lines.index("")], lines[lines.index("") + 1:]
        ordering_rules = [tuple(int(y) for y in x.split("|")) for x in raw_ordering]
        page_updates = [tuple(int(y) for y in x.split(",")) for x in raw_pages]
        return ordering_rules, page_updates
