import random
import sys

def roll_one_die():
    return random.randint(1, 6)


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def initialize_flaps():
    # Returns a dict with flap numbers as keys and flap statuses (True for open, False for closed) as values
    return {i: True for i in range(1, 10)}


def close_flaps(numbers_to_replace, flaps):
    updated_flaps = flaps[:]  # Make a copy of flaps
    for num in numbers_to_replace:
        if num in updated_flaps:
            updated_flaps[updated_flaps.index(num)] = '*'
    return updated_flaps


def open_flaps(number_to_open, flaps):
    flaps[number_to_open] = True
    return flaps


def is_move_possible(dice_roll, flaps, possible_combos):
    # Create a list of the open flaps
    open_flaps = [flap for flap in flaps if flap != '*']

    # If dice roll is larger than the sum of remaining flaps, no move is possible
    if dice_roll > sum(open_flaps):
        return False

    # Check possible combinations for dice roll
    for combo in possible_combos[dice_roll]:
        if all(num in open_flaps for num in combo):
            return True

    # No possible move found
    return False


def draw_flaps(flaps):
    return f"""
---+---+---+---+---+---+---+---+---
 {' | '.join(map(str, flaps))} 
---+---+---+---+---+---+---+---+---
"""


# Now we initialize the flaps at the start of the game using the new function
flaps = initialize_flaps()


def computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice):
    # Check the sum of the open flaps and choose to roll one or two dice
    dice_roll = roll_one_die() if sum(flap for flap in flaps if isinstance(flap, int)) <= 6 else roll_two_dice()

    print(f"\nComputer's turn!")
    print(f"Computer rolled: {dice_roll}")

    # Check if a move is possible
    if not is_move_possible(dice_roll, flaps, possible_combos_one_die if dice_roll <= 6 else possible_combos_two_dice):
        print("No possible moves for the computer! Ending the game...")
        sys.exit(0)

    # Open flaps
    # Computer will always try to open the highest possible flap or combination of flaps
    possible_combos = possible_combos_one_die[dice_roll] if dice_roll <= 6 else possible_combos_two_dice[dice_roll]
    for combo in reversed(possible_combos):
        if all(num not in flaps for num in combo):
            flaps = open_flaps(combo, flaps)
            break

    print("Here's the new state of the box after the computer's turn:")
    print(draw_flaps(flaps))

    return flaps



flaps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

possible_combos_one_die = {
    1: [[1]],
    2: [[2]],
    3: [[3]],
    4: [[4]],
    5: [[5]],
    6: [[6]],
}

possible_combos_two_dice = {
    2: [2],
    3: [[1, 2], [3]],
    4: [[1, 3], [4]],
    5: [[1, 4], [2, 3], [5]],
    6: [[1, 2, 3], [1, 5], [2, 4], [6]],
    7: [[1, 6], [2, 5], [3, 4], [1, 2, 4], [7]],
    8: [[1, 7], [2, 6], [3, 5], [1, 2, 5], [8]],
    9: [[1, 8], [2, 7], [3, 6], [4, 5], [1, 2, 6], [1, 3, 5], [2, 3, 4], [9]],
    10: [[1, 9], [2, 8], [3, 7], [4, 6], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [1, 2, 3, 4]],
    11: [[2, 9], [3, 8], [4, 7], [5, 6], [1, 3, 7], [1, 2, 8], [1, 4, 6], [2, 3, 6], [2, 4, 5], [1, 2, 3, 5]],
    12: [[3, 9], [4, 8], [5, 7], [1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [2, 3, 7], [2, 4, 6], [3, 4, 5],
         [1, 2, 3, 6], [1, 2, 4, 5]]
}

# Start of the game
print("Welcome to 'Shut the Box'!")
print("Here's the initial state of the box:")
print(draw_flaps(flaps))

while any(isinstance(flap, int) for flap in flaps):  # Keep playing as long as there are open flaps
    print("Player 1, it's your turn!")
    dice_roll_choice = input("Press 1 to roll one die, or 2 to roll two dice: ")

    if dice_roll_choice == '1':
        dice_roll = roll_one_die()
        possible_combos = possible_combos_one_die
    else:
        dice_roll = roll_two_dice()
        possible_combos = possible_combos_two_dice

    print(f"You rolled: {dice_roll}")

    # Check if a move is possible
    if not is_move_possible(dice_roll, flaps, possible_combos):
        print("No possible moves!")

        # Computer's turn
        flaps = computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice)

        # If there are still closed flaps, continue with player 1's turn
        if any(isinstance(flap, int) for flap in flaps):
            continue
        else:
            break

    # Get the player's flap selections
    flap_selections = []
    while sum(flap_selections) != dice_roll or not all(selection in flaps for selection in flap_selections):
        flap_selections = input(
            f"Enter the numbers of the flaps you want to close, separated by spaces (they should add up to {dice_roll}): ")
        flap_selections = list(map(int, flap_selections.split()))

    # Apply the player's selection
    flaps = close_flaps(flap_selections, flaps)
    print("Here's the new state of the box:")
    print(draw_flaps(flaps))
