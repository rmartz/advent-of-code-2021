import sys
from collections import defaultdict

def binary_to_int(binary):
    strval = ''.join(binary)
    return int(f'0b{strval}', 2)

def collect(iter, callback):
    groups = defaultdict(list)
    for val in iter:
        key = callback(val)
        groups[key].append(val)
    return groups


def apply_bit_criteria(values, width, default: str, useMax: bool):
    for i in range(width):
        if len(values) == 1:
            return binary_to_int(values[0])

        groups = collect(values, lambda val: val[i])

        if len(groups['0']) == len(groups['1']):
            values = groups[default]
        elif useMax:
            values = max(groups.values(), key=len)
        else:
            values = min(groups.values(), key=len)
    raise Exception("Whoops")

def get_oxygen_rating(values, width):
    return apply_bit_criteria(values, width, '1', True)


def get_co2_rating(values, width):
    return apply_bit_criteria(values, width, '0', False)

input = list(sys.stdin)
width = len(input[0])

oxygen_rating = get_oxygen_rating(input, width)
co2_rating = get_co2_rating(input, width)

print(oxygen_rating * co2_rating)
