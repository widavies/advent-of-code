# Load file
from functools import reduce
from operator import add


def load_nums():
    with open('input.txt', 'r') as f:
        nums = list(map(lambda line: [int(digit) for digit in line.rstrip('\n')], f.readlines()))
        return nums


# nums is an array of digit arrays
def get_common(nums):
    sums = list(reduce(lambda a, b: map(add, a, b), nums))

    # Map each to a binary string
    count = len(nums) / 2
    common = list(map(lambda x: int(x >= count), sums))
    uncommon = list(map(lambda x: int(x < count), sums))

    return common, uncommon


def to_binary(digits):
    return int(''.join(list(map(str, digits))), 2)


def p1():
    a, b = get_common(load_nums())
    return to_binary(a) * to_binary(b)


def p2():
    # Load all numbers
    items = load_nums()

    o2_candidates, c02_candidates = items[:], items[:]

    digit = 0

    while len(c02_candidates) + len(c02_candidates) != 2:
        common, _ = get_common(o2_candidates)
        _, uncommon = get_common(c02_candidates)

        o2_candidates = list(filter(lambda x: x[digit] == common[digit], o2_candidates))
        c02_candidates = list(filter(lambda x: x[digit] == uncommon[digit], c02_candidates))

        digit += 1

    return to_binary(o2_candidates[0]) * to_binary(c02_candidates[0])


print("Power consumption", p1())
print("O2 generator rating", p2())

# Look into counter collection
# Look into: https://www.reddit.com/r/adventofcode/comments/r7r0ff/comment/hn1ski3/?utm_source=share&utm_medium=web2x&context=3
