guests = ["henry", "sarah", "mike"]

for g in guests:
    print(f"Hi {g.title()}, you're invited to dinner!")

print("\nMike can’t make it.")

guests[2] = "alex"

for g in guests:
    print(f"Hi {g.title()}, please come to dinner!")

print("\nWe found a bigger table!")
guests.insert(0, "bryn")
guests.insert(2, "otis")
guests.append("maddie")

for g in guests:
    print(f"Hi {g.title()}, you're invited to dinner!")

print("\nBad news — only two guests allowed.")

while len(guests) > 2: 
    removed = guests.pop()
    print(f"Sorry {removed.title()}, no room at the table.")

print("\nFinal guests:")
for g in guests:
    print(g.title())