import sys

def get_neighbor_coords(x, y, max_x, max_y):
    if x > 0:
        yield (x - 1, y)
    if y > 0:
        yield (x, y - 1)
    if x < max_x - 1:
        yield (x + 1, y)
    if y < max_y - 1:
        yield (x, y + 1)

def get_neighbor_heights(x, y, map):
    max_x = len(map)
    max_y = len(map[0])

    for (x, y) in get_neighbor_coords(x, y, max_x, max_y):
        yield map[x][y]

def is_low_point(x, y, map):
    neighbor_heights = get_neighbor_heights(x, y, map)

    val = map[x][y]
    return val < min(neighbor_heights)

def find_low_points(map):
    max_x = len(map)
    max_y = len(map[0])
    for x in range(max_x):
        for y in range(max_y):
            if is_low_point(x, y, map):
                yield (x, y)

def find_low_point_risks(map):
    for x, y in find_low_points(map):
        yield map[x][y] + 1

map = [
    [int(val) for val in line.strip()]
    for line in sys.stdin
]
print(sum(find_low_point_risks(map)))
