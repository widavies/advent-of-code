import re
import time

with open('input.txt') as f:
    count = 0

    start = time.process_time()

    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def convert(i):
        if i in digits:
            return digits.index(i) + 1
        else:
            return int(i)

    for line in f:
        matches = re.findall(rf'(?=({"|".join(digits)}|\d))', line)

        first = convert(matches[0])
        two = convert(matches[-1])

        count += int(f'{first}{two}')

    print(time.process_time() - start)
    print(count)
