from functools import cache


def solve(patterns, designs) -> int:
    return sum(is_possible(design, frozenset(patterns)) for design in designs)


@cache
def is_possible(design, patterns):
    next_moves = [p for p in patterns if design.startswith(p)]
    if len(design) == 0:
        return True
    elif not next_moves:
        return False
    else:
        return any(is_possible(design[len(p):], patterns) for p in next_moves)
