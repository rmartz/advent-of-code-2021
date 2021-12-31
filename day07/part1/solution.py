import sys

def total_difference(values, target):
    return sum(abs(value - target) for value in values)

input = next(sys.stdin)
positions = [int(pos) for pos in input.split(',')]

interval = range(min(positions), max(positions) + 1)

costs = (total_difference(positions, target) for target in interval)

optimal_cost = min(costs)

print(optimal_cost)
