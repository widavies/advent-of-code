# Rules
# - Amphipods want to be sorted
#       A-B-C-D
#       A-B-C-D
# - Can move in any direction. A,B,C,D take 1,10,100,1000 energy each move
# - Cannot stop on space directly outside a hallway for more than 1 turn
# - Amphipods will never move into a room from teh hallway unless they belong in it and no one else who doesn't belong in there is in there
# - Once an amphipod stops in the hallway, it must stop moving until it can move into a room

hallway = ['.' for _ in range(11)]
# rooms_top = ['.' for _ in range(4)]
# rooms_bottom = ['.' for _ in range(4)]

rooms_top = ['B', 'C', 'B', 'D']
rooms_bottom = ['A', 'D', 'C', 'A']

def is_done():
    return all(map(lambda x: x == '.', hallway)) and ''.join(rooms_top) == 'ABCD' == ''.join(rooms_bottom)

# Don't return the move if it would exceed less_than_energy
def generate_all_moves(game_state, less_than_energy):
    # Tuple is (amphipod, destination, energy delta)
    return []

# Generate all possible moves
exploring = generate_all_moves(9999999999)

while True:

    # Select one, and play out that game
    exploring.pop()


