import re
from functools import cmp_to_key

with open('input.txt') as f:
    rules = []

    orders = []

    for line in f:
        line = line.rstrip()
        m = re.match(r"(\d+)\|(\d+)", line)

        if m:
            rules.append((int(m.group(1)), int(m.group(2))))
        elif line != '':
            r = list(map(int, line.split(',')))
            orders.append(r)

    def compare(item1, item2):
        return -1 if (item1, item2) in rules else 0

    part1 = 0
    part2 = 0

    for o in orders:
        updated = sorted(o, key=cmp_to_key(compare))

        # invalid
        if updated != o:
            part2 += updated[len(updated) // 2]
        # valid
        else:
            part1 += o[len(o) // 2]

    print(part1)
    print(part2)
