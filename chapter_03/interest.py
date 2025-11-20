p = float(input("How much is the initial deposit? "))
r = float(input("What is the interest rate?\n(Enter a number between 0 and 100) "))/100
t = float(input("How many years will interest accrue? "))
print("The total amount after interest is: $", (p*r*t)+p)
