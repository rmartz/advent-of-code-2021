import sys
from itertools import chain

def binary_to_int(binary):
    strval = ''.join(binary)
    return int(f'0b{strval}', 2)

sample = next(sys.stdin)
input = chain([sample], sys.stdin)


sums = [0] * (len(sample) - 1)

for count, row in enumerate(input):
    for i, bit in enumerate(row):
        if bit == '1':
            sums[i] += 1

gamma = binary_to_int('1' if sum > count / 2 else '0' for sum in sums)
epsilon = binary_to_int('1' if sum < count / 2 else '0' for sum in sums)

print(gamma * epsilon)
