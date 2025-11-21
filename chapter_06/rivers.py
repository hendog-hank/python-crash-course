rivers = {
    "mississippi": "mississippi",
    "saint lawrence": "new york",
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
    "congo": "cameroon",
}

for k, v in rivers.items():
    print(k.title())

for k, v in rivers.items():
    print(v.title())

for k, v in rivers.items():
    print(f"The {k.title()} river runs through {v.title()}.")