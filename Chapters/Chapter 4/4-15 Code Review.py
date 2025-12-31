# 4-1 Pizzas
pizzas = ["Meat Lovers", "Pepperoni", "Sausage"]

for pizza in pizzas:
    print(f"I like {pizza} Pizza!")

print("I'm ngl I'm not a big fan of pizza")

# 4-10 Slices
animals = ["Cheetah", "Road Runner", "Bunny", "Eagle", "Lion"]

for animal in animals:
    print(f"A {animal} is fast!")

print("All these animals are fast!")
print(f"The first three animals in the list are: {animals[:3]}")
print(f"Three items from the middle of the list are: {animals[1:4]}")
print(f"The last three animals in the list are: {animals[2:]}")

# 4-12 More Loops
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food.title())