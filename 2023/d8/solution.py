import re
from math import lcm

with open('input.txt') as f:
    directions = next(f).rstrip()
    next(f)

    network = {}

    for line in f.read().splitlines():
        match = re.match(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', line)
        if match:
            network[match.group(1)] = (match.group(2), match.group(3))

    #
    # Part 1
    #
    step = 0
    ix = 0
    current = 'AAA'

    while current != 'ZZZ':
        (left, right) = network[current]

        if directions[ix] == 'L':
            current = left
        else:
            current = right

        step += 1
        ix = (ix + 1) % len(directions)

    print('Part 1', step)

    #
    # Part 2
    #
    starting = []
    for k in network:
        if k.endswith('A'):
            starting.append(k)

    result = []

    for s in starting:
        ix = 0
        step = 0
        current = s

        while not current.endswith('Z'):
            (left, right) = network[current]

            if directions[ix] == 'L':
                current = left
            else:
                current = right

            step += 1
            ix = (ix + 1) % len(directions)

        result.append(step)

    # Result
    print("Part 2", lcm(*result))


