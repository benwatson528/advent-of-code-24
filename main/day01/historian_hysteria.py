from collections import Counter


def solve_p1(l, r) -> int:
    return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(l), sorted(r))))


def solve_p2(l, r) -> int:
    l_counter, r_counter = Counter(l), Counter(r)
    return sum(r_counter[k] * k * v for k, v in l_counter.items())
