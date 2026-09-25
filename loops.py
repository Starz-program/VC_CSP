#VC 7th, Loops Notes
import random


count = 1

while count<= 10:
    print(count)
    count += 1


ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck....")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!")

# Comprex Data Type = holds other data in it.
siblings  = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
print(siblings [2])
#Adding to a list
siblings.append("name") # <= adds the item to the end of the list.
siblings.insert(3, "Vienna")
print(siblings)
#Remove from a list
siblings.pop(3) # <= if no number given pop removes the last item
print(siblings)


#print each item in a list
for siblings in siblings:
    print(siblings)


#for loops
for num in range(1,25):
    if num % 15 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)