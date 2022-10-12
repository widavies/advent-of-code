# Store all points as list
# Perform all reflections
# Remove duplicates
import operator

folds = []
points = []

for line in open('input.txt'):
    line = line.rstrip()

    updated = line.replace('fold along ', '')

    if updated == line:
        if not updated:
            continue

        x, y = updated.split(',')
        points.append((int(x), int(y)))
    else:
        kind, point = updated.split('=')

        if kind == 'x':
            folds.append((int(point), 100000))
        else:
            folds.append((100000, int(point)))

for fx, fy in folds:
    for i in range(len(points)):
        px, py = points[i]

        points[i] = fx - abs(fx - px), fy - abs(fy - py)

    print('Folds: ', len(set(points)))

unique = set(points)
mx = max(unique, key=operator.itemgetter(0))[0]
my = max(unique, key=operator.itemgetter(1))[1]

# Print result
print('Part #2:')
for row in range(my + 1):
    for col in range(mx + 1):
        if (col, row) in unique:
            print('|', end='')
        else:
            print('.', end='')

    print()


# Learnings:
# https://pypi.org/project/parse/ - useful library for parsing stuff
# for y in range(6): print(*[' #'[(x,y) in dots] for x in range(40)]) - good idea for printing, print can take multiple arguments then a new line isn't needed
# Numpy solution is kinda nice, just flips half of the matrix and ors it
