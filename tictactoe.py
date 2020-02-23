# Tic Tac Toe Game version 1
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#  1 | 2 | 3   1
# ------------ 2
#  4 | 5 | 6   3
# ------------ 4
#  7 | 8 | 9   5
# 123456789111
#        

# function to draw the playing board
# cells is a  9 element list with 'X', 'O' or ' ' for each element
# cells on the playing board are numbered 1 - 9 starting in the upper left corner
def draw_board(squares): # draws the playing board with the values in the array cells
    print(12*' ') # prints a blank line above the playing board
    print(' ' + cells[0] + ' ' + '|' + ' ' + cells[1] + ' ' + '|' + ' ' + cells[2]) # prints the first row
    print(12*'-') #draws horizontal line
    print(' ' + cells[3] + ' ' + '|' + ' ' + cells[4] + ' ' + '|' + ' ' + cells[5]) # prints the second row
    print(12*'-') #draws horizontal line
    print(' ' + cells[6] + ' ' + '|' + ' ' + cells[7] + ' ' + '|' + ' ' + cells[8]) # prints the third row

def valid_input(n): # funtion to check for valid player input
    return (n >= 1 and n <= 9 and cells[n-1] == ' ')

def check_winner(cells): # check to see if there is a winner
    if (cells[0:3] == ['X', 'X', 'X'] or cells[0:3] == ['O', 'O', 'O']):
        return True # first row     
    if (cells[3:6] == ['X', 'X', 'X'] or cells[3:6] == ['O', 'O', 'O']): # second row
        return True
    if (cells[6:9] == ['X', 'X', 'X'] or cells[6:9] == ['O', 'O', 'O']): # third row
        return True
    if (cells[0:7:3] == ['X', 'X', 'X'] or cells[0:7:3] == ['O', 'O', 'O']): # first column
        return True
    if (cells[1:8:3] == ['X', 'X', 'X'] or cells[1:8:3] == ['O', 'O', 'O']): # second column
        return True
    if (cells[2:9:3] == ['X', 'X', 'X'] or cells[2:9:3] == ['O', 'O', 'O']): # third column
        return True

def check_tie(cells): # check to see if there are no more moves left
    for square in cells:
        if square == ' ':
            return False
    return True

cells = [' ', ' ',' ',' ',' ',' ',' ',' ',' '] # keeps track of X, O and blank spaces on the playing board
game_playing = True
draw_board(cells)
print('Tic Tac Toe Game')
print ('Player 1 is X , Player 2 is O')
p1 = True
while game_playing: #main loop for game
    while p1:
        n1 = int(input('Player 1 enter your square number: '))
        draw_board(cells)
        if valid_input(n1): #check to see if input is valid
            cells[n1 - 1] = 'X' # if it is valid, enter an X in the square
            draw_board(cells) #draw the new board
            if check_winner(cells): # if there is a winner
                print('Winner !!!')
                game_playing == False # end the game
                p1 = False
                p2 = False
            elif check_tie(cells):
                print('Tie')
                game_playing == False # end the game
                p1 = False
                p2 = False
            else:
                p1 = False # end player 1 turn
                p2 = True
        else: # if input is not valid
            draw_board(cells)
            print('Invalid number. Number should be from 1 to 9 and space blank')
           
            
    while p2:
        n2 = int(input('Player 2 enter your square number: '))
        if valid_input(n2): #check to see if input is valid
            cells[n2 - 1] = 'O' # if it is valid, enter an O in the square
            draw_board(cells) #draw the new board
            if check_winner(cells): # if there is a winner
                print('Winner !!!')
                game_playing == False # end the game
                p1 = False
                p2 = False
            elif check_tie(cells):
                print('Tie')
                game_playing == False # end the game
                p1 = False
                p2 = False
            else:
                p2 = False # and end player 2 turn
                p1 = True
        else:
            draw_board(cells)
            print('Invalid number. Number should be from 1 to 9 and space blank')
   




