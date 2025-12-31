# Equality and Inequality (str)
x = "hello"
y = "Hello"
print(x == y)
print(x == "hello")
# lower() and upper()
print(x == y.lower())
print(x == y.upper())

# Numerical (==, !=, <, >, <=, >=)
x = 5
y = 3
z = 8
print(x == y)
print(x + y == z)
print(y != 3)
print(y != z)
print(y < z)
print(z < x)
print(z > x)
print(y > z)
print(y <= z)
print(z <= x)
print(z >= x)
print(y >= z)

# and or keywords
print(True and True)
print(True and False)
print(True or False)
print(False or False)

# item in list
lst = ["apple", "orange", "banana"]
print("apple" in lst)
print("peach" in lst)

# item not in list
print("banana" not in lst)
print("tomato" not in lst)