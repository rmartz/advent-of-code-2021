from functools import lru_cache
from itertools import chain
from collections import Counter, defaultdict
import sys

def window(seq, l=2):
    num = len(seq) - l + 1
    for i in range(num):
        yield seq[i:i+l]


@lru_cache(maxsize=None)
def pair_expansion_counts(pair, iterations):
    if iterations == 0:
        return Counter(pair)
    try:
        joiner = rules[pair]

        acc = defaultdict(int)
        for subpair in window((pair[0], rules[pair], pair[1]), 2):
            counts = pair_expansion_counts(subpair, iterations - 1)
            for key, count in counts.items():
                acc[key] += count
        acc[joiner] -= 1

        return acc
    except KeyError:
        return Counter(pair)

def polymer_expansion_counts(polymer, iterations):
    acc = defaultdict(int)
    for pair in window(polymer, 2):
        counts = pair_expansion_counts(tuple(pair), iterations)
        for key, count in counts.items():
            acc[key] += count
        acc[pair[1]] -= 1
    acc[pair[1]] += 1
    return acc



lines = (line.strip() for line in sys.stdin)

polymer = next(lines)
next(lines)

rule_pairs = (line.strip().split(' -> ') for line in lines)
rules = dict((tuple(key), val) for key, val in rule_pairs)

steps = 40
counts = polymer_expansion_counts(polymer, steps)
print(max(counts.values()) - min(counts.values()))
