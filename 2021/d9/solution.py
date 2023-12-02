from functools import reduce
from math import prod
import time

with open('input.txt') as f:
    matrix = [[10] + [int(h) for x, h in enumerate(l.strip())] + [10] for y, l in enumerate(f.readlines())]
    matrix = [[10]*len(matrix[0]), *matrix, [10]*len(matrix[0])]

    corners = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    M, N = len(matrix), len(matrix[0])

    # Count the size of the basin at cx, cy
    def spiral(cx, cy, height_mode=False):
        if not all([matrix[cy + j][cx + k] > matrix[cy][cx] for j, k in corners]):
            return 0
        elif height_mode:
            return int(matrix[cy][cx]) + 1

        adjacent = {(cy, cx)}

        def check_point(a, b):
            if not (1 <= a < N - 1 and 1 <= b < M - 1) or (b, a) in adjacent or matrix[b][a] == 9:
                return 0

            res = any([(b + j, a + k) in adjacent for j, k in corners])

            if res:
                adjacent.add((b, a))

            return res

        size, radius, last, found = 1, 1, -1, 0

        while last != found:
            last = found
            found = 0

            # Top & Bottom
            for x in range(cx - radius, cx + radius + 1):
                found += check_point(x, cy - radius) + check_point(x, cy + radius)

            # Left & Right
            for y in range(cy - radius + 1, cy + radius):
                found += check_point(cx - radius, y) + check_point(cx + radius, y)

            size += found
            radius += int(found == 0)

        return size


    t0 = time.time()

    # Part one
    counts = [spiral(x, y, height_mode=True) for x in range(1, N - 1) for y in range(1, M - 1)]
    print(sum(counts))

    # Part two
    counts = [spiral(x, y) for x in range(1, N - 1) for y in range(1, M - 1)]
    print(prod(sorted(counts)[-3:]))

    t1 = time.time()

    total = t1 - t0
    print(total)

    # Improvements:
    # - Instead of checking if it's a neighbor, just produce a list of neighbors for each point
    # - Insight: Don't need to check neighbors height at all - basins don't mix, so they must be separated by 9s
