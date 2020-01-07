#Exercise 9
#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

x = random.randint(1,9)
guess = 0
count = 0

while guess != x and guess != 'exit':
    guess = int(input("What's your guess of an integer between 1 and 9 both included - "))

    if guess == 'exit':
        break

    count = count + 1

    if guess > x:
        print("Your guess is too high, try again!\n")
    elif guess < x:
        print("Your guess is too low, try again!\n")
    else:
        print("Your guess is correct!!!")
        print("Number of guesses you made - ", count)



