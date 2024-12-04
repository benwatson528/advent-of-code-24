DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def solve_p1(grid) -> int:
    rotated_grid = ["".join(row) for row in zip(*grid[::-1])]
    return find_horizontal(grid) + find_horizontal(rotated_grid) + find_diagonal(grid)


def solve_p2(grid) -> int:
    return sum(is_cross(i, j, grid) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] == "A")


def find_horizontal(grid):
    return sum(row.count("XMAS") + row.count("SAMX") for row in grid)


def find_diagonal(grid):
    return sum(is_diagonal_match(i, j, grid, direction) for direction in DIRECTIONS for i in range(len(grid)) for j in
               range(len(grid)))


def is_diagonal_match(i, j, grid, direction):
    word = []
    for n in range(4):
        if letter := get_element(i + (n * direction[0]), j + (n * direction[1]), grid):
            if letter == "XMAS"[n]:
                word.append(letter)
            else:
                return False
    return len(word) == 4


def is_cross(i, j, grid):
    return all(is_mas_diagonal(diagonal, grid) for diagonal in
               [((i - 1, j - 1), (i + 1, j + 1)), ((i - 1, j + 1), (i + 1, j - 1))])


def is_mas_diagonal(diagonal, grid):
    a, b = [get_element(*d, grid) for d in diagonal]
    return a != b and a in ("S", "M") and b in ("S", "M")


def get_element(i, j, grid):
    return grid[i][j] if 0 <= i < len(grid) and 0 <= j < len(grid[0]) else None
