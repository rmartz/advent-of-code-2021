from collections import namedtuple
import sys

Point = namedtuple("Point", ["x", "y"])
Fold = namedtuple("Fold", ["axis", "pos", "func"])

def until(iter, sentinel):
    while True:
        val = next(iter)
        if val == sentinel:
            return
        yield val

def fold_on(value, fold_at):
    if value < fold_at:
        return value
    return fold_at - abs(fold_at - value)

assert(fold_on(3, 7) == 3)
assert(fold_on(10, 7) == 4)


def fold_x(point: Point, fold_at) -> Point:
    if point.x < fold_at:
        return point
    return Point(x=fold_on(point.x, fold_at), y=point.y)

def fold_y(point: Point, fold_at) -> Point:
    if point.y < fold_at:
        return point
    return Point(x=point.x, y=fold_on(point.y, fold_at))


def apply_folds(point: Point, folds: "list[Fold]") -> Point:
    for fold in folds:
        point = fold.func(point, fold.pos)
    return point

def point_from_coords(coords: str) -> Point:
    x, y = coords.split(',')
    return Point(int(x), int(y))

fold_funcs = {
    'x': fold_x,
    'y': fold_y
}
def fold_from_term(term):
    direction, fold_at = term.split('=')
    return Fold(direction, int(fold_at), fold_funcs[direction])

def print_points(points: "set[Point]"):
    max_x = max(point.x for point in points) + 1
    max_y = max(point.y for point in points) + 1

    grid = [list(' ' * max_x) for _ in range(max_y)]

    for point in points:
        grid[point.y][point.x] = '#'

    print('')
    for line in grid:
        print(''.join(line))

point_coords = until((line.strip() for line in sys.stdin), '')
points = [point_from_coords(coords) for coords in point_coords]

fold_lines = (line.strip() for line in sys.stdin)
fold_terms = (line.rsplit(' ', 1)[1] for line in fold_lines)
folds = [fold_from_term(term) for term in fold_terms]

points = set(apply_folds(point, folds) for point in points)

print_points(points)
