import json

with open('input.txt') as f:
    numbers = []

    for line in f.readlines():
        numbers.append(json.loads(line))


def magnitude(number):
    left, right = number

    if type(left) is int and type(right) is int:
        return 3 * left + 2 * right
    elif type(left) is int and type(right) is not int:
        return 3 * left + 2 * magnitude(right)
    elif type(left) is not int and type(right) is int:
        return 3 * magnitude(left) + 2 * right
    else:
        return 3 * magnitude(left) + 2 * magnitude(right)


def _reduce(number, check, simplified=False, depth=0):
    left, right = number

    #
    # Check for explode / split
    #
    if not simplified and type(left) is int and type(right) is int and depth > 3 and check == 'explode':
        return left, 0, right, True
    elif not simplified and type(left) is int and left >= 10 and check == 'split':
        return 0, [[left // 2, (left + 1) // 2], right], 0, True
    elif not simplified and type(left) is int and type(right) is int and right >= 10 and check == 'split':
        return 0, [left, [right // 2, (right + 1) // 2]], 0, True

    #
    # Otherwise, keep recursing
    #

    elif type(left) is int and type(right) is int:
        return 0, [left, right], 0, simplified
    elif type(left) is int and type(right) is not int:
        if not simplified and check == 'split' and left >= 10:
            return 0, [[left // 2, (left + 1) // 2], right], 0, True
        else:
            (lu, update, ru, simplified) = _reduce(right, check, simplified, depth + 1)
            return 0, [left + lu, update], ru, simplified
    elif type(left) is not int and type(right) is int:
        (lu, update, ru, simplified) = _reduce(left, check, simplified, depth + 1)

        if not simplified and check == 'split' and right >= 10:
            return 0, [left, [right // 2, (right + 1) // 2]], 0, True

        return lu, [update, right + ru], 0, simplified
    else:
        (left_lu, left_update, left_ru, simplified) = _reduce(left, check, simplified, depth + 1)
        (right_lu, right_update, right_ru, simplified) = _reduce(right, check, simplified, depth + 1)

        if type(right_update) is not int:
            n = right_update

            while type(n[0]) is not int:
                n = n[0]

            n[0] += left_ru

        if type(left_update) is not int:
            n = left_update

            while type(n[-1]) is not int:
                n = n[-1]

            n[-1] += right_lu

        return left_lu, [left_update, right_update], right_ru, simplified


def reduce(number):
    (_, val, _, simplified) = _reduce(number, 'explode')
    if not simplified:
        (_, val, _, simplified) = _reduce(number, 'split')
        return val, simplified
    else:
        return val, simplified


def sum_numbers(nums):
    nums = nums.copy()
    working = nums.pop(0)

    while nums:
        a = nums.pop(0)

        res, simplified = reduce([working, a])

        while simplified:
            res, simplified = reduce(res)

        working = res

    return working


# Part 1

res = sum_numbers(numbers)
print(magnitude(res))

# Part 2

largest = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue

        largest = max(largest, magnitude(sum_numbers([numbers[i], numbers[j]])))

print(largest)