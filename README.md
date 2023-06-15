# Shut the Box Game

This repository contains the Python code for a single-player variation of the classic pub game 'Shut the Box'.

## Introduction

'Shut the Box' is a dice game traditionally played with one or more players. In our unique adaptation, a single player competes against the computer. The game uses a board with flaps numbered from 1 to 9. The flaps can be in either an open or closed state. The player and the computer take turns rolling a die or pair of dice, aiming to change the state of the flaps to match the roll's total. 

## How to Play

In this variation, the game begins with all flaps in the open state. The player takes the first turn to roll a die (or pair of dice) and closes the flaps that match the total value of the roll. For example, if a player rolls a total of 7, they can choose to close the flaps in the following combinations:

- 7
- 1, 6
- 2, 5
- 3, 4
- 1, 2, 4

If no more moves are possible based on the state of the box, the player's turn ends, and the computer's turn begins. The computer's objective is to reopen the flaps using the same rules. 

The player wins the game by closing all flaps during their turn. If the computer manages to open all the flaps during its turn, the computer wins.

## Requirements

- Python 3.x

## How to Run the Game

To start the game, run the `shut_the_box.py` script in your Python environment.

Enjoy this unique variation of the classic 'Shut the Box' game!
