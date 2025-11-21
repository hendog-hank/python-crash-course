age = float(input("What is the age? "))

if age < 2:
    print("They are a baby.")
elif age >= 2 and age < 4:
    print("They are a toddler.")
elif age >= 4 and age < 13:
    print("They are a kid.")
elif age >= 13 and age < 20:
    print("They are a teenager.")
elif age >= 20 and age < 65:
    print("They are a adult.")
elif age >= 65:
    print("They are a senior.")