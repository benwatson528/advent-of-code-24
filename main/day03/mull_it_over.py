import re
from math import prod


def solve(instruction, handle_ranges=False) -> int:
    return sum(prod(int(x) for x in match.groups())
               for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
               if not (handle_ranges and is_disabled(instruction, match)))


def is_disabled(instruction, match):
    nearest_do_idx, nearest_dont_idx = [instruction.rfind(w, 0, match.start()) for w in ("do()", "don't()")]
    return nearest_dont_idx != -1 and nearest_dont_idx > nearest_do_idx
