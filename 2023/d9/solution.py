with open('input.txt') as f:
    seqs = []

    for line in f.read().splitlines():
        seqs.append(list(map(int, line.split(' '))))

total = 0
total_2 = 0

for s in seqs:
    history = [s]

    working = s.copy()

    while any(working):
        n = []

        for i in range(1, len(working)):
            n.append(working[i] - working[i - 1])

        history.append(n)
        working = n.copy()

    diff = 0

    this_history = 0

    for h in reversed(history):
        item = h[0] - diff
        this_history += item
        diff = item

    total += sum(map(lambda x: x[0], history))
    total_2 += diff

print(total)
print(total_2)
