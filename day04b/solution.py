import sys
from itertools import islice
from operator import itemgetter

class Board(object):
    lines: "list[set[int]]" = []
    numbers: "set[int]" = set()
    original: "list[list[int]]" = []

    def __init__(self, numbers: "list[list[int]]", column_count: int, row_count: int):
        self.original = numbers
        self.lines = [
            set(numbers[row][col] for col in range(column_count))
            for row in range(row_count)
        ] + [
            set(numbers[row][col] for row in range(row_count))
            for col in range(column_count)
        ]
        self.numbers = set(numbers[row][col] for col in range(column_count) for row in range(row_count))

    def moves_to_win(self, moves: "list[int]"):
        all_moves = set(moves)

        winning_lines = (line for line in self.lines if line & all_moves == line)

        move_index = {move: pos for pos, move in enumerate(moves)}
        return min(
            max(move_index[move] for move in line) for line in winning_lines
        )

def load_row(line: str, column_count: int):
    # Row are fixed column_count, 2 characters for the number and a whitespace
    width = column_count * 3
    symbols = (line[pos:pos+2] for pos in range(0, width, 3))
    return (int(val) for val in symbols)

def load_board(input: "iter[str]", column_count: int, row_count: int):
    # Each board has a blank line before it
    next(input)
    return list(
        list(load_row(line, column_count)) for line in islice(input, row_count)
    )


def load_boards(input: "iter[str]", column_count: int, row_count: int):
    while True:
        try:
            numbers = load_board(input, column_count, row_count)
            yield Board(numbers, column_count, row_count)
        except StopIteration:
            return


moves = [int(val) for val in next(sys.stdin).split(",")]

boards = list(load_boards(sys.stdin, 5, 5))

board_moves_to_win = ((board, board.moves_to_win(moves)) for board in boards)
losing_board, moves_to_win = max(board_moves_to_win, key=itemgetter(1))


winning_move = moves[moves_to_win]
drawn_numbers = set(moves[:moves_to_win + 1])
unmarked_numbers = losing_board.numbers - drawn_numbers

unmarked_number_sum = sum(unmarked_numbers)

print(winning_move * unmarked_number_sum)
