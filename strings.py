#VC Strings Notes

# Strings => any saved inside of quotation marks "" ''

name = input("what is your name: ").strip().capitalize()

age = input('How old are you?: ')
print(type(age))

# Cibcatebatuib => puts two strings directly next to each other

print(age+age)

print(name+ " " + "Larose")

#

sentence = "The quick brown fox jumped over the lazy dog."

print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long, Your first initial is {name[0]} I think I will call your {name[0:2]}")