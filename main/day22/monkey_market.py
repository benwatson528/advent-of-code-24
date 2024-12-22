def solve_p1(secrets, num_secrets) -> int:
    return sum(find_secret(secret, num_secrets) for secret in secrets)


def solve_p2(secrets, num_secrets) -> int:
    all_diffs = [find_secret_trade(secret, num_secrets) for secret in secrets]
    goals = []
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    goals.append(tuple([i, j, k, l]))
    max_score = 0
    for goal in goals:
        score = sum(diffs.get(goal, 0) for diffs in all_diffs)
        if score > max_score:
            max_score = score
    return max_score


def find_secret(secret, num_secrets):
    for _ in range(num_secrets):
        secret = transform_secret(secret)
    return secret


def find_secret_trade(secret, num_secrets):
    diffs = []
    secret_diffs = {}
    for i in range(num_secrets):
        last_secret = int(str(secret)[-1])
        secret = transform_secret(secret)
        score = int(str(secret)[-1])
        diffs.append(score - last_secret)
        last_four = tuple(diffs[-4:])
        if i >= 3 and last_four not in secret_diffs:
            secret_diffs[last_four] = score
    return secret_diffs


def transform_secret(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    return ((secret * 2048) ^ secret) % 16777216
