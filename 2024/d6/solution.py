import time

matrix = []

with open('input.txt') as f:
    for l in f:
        matrix.append(l.strip())

n_rows = len(matrix)
n_cols = len(matrix[0])

# find the guard
def find_guard():
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '^':
                return row, col

    return None

init_y, init_x = find_guard()

def run_simulation(obstruction=None):
    y, x = init_y, init_x
    dy, dx = -1, 0

    loop_track = set()

    while True:
        check = (y, x, dy, dx)

        if check in loop_track:
            break

        loop_track.add(check)

        ny, nx = y + dy, x + dx

        if not (0 <= ny < n_rows and 0 <= nx < n_cols):
            # calculate the real duplicate difference
            pos = set()

            for (y, x, _, _) in loop_track:
                pos.add((y, x))

            return len(pos)
        elif matrix[ny][nx] == '#' or (ny, nx) == obstruction: # obstacle
            dy, dx = dx, -dy  # turn right 90 degrees
        else:
            y, x = ny, nx

    return -1 # indicate loop, and would never return

print(run_simulation())

# try placing an obstruction at each position
num_obstacles = 0

start = time.time()

for oy in range(n_rows):
    for ox in range(n_cols):
        if matrix[oy][ox] == '.' and run_simulation((oy, ox)) == -1:
            num_obstacles += 1

print(num_obstacles)

print('Took', time.time() - start)

# improvements - use Python complex numbers to store location & distance more cleanly
# optimization - only have to place obstacles on the guard's traversed path, not every spot