# reducing
# - pair, ordered list of two elements
# - element can be a regular number, or another pair
# addition: create new pair
# reduction:
# - if a pair is nested inside four pairs, leftmost pair explodes
import json

with open('input.txt') as f:
    numbers = []

    for line in f.readlines():
        numbers.append(json.loads(line))


def add(left, right):
    return [left, right]


def magnitude(number):
    left, right = number[0], number[-1]

    if type(left) == int and type(right) == int:
        return 3 * left + 2 * right
    elif type(left) == int and type(right) != int:
        return 3 * left + 2 * magnitude(right)
    elif type(left) != int and type(right) == int:
        return 3 * magnitude(left) + 2 * right
    else:
        return 3 * magnitude(left) + 2 * magnitude(right)


def _reduce(number, check, simplified=False, depth=0):
    left, right = number

    # condition 1 - explode
    if not simplified and check == '1' and type(left) == int and type(right) == int and depth > 3:
        return left, 0, right, True
    # condition 2 - split
    elif not simplified and check == '2' and type(left) == int and left >= 10:
        return 0, [[left // 2, (left + 1) // 2], right], 0, True
    # condition 2 - split
    elif not simplified and check == '2' and type(right) == int and right >= 10:
        return 0, [left, [right // 2, (right + 1) // 2]], 0, True
    elif type(left) == int and type(right) == int:
        return 0, [left, right], 0, simplified

    # Recursive

    elif type(left) == int and type(right) != int:
        (lu, update, ru, simplified) = _reduce(right, check, simplified, depth + 1)
        return 0, [left + lu, update], ru, simplified

    elif type(left) != int and type(right) == int:
        (lu, update, ru, simplified) = _reduce(left, check, simplified, depth + 1)
        return lu, [update, right + ru], 0, simplified

    # Both sides are arrays
    else:
        (left_lu, left_update, left_ru, simplified) = _reduce(left, check, simplified, depth + 1)
        (right_lu, right_update, right_ru, simplified) = _reduce(right, check, simplified, depth + 1)

        if type(right_update) != int:
            n = right_update

            while type(n[0]) != int:
                n = n[0]

            n[0] += left_ru
        else:
            right_update += left_ru

        if type(left_update) != int:
            n = left_update

            while type(n[-1]) != int:
                n = n[-1]

            n[-1] += right_lu
        else:
            left_update += right_lu

        return left_lu, [left_update, right_update], right_ru, simplified


def reduce(number):
    (_, val, _, simplified) = _reduce(number, '1')
    if not simplified:
        (_, val, _, simplified) = _reduce(number, '2')
    return val, simplified


def sum_numbers(nums):
    working = nums.pop(0)

    while nums:
        print(working)
        a = nums.pop(0)
        print("+", a)
        working = add(working, a)

        working, simplified = reduce(working)

        while simplified:
            working, simplified = reduce(working)
            print(working)

        print('=', working)
        print()

    return working


# res = sum_numbers(numbers)
# print(res)
# print(magnitude(res))

bad1 = [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]]
bad2 = [7, [5, [[3, 8], [1, 4]]]]

print(sum_numbers([bad1, bad2]))

print(reduce([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))
