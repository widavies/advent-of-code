# keep track of how many fish exist with a certain timer
def p1():
    counts = [0 for _ in range(9)]

    # load in the counts
    with open('input.txt', 'r') as f:
        timers = list(map(int, f.readline().split(',')))
        for timer in timers:
            # alternatively: data.count(i)
            counts[timer] += 1

    # perform the updates
    for i in range(256):
        # good use of a queue here, interesting part is that
        # timers[6] is updated after a pop, but after a full
        # rotation of pop'ing and append'ing, it is rotated into its
        # correction position
        zeros = counts[0]
        counts[0] = 0

        for j in range(1, len(counts)):
            counts[j - 1] += counts[j]
            counts[j] = 0

        counts[8] += zeros
        counts[6] += zeros

        # another fascinating solution:
        # for _ in range(256):
        #     f = f[1:] + f[:1]
        #     f[6] += f[-1]
        # big thing to note here: adding doesn't really need to occur
        # because mostly elements are just getting swapped, save for the 6's

    print("sum", sum(counts))


p1()
