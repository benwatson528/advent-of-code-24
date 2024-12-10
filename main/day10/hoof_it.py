def solve_p1(grid, trailheads) -> int:
    return sum(len(get_ends_rec(t, grid)) for t in trailheads)


def solve_p2(grid, trailheads) -> int:
    return sum(get_distinct_trails_rec(t, grid) for t in trailheads)


def get_ends_rec(c, grid):
    return {c} if grid[c] == 9 else {s for n in get_neighbours(c)
                                     if grid.get(n) == grid[c] + 1 for s in get_ends_rec(n, grid)}


def get_distinct_trails_rec(c, grid):
    return 1 if grid[c] == 9 else sum(get_distinct_trails_rec(n, grid) for n in get_neighbours(c)
                                      if grid.get(n) == grid[c] + 1)


get_neighbours = lambda c: [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]
