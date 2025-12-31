atl = {"population": 250_000,
       "country": "USA",
       "fact": "coca cola factory"}
chicago = {"population": 150_000,
       "country": "USA",
       "fact": "bears football"}
boston = {"population": 300_000,
       "country": "USA",
       "fact": "celtics"}
cities = {"atlanta": atl,
          "chicago": chicago,
          "boston": boston}

for city, dic in cities.items():
    print(city.title())
    for key, value in dic.items():
        print(f"\t{key.title()}: {dic[key]}")