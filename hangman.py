#VC 7th, Hangman

import random

#create a list of 10 words on a seperate txt file

#create another file holds win/loss counts, 0,0

#Uses split(",") on the content of the words txt document to create your list of words.
#reads the txt file
#Pull win and lose totals from the other txt file and save them as 2 separate variables.
#Build the hangman game

#save the correct word as a variable random.choice(name of the list)
#number of wrong guesses
#What letters have been guessed []

#function to display the hangman (needs number of wrong guesses)
#_____
#|   |
#|   O
#|  /|\
#|  / \
#|____

#Function to show the letters and spaces (The correct word, letters that have been guessed.)
#variable for display word(starts as an empty string)
#loop over the correct word
#check if letter has been guessed
#then add the letter to the display word
#if they havent guessed the letter add an underscore to the display word
#return the finished display word(outside of the loop)


# Main game loop (while true loop)
#call the function the show handman
#print function call to show display word
#create variable and ask user to guess a letter
#add the letter to list of guessed_letter
#check if not letter in word:
#increase incorrect guesses
#check if (display word, call function)is same as the word
#tell user they won!
#increase win total
#ask if they want to play again
#reset random word, rest wrong guess count(guessed letters)
#check to see if they lost(if they have 6 wrong guesses)
#tell them they lost
#tell them what the word was
#Increase the lost count
#ask if they wanna play again
print("Welcome to hangman! You get 6 guesses for a letter in a random word chosen by me. Good luck!")
hangman_art =[
"""_______
|       |
|
|
|
|
|__________""",
"""_______
|       |
|       O
|
|
|
|__________""",
"""_______
|       |
|       O
|       |
|
|
|__________""",
"""_______
|       |
|       O
|      /|
|
|
|__________""",
"""_______
|       |
|       O
|      /|\\
|
|
|__________""",
"""_______
|       |
|       O
|      /|\\
|      /
|
|__________""",
"""_______
|       |
|       O
|      /|\\
|      / \\
|
|__________""",
]

with open("hangman.txt", "r") as file:
    words = file.read().split(",")
with open("hangman_win_loss.txt", "r") as file:
    score = file.readlines()
    wins = int(score[0].split("=")[1])
    losses = int(score[1].split("=")[1])
answer = random.choice(words).strip().lower()
guessed_letters = []
max_wrong_guesses = 6
wrong_guesses = 0
won = False

while wrong_guesses < max_wrong_guesses:
    print(hangman_art[wrong_guesses])
    shown_word = ""
    for letter in answer:
        if letter in guessed_letters:
            shown_word = shown_word + letter + " "
        else:
            shown_word = shown_word + "_ "

    print(f"\nWord: {shown_word}")
    print(f"Attempts remaining: {max_wrong_guesses - wrong_guesses}")

    if "_" not in shown_word:
        print("You win!")
        wins = wins + 1
        won = True
        break

    guess = input("Guess a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess not in answer:
        wrong_guessed = wrong_guesses + 1
        print("That letter is not in the word.")

if not won:
    print(hangman_art[wrong_guesses])
    print(f"\nYou lose! the word was: {answer}.")
    losses = losses + 1

print(f"Score:{wins} wins, {losses} losses.")
with open("hangman_win_loss.txt", "w") as file:
    file.write(f"win = {wins}\n")
    file.write(f"loss = {losses}\n")