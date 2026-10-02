#VC 7th, Number information

for num in range (1, 21):
    if num %2 == 0:
        if num %5 == 0:
            print(num, "is even and divisable by 5")
    else:
        print(num, "is odd and not divisable by 5")
    if num %5 == 0:
        print(f"{num} is odd and is divisable by 5")
    else:
        print(f"{num} is odd and is not divisable by 5")