from collections import namedtuple, Counter
from enum import Enum
from itertools import combinations, chain
import sys


Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])

class DiagonalLineException(Exception):
    pass

class Direction(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

def min_max(a, b):
    m = min(a, b)
    return m, a + b - m

def interval_to_range(start, end):
    if start < end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)

class Line(object):
    direction = None
    offset = None
    interval = None

    def __init__(self, left: Point, right: Point):
        if left.x == right.x:
            self.direction = Direction.VERTICAL
            self.offset = left.x
            min_y, max_y = min_max(left.y, right.y)
            self.interval = range(min_y, max_y + 1)
        elif left.y == right.y:
            self.direction = Direction.HORIZONTAL
            self.offset = left.y
            min_x, max_x = min_max(left.x, right.x)
            self.interval = range(min_x, max_x + 1)
        else:
            raise DiagonalLineException("Diagonal line not supported")

    def points(self):
        if self.direction == Direction.VERTICAL:
            return set(
                Point(x=self.offset, y=y) for y in self.interval
            )
        else:
            return set(
                Point(x=x, y=self.offset) for x in self.interval
            )

class DiagonalLine(object):
    x_interval = None
    y_interval = None

    def __init__(self, left: Point, right: Point):
        self.x_interval = interval_to_range(left.x, right.x)
        self.y_interval = interval_to_range(left.y, right.y)
        if len(self.x_interval) != len(self.y_interval):
            print(left)
            print(right)
            print(self.x_interval)
            print(self.y_interval)
            print(self.points())
            assert False

    def points(self):
        return set(
            Point(x=x, y=y) for x, y in zip(self.x_interval, self.y_interval)
        )

def coords_to_point(coords):
    x,y = coords.split(',')
    return Point(x=int(x), y=int(y))

def row_to_line(left: Point, right: Point):
    try:
        return Line(left, right)
    except DiagonalLineException:
        return DiagonalLine(left, right)


def parse_input(input):
    for row in input:
        left, right = row.split(' -> ')
        yield row_to_line(
            left=coords_to_point(left),
            right=coords_to_point(right),
        )

def print_grid(width, height, point_counts):
    def build_line(y):
        for x in range(width):
            point = Point(x=x, y=y)
            yield str(point_counts.get(point, '.'))
    for y in range(height):
        print(''.join(build_line(y)))

lines = parse_input(sys.stdin)
points = chain.from_iterable(line.points() for line in lines)

point_counts = Counter(points)
#print_grid(100, 100, point_counts)

intersections = (point for point, count in point_counts.items() if count > 1)
print(sum(1 for _ in intersections))
