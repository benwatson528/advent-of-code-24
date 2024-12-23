from collections import deque
from itertools import permutations

DIRECTIONS = {"<": (-1, 0), "v": (0, 1), "^": (0, -1), ">": (1, 0)}
ARROWPAD_GRID = {"^": (1, 0), "A": (2, 0),
                 "<": (0, 1), "v": (1, 1), ">": (2, 1)}
NUMPAD_GRID = {"7": (0, 0), "8": (1, 0), "9": (2, 0),
               "4": (0, 1), "5": (1, 1), "6": (2, 1),
               "1": (0, 2), "2": (1, 2), "3": (2, 2),
               "0": (1, 3), "A": (2, 3)}

def solve(commands, num_robots) -> int:
    numpad_paths = build_pad_paths(NUMPAD_GRID)
    arrowpad_paths = build_pad_paths(ARROWPAD_GRID)
    score = 0
    for command in commands:
        numeric_component = int(command[:3])
        ans_length = move_keypad(command, numpad_paths, arrowpad_paths, num_robots)
        score += ans_length * numeric_component
    return score


def move_keypad(command, numpad_paths, arrowpad_paths, num_robots):
    numpad_position = 'A'
    top_level_moves = []
    for next_numpad in command:
        numpad_moves = numpad_paths[(numpad_position, next_numpad)]
        ans = move_arrows_rec(numpad_moves, num_robots, arrowpad_paths)
        top_level_moves.extend(ans)
        # top_level_moves.append("A")
        numpad_position = next_numpad
    str_ans = "".join(top_level_moves)
    return len(top_level_moves)


def move_arrows_rec(movements, num_robots, arrowpad_paths):
    if num_robots == 0:
        return movements
    else:
        robot_position = "A"
        result = ""
        for m in movements:
            partial = move_arrows_rec(arrowpad_paths[("A", m)] + "A" + arrowpad_paths[(m, "A")], num_robots - 1, arrowpad_paths)
            robot_position = m
            result += partial
        return result


def build_pad_paths(pad):
    pad_paths = {(k, k): "" for k in pad.keys()}
    valid_coords = set(pad.values())
    for start, end in permutations(pad.items(), 2):
        to_visit = deque([(start[1], [], "")])
        while to_visit:
            coord, visited, direction = to_visit.popleft()
            if coord not in valid_coords:
                continue
            elif coord == end[1]:
                pad_paths[(start[0], end[0])] = "".join(visited + [direction])
                break
            else:
                for d_sign, d_coord in DIRECTIONS.items():
                    to_visit.append(((coord[0] + d_coord[0], coord[1] + d_coord[1]), visited + [direction], d_sign))
    return pad_paths
