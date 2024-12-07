import operator


def solve(cases, is_concat=False) -> int:
    return sum(target for target, *args in cases if is_calibrated_rec(args[1:], args[0], target, build_ops(is_concat)))


def is_calibrated_rec(ls, total, target, ops):
    return total == target if not ls else any(is_calibrated_rec(ls[1:], op(total, ls[0]), target, ops) for op in ops)


def build_ops(is_concat):
    return {operator.mul, operator.add, operator.rshift} if is_concat else {operator.mul, operator.add}


class ConcatableNumber:
    def __init__(self, n):
        self.n = n

    def __rshift__(self, other):
        return ConcatableNumber(int(f"{self.n}{other.n}"))

    def __mul__(self, other):
        return ConcatableNumber(self.n * other.n)

    def __add__(self, other):
        return ConcatableNumber(self.n + other.n)

    def __radd__(self, other):
        return self.n + other

    def __eq__(self, other):
        if isinstance(other, ConcatableNumber):
            return self.n == other.n
        return False
