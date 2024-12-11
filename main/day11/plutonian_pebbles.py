from collections import Counter


def solve(stones, num_blinks) -> int:
    stones_counter = Counter(stones)
    for _ in range(num_blinks):
        new_stones_counter = Counter()
        for stone, multiplier in stones_counter.items():
            for s in apply_stone_rule(stone):
                new_stones_counter[s] += multiplier
        stones_counter = new_stones_counter
    return sum(stones_counter.values())


def apply_stone_rule(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_s = str(stone)
        return [int(str_s[:len(str_s) // 2])] + [int(str_s[len(str_s) // 2:])]
    else:
        return [stone * 2024]
