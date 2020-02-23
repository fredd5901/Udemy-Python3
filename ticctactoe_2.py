# Tic Tac Toe Game version 2
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#  1 | 2 | 3   1
# ------------ 2
#  4 | 5 | 6   3
# ------------ 4
#  7 | 8 | 9   5
# 123456789111
#          012

import random

# Function that can print out a board. Board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.


def display_board(board):
    print('\n' * 100)
    print(12*' ')  # prints a blank line above the playing board
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] +
          ' ' + '|' + ' ' + board[3])  # prints the first row
    print(12*'-')  # draws horizontal line
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] +
          ' ' + '|' + ' ' + board[6])  # prints the second row
    print(12*'-')  # draws horizontal line
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] +
          ' ' + '|' + ' ' + board[9])  # prints the third row

# function that can take in a player input and assign their marker as 'X' or 'O'


def player_input():
    player1 = ''
    player2 = ''
    while (player1 != 'X' and player1 != 'x' and player1 != 'O' and player1 != 'o'):
        player1 = input('Please pick a marker "X" or "O"')
    if player1 == 'X' or player1 == 'x':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = '0'
        player2 = 'X'
    print(f"player1 is : {player1}")
    print(f"player2 is : {player2}")

# Function that takes in the board list object, marker ('X' or 'O'), desired position (number 1-9) and assigns it to the board


def place_marker(board, marker, position):
    board[position] = marker

# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won


def win_check(board, mark):
    if board[1:4] == [mark, mark, mark]:  # first row
        return True
    if board[4:7] == [mark, mark, mark]:  # second row
        return True
    if board[7:] == [mark, mark, mark]:  # third row
        return True
    if board[1:8:3] == [mark, mark, mark]:  # first column
        return True
    if board[2:9:3] == [mark, mark, mark]:  # second column
        return True
    if board[3::3] == [mark, mark, mark]:  # third column
        return True
    if board[1::4] == [mark, mark, mark]:  # diagonal 1
        return True
    if board[3:8:2] == [mark, mark, mark]:  # diagonal 2
        return True
    else:
        return False

# Function that uses the random module to randomly decide which player goes first


def choose_first():
    p1name = input('Player 1 enter your name')
    p2name = input('Player 2 enter your name')
    rannum = random.randint(1, 2)
    if rannum == 1:
        print(f'{p1name} you get to go first')
    else:
        print(f'{p2name} you get to go first')



