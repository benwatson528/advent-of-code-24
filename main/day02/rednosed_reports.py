import operator


def solve(reports, dampen=False) -> int:
    return sum(is_safe_report(r, dampen) for r in reports)


def is_safe_report(r, dampen=False):
    is_safe = True
    if r[0] == r[1]:
        is_safe = False
    direction = operator.gt if r[0] < r[1] else operator.lt

    for a, b in zip(r, r[1:]):
        if not direction(b, a):
            is_safe = False
            break
        if abs(b - a) not in (1, 2, 3):
            is_safe = False
            break

    if dampen and not is_safe:
        for i in range(len(r)):
            if is_safe_report(r[:i] + r[i + 1:]):
                return True

    return is_safe
