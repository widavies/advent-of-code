# Load file
import math
from itertools import islice, zip_longest

coefficients = {
    'forward': 1,
    'down': 1,
    'up': -1
}

def p1():

    with open('input.txt', 'r') as f:
        depth = 0
        horizontal_pos = 0

        for line in f:
            op, arg = line.split()

            delta = coefficients[op] * int(arg)
            horizontal_pos += int(op == 'forward') * delta
            depth += int(op != 'forward') * delta

        print("Multiplied", depth * horizontal_pos)


def p2():
    with open('input.txt', 'r') as f:
        aim = 0
        horizontal_pos = 0
        depth = 0

        for line in f:
            op, arg = line.split()

            delta = coefficients[op] * int(arg)

            horizontal_pos += int(op == 'forward') * delta
            aim += int(op != 'forward') * delta
            depth += int(op == 'forward') * aim * delta

        print("Multiplied", depth * horizontal_pos)


p1()
p2()
