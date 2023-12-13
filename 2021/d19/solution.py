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


def transform(code, coords, invert=False):
    [x, y, z] = coords

    back_swaps = [
        [x, y, z],
        [x, -y, -z],
        [x, -z, y],
        [x, z, -y],

        [-x, -y, z],
        [-x, y, -z],
        [-x, z, y],
        [-x, -z, -y],

        [-y, x, z],  #
        [y, x, -z],
        [-z, x, -y],
        [z, x, y],

        [y, -x, z],
        [-y, -x, -z],
        [-z, -x, y],
        [z, -x, -y],

        [-y, -z, x],
        [y, z, x],
        [-z, y, x],
        [z, -y, x],

        [y, -z, -x],
        [-y, z, -x],
        [z, y, -x],
        [-z, -y, -x],
    ]

    if invert:
        return back_swaps[code]

    swaps = [
        [x, y, z],
        [x, -y, -z],
        [x, z, -y],
        [x, -z, y],

        [-x, -y, z],
        [-x, y, -z],
        [-x, z, y],
        [-x, -z, -y],

        [y, -x, z],  #
        [y, x, -z],
        [y, -z, -x],
        [y, z, x],

        [-y, x, z],
        [-y, -x, -z],
        [-y, z, -x],
        [-y, -z, x],

        [z, -x, -y],
        [z, x, y],
        [z, y, -x],
        [z, -y, x],

        [-z, x, -y],
        [-z, -x, y],
        [-z, y, x],
        [-z, -y, -x],
    ]

    return swaps[code]


# None or scanner 2 position relative to 1
def check_scanner(scanner1, scanner2):
    for change1 in range(24):
        for change2 in range(24):
            transformed1 = list(map(lambda x: transform(change1, x), scanner1))
            transformed2 = list(map(lambda x: transform(change2, x), scanner2))

            for coord1 in transformed1:
                for coord2 in transformed2:
                    matching = 0
                    # Assume coord1 and coord2 are the same

                    for r1 in transformed1:
                        (rx, ry, rz) = (r1[0] - coord1[0], r1[1] - coord1[1], r1[2] - coord1[2])

                        if [coord2[0] + rx, coord2[1] + ry, coord2[2] + rz] in transformed2:

                            matching += 1

                            if matching >= 12:
                                return change2, transform(change1, [coord1[0] - coord2[0], coord1[1] - coord2[1],
                                        coord1[2] - coord2[2]], True)


c1, t1 = check_scanner(scanners[1], scanners[4])
c2, t2 = check_scanner(scanners[0], scanners[1])
c3, t3 = check_scanner(scanners[4], scanners[2])

up_dated = transform(c2, t1)

print(t2)
print(up_dated)
four_to_one = t2[0] + up_dated[0], t2[1] + up_dated[1], t2[2] + up_dated[2]
print(four_to_one) # scanner 4 is -20, -1133, 1061
#                    scanner 2-4 is 168, -1125, 72

up_dated = transform(c3, t3)

four_to_one = up_dated[0] + four_to_one[0], up_dated[1] + four_to_one[1], up_dated[2] + four_to_one[2]
print(four_to_one)
# up_dated = transform(c3, up_dated)
# four_to_one = t3[0] + up_dated[0], t3[1] + up_dated[1], t3[2] + up_dated[2]
# print(four_to_one)

# print(t1)
# print(t2)
# print(s2c)
# print(transform(c1, s2c, True))

# scan_coords = {}
#
# for i in range(1, len(scanners)):
#     for j in range(len(scanners)):
#         if i == j:
#             continue
#
#         print(i, j)
#         res = check_scanner(scanners[j], scanners[i])
#
#         if res is not None:
#             scan_coords[i] = (j, res)
#             break
#
# print(scan_coords)
exit(0)
#
# for i in range(1, len(scanners)):
#     # Make all scanners relative to scanner 0
#     (target, code, rel) = scan_coords[i]
#
#     #
#
#     while target != 0:
#         (target_target, target_code, target_rel) = scan_coords[target]
#
#         # Transform rel
#         target = target_target
#
#         if target_code == 0:
#             rel = [target_rel[0] - rel[0], target_rel[1] - rel[1], target_rel[2] - rel[2]]
#         else:
#             rel = transform(target_code, [target_rel[0] - rel[0], target_rel[1] - rel[1], target_rel[2] - rel[2]])
#
#     scan_coords[i] = (0, 0, rel)
#
# print(scan_coords)
