import sys
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Map = namedtuple("Map", ["grid", "max_x", "max_y"])

def get_neighbor_points(point: Point, map: Map):
    all_neighbors = (Point(point.x + x, point.y + y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0)
    return (point for point in all_neighbors if 0 <= point.x < map.max_x and 0 <= point.y < map.max_y)

def map_lookup(map: Map, point: Point):
    return map.grid[point.x][point.y]

def set_point(map, point, value: int):
    map.grid[point.x][point.y] = value

def decrement_point(map, point):
    val = map.grid[point.x][point.y] - 1
    map.grid[point.x][point.y] = val
    return val


def map_points(map: Map) -> "iter[Point]":
    for x in range(map.max_x):
        for y in range(map.max_y):
            yield Point(x, y)



# Instead of increasing all values every, we can shift the threshold that we are comparing to
# and change only the values that flash and their neighbors
# 8 -> 9 -> 0 can become (8, 7) -> (8, 8) -> (17, 9)
# This requires inverting numbers at start, so 9 becomes 1 and 1 becomes 8

def find_flashers(map, tick):
    flashers = set(point for point in map_points(map) if map_lookup(map, point) <= tick)
    while flashers:
        point = flashers.pop()
        yield point
        neighbors = set(get_neighbor_points(point, map))
        for neighbor in neighbors:
            val = decrement_point(map, neighbor)
            if val == tick:
                flashers.add(neighbor)

def perform_tick(map, tick, interval):
    flashers = set(find_flashers(map, tick))
    for point in flashers:
        set_point(map, point, tick + interval)

    return len(flashers)

def print_map(map: Map, tick, interval):
    print(f"Tick {tick}")
    for row in map.grid:
        print(''.join(str((tick - val + interval) % 10) for val in row))


grid = [
    [10 - int(val) for val in line.strip()]
    for line in sys.stdin
]
map = Map(grid, len(grid), len(grid[0]))

interval = 10
flashes = 0
for tick in range(101):
    #print_map(map, tick, interval)
    flashes += perform_tick(map, tick, interval)

print(flashes)
