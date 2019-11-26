#This is a "Guess the number" game. 

import random

print('What is your name?')
name = input()

print("Hello, " + name + " I'm thinking of a number between 1 and 20.")
secretnumber = random.randint(1, 20)

#print('DEBUG: I was thinking of ' + str(secretnumber))

for guessestaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess > secretnumber: 
        print('Your guess is too high.')
    elif guess < secretnumber:
        print('Your guess is too low.')
    else: 
        break #this part is for the correct answer.

if guess == secretnumber:
    print('Good job! You got the right number in {} guesses.'.format(guessestaken))   
else: 
    print('I was thinking of {}. You did not get the right answer in {} guesses, you loser!'.format(secretnumber, guessestaken))      
