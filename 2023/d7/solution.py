from collections import defaultdict, Counter
from functools import cmp_to_key
import itertools

with open('input.txt') as f:
    hands = []
    bids = {}

    for line in f.read().splitlines():
        hand, bid = line.split(' ')
        bids[hand] = int(bid)
        hands.append((hand, int(bid)))

types = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5]
]

def determine_kind(hnd):
    counts = list(sorted(Counter([c for c in hnd]).values()))
    return types.index(counts)


def determine_kind_j(hnd):
    if 'J' not in hnd:
        return determine_kind(hnd)

    ex = [c for c in hnd]
    js = []
    for i in range(len(ex)):
        if ex[i] == 'J':
            js.append(i)

    scores = []

    for substitutions in itertools.product(set(ex), repeat=ex.count('J')):
        for i in range(len(js)):
            ex[js[i]] = substitutions[i]
        hd = ''.join(ex)
        scores.append(determine_kind(hd))

    return max(scores)



# returns which is a stronger hand
def grade_hand(hnd1, hnd2):
    cards = 'AKQT98765432J'

    kind1 = determine_kind_j(hnd1)
    kind2 = determine_kind_j(hnd2)

    if kind1 > kind2:
        return -1
    elif kind2 > kind1:
        return 1
    else:
        for i in range(5):
            if cards.index(hnd1[i]) < cards.index(hnd2[i]):
                return -1
            elif cards.index(hnd1[i]) > cards.index(hnd2[i]):
                return 1

ranked = list(sorted(map(lambda x: x[0], hands), key=cmp_to_key(grade_hand)))
total = 0

for ix in range(len(ranked)):
    rank = len(ranked) - ix
    total += rank * bids[ranked[ix]]

print('Part 2', total)
