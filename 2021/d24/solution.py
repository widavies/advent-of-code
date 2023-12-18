from collections import deque

with open('input.txt') as f:
    program = f.read().splitlines()
    program = list(map(lambda l: l.split(), program))

def skip(file, n):
    for _ in range(n):
        next(file)

def get_constraints(fin):
    constraints = []
    stack = deque()

    for i in range(14):
        skip(fin, 4)
        op = next(fin).rstrip()
        assert op.startswith('div z '), 'Invalid input!'

        if op == 'div z 1':
            skip(fin, 10)
            op = next(fin)
            assert op.startswith('add y '), 'Invalid input!'

            a = int(op.split()[-1])
            stack.append((i, a))
            skip(fin, 2)
        else:
            op = next(fin)
            assert op.startswith('add x '), 'Invalid input!'

            b = int(op.split()[-1])
            j, a = stack.pop()
            constraints.append((i, j, a + b))
            skip(fin, 12)

    return constraints

print(get_constraints(open('input.txt')))

# Key observations - The program is basically the same program
# 14 times in a row. lines 2 - 8 useless, x is basically always 1

# Work out the constraints for each digit
constraints = [

]

for chunk in range(0, len(program), 18):
    print(program[chunk])

    # Chunk kind 1
    # z = z * 26 + w + N
    # Chunk kind 2
    # if (z % 26 + N) != input





