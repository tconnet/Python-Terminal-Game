import random
import time

def roll_one_die():
    return random.randint(1, 6)


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def initialize_flaps():
    # Returns a dict with flap numbers as keys and flap statuses (True for open, False for closed) as values
    return {i: True for i in range(1, 10)}


def close_flaps(numbers_to_close, flaps):
    for num in numbers_to_close:
        flaps[num] = False
    return flaps


def open_flaps(numbers_to_open, flaps):
    for number in numbers_to_open:
        flaps[number] = True
    return flaps


def is_player_move_possible(dice_roll, flaps, possible_combos):
    remaining_flaps = [i for i, flap in flaps.items() if flap]  # Flaps that are still open
    possible_moves = possible_combos.get(dice_roll, [])

    for move in possible_moves:
        if set(move).issubset(set(remaining_flaps)):  # Check if the move is valid based on remaining flaps
            return True

    return False


def is_computer_move_possible(dice_roll, flaps, possible_combos):
    closed_flaps = [i for i, flap in flaps.items() if not flap]  # Flaps that are closed
    possible_moves = possible_combos.get(dice_roll, [])

    for move in possible_moves:
        if set(move).issubset(set(closed_flaps)):  # Check if the move is valid based on closed flaps
            return True

    return False



def draw_flaps(flaps):
    return f"""
---+---+---+---+---+---+---+---+---
 {' | '.join(str(i) if flap else '*' for i, flap in flaps.items())}
---+---+---+---+---+---+---+---+---
"""


def player_turn(flaps, possible_combos_one_die, possible_combos_two_dice):
    print("Player's turn:")
    print("Here's the current state of the box:")
    print(draw_flaps(flaps))

    while True:
        if all(not flap for flap in flaps.values()):
            print("All flaps are closed. Player's turn ends.")
            break

        dice_roll_choice = input("Press 1 to roll one die, or 2 to roll two dice: ")
        if dice_roll_choice == '1':
            dice_roll = roll_one_die()
            possible_combos = possible_combos_one_die
        elif dice_roll_choice == '2':
            dice_roll = roll_two_dice()
            possible_combos = possible_combos_two_dice
        else:
            print("Invalid input. Please try again.")
            continue

        print("You rolled:", dice_roll)
        if not is_player_move_possible(dice_roll, flaps, possible_combos):
            print("No possible moves. Player's turn ends.")
            break

        while True:
            flap_input = input("Enter the numbers of the flaps you want to close, separated by spaces: ")
            flaps_to_close = list(map(int, flap_input.split()))  # Convert strings to integers

            if sum(flaps_to_close) == dice_roll:
                if all(flaps[flap] and flap in flaps for flap in flaps_to_close):
                    flaps = close_flaps(flaps_to_close, flaps)
                    print("Here's the current state of the box:")
                    print(draw_flaps(flaps))
                    break
                else:
                    print("One or more flaps you entered are not valid or already closed. Please try again.")
            else:
                print("The sum of the flaps you entered does not match the dice roll. Please try again.")

    return flaps


def computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice):
    print("Computer's turn:")
    time.sleep(1)
    print("Here's the current state of the box:")
    print(draw_flaps(flaps))

    while True:
        if all(not flap for flap in flaps.values()):
            print("All flaps are closed. Computer's turn ends.")
            break

        if all(flaps[flap] for flap in flaps):
            dice_roll = roll_two_dice()
            possible_combos = possible_combos_two_dice
        else:
            dice_roll = roll_one_die()
            possible_combos = possible_combos_one_die

        time.sleep(1)
        print("Computer rolled:", dice_roll)

        if not is_computer_move_possible(dice_roll, flaps, possible_combos):
            print("No possible moves. Computer's turn ends.")
            time.sleep(1)
            break

        valid_moves = possible_combos[dice_roll]
        closed_flaps = [i for i, flap in flaps.items() if not flap]  # Flaps that are closed

        possible_valid_moves = [
            move for move in valid_moves
            if all(flap in closed_flaps for flap in move)
        ]

        if possible_valid_moves:
            selected_move = random.choice(possible_valid_moves)
            flaps = open_flaps(selected_move, flaps)
            print("Here's the current state of the box:")
            print(draw_flaps(flaps))
            time.sleep(1)  # Add some delay to make the game feel more interactive

    return flaps


flaps = initialize_flaps()

possible_combos_one_die = {
    1: [[1]],
    2: [[2]],
    3: [[1, 2], [3]],
    4: [[1, 3], [4]],
    5: [[1, 4], [2, 3], [5]],
    6: [[1, 2, 3], [1, 5], [2, 4], [6]]
}

possible_combos_two_dice = {
    2: [[2]],
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

flaps = initialize_flaps()
print("Welcome to 'Shut the Box'!")

while True:
    print()
    flaps = player_turn(flaps, possible_combos_one_die, possible_combos_two_dice)
    if all(not flap for flap in flaps.values()):
        print("Congratulations! You've won the game.")
        break

    print()
    flaps = computer_turn(flaps, possible_combos_one_die, possible_combos_two_dice)
    if all(flap for flap in flaps.values()):
        print("Game over. The computer won.")
        break
