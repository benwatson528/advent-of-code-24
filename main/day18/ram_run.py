from collections import deque


def solve_p1(total_bytes, bounds, num_active_bytes) -> int:
    walls = set(total_bytes[:num_active_bytes+1])
    current = (0, 0)
    end = (bounds - 1, bounds - 1)
    to_visit = deque()
    to_visit.append((current, []))
    visited = set()
    while to_visit:
        current, path_travelled = to_visit.popleft()
        if current == end:
            return len(path_travelled)
        elif current in visited:
            continue
        elif current in walls:
            continue
        elif current[0] < 0 or current[0] > bounds or current[1] < 0 or current[1] > bounds:
            continue

        visited.add(current)
        to_visit.extend(
            ((current[0] + direction[0], current[1] + direction[1]), path_travelled + [current]) for direction in
            [(1, 0), (-1, 0), (0, 1), (0, -1)])
    return 0


def solve_p2(total_bytes, bounds) -> str:
    for i in range(len(total_bytes)):
        if not solve_p1(total_bytes, bounds, i):
            return f"{total_bytes[i][0]},{total_bytes[i][1]}"
