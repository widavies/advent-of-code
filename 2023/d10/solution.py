with open('example.txt') as f:
    grid = []

    for line in f.read().splitlines():
        grid.append([c for c in line])

    print(grid)

distance_grid = []

for row in grid:
    distance_grid.append(['.' for _ in range(len(row))])

print(distance_grid)

# Find S
s = None
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'S':
            s = (row, col)
            break

terminals = {
    '|': {'up', 'down'},
    '-': {'left', 'right'},
    'L': {'up', 'right'},
    'J': {'up', 'left'},
    '7': {'down', 'left'},
    'F': {'down', 'right'},
    '.': {}
}

distance_grid[s[0]][s[1]] = 0


# # returns distance
# def navigate(fr, to, distance=0):
#     fy, fx = fr
#     # If wx have the proper terminals
#     if terminals[grid[fy][fx]]
#
#     y, x  = to
#
#     if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
#         return -1
#
#     return max(
#         navigate(fr, (y, x - 1), distance + 1),  # left
#         navigate(fr, (y, x + 1), distance + 1),  # right
#         navigate(fr, (y - 1, x), distance + 1),  # up
#         navigate(fr, (y + 1, x), distance + 1)  # down
#     )
