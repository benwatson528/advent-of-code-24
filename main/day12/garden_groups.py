def solve_p1(garden) -> int:
    return sum(find_regions(plants) for plants in garden.values())


def solve_p2(garden) -> int:
    return sum(find_regions(plants) for plants in garden.values())


def find_regions(plants):
    regions = []
    for plant in plants:
        if plant not in [x for xs in regions for x in xs]:
            regions.append(build_region(plant, plants))
    return sum(price_region(r) for r in regions)


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


def price_region(region):
    return len(region) * sum(4 - sum([p in get_neighbours(*plant) for p in region]) for plant in region)


get_neighbours = lambda x1, y1: [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
