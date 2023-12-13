import time

def simulate_game(player1_pos, player2_pos, rolls, winning_score):
    player1_score = 0
    player2_score = 0

    total_rolls = 0

    roll_ix = 0

    player1_turn = True

    while player1_score < winning_score and player2_score < winning_score:
        roll1 = rolls[roll_ix]
        roll2 = rolls[(roll_ix + 1) % len(rolls)]
        roll3 = rolls[(roll_ix + 2) % len(rolls)]
        roll_ix = (roll_ix + 3) % len(rolls)

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
    #
    print('Part 1', rolls, min(player1_score, player2_score) * total_rolls)

    return player1_score, player2_score, total_rolls


# Part 1
start =time.time()

simulate_game(6, 1, list(range(1, 101)), 1000)
end = time.time() - start
print(end)

def increment_base3(rolls):
    rolls[-1] += 1

    last = -1

    while rolls[last] == 4:
        rolls[last] = 1
        last -= 1
        if abs(last) > len(rolls):
            return False
        rolls[last] += 1  # overflow

    return True


def part2():
    # Part 2
    rolls = [1] * 21
    tracked_wins = set()

    while True:
        p1_score, p2_score, total_rolls = simulate_game(4, 8, rolls, 21)
        print("YEEE", total_rolls)
        assert (total_rolls <= 36)


        tracked_wins.add((1 if p1_score > p2_score else 0, tuple(rolls[0:total_rolls])))

        if not increment_base3(rolls):
            break



# Idea is this, we need to simulate games. Kind of like a ternary number.
# One problem though, is that depending on the game outcome, the game may end early.
# It's possible that (depending on the


