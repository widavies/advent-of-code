import itertools
from collections import defaultdict

with open('input.txt') as f:
    matrix = [l.strip() for l in f]
# node - antinode occurs when it is inline with two nodes of the same frequency, one twice as far as the other

# find bags of same frequency letters
# compare every pair and determine point slope between the two letters
# find distance between, add on both ends, if its in bounds, then add antinode

nodes = defaultdict(lambda: [])

n = len(matrix)

for row in range(n):
    for col in range(n):
        cell = matrix[row][col]

        if cell != '.':
            nodes[cell].append((row, col))

def find_anti_nodes(find_all=False):
    anti_nodes = set()

    for key, value in nodes.items():
        for (y1, x1), (y2, x2) in itertools.combinations(value, 2):
            z = 0 if find_all else 1

            while True:
                dx = (x2 - x1) * z
                dy = (y2 - y1) * z

                # look up points on both ends
                end1_x, end1_y = x1 - dx, y1 - dy
                end2_x, end2_y = x2 + dx, y2 + dy

                added = False

                # are they within the map?
                if 0 <= end1_x < n and 0 <= end1_y < n:
                    anti_nodes.add((end1_x, end1_y))
                    added = True
                if 0 <= end2_x < n and 0 <= end2_y < n:
                    anti_nodes.add((end2_x, end2_y))
                    added = True

                if not added or not find_all:
                    break

                z += 1

    return anti_nodes

print(len(find_anti_nodes()))
print(len(find_anti_nodes(True)))
