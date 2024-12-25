import os
from pathlib import Path

from main.day25.code_chronicle import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 3155


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        keys = []
        locks = []
        current = []
        for l in f.read().splitlines():
            if not l:
                add_grid(current, keys, locks)
                current = []
            else:
                current.append(l)
        add_grid(current, keys, locks)
        return keys, locks


def add_grid(current, keys, locks):
    item = [r.count('#') for r in list(zip(*current[::-1]))]
    if current[0][0] == ".":
        keys.append(item)
    else:
        locks.append(item)
