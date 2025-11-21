current_users = ["admin", "henry", "mike"]
new_users = ["bryn", "Henry", "otis"]

#
current_users_lower = [u.lower() for u in current_users]

taken = []
available = []

for user in new_users:
    if user.lower() in current_users_lower:
        taken.append(user)
    else:
        available.append(user)

print(f"Taken: {', '.join(taken)}")
print(f"Available: {', '.join(available)}")
