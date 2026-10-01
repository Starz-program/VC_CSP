#VC 7th, Caeser Cipher

letter = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("Enter your message: ")
shift = input("How many times would you like to shift your message?: ")

def caeser_shift(message_shift):
    sentence = input

    if letter.isalpha():
        if letter.isupper():
            start = ord("t")
        else:
            start = ord("t")

else:
        sentence =+ letter

if letter == "E":
    sentence = caeser_shift(message, shift)
    print(f"your encrypted message is: {sentence}")

elif letter == "D":
    result = caeser_shift(message, shift)
    print(f"your decrypted message is: {result}")