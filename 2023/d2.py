import re

with open('inputs/input-d2.txt') as f:
    gid = 1

    good_sum = 0
    power_sum = 0

    red = 12
    green = 13
    blue = 14

    for line in f:
        rounds = line.split(';')

        max_red = 0
        max_blue = 0
        max_green = 0

        good = True

        for rnd in rounds:
            matches = re.findall(r'(\d+) (red|green|blue)', rnd)
            rnd = {'green': 0, 'red': 0, 'blue': 0}
            for (key, value) in matches:
                rnd[value] = int(key)

            if red < rnd['red'] or green < rnd['green'] or blue < rnd['blue']:
                good = False

            max_red = max(max_red, rnd['red'])
            max_blue = max(max_blue, rnd['blue'])
            max_green = max(max_green, rnd['green'])

        power_sum += max_red * max_blue * max_green
        good_sum += gid if good else 0

        gid += 1

    gid = 1

    print(good_sum)
    print(power_sum)
