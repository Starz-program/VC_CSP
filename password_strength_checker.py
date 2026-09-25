#VC 7th Password Strength Checker

Strength = 0
strengthstring = "null"
length = False
uppercase = False
lowercase = False
numbers = False
symbol = False


password = input("What is your password? ")

if len(password)>=8:
    length = True
for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        numbers = True
    if letter in "?!@#$%^&*()":
        symbol = True

   
if uppercase == True:
    Strength += 1
if lowercase == True:
    Strength += 1
if numbers == True:
    Strength += 1
if symbol == True:
    Strength += 1
if length == True:
    Strength += 1

print("At least 8 characters: ", length)
print("Has an uppercase letter: ", uppercase)
print("Has a lowercase letter: ", lowercase)
print("Has a number", numbers)
print("Has a symbol:", symbol)

if Strength >= 5:
    strengthstring = "Strong"
elif Strength >= 3 and Strength <= 4:
    strengthstring = "Medium"
else:
    strengthstring = "Weak"
print("Your password strength is:", strengthstring)

