def solve_p1(rules, pages) -> int:
    return sum(x[len(x) // 2] for x in pages if is_ordered(x, rules))


def solve_p2(rules, pages) -> int:
    return sum(x[len(x) // 2] for x in [find_lowest_rec(x, rules, []) for x in pages if not is_ordered(x, rules)])


def is_ordered(ls, rules):
    return all(
        (all((b, x) in rules for b in ls[:i]) and all((x, a) in rules for a in ls[i + 1:])) for i, x in enumerate(ls))


def find_lowest_rec(ls, rules, ordered):
    if not ls:
        return ordered
    for x in ls:
        if all((y, x) not in rules for y in ls):
            return find_lowest_rec([i for i in ls if i != x], rules, ordered + [x])
