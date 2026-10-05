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

with open ("hangman.txt", "r") as file:
    content = file.read()

word = random.choice("hangman.txt")
guess = 0
correct = 0
wrong = 0
attempts = 0
play = 0
with open ("hangman_win_loss.txt", "r+") as file:
    content = file.read().split(",")

wins = 
losses = 


print("Welcome to hangman! I am going to think of a word, and you are gonna guess what it is by guessing the letters in the word. Good luck!")
print("_" * len(word))

while attempts > 0:
    guess_letters = input("Guess a letter: ").lower()

if guess.isalpha() or len(guess)!= 1:
    print("please enter a single letter")
if guess in guess:
    print("you have already guessed that.")