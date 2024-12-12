import itertools


def solve(garden, count_straight=False) -> int:
    return sum(find_regions(plants, count_straight) for plants in garden.values())


def find_regions(plants, count_straight):
    regions = []
    for plant in plants:
        if plant not in [p for ps in regions for p in ps]:
            regions.append(build_region(plant, plants))
    return sum(price_region(r, count_straight) for r in regions)


def build_region(plant, plants):
    to_visit = get_neighbours(*plant)
    visited = set()
    region = {plant}
    while to_visit:
        current = to_visit.pop()
        visited.add(current)
        if current in plants:
            region.add(current)
            to_visit.extend(n for n in get_neighbours(*current) if n not in visited)
    return region


def price_region(region, count_straight):
    if count_straight:
        return len(region) * sum(find_line_matches(region, d, r) for d, r in itertools.product([1, -1], [True, False]))
    else:
        return len(region) * sum(4 - sum([p in get_neighbours(*plant) for p in region]) for plant in region)


def find_line_matches(plants, direction, reverse=False):
    if reverse:
        plants = [(y, x) for x, y in plants]
    edges = 0
    for wall in range(min(y for x, y in plants), max(y for x, y in plants) + 1):
        plants_in_line = sorted(
            [p for p in plants if p[1] == wall and (p[0], p[1] + direction) not in plants],
            key=lambda p: p[0])
        connected_plants = sum(abs(x1 - x2) == 1 for (x1, _), (x2, _) in zip(plants_in_line, plants_in_line[1:]))
        edges += len(plants_in_line) - connected_plants
    return edges


get_neighbours = lambda x1, y1: [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
