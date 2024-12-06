with open('input.txt') as f:
    matrix = []

    for line in f:
        matrix.append(line.rstrip())

    n = len(matrix)

# return all indices of 'ch' in s
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def check(txt):
    total = 0
    for xi in find(txt, 'X'):
        # forward
        if txt[xi:xi + 4] == 'XMAS':
            total += 1
        # backward
        if txt[xi-3:xi+1] == 'SAMX':
            total += 1

    return total

def p1():
    total = 0

    # rows
    for row in matrix:
        total += check(row)

    # cols
    for col in range(n):
        row = ''.join([matrix[r][col] for r in range(n)])

        total += check(row)

    # '\' diagonals
    for zed in range(n):
        row = ''.join(matrix[k][zed + k] for k in range(n - zed))

        total += check(row)

        # don't process main diagonal twice
        if zed == 0:
            continue

        row = ''.join(matrix[zed + k][k] for k in range(n - zed))

        total += check(row)

    # '/' diagonals
    for zed in range(n):
        row = ''.join(matrix[n - 1 - zed - k][k] for k in range(n - zed))

        total += check(row)

        # don't process main diagonal twice
        if zed == 0:
            continue

        row = ''.join(matrix[n - 1 - k][zed + k] for k in range(n - zed))
        total += check(row)

    print('Part 1', total)


def p2():
    total = 0

    for r in range(1, n - 1):
        for c in range(1, n - 1):
            if matrix[r][c] == 'A':
                down = matrix[r - 1][c - 1] + matrix[r + 1][c + 1]
                up = matrix[r - 1][c + 1] + matrix[r + 1][c - 1]

                if down in ['SM', 'MS'] and up in ['SM', 'MS']:
                    total += 1

    print('Part 2', total)

p1()
p2()