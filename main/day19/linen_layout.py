from functools import cache


def solve_p1(patterns, designs) -> int:
    return sum(x != 0 for x in [is_possible(design, frozenset(patterns)) for design in designs])


def solve_p2(patterns, designs) -> int:
    return sum(is_possible(design, frozenset(patterns)) for design in designs)


@cache
def is_possible(design, patterns):
    return sum(
        is_possible(design.removeprefix(p), patterns) for p in [p for p in patterns if design.startswith(p)]) if len(
        design) else 1
