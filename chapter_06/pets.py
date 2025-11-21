pets = [
 {  "type": "dog",
    "breed": "golden retriever",
    "name": "otis",
    "owner": "henry",
},

{   "type": "dog",
    "breed": "mixed",
    "name": "rupert",
    "owner": "bryn",
},

{   "type": "cat",
    "breed": "mixed",
    "name": "alfie",
    "owner": "ann",
}
]

for pet in pets:
    for k, v in pet.items():
        print(f"{k.title()}: {v.title()}")
    print()