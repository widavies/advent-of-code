import json
import time

with open('input.txt') as f:
    numbers = []

    for line in f.readlines():
        numbers.append(json.loads(line))


def magnitude(number):
    if type(number) is int:
        return number

    left, right = number
    return 3 * magnitude(left) + 2 * magnitude(right)


def emplace_adj(stack, d, val):
    if type(stack) is not int:
        while type(stack[d]) is not int:
            stack = stack[d]
        stack[d] += val


def reduce(number, check, simplified=False, depth=0):
    left, right = number
    if not simplified and type(left) is int and type(right) is int and depth > 3 and check == 'explode':
        return left, 0, right, True
    elif not simplified and type(left) is int and left >= 10 and check == 'split':
        return 0, [[left // 2, (left + 1) // 2], right], 0, True
    elif not simplified and type(left) is int and type(right) is int and right >= 10 and check == 'split':
        return 0, [left, [right // 2, (right + 1) // 2]], 0, True
    elif type(left) is int and type(right) is int:
        return 0, [left, right], 0, simplified
    elif type(left) is int and type(right) is not int:
        (lu, update, ru, simplified) = reduce(right, check, simplified, depth + 1)
        return 0, [left + lu, update], ru, simplified
    elif type(left) is not int and type(right) is int:
        (lu, update, ru, simplified) = reduce(left, check, simplified, depth + 1)

        if not simplified and check == 'split' and right >= 10:
            return 0, [left, [right // 2, (right + 1) // 2]], 0, True

        return lu, [update, right + ru], 0, simplified
    else:
        (left_lu, left_update, left_ru, simplified) = reduce(left, check, simplified, depth + 1)
        (right_lu, right_update, right_ru, simplified) = reduce(right, check, simplified, depth + 1)

        emplace_adj(right_update, 0, left_ru)
        emplace_adj(left_update, -1, right_lu)

        return left_lu, [left_update, right_update], right_ru, simplified


def sum_numbers(nums):
    nums = nums.copy()
    working = nums.pop(0)

    while nums:
        working = [working, nums.pop(0)]
        simplified = True

        while simplified:
            _, working, _, simplified = reduce(working, 'explode')
            _, working, _, simplified = reduce(working, 'split', simplified)

    return magnitude(working)


# Part 1

os = time.process_time()

print(sum_numbers(numbers))

# Part 2

largest = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue

        largest = max(largest, magnitude(sum_numbers([numbers[i], numbers[j]])))

print(largest)

print('Time: ' + str(time.process_time() - os) + ' s')
