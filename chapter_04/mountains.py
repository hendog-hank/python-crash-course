mountains = ["everest", "fuji", "denali", "rainier"]

print("Original:", mountains)
print("Sorted temporary:", sorted(mountains))
print("Still original:", mountains)

mountains.sort()
print("Sorted:", mountains)

mountains.sort(reverse=True)
print("Reverse sorted:", mountains)

mountains.reverse()
print("Reversed:", mountains)

print("Length:", len(mountains))
