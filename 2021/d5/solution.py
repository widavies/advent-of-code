from itertools import zip_longest


def load_lines():
    with open('input.txt', 'r') as f:
        lines = []

        for line in f:
            coords = list(map(int, line.strip().replace('->', ',').split(',')))
            lines.append(coords)

        return lines

def bidirectional_range(start, stop):
    if start > stop:
        a = list(reversed(range(stop, start + 1)))
    else:
        a = list(range(start, stop + 1))

    return a, a[-1]

def p1():
    # Fetch only horizontal/vertical lines
    lines = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], load_lines()))

    x_max = max(max(row[0], row[2]) for row in lines) + 1
    y_max = max(max(row[1], row[3]) for row in lines) + 1
    plot = [[0 for _ in range(0, x_max)] for _ in range(0, y_max)]

    for line in lines:
        r1, a1 = bidirectional_range(line[0], line[2])
        r2, a2 = bidirectional_range(line[1], line[3])

        for x, y in zip_longest(r1, r2, fillvalue=a1 if len(r1) < len(r2) else a2):
            plot[y][x] += 1

    most_crosses = sum(sum(col >= 2 for col in row) for row in plot)
    print("DONE", most_crosses)


def p2():
    # Fetch only horizontal/vertical lines
    lines = load_lines()

    x_max = max(max(row[0], row[2]) for row in lines) + 1
    y_max = max(max(row[1], row[3]) for row in lines) + 1
    plot = [[0 for _ in range(0, x_max)] for _ in range(0, y_max)]

    for line in lines:
        r1, a1 = bidirectional_range(line[0], line[2])
        r2, a2 = bidirectional_range(line[1], line[3])

        for x, y in zip_longest(r1, r2, fillvalue=a1 if len(r1) < len(r2) else a2):
            plot[y][x] += 1

    most_crosses = sum(sum(col >= 2 for col in row) for row in plot)
    print("DONE", most_crosses)


def better():
    import numpy as np

    grid = np.zeros((2, 1000, 1000))
    ls = np.fromregex(open('input.txt'), r'\d+', [('', int)] * 4)

    print(ls)

    for (x, y, X, Y) in ls:
        dx, dy = np.sign([X - x, Y - y])
        print(dx, dy)
        while (x, y) != (X + dx, Y + dy):
            grid[dx * dy, x, y] += 1
            x += dx
            y += dy

    print((grid[0] > 1).sum(), (grid.sum(0) > 1).sum())

p1()
p2()
better()
