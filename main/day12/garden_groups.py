def solve(garden, count_straight=False) -> int:
    return sum(find_regions(plants, count_straight) for plants in garden.values())


def find_regions(plants, count_straight):
    regions = []
    for plant in plants:
        if plant not in [x for xs in regions for x in xs]:
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
        return 0
    else:
        return len(region) * sum(4 - sum([p in get_neighbours(*plant) for p in region]) for plant in region)


get_neighbours = lambda x1, y1: [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
