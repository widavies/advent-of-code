from collections import defaultdict, Counter
import time

player1_pos = 6
player2_pos = 1

player1_score = 0
player2_score = 0

random_state = 1

total_rolls = 0
last_roll = 100


def determined_roll(lr):
    if lr == 100:
        return 1
    else:
        return lr + 1


player1_turn = True

while player1_score < 1000 and player2_score < 1000:
    roll1 = determined_roll(last_roll)
    roll2 = determined_roll(roll1)
    roll3 = determined_roll(roll2)
    last_roll = roll3
    total_rolls += 3

    move = roll1 + roll2 + roll3

    if player1_turn:
        updated = player1_pos + move
        while updated > 10:
            updated = updated - 10
        player1_pos = updated
        player1_score += player1_pos
        # print(f'{roll1}+{roll2}+{roll3}', 'P1 moves to', player1_pos)
    else:
        updated = player2_pos + move
        while updated > 10:
            updated = updated - 10
        player2_pos = updated
        player2_score += player2_pos
        # print(f'{roll1}+{roll2}+{roll3}', 'P2 moves to', player2_pos)

    player1_turn = not player1_turn

# print('P1', player1_score)
# print('P2', player2_score)
# print('Rolls', total_rolls)

print('Part 1', min(player1_score, player2_score) * total_rolls)

#
# Part 2
# Key idea: Remember day 6 lantern fish
# Frequency analysis. Second main idea is that many universes are similar, so we will
# just count them as the same and not bother needing to simulate the duplicates.
#
def part2():
    def map_index(i, r):
        s = i + r
        return s % 10 if s > 10 else s

    dice = []
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                dice.append(d1 + d2 + d3)

    dice = list(Counter(dice).items())

    p1_wins = 0
    p2_wins = 0

    universes = {(6, 0, 1, 0): 1} # the universe is identified by its started positions, and its frequency

    while universes:
        new_universes = defaultdict(lambda: 0)

        for unv, fq in universes.items():
            p1, s1, p2, s2 = unv

            # Add new universes
            for r1, c1 in dice:
                spot1 = map_index(p1, r1)

                if s1 + spot1 >= 21:
                    p1_wins += fq * c1
                    continue

                for r2, c2 in dice:
                    spot2 = map_index(p2, r2)

                    if s2 + spot2 >= 21:
                        p2_wins += fq * c1 * c2
                    else:
                        new_universes[(spot1, s1 + spot1, spot2, s2 + spot2)] += fq * c1 * c2

        universes = new_universes

    print('Part 2', max(p1_wins, p2_wins))

start = time.time()
part2()
print(time.time() - start)

# This is a top-down approach
# Alternative would be to use a bottom up approach with recursion
