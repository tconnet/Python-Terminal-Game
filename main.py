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


def open_flaps(numbers_to_open, flaps):
    for number in numbers_to_open:
        flaps[number - 1] = '*'  # Flap numbers are 1-based, but list indices are 0-based
    return flaps


def is_move_possible(dice_roll, flaps, possible_combos, is_computer=False):
    relevant_flaps = [flap if is_computer else flap for flap in flaps if (flap == '*' if is_computer else isinstance(flap, int))]
    # only consider numeric values in relevant_flaps for sum operation
    relevant_flaps_nums = [flap for flap in relevant_flaps if isinstance(flap, int)]

    for combo in possible_combos[dice_roll]:
        if all(num in relevant_flaps_nums for num in combo):
            return True

    return False


def draw_flaps(flaps):
    return f"""
---+---+---+---+---+---+---+---+---
 {' | '.join(map(str, flaps))} 
---+---+---+---+---+---+---+---+---
"""


def computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice):
    while True:
        dice_roll = random.choice([roll_one_die(), roll_two_dice()])
        print(f"Computer rolled: {dice_roll}")

        # Create a list of tuples (score, flaps_to_open) for all possible moves
        possible_moves = []
        for combo in possible_combos_two_dice[dice_roll] if dice_roll > 6 else possible_combos_one_die[dice_roll]:
            if any((flap == '*' for flap in [flaps[num - 1] for num in combo])):
                possible_moves.append((sum(combo), combo))

        # If there are possible moves, pick the one with the highest score
        if possible_moves:
            best_move = max(possible_moves, key=lambda x: x[0])
            for flap in best_move[1]:
                if flaps[flap - 1] == '*':  # Only open flaps that are closed
                    flaps[flap - 1] = flap
            print("Here's the new state of the box after the computer's turn:")
            print(draw_flaps(flaps))
        else:
            print("No possible moves for the computer!")
            break  # Exit the loop when there are no possible moves left
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

while True:  # The game continues until someone wins
    print("Here's the current state of the box:")
    print(draw_flaps(flaps))

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
    if not is_move_possible(dice_roll, flaps, possible_combos, False):
        print("No possible moves for you!")
        # Computer's turn
        while True:
            flaps = computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice)
            # If all flaps are closed (none are "*"), computer wins
            if not any(isinstance(flap, int) for flap in flaps):
                print("Computer won! All flaps are closed.")
                sys.exit(0)
            # If computer cannot make a move (no more "*"), break to player's turn
            dice_roll = roll_one_die() if sum(flap for flap in flaps if isinstance(flap, int)) <= 6 else roll_two_dice()
            if not is_move_possible(dice_roll, flaps, possible_combos_one_die if dice_roll <= 6 else possible_combos_two_dice, True):
                break
    else:
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

        # Check if player has won (all flaps are "*")
        if all(flap == '*' for flap in flaps):
            print("Congratulations! You've won by closing all the flaps!")
            sys.exit(0)


