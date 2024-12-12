def solve(garden) -> int:
    return sum(find_regions(plant_type) for plant_name, plant_type in garden.items() if plant_name == "I")


def find_regions(plants):
    regions = []
    assigned = ()
    for plant in plants:
        if plant in assigned:
            continue
        else:
            regions.append(build_region(plant, plants, set()))
    print_grid(regions)
    return sum(price_region(r) for r in regions)


def price_region(region):
    perimeter = 0
    for plant in region:
        perimeter += 4 - sum([p in get_neighbours(*plant) for p in region])
    return len(region) * perimeter


def build_region(plant, plants, region):
    for neighbour in get_neighbours(*plant):
        if neighbour in plants:
            region.add(neighbour)

    return region


get_neighbours = lambda x1, y1: [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]


def print_grid(regions):
    print()
    for y in range(11):
        for x in range(11):
            found = False
            for i, region in enumerate(regions):
                if (x, y) in region:
                    print(i, end="")
                    found = True
                    break
            if not found:
                print(".", end="")
        print()
