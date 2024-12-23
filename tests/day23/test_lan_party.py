import os
from pathlib import Path

from main.day23.lan_party import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 7


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1411


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == "co,de,ka,ta"


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == "aq,bn,ch,dt,gu,ow,pk,qy,tv,us,yx,zg,zu"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [l.split("-") for l in f.read().splitlines()]
