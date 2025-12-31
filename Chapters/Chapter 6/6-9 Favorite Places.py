favorite_places = {"bowen": "puetro rico",
                   "james": ["japan", "denmark", "france"],
                   "ronan": ["iceland", "greece"],}
for name, places in favorite_places.items():
    print(f"{name.title()} likes:")
    if type(places) == str:
        print(f"\t{places.title()}")
    else:
        for place in places:
            print(f"\t{place.title()}")