bowen = {"first_name": "Bowen",
         "last_name": "Giardina",
         "age": 18,
         "city": "Acworth",}

james = {"first_name": "James",
         "last_name": "Cavanaugh",
         "age": 18,
         "city": "Raleigh",}

curtis = {"first_name": "Curtis",
          "last_name": "Cavanaugh",
          "age": 54,
          "city": "Kennesaw"}

people = [bowen, james, curtis]
for person in people:
    print(person["first_name"])
    print(person["last_name"])
    print(person["age"])
    print(person["city"])