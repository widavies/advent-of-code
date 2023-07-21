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

# ideas:
# try to come up with a closed form equation
# run simulations
#
# can we create a function?
# y += dy
# dy -= 1

# option one - create a function that takes a dy0 and a t and spits out a location
# Then, swap the formula around to take location and a t and spit out a dy0 to get there
# for t, just iterate a bunch of values. Once
# We could do this for y. That gives us a bounded range of valid dy0s to try. Then we can just try a whole bunch of x's

# simpler:
# - just choose a velocity and run with it. We'll record its maximum height and check if it every passes through our rectangle.
#   we'll cut it off after the height drops below the bottom

simulation = []

x_min = -100
x_max = 100

y_min = -100
y_max = 100

# returns the maximum height of the probe & whether it passes through the rectangle
def simulate(dx, dy, left, top, right, bottom):
    # Position
    px = 0
    py = 0

    if py < bottom:
        # return
        pass

for x in range(x_min):
    for y in range(y_max):
        simulate(x, y, 0, 0, 100, 100)



