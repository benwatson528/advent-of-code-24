from collections import deque, defaultdict
from typing import Set

DIRECTIONS = {'v': (0, 1), '^': (0, -1), '>': (1, 0), '<': (-1, 0)}
CLOCKWISE_TURNS = {'v': '<', '<': '^', '^': '>', '>': 'v'}
ANTICLOCKWISE_TURNS = {v: k for k, v in CLOCKWISE_TURNS.items()}


def solve(walls, start, end, direction='>') -> (int, Set[str]):
    return find_min_path(start, direction, walls, end)


def find_min_path(current, direction, walls, end):
    to_visit = deque()
    total_visited = defaultdict(set)
    to_visit.append((current, direction, 0, {current}))
    visited = {}
    while to_visit:
        current, direction, score, tiles_visited = to_visit.popleft()
        if (current, direction) in visited and score > visited[(current, direction)][0]:
            continue
        elif current in walls:
            continue

        if (current, direction) in visited and score < visited[(current, direction)][0]:
            total_visited[(current, direction)] = tiles_visited
        else:
            total_visited[(current, direction)].update(tiles_visited)

        visited[(current, direction)] = (score, tiles_visited | {current})
        to_visit.append((move(current, direction), direction, score + 1, tiles_visited | {current}))
        to_visit.append((current, CLOCKWISE_TURNS[direction], score + 1000, tiles_visited | {current}))
        to_visit.append((current, ANTICLOCKWISE_TURNS[direction], score + 1000, tiles_visited | {current}))

    lowest_end_paths = {k: v for k, v in total_visited.items() if k[0] == end}
    return min(s[0] for t, s in visited.items() if t[0] == end)


move = lambda o, m: (o[0] + DIRECTIONS[m][0], o[1] + DIRECTIONS[m][1])
