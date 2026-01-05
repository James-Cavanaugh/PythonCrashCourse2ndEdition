def describe_city(city, country="united states"):
    print(f"{city.title()} is in {country.title()}")

describe_city("kennesaw")
describe_city(city="new york")
describe_city("reykjavic", "iceland")