users = [
 {  "first name": "henry",
    "last name": "sacco",
    "location": ["savannah"]

},

{   "first name": "bryn",
    "last name": "golesworthy",
    "location": ["savannah"]
},

{   "first name": "rupert",
    "last name": "the bear",
    "location": ["savannah"]
},

{   "first name": "otis",
    "last name": "the dog",
    "location": ["savannah"]
},
]

for u in users:
    name = f"{u['first name'].title()} {u['last name'].title()}"
    location = ', '.join(u["location"]).title()
    print(f"{name} is from : {location}. \n")
