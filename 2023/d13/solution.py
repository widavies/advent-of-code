# load the file
from collections import defaultdict

f = open("input.txt")

content = f.read().split('\n\n')
grids = map(lambda c: c.split('\n'), content)


# finds all lines of reflections in grid indexed by
# how many points they are off from being perfect
def find_reflection(grid):
    coords = set()

    rows = len(grid)
    cols = len(grid[0])

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '#':
                coords.add((y, x))

    horizontal_solutions = defaultdict(lambda: 0)
    vertical_solutions = defaultdict(lambda: 0)

    # check vertical lines
    for v in range(max(cols, rows) - 1):
        v += 0.5

        points = 0

        for (cy, cx) in coords:
            # reflect the point
            ry, rx = cy, (v - cx + v)

            if (ry, rx) not in coords and 0 <= rx < cols:
                points += 1

        vertical_solutions[points] = v

    # check horizontal lines
    for v in range(rows - 1):
        v += 0.5

        points = 0

        for (cy, cx) in coords:
            # reflect the point
            ry, rx = v - cy + v, cx

            if (ry, rx) not in coords and 0 <= ry < rows:
                points += 1

        horizontal_solutions[points] = v

    return vertical_solutions, horizontal_solutions


p1_col_sum = 0
p2_col_sum = 0

p1_row_sum = 0
p2_row_sum = 0

for grid in grids:
    vert, h = find_reflection(grid)

    p1_col_sum += int(vert[0] + 0.5)
    p1_row_sum += int(h[0] + 0.5)

    p2_col_sum += int(vert[1] + 0.5)
    p2_row_sum += int(h[1] + 0.5)


print(p1_col_sum + 100 * p1_row_sum)
print(p2_col_sum + 100 * p2_row_sum)