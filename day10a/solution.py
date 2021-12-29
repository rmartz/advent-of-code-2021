import sys

push_char_pairs = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}

def find_corrupted_char(line):
    stack = []
    for char in line:
        if char in push_char_pairs:
            stack += char
            continue
        opener = stack.pop()
        target = push_char_pairs[opener]
        if char != target:
            return char
    return None

corrupted_chars = (find_corrupted_char(line.strip()) for line in sys.stdin)

char_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores = (char_scores[char] for char in corrupted_chars if char is not None)
print(sum(scores))
