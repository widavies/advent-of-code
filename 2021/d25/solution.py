with open('input.txt') as f:
    grid = []

    for line in f.read().splitlines():
        grid.append([c for c in line])

steps = 0

while True:
    any_moves = False

    updated = []
    for row in grid:
        updated.append(['.' for _ in range(len(row))])

    # The grid is mutable
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '>':
                spot = (col + 1) % len(grid[row])
                if grid[row][spot] == '.':
                    updated[row][spot] = '>'
                    any_moves = True
                else:
                    updated[row][col] = '>'
            elif grid[row][col] == 'v':
                updated[row][col] = 'v'

    grid = updated

    updated = []
    for row in grid:
        updated.append(['.' for _ in range(len(row))])


    # The grid is mutable
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'v':
                spot = (row + 1) % len(grid)
                if grid[spot][col] == '.':
                    updated[spot][col] = 'v'
                    any_moves = True
                else:
                    updated[row][col] = 'v'
            elif grid[row][col] == '>':
                updated[row][col] = '>'

    grid = updated

    steps += 1

    if not any_moves:
        break

print(steps)
