
# Guessing Game Challenge
# Let's use while loops to create a guessing game.
# 
# The Challenge:
# 
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

from random import randint

game_playing = True
num = randint(0, 100)
print(num)
num_guesses = 0
while game_playing:   
    guess = int(input('Guess a number from 1 to 100, 0 to quit : '))
    if guess == 0:      # check to see if player ended game
        game_playing = False
        print('Game Over')
    elif guess <= 100 and guess >= 1:    # check to see if number entered is valid
        num_guesses = num_guesses +1
        print('valid input')
        print('number guesses: ', num_guesses)
        if guess == num:  # check to see if a winner
            print('You Won')
            print('It took ', num_guesses,' guesses')
            game_playing = False
        elif num_guesses == 1:
            last_guess = guess
            if abs(num - guess) <= 10:
                print('WARM')
            else:
                print('COLD')
        else:
            if abs(guess - num) < abs(last_guess - num):
                print('WARMER')
            else:
                print('COLDER')
            last_guess = guess    
    else:
        print('OUT OF BOUNDS')
        





