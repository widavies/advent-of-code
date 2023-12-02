# probe starts at 0,0
# it is launched with some x,y velocity. x must be positive. y can be positive/negative
#
# steps
# x + dx
# y + dy
# dx goes towards 0
# dy -= 1
#
#
# want to find a dx, dy
# such that
# 1. max y is maximized
# 2. it passes through a rectangular region at a particular step
import re


# load bounds
def load_bounds():
    with open('input.txt') as f:
        line = f.readline()
        match = re.search(r'x=([0-9-]+)\.\.([0-9-]+), y=([0-9-]+)\.\.([0-9-]+)', line)

        left, right, bottom, top = match.group(1), match.group(2), match.group(3), match.group(4)

        return int(left), int(right), int(top), int(bottom)


# returns the maximum height of the probe & whether it passes through the rectangle
def simulate(dx, dy, rect):
    # results
    within = False
    max_h = 0

    # Position
    px = 0
    py = 0

    (left, right, top, bottom) = rect

    while True:
        if dy < 0 and py < bottom:
            break
        if dx == 0 and (px < left or px > right):
            break

        px += dx
        py += dy

        max_h = max(max_h, py)

        # is it within the target region?
        within = within or (left <= px <= right and bottom <= py <= top)

        # velocity updates
        if dx < 0:
            dx += 1
        elif dx > 0:
            dx -= 1

        dy -= 1

    return within, max_h


def main():
    rect = load_bounds()

    x_min = 0
    x_max = rect[1] + 10

    y_min = -2000
    y_max = 4000

    max_attempt = None
    count = 0

    # test a lot of velocities!
    for dy in range(y_min, y_max):
        for dx in range(x_min, x_max):
            (within1, max_h) = simulate(dx, dy, rect)

            if within1:
                count += 1

            if within1 and (max_attempt is None or max_h > max_attempt[0]):
                max_attempt = (max_h, dx, dy)

    # Chose the one with the maximum max_h
    print(max_attempt)
    print(count)


main()
