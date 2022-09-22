import random

randNumber = random.randint(1,100)
userGuess = None
Guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess:"))
    Guesses += 1 
    if(userGuess == randNumber):
        print("You Guess is Right")
    else:
        if (userGuess>randNumber):
            print("You Guessed is Wrong. enter a smaller numer!")
        else:
            print("You Guessed is Wrong. enter a larger numer!")  

print(f"You guessed the number in {Guesses} gusses")
