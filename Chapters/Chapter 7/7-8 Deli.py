sandwich_orders = ["deli", "tuna", "meatball", "roast beef"]
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)
print("Today I made:")
for sandwich in finished_sandwiches:
    print(f"\tA {sandwich.title()} Sandwich")
