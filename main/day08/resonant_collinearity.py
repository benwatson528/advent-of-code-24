from itertools import combinations

manhattan = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
# checks that the area of the triangle formed by the three points == 0
in_line = lambda x1, y1, x2, y2, x3, y3: (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 == 0


def solve(antennas, grid_edge, is_expanded=False) -> int:
    return len({antinodes for posns in antennas.values() for pair in combinations(posns, 2) for antinodes in
                find_antinode_locations(pair, grid_edge, is_expanded)})


def find_antinode_locations(pair, grid_edge, is_expanded):
    return {(x, y) for x in range(grid_edge + 1) for y in range(grid_edge + 1) if
            is_valid_antinode(x, y, pair, is_expanded)}


def is_valid_antinode(x, y, pair, is_expanded):
    manhattans = [manhattan(x, y, *p) for p in pair]
    is_valid_distance = abs(manhattans[0] - manhattans[1]) // manhattan(*pair[0], *pair[1]) == 1 if is_expanded else (
            manhattans[0] == 2 * manhattans[1] or manhattans[1] == 2 * manhattans[0])
    return is_valid_distance and in_line(x, y, *pair[0], *pair[1])
