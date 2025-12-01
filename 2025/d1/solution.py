with open('input.txt') as f:
    lines = f.read().splitlines()

dial = 50
password1 = 0
password2 = 0

for i in lines:
    (degree, amount) = (i[0], int(i[1:]))

    start = dial

    if degree == 'R':
        dial += amount
    else:
        dial -= amount

    quot, dial = divmod(dial, 100)

    if dial == 0:
        password1 += 1

    # If we didn't wrap, but ended up exactly at zero
    if quot == dial == 0:
        password2 += 1
    if quot < 0:
        # Don't overcount if started at 0
        if start == 0:
            password2 -= 1
        # Need to count going back to zero
        if dial == 0:
            password2 += 1

    password2 += abs(quot)

print('Part 1', password1)
print('Part 2', password2)