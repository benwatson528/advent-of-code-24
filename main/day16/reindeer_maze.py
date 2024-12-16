from collections import deque
from typing import Set

DIRECTIONS = {'v': (0, 1), '^': (0, -1), '>': (1, 0), '<': (-1, 0)}
CLOCKWISE_TURNS = {'v': '<', '<': '^', '^': '>', '>': 'v'}
ANTICLOCKWISE_TURNS = {v: k for k, v in CLOCKWISE_TURNS.items()}


def solve(walls, start, end, direction='>') -> (int, Set[str]):
    return find_min_path(start, direction, walls, end)


def find_min_path(current, direction, walls, end):
    to_visit = deque()
    to_visit.append((current, direction, 0, []))
    visited = {}
    while to_visit:
        current, direction, score, path_travelled = to_visit.popleft()
        if (current, direction) in visited and score > visited[(current, direction)][0]:
            continue
        elif current in walls:
            continue

        visited[(current, direction)] = (score, path_travelled)
        to_visit.append((move(current, direction), direction, score + 1, path_travelled + [current]))
        to_visit.append((current, CLOCKWISE_TURNS[direction], score + 1000, path_travelled + [current]))
        to_visit.append((current, ANTICLOCKWISE_TURNS[direction], score + 1000, path_travelled + [current]))


    min_score = min(s[0] for t, s in visited.items() if t[0] == end)
    shortest = {t: s for t, s in visited.items() if t[0] == end and s[0] == min_score}
    return min_score


move = lambda o, m: (o[0] + DIRECTIONS[m][0], o[1] + DIRECTIONS[m][1])
