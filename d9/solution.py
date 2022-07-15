from queue import Queue

with open('input.txt') as f:
    matrix = list(map(lambda x: [':', *x, ':'], f.read().splitlines()))
    matrix = [[':']*len(matrix[0]), *matrix, [':']*len(matrix[0])]

    empty = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    q = Queue()

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            left = matrix[row][col - 1] > matrix[row][col]
            right = matrix[row][col + 1] > matrix[row][col]
            up = matrix[row - 1][col] > matrix[row][col]
            down = matrix[row + 1][col] > matrix[row][col]

            empty[row][col] = int(left and right and up and down)

            if int(left and right and up and down):
                q.put((col, row))

    M = len(matrix)
    N = len(matrix[0])

    # Checks if zx/zy should be added
    # returns the next points to search, otherwise
    def maybe_add(zx, zy, direction):
        # The point is out of bounds
        if zx < 1 or zx >= N - 1 or zy < 1 or zy >= M - 1:
            return []

        # We've already evaluated this point
        if empty[zy][zx] != 0:
            return []

        if matrix[zy][zx] == 9:
            return []

        # Check the point we came from
        if direction == 'west' and matrix[zy][zx] > matrix[zy][zx + 1]:
            print("DOPE")
            empty[zy][zx] = empty[zy][zx + 1] + 1
            return [(zx, zy - 1), (zx - 1, zy)]
        if direction == 'east' and matrix[zy][zx] > matrix[zy][zx - 1]:
            empty[zy][zx] = empty[zy][zx - 1] + 1
            return [(zx + 1, zy), (zx, zy + 1)]
        if direction == 'north' and matrix[zy][zx] > matrix[zy - 1][zx]:
            empty[zy][zx] = empty[zy + 1][zx] + 1
            return [(zx, zy - 1), (zx + 1, zy)]
        if direction == 'south' and matrix[zy][zx] > matrix[zy - 1][zx]:
            return [(zx - 1, zy), (zx, zy + 1)]

        return []



    while not q.empty():
        x, y = q.get()

        print(x, y)

        for p in maybe_add(x - 1, y, 'west'):
            q.put(p)
        for p in maybe_add(x + 1, y, 'east'):
            q.put(p)
        for p in maybe_add(x, y - 1, 'north'):
            q.put(p)
        for p in maybe_add(x, y + 1, 'south'):
            q.put(p)


    for row in empty:
        for col in row:
            print(col, end=' ')
        print()





