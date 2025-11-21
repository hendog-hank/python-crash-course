# Dictionary containing a list (common in JSON APIs)

pizza = {
    "crust": "thick",
    "toppings": ["pepperoni", "mushrooms", "extra cheese"],
}

print(f"You ordered a {pizza['crust']}-crust pizza with:")

# Loop through list inside the dictionary
for topping in pizza["toppings"]:
    print(f"- {topping}")
