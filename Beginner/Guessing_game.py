#Importing random
import random
print("Welcome to Number Guessing Game")
print("Hmm.... I'm thinking of a number between 1 and 100... done! lets begin the game")
secret_number = random.randint(1,100)
found = False
num_of_attempts = 0
#Taking inputs and validating
while not found:
    guess = input("Enter your guess")
    if int(guess)== secret_number:
        found = True
        num_of_attempts = num_of_attempts + 1
    elif int(guess) > secret_number:
        print("Too High")
        num_of_attempts = num_of_attempts + 1
    elif int(guess) < secret_number:
        print("Too low")
        num_of_attempts = num_of_attempts + 1
print("congrats you've guessed it! your num of attempts are" , num_of_attempts)
   