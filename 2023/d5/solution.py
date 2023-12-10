import re
import time

start = time.time()

with open('input.txt') as f:
    # Process out seeds
    seeds = list(map(int, next(f).replace("seeds: ", "").split(' ')))

    maps = []
    run = []

    # Then, start parsing the maps
    for line in f:
        if re.match(r"^(\d+) (\d+) (\d+)", line):
            run.append(list(map(int, line.split(' '))))
        elif run:
            maps.append(run)
            run = []

    if run:
        maps.append(run)


# Compress the ranges down into a single range
def find_minimum(initial):
    # assumption: endpoints are inclusive
    ranges = []
    working = initial

    for level in maps:

        # discovered, mapped "to"
        ranges = working
        working = []

        while ranges:
            (st, end) = ranges.pop()

            if st > end:
                continue

            # Go through each range in level and check if it intersects
            for (dest, source, size) in level:
                ls = source
                le = source + size - 1

                left_endpoint_contained = st <= ls <= end
                right_endpoint_contained = st <= le <= end
                fully_contained = ls <= st and le >= end

                if fully_contained:
                    working.append((dest + (st - source), dest + (end - source)))
                    break
                elif not left_endpoint_contained and not right_endpoint_contained:
                    continue
                elif left_endpoint_contained and not right_endpoint_contained:
                    working.append((dest, dest + (end - ls)))
                    ranges.append((st, source - 1))
                    break
                elif not left_endpoint_contained and right_endpoint_contained:
                    working.append((dest + (st - source), dest + size - 1))
                    ranges.append((source + size, end))
                    break
                else:
                    working.append((dest, dest + size - 1))

                    ranges.append((st, source - 1))
                    ranges.append((source + size, end))
                    break
            else:
                working.append((st, end))


    return min(working, key=lambda x: x[0])[0]

# Part 1
# Feed it the starting range as single numbers
p = []
for s in seeds:
    p.append((s, s))
print(find_minimum(p))

# Part 2
# Feed it in the starting as ranges
p = []
for ix in range(0, len(seeds), 2):
    p.append((seeds[ix], seeds[ix] + seeds[ix + 1] - 1))
print(find_minimum(p))

print(time.time() - start)
