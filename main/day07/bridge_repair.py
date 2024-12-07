import operator

cat = lambda a, b: int(str(a) + str(b))


def solve(cases, is_concat=False) -> int:
    return sum(target for target, *args in cases if is_calibrated_rec(args[1:], args[0], target, build_ops(is_concat)))


def is_calibrated_rec(ls, total, target, ops):
    return total == target if not ls else any(is_calibrated_rec(ls[1:], op(total, ls[0]), target, ops) for op in ops)


def build_ops(is_concat):
    return {operator.mul, operator.add, cat} if is_concat else {operator.mul, operator.add}
