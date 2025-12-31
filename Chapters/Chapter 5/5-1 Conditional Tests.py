fruits = ["apple", "Banana", "cherry", "orange", "tomato", "PEACH"]

print(f'Is apple in fruits? - {"apple" in fruits}')
print(f'Is banana in fruits? - {"banana" in fruits}')
print(f'Is Banana in fruits? - {"banana".title() in fruits}')
print(f'Is pear in fruits? - {"pear" in fruits}')
print(f'Is orange in fruits? - {"orange" in fruits}')
print(f'Is ORANGE in fruits? - {"orange".upper() in fruits}')
print(f'Is PEACH and cherry in fruits? - {"peach".upper() and "cherry" in fruits}')
print(f'Is Peach in fruits? - {"peach".title() in fruits}')
print(f'Is PEACH in fruits? - {"peach".upper() in fruits}')
print(f'Is APPLE in fruits? - {"apple".upper() in fruits}')