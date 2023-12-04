def check_around(mat, width, height, x, y):
    indices = [
        # top
        [-1, -1],
        [0, -1],
        [1, -1],
        # bottom
        [-1, 1],
        [0, 1],
        [1, 1],
        # left
        [-1, 0],
        # right
        [1, 0]
    ]

    for (ix, iy) in indices:
        if not (0 <= x + ix < width and 0 <= y + iy < height):
            continue
        elif '0' <= mat[y + iy][x + ix] <= '9' or mat[y + iy][x + ix] == '.':
            continue

        return True, x + ix, y + iy, mat[y + iy][x + ix]

    return False, 0, 0, ''


def main():
    height = 0
    width = 0
    with open('input.txt') as f:
        matrix = []

        for line in f.readlines():
            l = []
            for c in line.rstrip():
                l.append(c)

            width = len(l)
            matrix.append(l)
            height += 1

        s = 0

        adj_map = {}

        for y in range(height):
            run = ''
            fnd = False
            loc = None

            for x in range(width):
                if '0' <= matrix[y][x] <= '9':
                    run += matrix[y][x]

                    (res, loc_x, loc_y, c) = check_around(matrix, width, height, x, y)

                    if res:
                        fnd = True
                        if c == '*':
                            loc = (loc_x, loc_y)

                if not '0' <= matrix[y][x] <= '9' or x == width - 1:
                    if fnd and run != '':
                        s += int(run)
                        if loc is not None:
                            if loc in adj_map:
                                adj_map[loc].append(int(run))
                            else:
                                adj_map[loc] = [int(run)]
                    run = ''
                    fnd = False
                    loc = None

        # Part 1
        print(s)

        ratio = 0

        # Figure out the sum
        for k in adj_map:
            if len(adj_map[k]) == 2:
                ratio += adj_map[k][0] * adj_map[k][1]

        # Part 2
        print(ratio)


main()
