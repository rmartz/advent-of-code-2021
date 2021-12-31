from collections import defaultdict, namedtuple
from functools import lru_cache
import sys

Node = namedtuple("Node", ["label", "is_small"])

@lru_cache
def node_from_label(label: str):
    is_small = (label.lower() == label)
    return Node(label, is_small)

def traverse(vertexes: "dict[Node, set[Node]]", path: "list[Node]", end: Node):
    current = path[-1]
    if current == end:
        yield path
        return

    neighbors = vertexes[current] - set([path[0]])
    if path[0] in neighbors:
        print(path[0], neighbors)

    visited_small_rooms = [node for node in path if node.is_small]
    if len(set(visited_small_rooms)) < len(visited_small_rooms):
        visitable_neighbors = (node for node in neighbors if not node.is_small or node not in path)
    else:
        visitable_neighbors = neighbors
    for neighbor in visitable_neighbors:
        path.append(neighbor)
        yield from traverse(vertexes, path, end)
        path.pop()


vertexes: "dict[Node, set[Node]]" = defaultdict(set)
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
