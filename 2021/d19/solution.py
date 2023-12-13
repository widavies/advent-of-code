import re

# scanners detect beacons up to 1000 units away in each axis
# can construct region if two scanners both have a common 12 beacons they detectcA
with open('input.txt') as f:
    scanners = []

    run = []

    for line in f.read().splitlines():
        if re.match(r'([-0-9]+),([-0-9]+),([-0-9]+)', line):
            run.append(tuple(map(int, line.split(','))))
        elif run:
            scanners.append(run)
            run = []

    if run:
        scanners.append(run)

transforms = [
    lambda v: (v[0], v[1], v[2]),
    lambda v: (v[0], -v[1], -v[2]),
    lambda v: (v[0], v[2], -v[1]),
    lambda v: (v[0], -v[2], v[1]),
    lambda v: (-v[0], v[1], -v[2]),
    lambda v: (-v[0], -v[1], v[2]),
    lambda v: (-v[0], v[2], v[1]),
    lambda v: (-v[0], -v[2], -v[1]),
    lambda v: (v[1], -v[0], v[2]),
    lambda v: (v[1], v[0], -v[2]),
    lambda v: (v[1], -v[2], -v[0]),
    lambda v: (v[1], v[2], v[0]),
    lambda v: (-v[1], v[0], v[2]),
    lambda v: (-v[1], -v[0], -v[2]),
    lambda v: (-v[1], v[2], -v[0]),
    lambda v: (-v[1], -v[2], v[0]),
    lambda v: (v[2], -v[0], -v[1]),
    lambda v: (v[2], v[0], v[1]),
    lambda v: (v[2], v[1], -v[0]),
    lambda v: (v[2], -v[1], v[0]),
    lambda v: (-v[2], v[0], -v[1]),
    lambda v: (-v[2], -v[0], v[1]),
    lambda v: (-v[2], v[1], v[0]),
    lambda v: (-v[2], -v[1], -v[0])
]


def transform(tr, coords):
    return transforms[tr](coords)


# None or scanner 2 position relative to 1
def check_scanner(scanner1, scanner2):
    for change in range(24):
        for (cx, cy, cz) in scanner1:

            for coord2 in scanner2:
                ref_x, ref_y, ref_z = transform(change, coord2)

                count = 0
                for r2 in scanner2:
                    x, y, z = transform(change, r2)

                    if (cx + (x - ref_x), cy + (y - ref_y), cz + (z - ref_z)) in scanner1:
                        count += 1

                        if count >= 12:
                            return change, (cx - ref_x, cy - ref_y, cz - ref_z)


# Our goal is to merge everyone into a new scanner
composite_scanner = set(scanners[0])
merged = {0}
scanner_locations = {0: (0, 0, 0)}

while len(merged) != len(scanners):
    for j in filter(lambda x: x not in merged, range(1, len(scanners))):
        res = check_scanner(composite_scanner, scanners[j])

        if res is not None:
            code, mapping = res

            scanner_locations[j] = mapping
            merged.add(j)

            for b in scanners[j]:
                t = transform(code, b)
                composite_scanner.add((t[0] + mapping[0], t[1] + mapping[1], t[2] + mapping[2]))

print('Part 1', len(composite_scanner))

#
# Part 2
#
max_dist = 0

for i in range(len(scanner_locations)):
    for j in range(len(scanner_locations)):
        if i == j:
            continue

        a, b, c = scanner_locations[i]
        d, e, f = scanner_locations[j]

        max_dist = max(max_dist, abs(d - a) + abs(e - b) + abs(f - c))

print('Part 2', max_dist)

# Improvements
# Time: 8 hours
# - There was one big key idea that immensely simplified the problem
# - Test with asserts earlier, much wasted time re-writing the same attempts multiple times
# - Much time spent on specifics, not conceptual
# - Assumed code was working too quickly, causes doubt on other code in the solution
