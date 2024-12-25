from itertools import product


def solve(keys, locks) -> int:
    return sum(1 for pair in product(keys, locks) if all(kc + lc <= 7 for kc, lc in zip(*pair)))
