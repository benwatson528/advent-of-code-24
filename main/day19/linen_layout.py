from functools import cache


def solve_p1(patterns, designs) -> int:
    return sum(x != 0 for x in [is_possible(design, frozenset(patterns), 0) for design in designs])


def solve_p2(patterns, designs) -> int:
    return sum(is_possible(design, frozenset(patterns), 0) for design in designs)


@cache
def is_possible(design, patterns, combinations):
    return 1 if len(design) == 0 else sum(
        is_possible(design.removeprefix(p), patterns, combinations + 1) for p in
        [p for p in patterns if design.startswith(p)])
