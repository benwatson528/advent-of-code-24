def solve(ordering_rules, page_updates) -> int:
    return sum(x[len(x) // 2] for x in page_updates if is_ordered(x, ordering_rules))


def is_ordered(update, ordering_rules):
    return all((not any((x, b) in ordering_rules for b in update[:i]) and not any(
        (a, x) in ordering_rules for a in update[i + 1:])) for i, x in enumerate(update))
