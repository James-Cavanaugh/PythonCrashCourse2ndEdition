favorite_numbers = {"james": [12, 67],
                    "bowen": [56, 89, 10],
                    "ronan": 33,
                    "elisha": [67, 420],
                    "curtis": 69,}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number(s) is")
    if type(numbers) is int:
        print(f"\t{numbers}")
    else:
        for number in numbers:
            print(f"\t{number}")