#VC 7th, Conditionals notes

#conditional

time = 1416
day = "Tuesday"

if time < 1200 and time > 500:
    print("Good morning!")
elif time < 1700:
    print("Good afternoon!")
    if day != "Saturday" or day != "Sunday":
        print("How has school been?")
elif time < 2000:
    print("Good Evening!")
else:
    print("Good night!")

print("Code is done")