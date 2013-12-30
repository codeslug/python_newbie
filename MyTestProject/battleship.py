'''
Created on Dec 29, 2013

@author: codeslug

This was created for a codeacademy exercise.

It is a one-player battleship game. It has 4 turns and prints to a 5x5 board. 
The ship is randomly generated and occupies 1 space.

'''
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)
# each iteration of this for statement adds another list to the variable board.
# each list contains 5 "O" strings.
# now, board is a list of 5 lists (0-4).

def print_board(board):
    for row in board:
        print " ".join(row)
# this "joins" the "O" characters and adds a space between them (contained in the brackets)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
# creates random coords for the ship.

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
# prints actual ship, for debugging purposes


for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
# int here prevents a non-integer from being entered

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row<0 or guess_row>4) or (guess_col<0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
        print "You have completed Turn " + str(turn+1)
        if (turn >= 3):
            print "Game Over"
            
            
""""
Enhancement ideas -

Make multiple battleships: you'll need to be careful because you need to make sure that you don’t 
place battleships on top of each other on the game board. You'll also want to make sure that you 
balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship 
need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place 
part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, 
statistics and more!

"""