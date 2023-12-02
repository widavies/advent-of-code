from collections import defaultdict

# Construct adjacency matrix
matrix = defaultdict(lambda: [], {'end': []})

for line in open('input.txt'):
    a, b = line.rstrip().split('-')

    if b != 'start' and a != 'end':
        matrix[a].append(b)

    if a != 'start' and b != 'end':
        matrix[b].append(a)


def solve(allow_onetime_duplicate_visit):
    found = 0

    # duplicate: one time duplicate visit pass
    # at: current node location
    # visited: a set of visited nodes
    working = [(not allow_onetime_duplicate_visit, 'start', set())]

    while working:
        duplicate, at, visited = working.pop()

        found += 1

        while at != 'end':
            if not duplicate:
                neighbors = list(map(lambda ne: (ne, ne.islower() and ne in visited), matrix[at]))
            else:
                neighbors = list(map(lambda x: (x, True), filter(lambda ne: ne.isupper() or ne not in visited, matrix[at])))

            if not neighbors:
                # Incomplete path - not at end, but no valid neighbors
                found -= 1
                break

            n, checked = neighbors.pop()

            # For the rest of the neighbors, create new paths
            for neighbor, duped in neighbors:
                updated = visited.copy()
                updated.add(neighbor)

                working.append((duped, neighbor, updated))

            visited.add(n)
            duplicate, at = checked, n

    return found

import time

for i in range(10):
    start = time.time()
    # Part 1
    print(solve(False))

    # Part 2
    print(solve(True))

    end = time.time() - start
    print(end)

# Mirrors the recursive structure in some other solutions ("working" is basically what the recursive stack would look like), but a bit faster which was a pleasant finding
# Could potentially try to share visited sets through a tree structure or something