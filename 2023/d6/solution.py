import re

with open('input.txt') as f:
    # Times
    result = re.sub('\s+', ' ', next(f).replace('Time: ', '').strip())
    times = list(map(int, result.split(" ")))
    time_long = int(result.replace(' ', ''))

    # Distances
    result = re.sub('\s+', ' ', next(f).replace('Distance: ', '').strip())
    distances = list(map(int, result.split(" ")))
    distance_long = int(result.replace(' ', ''))

    # Part 1:
    total = 1
    for (time, dist) in zip(times, distances):
        total *= len(list(filter(lambda x: (time - x) * x >= dist, [i for i in range(0, time)])))

    print(total)

    # Part 2:
    total = len(list(filter(lambda x: (time_long - x) * x >= distance_long, [i for i in range(0, time_long)])))
    print(total)

# Took: About 14 minutes
