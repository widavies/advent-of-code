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


print('P1', player1_score)
print('P2', player2_score)
print('Rolls', total_rolls)

print('Part 1', min(player1_score, player2_score) * total_rolls)
