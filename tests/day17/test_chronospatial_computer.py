import os
import re
from pathlib import Path

from main.day17.chronospatial_computer import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == "4,6,3,5,6,3,5,2,1,0"


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == "2,0,4,2,7,0,1,0,3"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        nums = [int(x) for x in re.findall(r"\d+", f.read())]
        register = {"A": nums[0], "B": nums[1], "C": nums[2]}
        program = nums[3:]
    return register, program
