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


def coords_to_point(coords):
    x,y = coords.split(',')
    return Point(x=int(x), y=int(y))

def row_to_line(row: str):
    left, right = row.split(' -> ')
    return Line(
        left=coords_to_point(left),
        right=coords_to_point(right),
    )

def parse_input(input):
    for row in input:
        try:
            yield row_to_line(row)
        except DiagonalLineException:
            continue

lines = parse_input(sys.stdin)
points = chain.from_iterable(line.points() for line in lines)

point_counts = Counter(points)
count = sum(1 if count > 1 else 0 for count in point_counts.values())

print(count)
