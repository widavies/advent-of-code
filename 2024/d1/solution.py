from collections import Counter

left = []
right = []

with open('input.txt') as f:
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

print("P1", sum(map(lambda x, y: abs(x - y), sorted(left), sorted(right))))

right_counts = Counter(right)

print("P2",  sum(map(lambda i: right_counts[i] * i, left)))