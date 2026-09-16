#VC 7th Integers, Floats, and Expressions notes

# Integer => a whole number
Students = 23
cars = 50
computers = 29
awareness = -12

# Float => numbers with decimals
pi = 3.1415
temp = -95.6
cost = 1.99
rain = 2.17

#Arithmetic Operators (+ - * / // ** %)
print(f" 18/4 is {18/4} or {18//4} the remainder is {18%4}")
print(f"18/5 is {18/5} or {18//5} the remainder is {18%5}")

#order of operations
grades =[85,66,94,72,88,79,100]
students = len(grades)
average = sum(grades)/students

print(f"The average is {int(average)}")

# Convert the data type
price =float (input("How much did the item cost: "))
tax = 0.0485
sales_tax = price * tax
total = price + sales_tax
print(f"Your total is {total}")