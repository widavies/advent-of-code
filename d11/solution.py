# create adjacency matrix for the given input
from math import sqrt

values = [int(c) for line in open('input.txt') for c in line.strip()]

L = len(values)
W = int(sqrt(L))


def neighbors(z):
    row, col = z // W, z % W

    return list(map(lambda m: m[0] * W + m[1], filter(lambda m: 0 <= m[0] < W and 0 <= m[1] < W, [(row + y, col + x) for y in range(-1, 2) for x in range(-1, 2)])))


def forward(z):
    values[z] += 1

    if values[z] % 10 == 0:
        for neighbor in neighbors(z):
            forward(neighbor)


count = 0
step = 0

while True:
    for i in range(L):
        forward(i)

    flashes = 0

    for i in range(L):
        if values[i] >= 10:
            values[i] = 0
            flashes += 1

    if flashes == L:
        # Part 2
        print("Simultaneous", step + 1)
        break

    count += int(step < 100) * flashes
    step += 1

# Part 1
print(count)

# Improvements:
# Filter using a dict.get is nice
# Instead of recursion, a stack/queue is a nice alternative
# Problems: 0,0 neighbor? Get rid of modulo?
# Eliminate sqrt L thing?