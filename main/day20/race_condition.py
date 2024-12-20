from collections import deque
from typing import List

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(paths, start, cheat_duration) -> List[int]:
    visited = find_visited(paths, start)
    bounds = max(x for x, _ in paths), max(y for _, y in paths)
    return [time for p in paths for time in find_time_saved(p, visited, cheat_duration, bounds)]


def find_visited(path, start):
    to_visit = start
    visited = {}
    while to_visit:
        visited[to_visit] = len(visited.keys())
        to_visit = next((x for x in [(to_visit[0] + d[0], to_visit[1] + d[1]) for d in DIRECTIONS] if
                         x in path and x not in visited), None)
    return visited


def find_time_saved(current, visited, cheat_duration, bounds):
    all_reachable_paths = find_valid_ends(current, visited, cheat_duration, bounds)
    return [visited[end] - visited[current] - steps for end, steps in all_reachable_paths.items() if
            visited[end] - visited[current] > steps]


def find_valid_ends(start, paths, radius, bounds):
    to_visit = deque([(start, 0)])
    seen = set()
    valid_ends = {}
    while to_visit:
        current, steps = to_visit.popleft()
        if current in seen or current[0] < 0 or current[1] < 0 or current[0] > bounds[0] or current[1] > bounds[1]:
            continue
        seen.add(current)
        if current in paths:
            valid_ends[current] = steps
        if steps != radius:
            to_visit.extend(((current[0] + d[0], current[1] + d[1]), steps + 1) for d in DIRECTIONS)
    return valid_ends
