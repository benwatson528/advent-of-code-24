DIRECTIONS = {"^": ">", ">": "v", "v": "<", "<": "^"}
MOVEMENTS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def solve_p1(obstructions, start) -> int:
    return len({c for c, d in move(start, "^", obstructions)})


def solve_p2(obstructions, start) -> int:
    original_visited = move(start, "^", obstructions)
    return sum(not move(start, "^", obstructions | {c}) for c in {c for c, _ in original_visited if c != start})


def move(current, direction, obstructions):
    visited = {(current, direction)}
    max_x, max_y = max(x for x, _ in obstructions), max(y for y, _ in obstructions)
    while 0 <= current[0] <= max_x and 0 <= current[1] <= max_y:
        next_step = current[0] + MOVEMENTS[direction][0], current[1] + MOVEMENTS[direction][1]
        if next_step in obstructions:
            direction = DIRECTIONS[direction]
        elif (next_step, direction) in visited:
            return None
        else:
            current = next_step
        visited.add((current, direction))

    visited.remove((current, direction))
    return visited
