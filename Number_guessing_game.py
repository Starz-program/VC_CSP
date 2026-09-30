# VC, 7th, Number Guessing Game
import random
print("I'm thinking of a number from 1 to 100. You have 6 tries to guess it!")


number = random.randint(1,100)

print(number)

attempts = 0

while attempts < 6:
    guess1 = int(input("Enter your first guess: "))
    attempts += 1

    if guess1 == number:
        print(f"Correct you got it in {attempts} tries!")
        break
    elif guess1 < number:
        print("Too low!")
    else:
        print("Too high!")

    guess2 = int(input("Enter your second guess: "))
    attempts += 1

    if guess2 == number:
        print(f"Correct! you got it in {attempts} tries!")
        break
    elif guess2 < number:
        print("Too low!")
    else:
        print("Too high!")

    guess3 = int(input("Enter your third guess: "))
    attempts += 1

    if guess3 == number:
        print(f"Correct! you got it in {attempts} tries!")
        break
    elif guess3 < number:
        print("Too low!")
    else:
        print("Too high!")

    guess4 = int(input("Enter your fourth guess: "))
    attempts += 1
    
    if guess4 == number:
        print(f"Correct! you got it in {attempts} tries!")
        break
    elif guess4 < number:
        print("Too low!")
    else:
        print("Too high!")

    guess5 = int(input("Enter your fifth guess: "))
    attempts += 1
    
    if guess5 == number:
        print(f"Correct! you got it in {attempts} tries!")
        break
    elif guess5 < number:
        print("Too low!")
    else:
        print("Too high!")

    guess6 = int(input("Enter your sixth guess: "))
    attempts += 1
    
    if guess6 == number:
        print(f"Correct! you got it in {attempts} tries!")
        break
    elif guess6 < number:
        print("Too low!")
    else:
        print("Too high!")


    if guess6 != number:
        print(f"Game over! The number was {number}.")