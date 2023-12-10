import re
from collections import defaultdict

with open('input.txt') as f:
    score = 0

    id = 1

    # Cards that need scoring
    copies = []

    cache = defaultdict(lambda: [])

    # Stores an array of copies that this number wins
    for line in f.readlines():
        tokens = line.split(":")[1].split("|")
        left, right = tokens
        left = re.sub('\\s+', ' ', left).strip()
        right = re.sub('\\s+', ' ', right).strip()

        winning = list(map(int, left.split(' ')))
        have = list(map(int, right.split(' ')))
        # Count number of "have" in winning
        count = 0

        match_count = 0

        for h in have:
            if h in winning:
                if count == 0:
                    count = 1
                else:
                    count *= 2

                match_count += 1

        for c in range(id + 1, id + match_count + 1):
            cache[id].append(c)

        if match_count == 0:
            cache[id] = []

        score += count
        id += 1

    print(score)

    # Start processing
    scorecards = defaultdict(lambda: 0)
    queue = [k for k in cache]

    while queue:
        k = queue.pop()
        scorecards[k] += 1
        queue.extend(cache[k])

    print(scorecards)

    print('Part 2:', sum([scorecards[k] for k in scorecards]))




