#VC 7th, Caeser cipher

letter = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ")
message = input("Enter your message: ")
shift = int(input("How many times would you like to shift your message?: "))

def caeser_shift(text, shift_amount):
    result = " "
    for char in text:
        if char.isalphs():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += new_char
        else:
            result += char
    return result
if letter == 'E' or letter == 'e':
    encrypted_message = caeser_shift(message,shift)
    print(f"Your encrypted message is: {encrypted_message}")
elif letter == 'D' or letter == 'D':
    decrypted_message = caeser_shift(message, -shift)
    print(f"Your decrypted message is: {decrypted_message}")
else:
    print("Invalid letter. Please choose 'D' or 'E'.")