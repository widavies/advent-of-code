import itertools

with open('input.txt') as f:
    records = []

    for line in f.read().splitlines():
        left, right = line.split(' ')
        groups = list(map(int, right.split(',')))

        records.append((left, groups))

    print(records)


    def cross_check(st, runs):
        assert not '?' in st

        check = []

        run = 0

        for c1 in st:
            if c1 == '#':
                run += 1
            elif run:
                check.append(run)
                run = 0


        if run:
            check.append(run)
        return check == runs

    def unfold(st, runs):
        return '?'.join([st] * 5), list(itertools.chain(*([runs] * 5)))

    valid = 0

    for r in records:
        left, right = r
        # left, right = unfold(left, right)
        qi = []
        for c in range(len(left)):
            if left[c] == '?':
                qi.append(c)

        ex = [c for c in left]

        for s in itertools.product('.#', repeat=left.count('?')):
            for i in range(len(s)):
                ex[qi[i]] = s[i]

            # Test it out
            if cross_check(''.join(ex), right):
                valid += 1

        print('done')

    print(valid)

    print(cross_check('.#...#....###.', [1, 1, 3]))

    print(unfold('.#', [1]))
