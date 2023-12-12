import re

# scanners detect beacons up to 1000 units away in each axis
# can construct region if two scanners both have a common 12 beacons they detectcA
with open('input.txt') as f:
    scanners = []

    run = []

    for line in f.read().splitlines():
        if re.match(r'([-0-9]+),([-0-9]+),([-0-9]+)', line):
            run.append(list(map(int, line.split(','))))
        elif run:
            scanners.append(run)
            run = []

    if run:
        scanners.append(run)

# None or scanner 2 position relative to 1
def check_scanner(scanner1, scanner2):
    # Check all the scanner orientations.
    orientations = [
        [-1, 1, 1],
        [1, -1, 1],
        [1, 1, -1],
        [-1, -1, 1],
        [1, -1, -1],
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, 1]
    ]

    swaps = [
        'right',
        'left',
        'outside',
    ]

    def transform(sw, orientation, coords):
        (x, y, z) = coords

        if sw == 'outside':
            a = x
            x = z
            z = a
        elif sw == 'left':
            a = x
            x = y
            y = a
        elif sw == 'right':
            a = y
            y = z
            z = a

        x *= orientation[0]
        y *= orientation[1]
        z *= orientation[2]

        return x, y, z

    for swap1 in swaps:
        for ori1 in orientations:
            for swap2 in swaps:
                for ori2 in orientations:
                    transformed1 = list(map(lambda x: transform(swap1, ori1, x), scanner1))
                    transformed2 = list(map(lambda x: transform(swap2, ori2, x), scanner2))

                    for coord1 in transformed1:
                        for coord2 in transformed2:
                            # Normalize both to the same beacon
                            mapped1 = list(
                                map(lambda x: (x[0] - coord1[0], x[1] - coord1[1], x[2] - coord1[2]), transformed1))
                            mapped2 = list(
                                map(lambda x: (x[0] - coord2[0], x[1] - coord2[1], x[2] - coord2[2]), transformed2))

                            # Now, check if they have more than 12 duplicates
                            if len(list(filter(lambda x: x in mapped2, mapped1))) >= 12:
                                return coord2[0] - coord1[0], coord2[1] - coord1[1], coord2[2] - coord1[2]

#
# Next idea. We can find all scanners relative coords to scanner 0.
# Transform all beacons into the same location.
#


pool = []

scan_coords = {}

# The sum is the number
for i in range(len(scanners)):
    for j in range(len(scanners)):
        if i == j:
            continue
        res = check_scanner(scanners[j], scanners[i])
        print('done')
        if res is not None:
            scan_coords[(j, i)] = res

print(scan_coords)
