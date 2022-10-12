# Idea: basic A* search
from collections import defaultdict

import heapq

loaded_map = []

TILES = 5

# Adjacency matrix
width, height = 0, 0

for line in open('input.txt'):
    line = line.strip()
    width = len(line)
    loaded_map += list(map(int, line))
    height += 1

og_width = width
og_height = height
width *= TILES
height *= TILES

full_map = {}

increment_cache = [1, 2, 3, 4, 5, 6, 7, 8, 9] * TILES

def lookup_impl(x, y):
    # Figure out the tile we sit in and add these together.
    # This is the distance we are from tile 0,0, and thus
    # the number of times we need to increment values
    effective_multiplier = x // og_width + y // og_height

    # Find targeted cell
    ax = x % og_width
    ay = y % og_height

    return increment_cache[loaded_map[ax + ay * og_width] - 1 + effective_multiplier]


adjacent_matrix = {}

for row in range(width):
    for col in range(height):
        adjacent_matrix[(row, col)] = []

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = row + dx, col + dy

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            adjacent_matrix[(row, col)].append((nx, ny))

# For speed,
# we precompute the values of the entire map. If memory limits are in place,
# then lookup_impl() can be swapped into the lookup() function.
#
# This takes advantage of the fact that the map is symmetric across
# the diagonal.
for ty in range(TILES):
    for tx in range(TILES):
        if tx < ty:
            continue

        for row in range(og_height):
            for col in range(og_width):
                # Our partner tile
                p_tx = ty
                p_ty = tx

                # For our tile, compute the value and figure it out
                ax = tx * og_width + col
                ay = ty * og_height + row

                value = lookup_impl(ax, ay)

                full_map[ax + ay * width] = value

                # If we happen to be on the diagonal, then we don't care about the next bit
                if p_tx == tx and p_ty == p_ty:
                    continue

                # For our partner tile
                ax = p_tx * og_width + col
                ay = p_ty * og_height + row

                full_map[ax + ay * width] = value

#
# Everything is loaded,
# the rest is the A* algorithm
#


def lookup(x, y):
    # change to return lookup_impl(x, y) for memory constrained version
    # (also comment out the map precompute step)
    return full_map[x + y * width]


# Heuristic is Manhattan distance
def heuristic(x, y):
    # Important: cannot overestimate the cost! So we must
    # assume 1 on each step
    return (height - 1 - y) + (width - 1 - x)


def solve(start, goal, h):
    open_set = [(heuristic(*start), start)]

    came_from = {}

    g_score = defaultdict(lambda: 9999)
    g_score[start] = 0

    f_score = defaultdict(lambda: 9999)
    f_score[start] = h(*start)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            n = goal
            score = 0

            while n != start:
                score += lookup(*n)
                n = came_from[n]

            return score

        for neighbor in adjacent_matrix[current]:
            tentative_g_score = g_score[current] + lookup(*neighbor)

            if tentative_g_score < g_score[neighbor]:
                past = f_score[neighbor]
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(*neighbor)

                if (past, neighbor) in open_set:
                    open_set.remove((past, neighbor))

                heapq.heappush(open_set, (f_score[neighbor], neighbor))


# Part 1
print(solve((0, 0), (og_width - 1, og_height - 1), heuristic))

# Part 2
print(solve((0, 0), (width - 1, height - 1), heuristic))

# Possible improvements
# Fibonacci heap?
# def __lt__(self, other):
#     return self.intAttribute < other.intAttribute