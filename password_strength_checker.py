#VC 7th Password Strength Checker

Strength = 0



uppercase = False
lowercase = False
numbers = False
symbol = False
length = False

password = input("What is your password?: ")
if len(password)>=8:
    length = True
for letter in password:
    if letter.isupper():
        uppercase = True
    else:
        uppercase = False
    if letter.islower():
        lowercase = True
    else:
        lowercase = False
    if letter.isnumeric():
        numbers = True
    else:
        numbers = False
    if letter in "?!@#$%^&*()":
        symbol = True
    else:
        symbol = False

   
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