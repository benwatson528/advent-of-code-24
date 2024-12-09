def solve_p1(disk_map) -> int:
    while "." in disk_map:
        id_to_move = disk_map[-1]
        first_empty = disk_map.index(".")
        disk_map = disk_map[:first_empty] + [id_to_move] + disk_map[first_empty + 1:-1]
    return sum(i * int(c) for i, c in enumerate(disk_map) if c != ".")


def solve_p2(disk_map) -> int:
    max_file_id = max(disk_map)
    for id_to_move in range(int(max_file_id), -1, -1):
        file_size_to_move = disk_map.count(str(id_to_move))
        disk_map = move_file(disk_map, file_size_to_move, id_to_move)
    return sum(i * int(c) for i, c in enumerate(disk_map) if c != ".")


def move_file(disk_map, file_size_to_move, id_to_move):
    empty_len = 0
    for i, c in enumerate(disk_map):
        if c == '.':
            empty_len += 1
            if empty_len == file_size_to_move:
                id_start_idx = disk_map.index(str(id_to_move))
                if id_start_idx < i:
                    return disk_map
                disk_map = (disk_map[:id_start_idx] + (["."] * file_size_to_move) + disk_map[
                                                                                    id_start_idx + file_size_to_move:])
                return disk_map[:i - empty_len + 1] + ([str(id_to_move)] * file_size_to_move) + disk_map[i + 1:]
        else:
            empty_len = 0
    return disk_map
