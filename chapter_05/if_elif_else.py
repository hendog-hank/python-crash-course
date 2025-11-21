age = float(input("What is your age? "))

if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 15

print(f"The price of your ticket is: ${price}")