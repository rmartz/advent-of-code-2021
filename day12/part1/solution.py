from collections import defaultdict, namedtuple
from functools import lru_cache
import sys

Node = namedtuple("Node", ["label", "is_small"])

@lru_cache
def node_from_label(label: str):
    is_small = (label.lower() == label)
    return Node(label, is_small)

def traverse(vertexes: "dict[Node, list[Node]]", path: "list[Node]", end: Node):
    current = path[-1]
    if current == end:
        yield path
        return

    neighbors = vertexes[current]
    visitable_neighbors = (node for node in neighbors if not node.is_small or node not in path)
    for neighbor in visitable_neighbors:
        path.append(neighbor)
        yield from traverse(vertexes, path, end)
        path.pop()


vertexes: "dict[Node, list[Node]]" = defaultdict(set)
start = node_from_label("start")
end = node_from_label("end")

input = (line.strip() for line in sys.stdin)
for line in input:
    left, right = (node_from_label(label) for label in line.split('-'))
    vertexes[left].add(right)
    vertexes[right].add(left)

all_paths = traverse(vertexes, [start], end)
"""
sorted_paths = sorted(','.join(node.label for node in path) for path in all_paths)
for count, path in enumerate(sorted_paths, start=1):
    print(path)
print(count)
"""
print(sum(1 for _ in all_paths))
