#VC 7th Your Budget Assignment

while True:
    try:
        income = float(input("What is your monthly income?: "))
        break
    except:
        print("Enter a valid number for your income: ")

while True:
    try:
        rent = float(input("What is your monthly rent?: "))
        break
    except:
        print("Enter a valid number for your rent: ")

while True: 
    try:
        utilities = float(input("How much do you spend monthly on utilities: "))
        break
    except:
        print("Enter a valid number for your monthly utilities: ")

while True:
    try:
        groceries = float(input("How much do you spend monthly on your groceries?: "))
        break
    except:
        print("Enter a valid number for your groceries: ")

while True:
    try:
        transportation = float(input("How much do you spend on your monthly transportation?: "))
        break
    except:
        print("Enter a valid number for your transportation: ")

print(f"Your rent is ${rent:.2f} and that is {int(rent/income*100)}")
print(f"Your utilities is ${utilities:.2f} and that is {int(utilities/income*100)}")
print(f"Your groceries is ${groceries:.2f} and that is {int(groceries/income*100)}")
print(f"Your transportation is ${transportation:.2f} and that is {int(transportation/income*100)}")

saving = income * 0.10
print(f"you should save ${saving} amd that's 10% of your income")
spending_money = income - rent - utilities - groceries - transportation - saving
print(f"${spending_money} is your spending money.")