# with open('example.txt') as f:
with open('input.txt') as f:
    algorithm = next(f).rstrip()
    next(f)

    # Load the image
    matrix = []

    for line in f:
        run = []
        for c in line.rstrip():
            run.append(c)
        matrix.append(run)


# Part 1
def pad_matrix(state, zero=False):
    bg_rad, mat = state

    padded = []

    width = len(mat[0])

    pad = bg_rad

    if zero:
        pad = '.'

    padding = [pad for _ in range(width + 2)]
    padded.append(padding.copy())
    for row in mat:
        if zero:
            padded.append(padding.copy())
        else:
            padded.append([pad] + row.copy() + [pad])
    padded.append(padding.copy())
    return bg_rad, padded


def transform(state):
    bg_rad, mat = state

    _, scan = pad_matrix(state)
    _, output = pad_matrix(state, True)

    check = 0
    for y in range(1, len(scan) - 1):
        for x in range(1, len(scan[y]) - 1):
            n = scan[y - 1][x - 1:x + 2] + scan[y][x - 1:x + 2] + scan[y + 1][x - 1:x + 2]
            n = ''.join(map(lambda z: '1' if z == '#' else '0', n))
            if algorithm[int(n, 2)] == '#':
                check += 1
            output[y][x] = algorithm[int(n, 2)]

    # Change the background radiation
    if bg_rad == '.' and algorithm[0] == '#':
        bg_rad = '#'
    elif bg_rad == '#' and algorithm[-1] == '.':
        bg_rad = '.'

    for y in range(0, len(output)):
        output[y][0] = bg_rad
        output[y][-1] = bg_rad

    for x in range(0, len(output[0])):
        output[0][x] = bg_rad
        output[-1][x] = bg_rad

    return bg_rad, output


def display(state):
    _, mat = state
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end='')
        print()


def count(state):
    _, mat = state
    r = 0

    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x] == '#':
                r += 1

    return r


st = '.', matrix

st = pad_matrix(st)

print('Part 1', count(transform(transform(st))))
for i in range(0, 50):
    st = transform(st)
print('Part 2', count(st))

# Time: 2.5 hours
# - Much time wasted on silly array reference mistakes
# - Took too long to find the trick of the "background level" also needing to get converted
