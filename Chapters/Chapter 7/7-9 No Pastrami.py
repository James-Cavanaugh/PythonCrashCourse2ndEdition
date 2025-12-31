# 7-8 Deli
sandwich_orders = ["deli", "pastrami", "tuna", "meatball", "pastrami", "roast beef", "pastrami"]
finished_sandwiches = []
print("We have run out of Pastrami for the day.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)
print("Today I made:")
for sandwich in finished_sandwiches:
    print(f"\tA {sandwich.title()} Sandwich")
