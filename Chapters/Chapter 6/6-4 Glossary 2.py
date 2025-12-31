glossary = {"get()": "A built-in method for dictionaries that takes a key as its first parameter and a value to return if it can't find that key in the dict.",
            "if": "A conditional that runs the indented code below if the condition that comes after it is met",
            "elif": "A conditional that runs the indented code below if the condition that comes after it is met, it also must come after an if statement",
            "else": "A conditional that runs the indented code below if all of the conditionals above it are not met",
            "dictionary": "A hasmap in python that takes key value pairs and stores them with O(1) access",
            "key":"A value that is used to find the value connected to it in a dictionary and cannot be a duplicate",
            "value":"A value that is connected to a key in a dictionary that can be a duplicate",
            "C":"The lowest level programming language aside from Assembly",
            "print()":"Displays its parameter to the console",
            "set()":"Creates a set that is empty with no parameters or unpacks any iterable to be a set if given",}

for key, value in glossary.items():
    print(f"{key}: {value}")