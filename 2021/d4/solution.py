# Load file
from collections import defaultdict
from functools import reduce
from operator import add

class Board:
    def __init__(self, matrix):
        # set up row col map
        self.coords = defaultdict(list)

        self.N = len(matrix)

        for row in range(self.N):
            for col in range(self.N):
                self.coords[matrix[row][col]].append((row, col))

        # set up counts
        self.row_counts, self.col_counts = defaultdict(int), defaultdict(int)

    def mark(self, value):
        coords = self.coords.pop(value, [])
        won = False

        for row, col in coords:
            self.row_counts[row] += 1
            self.col_counts[col] += 1

            won = won or (self.row_counts[row] >= self.N or self.col_counts[col] >= self.N)

        return won

    def summed(self):
        return sum(self.coords.keys())


def parse_input():
    with open('input.txt', 'r') as f:
        nums = list(map(int, f.readline().split(',')))

        # Parse boards
        boards = []

        working = []

        for line in f:
            if line.strip():
                working.append(list(map(int, line.split())))
            else:
                if len(working) > 0:
                    boards.append(Board(working))
                    working.clear()

        if len(working) > 0:
            boards.append(Board(working))

        return nums, boards

def p1():
    nums, boards = parse_input()

    for num in nums:
        for board in boards:
            if board.mark(num):
                return board.summed() * num

    return -1

def p2():
    nums, boards = parse_input()

    for num in nums:
        for board in range(len(boards)):
            if boards[board].mark(num):
                # Check if the board happens to be the last
                if sum(b is not None for b in boards) == 1:
                    return boards[board].summed() * num

                boards[board] = None

        while None in boards:
            boards.remove(None)


    return -1


print("Winning board has score:", p1())
print("Losing board has score:", p2())
# https://www.reddit.com/r/adventofcode/comments/r8i1lq/comment/hn63vwj/?utm_source=share&utm_medium=web2x&context=3