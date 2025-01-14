import time

with open('input.txt') as f:
    equations = []

    for l in f:
        target, rest = l.split(':')

        equations.append((int(target), list(map(int, rest.split()))))

def get_digit(number, index, base):
    return number // (base ** index) % base

def calc(nums, binary, base=2):
    result = nums[0]

    for ix in range(1, len(nums)):
        digit = get_digit(binary, ix - 1, base)

        if digit == 2: # concatenation
            result = int(str(result) + str(nums[ix]))
        elif digit == 1: # plus
            result += nums[ix]
        else:
            result *= nums[ix]

    return result

part1 = 0
part2 = 0

start = time.time()

for (target, values) in equations:
    for i in range(2 ** (len(values) - 1)):
        if calc(values, i) == target:
            part1 += target
            break

    for i in range(3 ** (len(values) - 1)):
        if calc(values, i, 3) == target:
            part2 += target
            break

print(part1, part2, 'took', time.time() - start)

# what went wrong - approach was correct, but too much time wasted on going from 2 operators to 3 operators
# optimization - work backwards instead of forwards