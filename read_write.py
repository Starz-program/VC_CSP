#VC 7th, Reading and writing files

#this is a string
with open("practice.txt", "r+") as file: #<= how to make another file show another files contents, r+ lets you read and write. # Let's you read and appending
    content = file.read()
    content = "Chapter 1: \n" + content + "And Christopher Robin was sitting on his doorstep putting on his boots."
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day.")