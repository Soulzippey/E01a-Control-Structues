#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')  # writes out Greetings!
colors = ['red','orange','yellow','green','blue','violet','purple'] # setting up a array
play_again = '' # setting up a variable
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): # a while loop  that checks the play_again variable
    match_color = random.choice(colors) # Sets match_color to one of the colors from the array of colors
    count = 0 # sets the count variable
    color = ''# sets the color va
    while (color != match_color):# A while loop that runs if the the the color is inputed
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()# Make the input nice to work with aka make it lowercase and without spaces
        count += 1# Adds a number to the conter of "tries"
        if (color == match_color):# If the color inputed and the match_color then do next line
            print('Correct!')# write out Correct!
        else:# if the If statement was not filled the run this
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))# write out Sorry, try again. You have guessed {guesses} times. and for {guesses} it displays the count variable
    print('\nYou guessed it in {0} tries!'.format(count))# If the if statement was forfilled
    if (count < best_count):# checks if this was your lowest count viriable
        print('This was your best guess so far!')# if it is your lowest count viriable 
        best_count = count# and updates you lowest count
    play_again = input("\nWould you like to play again? ").lower().strip()# an input that can restart the first while loop
print('Thanks for playing!')#if you end the program 