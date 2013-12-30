'''
Created on Dec 30, 2013

@author: codeslug

This was written for a codeacademy exercise. 

Instructions:

Using while/else structure, allow the user to guess what the number is three times. 
If they guess correctly, print 'You win!' and break. If they do not guess correctly, 
have the else execute at the end of the loop to print 'You lose.'

Use guess = int(raw_input("Enter a guess:")) to get a number from the user and 
store it as an integer. (Remember, raw_input turns user input into a string, 
so we use int() to make it a number again.)


'''
from random import randrange

random_number = randrange(1, 10)
# debugging - print "Random number is " + str(random_number)

count = 1

while (count <= 3):
    guess = int(raw_input("Enter a guess:"))
    count += 1
    if (guess == random_number):
        print "You win!"
        break
    elif (count <= 3):
        print "Sorry, that was incorrect. Please try again." # tracks guesses
else:
    print "You lose!" # loop ends with no matches and 3 guesses have passed


"""
Improving - 
- Debug for when the number entered is not a number.
- larger range for number guessed.
- give hints on whether guessed number is too high or too low.


"""