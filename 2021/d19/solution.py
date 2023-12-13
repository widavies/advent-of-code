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


def transform(code, coords):
    (x, y, z) = coords

    swaps = [
        (x, y, z),
        (x, -y, -z),
        (x, z, -y),
        (x, -z, y),

        (-x, y, -z),
        (-x, -y, z),
        (-x, z, y),
        (-x, -z, -y),

        (y, -x, z),
        (y, x, -z),
        (y, -z, -x),
        (y, z, x),

        (-y, x, z),
        (-y, -x, -z),
        (-y, z, -x),
        (-y, -z, x),

        (z, -x, -y),
        (z, x, y),
        (z, y, -x),
        (z, -y, x),

        (-z, x, -y),
        (-z, -x, y),
        (-z, y, x),
        (-z, -y, -x),
    ]

    return swaps[code]


# None or scanner 2 position relative to 1
def check_scanner(scanner1, scanner2):
    for change in range(24):
        transformed2 = list(map(lambda x: transform(change, x), scanner2))

        for coord1 in scanner1:
            for coord2 in transformed2:
                # relative to reference
                coord1_to_reference = set(map(lambda r1: sub(r1, coord1), scanner1))
                coord2_to_reference = set(map(lambda r2: sub(r2, coord2), transformed2))

                if len(coord1_to_reference & coord2_to_reference) >= 12:
                    return change, sub(coord1, coord2)

    return 0, None

def sub(v2, v1):
    return v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]


#
# Discover the scanner mappings
#

mappings = {}

for j in range(1, len(scanners)):
    print(j)
    for i in range(len(scanners)):
        if i <= j:
            continue

        code, mapping = check_scanner(scanners[i], scanners[j])

        if mapping is not None:
            print('got mapping to', i)
            print('apply', i)
            mappings[j] = i, code, mapping
            break
print(mappings)

final_mappings = {}
binned = set(scanners[0])

#
# Now, make them all relative to 0
#
for k in mappings:
    # 4, c3, t3
    target, _, mapping = mappings[k]

    while target != 0 and target in mappings:
        # 1, c2, t2
        #
        target, target_code, target_mapping = mappings[target]

        mapping = add(transform(target_code, mapping), target_mapping)

    final_mappings[k] = mapping

print(final_mappings)
#
# Now, count the number of unique beacons
#
for ix in range(1, len(scanners)):
    beacons = scanners[ix]

    for b in beacons:
        target, code, _ = mappings[ix]

        b = transform(code, b)

        while target != 0:
            target, code, _ = mappings[target]
            b = transform(code, b)

        binned.add(add(b, final_mappings[ix]))

print(len(binned))



