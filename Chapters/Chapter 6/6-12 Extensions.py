# 6-5 Rivers
nile = {"country": "Egypt",
        "length": 400}
mississippi = {"country": "USA",
               "length": 600}
euphrates = {"country": "Turkey",
             "length": 200}

rivers = {"nile": nile,
          "mississippi": mississippi,
          "euphrates": euphrates,}

for river, dct in rivers.items():
    print(f"Information about the {river.title()} river!")
    for value in dct.values():
        if type(value) is int:
            print(f"\tThe {river.title()} is {value} miles long!")
        else:
            print(f"\tThe {river.title()} starts in {value}!")
