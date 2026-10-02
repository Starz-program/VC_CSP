#VC 7th, Caeser Cipher

letter = input("Would you like to (E)ncrypt or (D)ecrypt a message?: ").strip().upper()
message = input("Enter your message: ")
shift = int(input("How many times would you like to shift your message?: "))

def caeser_shift(text, shift_amount):
    result = " "
    for char in text:
        if char.isalpha():
            start = ord ('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += new_char
        else:
            result += char
    return result

shift_num = int(shift)

choice = letter.strip().upper()

if choice == 'E':
    encrypted = caeser_shift(message, shift_num)
    print(f"Your encrypted message is: {encrypted}")
elif choice == 'D':
    decrypted = caeser_shift(message, -shift_num)
    print(f"Your decrypted message is: {decrypted}")
else:
    print("")