# reducing
# - pair, ordered list of two elements
# - element can be a regular number, or another pair
# addition: create new pair
# reduction:
# - if a pair is nested inside four pairs, leftmost pair explodes
import json

with open('input.txt') as f:
    for line in f.readlines():
        loaded = json.loads(line)


def add(left, right):
    return [left, right]


# def reduce(number):



# reduce([[6, [5, [4, [3, 2]]]], 1])
