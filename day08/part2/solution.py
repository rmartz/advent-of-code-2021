from itertools import permutations, chain
import sys

output_map = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

def swap_digits(input, lookup):
    return ''.join(sorted(
       lookup[c] for c in input
    ))

def check_permutation(rosetta_words, lookup):
    for word in rosetta_words:
        translation = swap_digits(word, lookup)
        if ''.join(translation) not in output_map:
            return False
    return True

def digit_permutations(digits):
    for permutation in permutations(digits, len(digits)):
        yield dict(zip(digits, permutation))


def brute_force_lookup(rosetta_words, digits):
    for lookup in digit_permutations(digits):
        if check_permutation(rosetta_words, lookup):
            return lookup
    raise Exception("No valid lookup found")

def translate_output(rosetta_words, output_words):
    #digits = set(''.join(rosetta_words + output_words))
    digits = 'abcdefg'
    lookup = brute_force_lookup(rosetta_words, digits)

    return int(''.join(
        output_map[swap_digits(output, lookup)]
        for output in output_words
    ))

def parse_input_line(line):
    rosetta_words, output_words = line.split(' | ')

    return (rosetta_words.split(' '), output_words.split(' '))

input = (parse_input_line(line.strip()) for line in sys.stdin)

outputs = (translate_output(rosetta_words, output_words) for rosetta_words, output_words in input)

print(sum(outputs))
