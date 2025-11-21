fruits = ["raspberry", 'apple', "banana", "orange"]

if "raspberry" in fruits:
    print("Raspberries are my favorite!")

if "apple" in fruits:
    print("I hate apples!")

if "watermelon" not in fruits:
    print("I really wish I had watermelon!")

print(f"I need to get more of these fruits: {', '.join(fruits[0:4])}")
