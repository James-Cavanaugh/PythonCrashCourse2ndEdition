# 9-1
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.name} is open!")

restaurant1 = Restaurant("Sushi Factory", "Asian")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("Jersey Mikes", "American")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Panda Express", "Asian")
restaurant3.describe_restaurant()