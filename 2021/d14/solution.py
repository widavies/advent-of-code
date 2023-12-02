from collections import defaultdict, Counter

swaps = {}

with open('input.txt') as f:
    template = next(f).rstrip()
    next(f)

    for line in f:
        frm, to = line.rstrip().split(' -> ')
        swaps[frm] = to


def solve(steps):
    # Keep track of all the pairs within the string
    pairs = defaultdict(lambda: 0)

    # Letter counts
    # counts = defaultdict(lambda: 0, {
    #  k: template.count(k) for k in set(template)
    # })
    # better:
    counts = Counter(template)

    for iz in range(len(template) - 1):
        pairs[template[iz:iz+2]] += 1

    # Loop through pairs
    for _ in range(steps):
        adding = defaultdict(lambda: 0)

        for pair in pairs:
            a, b = pair
            swap = swaps[pair]
            count = pairs[pair]

            counts[swap] += count
            adding[f'{a}{swap}'] += count
            adding[f'{swap}{b}'] += count

        pairs = adding

    # most = max(counts.items(), key=operator.itemgetter(1))[1]
    # least = min(counts.items(), key=operator.itemgetter(1))[1]
    #
    # return most - least

    # A little cleaner
    return max(counts.values()) - min(counts.values())


# Part 1
print(solve(10))

# Part 2
print(solve(40))


# Improvements:
# Use Counter instead of default dict - easy conversion as well
# Convenient to load file like: tpl, _, *rules = open(0).read().split('\n')
# for (a, b), c in is a nice loop convention
# other solutions just copy the pairs list and remove from it. Might be better for memory
