import re

with open('input.txt') as f:
    cubes = []

    for line in f.read().splitlines():
        m = re.match(r'(on|off) x=([-0-9]+)\.\.([-0-9]+),y=([-0-9]+)\.\.([-0-9]+),z=([-0-9]+)\.\.([-0-9]+)', line)
        if m:
            cubes.append(
                (m.group(1), ((int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))),
                              (int(m.group(6)), int(m.group(7))))))


def part1():
    # Naive way for part 1, but fast to code
    on_points = set()  # (x, y, z)

    for (op, ((x1, x2), (y1, y2), (z1, z2))) in cubes:
        if not (
                -50 <= x1 <= 50 and -50 <= x2 <= 50 and -50 <= y1 <= 50 and -50 <= y2 <= 50 and -50 <= z1 <= 50 and -50 <= z2 <= 50):
            continue

        # Iterate through all the points in the cube
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    if op == 'on':
                        on_points.add((x, y, z))
                    elif (x, y, z) in on_points:
                        on_points.remove((x, y, z))

    print(len(on_points))


def part2():
    def is_valid_cube(cube):
        ((x1, x2), (y1, y2), (z1, z2)) = cube

        return x2 >= x1 and y2 >= y1 and z2 >= z1

    # Part 2: We will have to keep track of ranges
    # The number of points in cube
    def cube_size(cube):
        ((x1, x2), (y1, y2), (z1, z2)) = cube

        if not is_valid_cube(cube):
            return 0

        return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

    # cut cube b from cube a
    def cut(cube_a, cube_b):
        # if they do not overlap, just return cube
        (left, right), (furthest, nearest), (bottom, top) = cube_a
        (cut_left, cut_right), (cut_forward, cut_backward), (cut_bottom, cut_top) = cube_b

        shared = (max(left, cut_left), min(right, cut_right)), (
            max(furthest, cut_forward), min(nearest, cut_backward)), (max(bottom, cut_bottom), min(top, cut_top))

        if not is_valid_cube(shared):
            return [cube_a]

        ((shared_left, shared_right), (shared_furthest, shared_nearest), (shared_bottom, shared_top)) = shared

        # return at most 6 cubes
        return list(filter(is_valid_cube, [
            # Bottom cube
            ((left, right), (furthest, nearest), (bottom, shared_bottom - 1)),
            # Top cube
            ((left, right), (furthest, nearest), (shared_top + 1, top)),
            # Back
            ((left, right), (furthest, shared_furthest - 1), (shared_bottom - 1 + 1, shared_top + 1 - 1)),
            # Front
            ((left, right), (shared_nearest + 1, nearest), (shared_bottom - 1 + 1, shared_top + 1 - 1)),
            #
            # These cubes are handled slightly differently,
            # because the back/front will take precedence
            #
            # Left
            ((left, shared_left - 1), (shared_furthest - 1 + 1, shared_nearest + 1 - 1),
             (shared_bottom - 1 + 1, shared_top + 1 - 1)),
            # Right
            ((shared_right + 1, right), (shared_furthest - 1 + 1, shared_nearest + 1 - 1),
             (shared_bottom - 1 + 1, shared_top + 1 - 1)),
        ]))

    # Invariant: None of them are overlapping
    on_cubes = set()

    for op, c in cubes:
        if op == 'on':
            trimmed = [c]

            # loop through the cubes in "on_cubes" and cut each of them away from ourselves
            for c_on in on_cubes:
                trimmed2 = []

                for tr in trimmed:
                    trimmed2.extend(cut(tr, c_on))

                trimmed = trimmed2

            for t in trimmed:
                on_cubes.add(t)
        else:
            updated = []

            for c_on in on_cubes:
                updated.extend(cut(c_on, c))

            on_cubes = set(updated)

    size = 0
    for k in on_cubes:
        size += cube_size(k)
    print(size)


# if off cube, easy, just loop through all cubes within the set,
# and "remove c" from them

# if on cube, loop through all cubes and cut our cube away
part1()
part2()

#
# A smarter approach here would have been to do the shared cube thing, store the shared cubes and a sign
# to designate cancelling
#
