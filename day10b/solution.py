import sys
from statistics import median

push_char_pairs = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}

def find_missing_suffix(line):
    stack = []
    for char in line:
        if char in push_char_pairs:
            stack += char
            continue
        opener = stack.pop()
        target = push_char_pairs[opener]
        if char != target:
            return None
    # Don't need to translate the stack into the missing closers... the scoring function expects the openers
    return stack[::-1]

def score_missing_suffix(suffix):
    char_scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    score = 0
    for char in suffix:
        score *= 5
        score += char_scores[char]
    return score


missing_suffixes = (find_missing_suffix(line.strip()) for line in sys.stdin)
scores = (score_missing_suffix(suffix) for suffix in missing_suffixes if suffix is not None)
print(median(scores))
