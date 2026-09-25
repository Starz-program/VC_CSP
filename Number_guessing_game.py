# VC, 7th, Number Guessing Game
import random
print("I'm thinking of a number from 1 to 100. You have 6 tries to guess it!")


number = random.randint(1,100)

print(number)

Guess1 = False
Guess2 = False
Guess3 = False
Guess4 = False
Guess5 = False
Guess6 = False

while True:
    if Guess1 == number:
        print("YOU GOT IT RIGHT THE FIRST TIME!!! GREAT JOB!")
    elif Guess1 <= number:
        print("Too low!")
    else:
        Guess1 >= number
        print("Too high!")