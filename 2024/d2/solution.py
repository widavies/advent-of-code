with open('input.txt', 'r') as f:
    levels = []

    for line in f:
        levels.append(list(map(int, line.split())))

def check_safe(level, ignore=None):

    if ignore:
        level = level[:ignore] + level[ignore+1:]

    zipped = zip(level, level[1:])

    ascending = True
    descending = True

    for x, y in zipped:
        if abs(x - y) not in [1, 2, 3]:
            return False

        if y < x:
            ascending = False
        elif y > x:
            descending = False

    return ascending or descending


safe = 0
safe_tolerated = 0

for lvl in levels:

    if check_safe(lvl):
        safe += 1

    for z in range(len(levels)):
        if check_safe(lvl, z):
            safe_tolerated += 1
            break

print(safe)
print(safe_tolerated)