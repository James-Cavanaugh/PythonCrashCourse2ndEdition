dream_place = {}

while True:
    name = input("What is your name? ")
    dream = input("If you could visit one place in the world, where would you go? ")
    dream_place[name] = dream
    if input("Will another person be taking this quiz? ").lower() == "no":
        for key, value in dream_place.items():
            print(f"{key} would like to go to {value} someday")
        break