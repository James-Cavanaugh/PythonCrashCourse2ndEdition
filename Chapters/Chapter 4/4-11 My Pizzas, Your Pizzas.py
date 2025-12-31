# 4-1 Pizzas
pizzas = ["Meat Lovers", "Pepperoni", "Sausage"]
for pizza in pizzas:
    print(f"I like {pizza} Pizza!")
print("I'm ngl I'm not a big fan of pizza")
friend_pizzas = pizzas[:]
pizzas.append("Hawaiian")
friend_pizzas.append("BBQ")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")
print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")