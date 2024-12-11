def solve(stones, num_blinks) -> int:
    for i in range(num_blinks):
        stones = [x for s in stones for x in apply_stone_rule(s)]
    return len(stones)


def apply_stone_rule(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_s = str(stone)
        return [int(str_s[:len(str_s) // 2])] + [int(str_s[len(str_s) // 2:])]
    else:
        return [stone * 2024]
