from itertools import islice
from collections import Counter
import sys

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result



def pair_insertion(polymer, rules):
    for pair in window(polymer, 2):
        yield pair[0]
        try:
            yield rules[pair]
        except KeyError:
            pass
    yield pair[1]

lines = (line.strip() for line in sys.stdin)

polymer = next(lines)
next(lines)

rule_pairs = (line.strip().split(' -> ') for line in lines)
rules = dict((tuple(key), val) for key, val in rule_pairs)

steps = 10
for _ in range(steps):
    polymer = pair_insertion(polymer, rules)

counts = Counter(polymer)
print(max(counts.values()) - min(counts.values()))
