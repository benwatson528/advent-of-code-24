from collections import deque, defaultdict
from functools import cache
from itertools import permutations

BIG_NUMBER = 99999999999999999999999
DIRECTIONS = {"<": (-1, 0), "v": (0, 1), "^": (0, -1), ">": (1, 0)}
ARROWPAD_GRID = {"^": (1, 0), "A": (2, 0),
                 "<": (0, 1), "v": (1, 1), ">": (2, 1)}
NUMPAD_GRID = {"7": (0, 0), "8": (1, 0), "9": (2, 0),
               "4": (0, 1), "5": (1, 1), "6": (2, 1),
               "1": (0, 2), "2": (1, 2), "3": (2, 2),
               "0": (1, 3), "A": (2, 3)}


def solve(commands, num_robots) -> int:
    score = 0
    for command in commands:
        numeric_component = int(command[:3])
        ans_length = move_keypad(command, num_robots)
        score += ans_length * numeric_component
    return score


def move_keypad(command, num_robots):
    numpad_position = 'A'
    top_level_moves = 0
    for next_numpad in command:
        shortest = BIG_NUMBER
        paths = NUMPAD_PATHS[(numpad_position, next_numpad)]
        if paths:
            for path in paths:
                ans = move_arrows_rec(path, num_robots)
                if ans < shortest:
                    shortest = ans
        else:
            shortest = 0
        top_level_moves += shortest + 1
        numpad_position = next_numpad
    return top_level_moves


@cache
def move_arrows_rec(movements, num_robots):
    if num_robots == 0:
        return len(movements)

    robot_position = "A"
    result = 0
    for m in movements:
        shortest = BIG_NUMBER
        paths = ARROWPAD_PATHS[(robot_position, m)]
        if paths:
            for path in paths:
                partial = move_arrows_rec(path, num_robots - 1)
                if partial < shortest:
                    shortest = partial
        else:
            shortest = 0
        robot_position = m
        result += shortest + 1
    shortest = BIG_NUMBER
    paths = ARROWPAD_PATHS[(robot_position, "A")]
    if paths:
        for path in paths:
            partial = move_arrows_rec(path, num_robots - 1)
            if partial < shortest:
                shortest = partial
    else:
        shortest = 0
    result += shortest
    return result


def build_pad_paths(pad):
    max_length = 5
    pad_paths = defaultdict(list)
    valid_coords = set(pad.values())
    for start, end in permutations(pad.items(), 2):
        to_visit = deque([(start[1], [], "")])
        while to_visit:
            coord, visited, direction = to_visit.popleft()
            if len(visited) > max_length:
                continue
            if coord not in valid_coords:
                continue
            elif coord == end[1]:
                pad_paths[(start[0], end[0])].append("".join(visited + [direction]))
                continue
            else:
                for d_sign, d_coord in DIRECTIONS.items():
                    to_visit.append(((coord[0] + d_coord[0], coord[1] + d_coord[1]), visited + [direction], d_sign))

    shortest_pad_paths = defaultdict(list)
    for k in pad.keys():
        shortest_pad_paths[(k, k)] = []
    for k, ls in pad_paths.items():
        shortest_length = len(min(ls, key=len))
        shortest_pad_paths[k].extend(l for l in ls if len(l) == shortest_length)
    return shortest_pad_paths


ARROWPAD_PATHS = build_pad_paths(ARROWPAD_GRID)
NUMPAD_PATHS = build_pad_paths(NUMPAD_GRID)
