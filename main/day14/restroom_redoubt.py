import math


def solve(robots, num_turns, bounds) -> int:
    for i in range(num_turns):
        robots = [move_robot(r, bounds) for r in robots]
        if is_potential_tree(robots):
            draw_grid(robots, bounds, i)
            return i + 1

    quadrants = [0] * 5
    for r in robots:
        if quadrant := find_quadrant(r, bounds):
            quadrants[quadrant] += 1
    return math.prod(quadrants[1:])


def move_robot(robot, bounds):
    robot[0] = (robot[0] + robot[2]) % bounds[0]
    robot[1] = (robot[1] + robot[3]) % bounds[1]
    return robot


def find_quadrant(robot, bounds):
    x_quad = y_quad = None
    if robot[0] < bounds[0] // 2:
        x_quad = 0
    elif robot[0] > bounds[0] // 2:
        x_quad = 1

    if robot[1] < bounds[1] // 2:
        y_quad = 0
    elif robot[1] > bounds[1] // 2:
        y_quad = 1

    match x_quad, y_quad:
        case 0, 0:
            return 1
        case 0, 1:
            return 2
        case 1, 0:
            return 3
        case 1, 1:
            return 4
        case _:
            return None


def is_potential_tree(robots):
    robot_coords = {(r[0], r[1]) for r in robots}
    for r in robot_coords:
        if all((r[0] + i, r[1]) in robot_coords for i in range(1, 30)):
            return True
    return False


def draw_grid(robots, bounds, i):
    print()
    robot_coords = {(r[0], r[1]) for r in robots}
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            print("X", end="") if (x, y) in robot_coords else print(".", end="")
        print("\n")
