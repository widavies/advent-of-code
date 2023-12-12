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
    def transform(code, coords):
        (x, y, z) = coords

        swaps = [
            (x, y, -z),
            (x, -z, y),
            (x, z, y),
            (x, -y, z),

            (-x, y, z),
            (-x, -y, -z),
            (-x, z, -y),
            (-x, -z, y),

            (x, y, z),
            (-x, y, -z),
            (z, y, -x),
            (-z, y, x),

            (x, -y, -z),
            (-x, -y, z),
            (z, -y, x),
            (-z, -y, -x),

            (-x, y, z),
            (y, x, z),
            (x, -y, z),
            (-y, -x, z),

            (-x, -y, -z),
            (y, -x, -z),
            (x, y, -z),
            (-y, x, -z),
        ]

        return swaps[code]

    for change1 in range(24):
        for change2 in range(24):
            # change = 1
            #
            # coord1 = transform(8, [-618, -824, -621])
            # coord2 = transform(9, [686, 422, 578])
            # print(coord1[0] - coord2[0], coord1[1] - coord2[1], coord1[2] - coord2[2])

            transformed1 = list(map(lambda x: transform(change1, x), scanner1))
            transformed2 = list(map(lambda x: transform(change2, x), scanner2))

            for coord1 in transformed1:
                for coord2 in transformed2:
                    # Normalize both to the same beacon
                    mapped1 = list(
                        map(lambda x: (x[0] - coord1[0], x[1] - coord1[1], x[2] - coord1[2]),
                            transformed1))
                    mapped2 = list(
                        map(lambda x: (x[0] - coord2[0], x[1] - coord2[1], x[2] - coord2[2]),
                            transformed2))

                    # Now, check if they have more than 12 duplicates
                    if len(list(filter(lambda x: x in mapped2, mapped1))) >= 12:
                        print('done', sorted(mapped1), sorted(mapped2))
                        print(coord1[0] - coord2[0], coord1[1] - coord2[1], coord1[2] - coord2[2])
                        # return coord1[0] - coord2[0], coord1[1] - coord2[1], coord1[2] - coord2[2]


print(check_scanner(scanners[0], scanners[1]))

# pool = []
#
# scan_coords = {}
#
# # Need to find the mapping for every i
# for i in range(len(scanners)):
#     for j in range(len(scanners)):
#         if i == j:
#             continue
#         res = check_scanner(scanners[j], scanners[i])
#         print('done', res)
#         if res is not None:
#             scan_coords[i] = (j, res)
#
# beacons = {}
#
# for i in range(len(scanners)):
#     # translate all the beacons relative to 0
#     (j, res) = scan_coords[i]
#     while j != 0:
#         # Translate all the points
#         for k in range(len(scanners[i])):
#             scanners[j][k] = (scanners[j][k][0] + res[0], scanners[j][k][1] + res[1], scanners[j][k][2] + res[2])
#
#         (j, res) = scan_coords[j]
#
#
# print(scan_coords)
