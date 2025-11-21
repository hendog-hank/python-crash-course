favorite_places = [
 {  "name": "henry",
    "locations": ["boston", "new york", "los angeles"]
},

{   "name": "bryn",
    "locations": ["london", "amsterdam", "paris"]
},

{   "name": "otis",
    "locations": ["park", "beach", "lake"]
}
]

for f in favorite_places:
    name = f["name"].title()
    places = ', '.join(f["locations"])
    print(f" {name}'s favorite places are: {places.title()}. \n")
