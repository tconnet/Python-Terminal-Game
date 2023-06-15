# Shut the Box Game

This repository contains the Python code for a simplified version of the traditional pub game 'Shut the Box'.

## Introduction

'Shut the Box' is a dice game for one or more players. The game uses a board with flaps numbered from 1 to 9. The flaps can be in either an open or closed state. In this simplified version of the game, players take turns rolling a die or pair of dice and then closing the flaps that match the roll's total. The game continues until there are no possible moves left.

## How to Play

The game begins with all flaps in the open state. Players take turns to roll a die (or pair of dice) and close the flaps based on the total value of the roll. For example, if a player rolls a total of 7, they can choose to close the flaps in the following combinations:

- 7
- 1, 6
- 2, 5
- 3, 4
- 1, 2, 4

If there are no possible moves left, the player's turn ends. The game continues until all flaps are closed, in which case the player wins, or until there are no more possible moves, in which case the computer wins.

## Requirements

- Python 3.x

## How to Run the Game

Simply run the `shut_the_box.py` script in your Python environment.

Enjoy the game!
