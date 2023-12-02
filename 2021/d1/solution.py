# Load file
import math
from itertools import islice, zip_longest


def p1():
    with open('input.txt', 'r') as f:
        last = math.inf
        count = 0

        for line in f:
            v = int(line)

            count += int(v > last)

            last = v

        print(count)

def p2():
    # Things that could be done better:
    # Entire input is enumerated, instead it would be beneficial to only enumerate
    # in chunks

    with open('input.txt', 'r') as f:
        nums = list(map(lambda x: int(x), f.readlines()))

        last = math.inf
        window = 3
        count = 0

        for i in range(len(nums) - (window - 1)):
            v = sum(nums[i:i+window])

            count += int(v > last)

            last = v

        print(count)

        # Improvements

        # Makes use of the fact that a + b + c < b + c + d can be simplified to d > a
        # Also uses zip function to clean things up. Mismatched zips aren't included.
        # sum works with list of True/False's as well
        # print(sum(x < y for x, y in zip(nums, nums[3:])))
        # Can create enumerates that pop three values at a time

p1()
p2()
