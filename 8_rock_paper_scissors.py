#Exercise 8
#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

print ("\nRock Paper Scissors Game, choose between one.\n")
x = input("Player 1 Enter your choice -  ")
y = input("Player 2 Enter your choice -  ")
x = str(x).lower()
y = str(y).lower()

if x == 'rock':
    if y == 'scissors':
        print ("\nPlayer 1 is the winner!")
    if y == 'paper':
        print("\nPlayer 2 is the winner!")
    if y == x:
        print("\nNo winner!")

if x == 'paper':
    if y == 'rock':
        print("\nPlayer 1 is the winner!")
    if y == 'scissors':
        print("\nPlayer 2 is the winner!")
    if y == x:
        print("\nNo winner!")

if x == 'scissors':
    if y == 'rock':
        print("\nPlayer 2 is the winner!")
    if y == 'paper':
        print("\nPlayer 1 is the winner!")
    if y == x:
        print("\nNo winner!")



#   END   #