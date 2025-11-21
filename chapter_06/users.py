# Nested dictionaries = structured, multi-field objects

users = {
    "hsacco": {
        "first": "henry",
        "last": "sacco",
        "location": "georgia",
    },
    "mjordan": {
        "first": "michael",
        "last": "jordan",
        "location": "chicago",
    },
}

# Outer loop: usernames
for k, v in users.items():
    print(f"\nUsername: {k}")

    # Access nested fields
    full_name = f"{v['first']} {v['last']}"
    location = v["location"]

    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")
