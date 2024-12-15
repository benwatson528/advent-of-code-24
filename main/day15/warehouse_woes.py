DIRECTIONS = {'v': (0, 1), '^': (0, -1), '>': (1, 0), '<': (-1, 0)}


def solve(walls, boxes, robot, movements, is_wide=False) -> int:
    for movement in movements:
        robot, boxes = take_turn_wide(robot, movement, walls, boxes) if is_wide else take_turn(robot, movement, walls,
                                                                                               boxes)
    return sum(b[0] + b[1] * 100 for b in boxes)


def take_turn(robot, movement, walls, boxes):
    new_robot = move(robot, movement)
    if new_robot in walls:
        return robot, boxes
    elif new_robot in boxes:
        if empty_space := move_boxes_rec(new_robot, movement, walls, boxes):
            boxes.remove(new_robot)
            boxes.add(empty_space)
        else:
            new_robot = robot
    return new_robot, boxes


def take_turn_wide(robot, movement, walls, boxes):
    new_robot = move(robot, movement)
    all_boxes = {(b[0] + 1, b[1]) for b in boxes} | boxes
    if new_robot in walls:
        return robot, boxes
    elif new_robot in all_boxes:
        if movement in ("v", "^"):
            box_position = new_robot if new_robot in boxes else (new_robot[0] - 1, new_robot[1])
            if vertical_neighbours := set(find_vertical_neighbours_rec(box_position, movement, walls, boxes)):
                return move_vertical(boxes, movement, new_robot, robot, vertical_neighbours, walls)
        else:
            if empty_space := move_boxes_rec(new_robot, movement, walls, all_boxes):
                move_horizontal(boxes, empty_space, movement, new_robot)
            else:
                new_robot = robot
    return new_robot, boxes


def move_vertical(boxes, movement, new_robot, robot, vertical_neighbours, walls):
    if any(is_against_wall(neighbour, movement, walls) for neighbour in vertical_neighbours):
        return robot, boxes
    else:
        move_boxes(vertical_neighbours, movement, boxes)
        return new_robot, boxes


def move_horizontal(boxes, empty_space, movement, robot):
    if movement == "<":
        for between in range(empty_space[0] + 1, robot[0], 2):
            boxes.remove((between, robot[1]))
            boxes.add(move((between, robot[1]), movement))
    else:
        for between in range(robot[0], empty_space[0], 2):
            boxes.remove((between, robot[1]))
            boxes.add(move((between, robot[1]), movement))


def find_vertical_neighbours_rec(current, movement, walls, boxes):
    if current in walls or (current[0] + 1, current[1]) in walls or current not in boxes:
        return []
    else:
        moved = move(current, movement)
        r1 = find_vertical_neighbours_rec((moved[0] - 1, moved[1]), movement, walls, boxes)
        r2 = find_vertical_neighbours_rec((moved[0] + 1, moved[1]), movement, walls, boxes)
        r3 = find_vertical_neighbours_rec((moved[0], moved[1]), movement, walls, boxes)
        return [x for xs in [r1] + [r2] + [r3] for x in xs] + [current]


def move_boxes_rec(current_box, movement, walls, boxes):
    next_box = move(current_box, movement)
    if next_box in walls:
        return None
    elif next_box not in boxes:
        return next_box
    else:
        return move_boxes_rec(next_box, movement, walls, boxes)


def is_against_wall(neighbour, direction, walls):
    return move(neighbour, direction) in walls or move((neighbour[0] + 1, neighbour[1]), direction) in walls


def move_boxes(vertical_neighbours, movement, boxes):
    moved_neighbours = {move(neighbour, movement) for neighbour in vertical_neighbours}
    boxes -= vertical_neighbours
    boxes.update(moved_neighbours)


move = lambda o, m: (o[0] + DIRECTIONS[m][0], o[1] + DIRECTIONS[m][1])

get_right_boxes = lambda boxes: {(x + 1, y) for x, y in boxes}
