rivers = {"nile": "egypt",
          "mississippi": "usa",
          "euphrates": "turkey",}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nRivers Mentioned:")
for river in rivers.keys():
    print(river.title())

print("\nCountries Mentioned:")
for country in rivers.values():
    print(country.title())