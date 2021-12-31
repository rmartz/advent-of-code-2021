import sys

def crab_cost(start, end):
    distance = abs(start - end)
    return distance * (distance + 1) / 2

def total_difference(values, target):
    return sum(crab_cost(value, target) for value in values)

input = next(sys.stdin)
positions = [int(pos) for pos in input.split(',')]

interval = range(min(positions), max(positions) + 1)

costs = (total_difference(positions, target) for target in interval)

optimal_cost = min(costs)

print(optimal_cost)
