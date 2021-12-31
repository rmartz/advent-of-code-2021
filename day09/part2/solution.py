from collections import namedtuple
from functools import reduce
import sys

Point = namedtuple("Point", ["x", "y"])
Map = namedtuple("Map", ["grid", "max_x", "max_y"])

def product(it):
    return reduce(lambda val, acc: val * acc, it, 1)

def map_lookup(map: Map, point: Point):
    return map.grid[point.x][point.y]

def get_neighbor_points(point: Point, map: Map):
    x = point.x
    y = point.y
    if x > 0:
        yield Point(x - 1, y)
    if y > 0:
        yield Point(x, y - 1)
    if x < map.max_x - 1:
        yield Point(x + 1, y)
    if y < map.max_y - 1:
        yield Point(x, y + 1)

def get_neighbor_heights(point, map):
    for point in get_neighbor_points(point, map):
        yield map_lookup(map, point)

def is_low_point(point: Point, map: Map):
    neighbor_heights = get_neighbor_heights(point, map)

    val = map_lookup(map, point)
    return val < min(neighbor_heights)

def find_low_points(map):
    for x in range(map.max_x):
        for y in range(map.max_y):
            point = Point(x, y)
            if is_low_point(point, map):
                yield point

def find_basin(starting_point: Point, map: Map):
    queue = [starting_point]
    basin = set()
    while True:
        if not queue:
            break
        point = queue.pop()
        height = map_lookup(map, point)
        if height == 9:
            continue

        # Basins are simple and are bordered only by 9s... any neighbor that isn't a 9 is part of the basin
        neighbors = set(get_neighbor_points(point, map))
        new_neighbors = neighbors - basin
        non_peak_neighbors = (neighbor for neighbor in new_neighbors if map_lookup(map, neighbor) < 9)
        queue.extend(non_peak_neighbors)
        basin.add(point)

    return basin

grid = [
    [int(val) for val in line.strip()]
    for line in sys.stdin
]
map = Map(grid, len(grid), len(grid[0]))

low_points = find_low_points(map)
basins = (find_basin(point, map) for point in low_points)

basin_sizes = (len(basin) for basin in basins)

largest = sorted(basin_sizes)[-3:]

print(product(largest))
